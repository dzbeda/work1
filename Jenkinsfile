pipeline {
    agent {
        dockerfile {
              args '--privileged -v $WORKSPACE/zip:/zip -u root'
              reuseNode true
              //label 'zip-job-docker'
        }
    }
    stages {
        stage ('first') {
            steps {
                sh 'python3 --version'
                sh '/tmp/get_info.sh'
                sh "pwd"

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
                rtUpload (
					             serverId: 'jfrog1',
					             spec: '''{
                              "files": [
                                 {
                                  "pattern": "$WORKSPACE/zip/*.zip",
                                  "target": "binary-storage/"
                                }
                             ]
                        }'''
				         )
            }
		     }
    }
}
