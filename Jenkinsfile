pipeline {
    agent { docker { image 'python:3.9-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('test') {
            steps {
                sh 'python -c "import os; print(os.name)"'
            }
        }
        stage('deploy') {
            steps {
                sh 'python -c "sum=2+2;print(sum)"'
            }
        }
    }
}
