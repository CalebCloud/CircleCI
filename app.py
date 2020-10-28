import boto3
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

#DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    key_id = TextField('AWS Key:', validators=[validators.DataRequired(), validators.Length(min=20, max=20)])
    secret_key_id = TextField('AWS SECRET KEY:', validators=[validators.DataRequired(), validators.Length(min=40, max=40)])
    bucket_name = TextField('Bucket Name:', validators=[validators.DataRequired()])
    object_name = TextField('Object Name:', validators=[validators.DataRequired()])
    object_content = TextField('Object Content:', validators=[validators.DataRequired()])
    aws_region = TextField('AWS Region:', validators=[validators.DataRequired()])
    
    @app.route("/", methods=['GET', 'POST'])
    def main():
        form = ReusableForm(request.form)
    
        print (form.errors)
        if request.method == 'POST':
            key_id         = request.form['key_id']
            secret_key_id  = request.form['secret_key_id']
            bucket_name    = request.form['bucket_name']
            object_name    = request.form['object_name']
            object_content = request.form['object_content']
            aws_region     = request.form['aws_region']

        if form.validate():
            client = boto3.client(
                's3',
                aws_access_key_id = key_id,
                aws_secret_access_key = secret_key_id
            )

            client.create_bucket(
                ACL = 'public-read-write',
                Bucket = bucket_name,
                CreateBucketConfiguration={
                    'LocationConstraint': str(aws_region)
                }
            )

            client.put_object(
                Body = object_content,
                Bucket = bucket_name,
                Key = object_name,
                ACL='public-read',
                ContentType='media-type'
            )

            flash(f'The link to your new bucket and object is https://{bucket_name}.s3-{aws_region}.amazonaws.com/{object_name} .')

        else:
            flash('Improper Input. Please fill out all fields again.')

        return render_template('index.html', form = form)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

def Add(a, b):
    return a + b