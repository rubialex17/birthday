
# 3. Deploy

Here we have two different folders, one for deploying the PostgresDB into aws and another one in order to deploy the app to kubernetes cluster

## aws

Here there are some simple terraform files in order to deploy the db to aws and a script.sh to run the needed commands.

## k8s

Here we have the different files in order to deploy the app to kubernetes.

- deploy_first.sh that deploys the ingress, service, hpa, configmap and secrets that shouldn't be deployed anymore.

- deploy.sh with different steps:
    - Retrieve the code from github
    - Build the app
    - Run the different tests
    - Build the docker image
    - Push the docker image 
    - Deploy the deployment.yaml file with the new image

