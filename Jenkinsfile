pipeline {
  agent any
  stages {
    stage('build') {
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