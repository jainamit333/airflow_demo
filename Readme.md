# Airflow on Kubernetes

## Requirements
- Kubernetes Cluster
- Helm
- Docker

## Components
- Dags
- Airflow Docker Image


## Deployment Steps
- Update or Add Dags (inside dag folder)
- Update the dockerfile (if required to change to base image)
- Pipeline should be triggered whenever new version have to be released. That will create and push  new version of docker image which will be used to run the airflow dags.  

