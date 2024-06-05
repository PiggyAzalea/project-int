pipeline {
    agent any
    stages {
        stage('Build docker image') {
            steps {
                    sh '''
                        cd project-int

                        docker build -t project-int:${BUILD_NUMBER} .
                        docker push exaclly/project-int:${BUILD_NUMBER}
                    '''

            }
        }
    }
}