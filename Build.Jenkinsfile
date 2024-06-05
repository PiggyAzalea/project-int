pipeline {
    agent any
    environment {
        // Define environment variables if needed
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build docker image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'your-credentials-id',
                                                 usernameVariable: 'DOCKER_USERNAME',
                                                 passwordVariable: 'DOCKER_PASSWORD')]) {
                    script {
                        // Use DOCKER_USERNAME and DOCKER_PASSWORD here
                        sh 'echo $DOCKER_USERNAME'
                        sh 'echo $DOCKER_PASSWORD'
                    }
                }
            }
        }
    }
}
