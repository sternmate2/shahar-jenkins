pipeline {
    agent any
    parameters {
        string(name: 'Dockerfile', defaultValue: 'Dockerfiletemp', description: 'Dockerfile name to build')
    }
    stages {
        stage('Test') {
            steps {
                sh ''' echo \'installing libs\'
                pip3 install .
                echo \'running tests\'
                python3 tests.py '''
            }
        }
        stage('Build') {
            steps {
                sh """ echo 'building docker image'
                echo ${params.Dockerfile}
                sudo docker build -t alison . -f ${params.Dockerfile} """
            }
        }
        stage('Artifact Push') {
            steps {
                echo 'Pushing to Artifactory....'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}