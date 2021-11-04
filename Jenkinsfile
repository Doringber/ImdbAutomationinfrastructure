pipeline {
  agent none
  stages {
    stage('build') {
      agent {
        docker {
                  image 'python:3-alpine'
              }
            }
       steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install -r ./requirements.txt'
                    sh 'pytest -m smoke'
                }
            }
      steps {
        echo 'Build and git'
      }
    }

    stage('test') {
      parallel {
        stage('test') {
          steps {
            sh 'docker-compose -f docker-compose-v3.yml up'
          }
        }

        stage('pip') {
          steps {
            sh 'pip install -r ./requirements.txt'
          }
        }

        stage('run test') {
          steps {
            sh 'pytest -m smoke'
          }
        }

      }
    }
  }
}