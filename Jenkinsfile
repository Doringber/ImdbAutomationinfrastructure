pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        echo 'Build and git'
      }
    }

    stage('test') {
      steps {
        sh 'sh run.sh'
      }
    }

  }
}