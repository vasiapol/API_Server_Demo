node {
    stage('checkout') {
      checkout scm
    }
    stage('prepare') {
      def customImage = docker.build("api:${env.BUILD_ID}")

    customImage.inside {
        sh 'make test'
#sh "git clean -fdx"
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