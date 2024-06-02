pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "hellow world"
                sh '''
                    echo "Multiline shell steps works too"
                    ls -lah
                '''
            }
        }
    }
}