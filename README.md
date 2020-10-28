# CircleCI

This was a personal project to design a docker flask app and setup a CI/CD pipeline with CircleCi to build and deploy my docker images to Amazon Web Services' Elastic Container Orchestration Service. 

When pushed to GitHub, CircleCi builds and deploys a docker image from this repo. If the image fails the pre determined test, the deployment will terminate. Once the image passes the test stage, it gets deployed to your AWS ECS cluster. Deployment using this pipeline prevents any faulty code from deployment while offering zero downtime between deployments.

The app.py file is a python flask application that uses the AWS SDK to create an S3 bucket and object based off of user input. The other python file is a simple test for CircleCi to run. The dockerfile uses a python base image with a working directory of /app, it installs the neccescary python modules, moves everything into the /app directory, and then it runs the app.py code. 

The CircleCi folder contains the config file for the service. This file tells CircleCi how the deployment is handled. The templates folder contain the index.html for the flask app. 

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

Setup for ECS can be found on circleci's blog (here)[https://circleci.com/blog/use-circleci-orbs-to-build-test-and-deploy-a-simple-go-application-to-aws-ecs/].

<pre>
Changes to make if you run this.
- On line 40 of app.py, change 'LocationConstraint': 'us-west-1' to the region that you created your ECS cluster in.
- 
</pre>

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
DISCLAIMER: This requires input of AWS Access keys. This app was created as an example app that you would deploy with CircleCi. Entering your credentials anywhere is bad practice and is best not done. Access keys used in screenshot have been reset.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Final Result Screenshots
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
![Screenshot 1](https://i.imgur.com/CASMeai.png)
![Screenshot 2](https://i.imgur.com/mNDx3HO.png)
![Screenshot 3](https://i.imgur.com/BkfMb9p.png)
