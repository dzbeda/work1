pipeline {
    agent {
        dockerfile {
              args '--privileged -v $WORKSPACE/zip:/zip -u root'
              reuseNode true
        }
    }
    stages {
        stage ('Agent information') {
            steps {
                sh '/tmp/get_info.sh'
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
         success {
           emailext(attachLog: true, body: 'Pleaee find attached log', subject: 'Job passed successfully', to: 'dudu.confirm@gmail.com;dudu.zbeda@gmail.com')
         }
         failure  {
           emailext(attachLog: true, body: 'Pleaee find attached log', subject: 'Job failed to run', to: 'dudu.confirm@gmail.com;dudu.zbeda@gmail.com')
         }
         always {
            cleanWs()
        }
    }
}
