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
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                    date
                    echo "Multiline shell steps works too"
                    ls -lah
                    javac -version
                '''
            }
        }
        stage('Deploy') {
            steps {
                sh '''
                    date
                    echo "Multiline shell steps works too"
                    ls -lah
                    java -jar
                '''
            }
        }        
    }
}

