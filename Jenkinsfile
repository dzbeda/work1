pipeline {
    agent {
        dockerfile {
              args '--privileged -v $WORKSPACE/zip:/zip -u root'
              //label 'zip-job-docker'
              reuseNode true
        }
    }
    stages {
        stage ('first') {
            steps {
                sh 'python3 --version'
                sh '/tmp/get_info.sh'
                sh 'echo $(hostname)'
                sh 'hostname'

            }
        }
		    stage ('Build') {
			      steps {
                sh 'python3 /tmp/zip_job.py'
            }
		    }
		    stage ('Show Log File') {
			      steps {
                sh 'cat /tmp/output.log'
            }
		    }
		    stage ('Publish') {
          // environment {
          //      FOLDER= sh(returnStdout: true,script: 'echo $VERSION')
          // }
			      steps {
                    rtUpload (
    					             serverId: 'jfrog1',
    					             spec: '''{
                                  "files": [
                                     {
                                      "pattern": "$WORKSPACE/zip/*.zip",
                                      "target":  "binary-storage/"
                                    }
                                 ]
                            }'''
    				         )
            }
		     }
    }
    post {
        always {
            cleanWs()
            step(emailext(attachLog: true, body: 'message', subject: 'hi', to: 'dudu.confirm@gmail.com'))
        }
    }
}
