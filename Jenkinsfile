pipeline {
    agent any

    environment {
        IMAGE_NAME     = 'ev3-vuln-app'
        CONTAINER_NAME = 'ev3-vuln-app-container'
    }

    stages {

        stage('Build') {
            steps {
                echo 'Instalando dependencias y construyendo la imagen Docker...'
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install --upgrade pip && pip install -r requirements-fixed.txt pytest'
                sh "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} ."
            }
        }

        stage('Test') {
            steps {
                echo 'Ejecutando pruebas unitarias...'
                sh '. venv/bin/activate && pytest tests/ -v --junitxml=test-results.xml'
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Desplegando contenedor en entorno de prueba...'
                sh "docker rm -f ${CONTAINER_NAME} || true"
                sh "docker run -d --name ${CONTAINER_NAME} -p 5000:5000 ${IMAGE_NAME}:${BUILD_NUMBER}"
            }
        }
    }

    post {
        success {
            echo 'Pipeline completado correctamente. App disponible en http://localhost:5000/hello'
        }
        failure {
            echo 'Pipeline falló - revisar logs de la etapa correspondiente.'
        }
    }
}
