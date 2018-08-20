node {
    stage('checkout') {
      checkout scm
    }
    stage('prepare') {
      sh "git clean -fdx"
    }
    stage('compile') {
      sh "python API.py &"
    }
    stage('test') {
      echo "nothing to do"
    }
    stage('package') {
      echo "nothing to do"
    }
    stage('publish') {
      echo "uploading package..."    }
    }