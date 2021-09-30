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
        stage('test') {
            agent { docker { image 'python:3.9-alpine' } }
            steps {
                sh '''
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
