pipeline {
    agent any

    environment {
        IMG_NAME = "project-int:${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build docker image') {
            steps {
                withCredentials(
                    [usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASS')]
                ) {
                    sh '''
                        cd project-int || exit 1
                        docker login -u $DOCKER_USERNAME -p $DOCKER_PASS
                        docker build -t $IMG_NAME .
                        docker tag $IMG_NAME exaclly/$IMG_NAME
                        docker push exaclly/$IMG_NAME
                    '''
                }
            }
        }
    }
}
