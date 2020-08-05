pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
		echo"starting"
     		sh 'pip install flask'
	}

    }
    stage('test') {
      steps {
	sh 'pip install --upgrade pip'	
	echo"finesh"
	sh 'python test.py'
      }   
    }
  }
}
