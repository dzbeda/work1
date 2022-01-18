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
                //sh 'echo $VERSION/ > $WORKSPACE/version.txt '
            }
		    }
		    stage ('Publish') {
          environment {
               FOLDER= """${sh(script: 'echo $VERSION')}"""
          }
            // environment {
            //   FOLDER= """${sh(
            //     returnStdout: true,
            //     script: 'echo $VERSION > $workspace/version.txt'
            // )}"""
            // }
			      steps {
                    rtUpload (
    					             serverId: 'jfrog1',
    					             spec: '''{
                                  "files": [
                                     {
                                      "pattern": "$WORKSPACE/zip/*.zip",
                                      "target":  "binary-storage/${FOLDER}"
                                    }
                                 ]
                            }'''
    				         )
            }
		     }
    }
}
