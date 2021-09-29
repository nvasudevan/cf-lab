pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'echo "Hello World"'
                sh '''
                    date
                    echo "Multiline shell steps works too"
                    ls -lah
                    java -version
                '''`
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

