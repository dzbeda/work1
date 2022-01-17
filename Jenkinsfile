pipeline {
    agent {
        dockerfile {
              args '--privileged -v $WORKSPACE/zip:/zip -u root'
              label 'zip-job-docker'
              reuseNode true
        }
    }
    environment {
        DUDU = "${env.VERSION}"
    }
    stages {
        stage ('first') {
            steps {
                sh 'python3 --version'
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
			      steps {
				        sh 'printenv'
                echo ${DUDU}
                rtUpload (
					             serverId: 'jfrog1',
					             spec: '''{
                              "files": [
                                 {
                                  "pattern": "$WORKSPACE/zip/*.zip",
                                  "target": "binary-storage/"+${DUDU}
                                }
                             ]
                        }'''
				         )
            }
		     }
    }
}
