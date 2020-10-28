# CircleCI

This was a personal project to design a docker flask app and setup a CI/CD pipeline with CircleCi to build and deploy my docker images to Amazon Web Services' Elastic Container Orchestration Service. 

When pushed to GitHub, CircleCi builds and deploys a docker image from this repo. If the image fails the pre-determined test, the deployment will terminate. Once the image passes the test stage, it gets deployed to your AWS ECS cluster. Deployment using this pipeline prevents any faulty code from going out while offering zero downtime between deployments.

The app.py file is a python flask application that uses the AWS SDK to create an S3 bucket and object based off user input. The other python file is a simple test for CircleCi to run. The dockerfile uses a python base image with a working directory of /app, it installs the necessary python modules, moves everything into the /app directory, and then it runs the app.py code. 

The CircleCi folder contains the config file for the service. This file tells CircleCi how the deployment is handled. The templates folder contains the index.html for the flask app. 

<pre>
To setup the CircleCi pipeline, you need to declare the following environmental variables within the project settings: 

- AWS_ACCESS_KEY_ID     AWS credentials are needed for CircleCi to push the image into production on AWS ECS.
- AWS_SECRET_ACCESS_KEY AWS credentials are needed for CircleCi to push the image into production on AWS ECS.
- AWS_REGION            The region that your ECS cluster is in.
- DOCKER_LOGIN          Docker credentials needed to build and push the image to Docker Hub.
- DOCKER_PASSWORD       Docker credentials needed to build and push the image to Docker Hub.
- ECS_CLUSTER_NAME      Title of your ECS cluster for CircleCi to push the image to.
- ECS_SERVICE           Title of the ECS service for CircleCI to deploy to.
</pre>

Setup for ECS can be found on [circleci's blog](https://circleci.com/blog/use-circleci-orbs-to-build-test-and-deploy-a-simple-go-application-to-aws-ecs/).

<pre>
Changes to make if you run this.
- The only changes that you need to make are in the CircleCi config.yml. 
- Lines 11 and 15 change the image to your own image on the dockerhub repo that you make.
- Line 41 change 'ecsDockerContainer' to the name of the ECS container that you make. 
- Line 41 change nehoc/circledocker to the repo you created.
- Make sure to keep your region consistent throughout everything.
</pre>

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
DISCLAIMER: This specific app requires input of AWS Access keys. This app was created as an example application that you would deploy with CircleCi. Entering your credentials anywhere is bad practice and is best not done. Access keys used in screenshot have been reset.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Final Result Screenshots
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Flask app screen
![Flask app screen](http://media.discordapp.net/attachments/400469377998258179/771138782652399666/unknown.png "test")


Flask app after input
![Flask app after input](https://media.discordapp.net/attachments/400469377998258179/771138857335914496/unknown.png)


Following the generated link
![Following the generated link](https://media.discordapp.net/attachments/400469377998258179/771138980904960010/unknown.png)
