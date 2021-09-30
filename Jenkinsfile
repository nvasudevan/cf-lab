pipeline {
    agent none

    options {
        ansiColor('xterm')
    }

    stages {
        stage('build') {
            agent { docker { image 'python:3.9-alpine' } }
            steps {
                sh 'python -m py_compile src/ec2.py'
                stash(name: 'compiled-results', includes: 'src/*.py*' )
            }
        }
        stage('build-docker') {
            agent { label 'master' }
            steps {
                sh 'docker build -t jenkins-python3 .'
            }
        }
        stage('test') {
            agent { docker { image 'jenkins-python3' } }
            steps {
                sh '''
                    pip install -U pytest troposphere
                    py.test --verbose --junit-xml test-reports/results.xml src/ec2_test.py
                   '''
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
        stage('deploy') {
            agent { docker { image 'jenkins-python3' } }
            steps {
                dir(path: env.BUILD_ID) {
                    unstash(name: 'compiled-results')
                    sh '''
                        ls -la 
                        pip install -U troposphere
                        python src/ec2.py
                        ls -al ./ ./src/
                       '''
                    stash(name: 'cf-json', includes: 'cf_lab.json' )
                }
            }
        }
        stage('terraform') {
            agent any
            environment {
                IMAGE = "hashicorp/terraform"
                JSON_DIR = "env.BUILD_ID"
            }
            steps {
                dir(path: "${JSON_DIR}") {
                    unstash(name: 'cf-json')
                }
                sh '''
                    ls -la 
                    docker run -v ${JSON_DIR}:/json ${IMAGE} version
                '''
            }
        }
    }
}
