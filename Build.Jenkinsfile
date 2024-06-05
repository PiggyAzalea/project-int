pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Debug Workspace') {
            steps {
                sh 'ls -l'
                sh 'ls -l JenkinsProject'
            }
        }

        stage('Build docker image') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-credentials', variable: 'USERPASS')]) {
                    script {
                        dir('JenkinsProject/project-int') {
                            sh 'docker build -t my-image .'
                        }
                    }
                }
            }
        }
    }
}
