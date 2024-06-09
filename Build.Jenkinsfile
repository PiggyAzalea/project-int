pipeline {
    agent any

    environment {
        IMG_NAME = "Build.Jenkinsfile:${BUILD_NUMBER}"
    }

    stages {
        stage('Build docker image') {
            steps {
                withCredentials(
                 [usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USERNAME', passwordVariable: 'USERPASS')]
              ) {
                    sh '''

                        docker login  -u $DOCKER_USERNAME -p $DOCKER_PASS
                        docker build -t $IMG_NAME
                        docker tag $IMG_NAME exaclly/$IMG_NAME
                        docker push exaclly/$IMG_NAME
                    '''
                }
            }
        }
    }
}