pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "=> $(date)"
                echo 'Building Hello World ...'
            }
        }
        stage('Test') {
            steps {
                echo "=> $(date)"
                echo 'Testing Hello World ...'
            }
        }
        stage('Deploy') {
            steps {
                echo "=> $(date)"
                echo 'Deploying Hello World ...'
            }
        }        
    }
}

