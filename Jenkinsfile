pipeline {
    agent any
    stages {
        stage('Compile-Package'){
            steps {
            git 'https://github.com/hassanbagheri-developer/java-ee1.git'
            sh "./script.sh"
            sh "/opt/maven/bin/mvn package"
            sh "/opt/maven/bin/mvn clean compile"
            sh "/opt/maven/bin/mvn package"
            }
        }
        
        // stage('create image'){
        //   steps {
        //         sh "docker build . -t 192.168.56.133:5000/java/firstweb/firstweb_image:${BUILD_NUMBER}"
        //         sh "docker push 192.168.56.133:5000/java/firstweb/firstweb_image:${BUILD_NUMBER}"
        //         }
        //     }
            

        
        stage('Test selenium'){
            agent { label 'myslave02'
            }
            steps {
                try {
                    python --version
                    currentBuild.result = "SUCCESS"
                    }
                catch (exc) {
                    currentBuild.result = "FAILURE"
                    }
            
            }
        }
        

        // stage('Test API'){
        //      steps {
        //       script {
        //         dir ('postman') {
        //             try {
        //                 sh 'npm run api-test'
        //                 currentBuild.result = "SUCCESS"
        //                 }
        //             catch (exc) {
        //                 currentBuild.result = "FAILURE"
        //                 }
        //             junit 'newman.xml'
        //             }
        //         }
        //     }
        // }

        // stage('Unit Test') {
        //     steps {
        //       sh 'whoami'
        //       script {
        //         try {
        //             sh 'pwd'
        //             sh '/opt/apache-maven-3.8.3/bin/mvn test'
        //             currentBuild.result = "SUCCESS"
        //             }
        //         catch (exc) {
        //             currentBuild.result = "FAILURE"
        //             }
        //         junit '**/target/surefire-reports/TEST*.xml'
        //         }
        //     }
        // }
        
        // stage('sonar'){
//       steps {
//         def mvnHome = tool name: '3.6.0', type: 'maven'
//         withSonarQubeEnv('Snoar_server') {
//         sh "${mvnHome}/bin/mvn sonar:sonar"
//   }}
//   }

        // stage('run image'){
        //   steps {
        //     sh "docker run -t -d -p 8080:8080 --rm --name firstweb 192.168.56.133:5000/java/firstweb/firstweb_image:${BUILD_NUMBER}"
        //         }
        //     }
        
        // stage('Docker Swarm'){
        //     agent { label 'swarm2'
        //     }
        //     steps {
        //     // sh "docker service create --name firstweb_image -p 8080:8080 --mode global --with-registry-auth 192.168.56.133:5000/java/firstweb/firstweb_image:${BUILD_NUMBER}"
        //         sh 'docker service update  --with-registry-auth --image 192.168.56.133:5000/java/firstweb/firstweb_image:${BUILD_NUMBER}  --update-parallelism 1 --update-delay 10s firstweb_image'
        //     }
        // }

        // stage('JIRA') {
        //     steps {
        //       script {
        //         response = jiraAddComment site: 'jira' , idOrKey: 'PROJ-38' ,  comment : "${JOB_NAME} => ${BUILD_NUMBER} - BUILD URL : ${BUILD_URL} => Status Job = ${currentBuild.currentResult}"
        //         jiraUploadAttachment file: 'Jenkinsfile', idOrKey: 'PROJ-38', site: 'jira'
        //         }
        //     }
        // }
    }
}
