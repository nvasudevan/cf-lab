pipeline {
    agent none
    stages {
        stage('build') {
            agent { docker { image 'python:3.9-alpine' } }
            steps {
                sh 'python -m py_compile src/ec2.py'
                stash(name: 'compiled-results', includes: 'src/*.py*' )
            }
        }
        stage('build-docker') {
            agent { label 'docker' }
            steps {
                sh 'docker build -t jenkins-python3 .'
            }
        }
        stage('test') {
            agent { docker { image 'jenkins-python3' } }
            steps {
                sh '''
                    env
                    id
                    pip install -U pytest troposphere
                    py.test --verbose --junit-xml test-reports/results.xml ec2_test.py
                   '''
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
        stage('deploy') {
            agent { docker { image 'python:3.9-alpine' } }
            steps {
                sh 'python -c "sum=2+2;print(sum)"'
            }
        }
    }
}
