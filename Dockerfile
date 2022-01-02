# Pull base image.
FROM tomcat

#RUN 
# Update
#apt-get update -y && \
# Install Java
#apt-get install default-jre -y

ADD ./target/firstWeb.war /usr/local/tomcat/webapps/firstWeb.war
  
#EXPOSE 8080

CMD bash /usr/local/tomcat/bin/startup.sh ; tail -f /dev/null
#CMD ["/usr/local/tomcat/bin/startup.sh", "run"]


######### http://192.168.56.133:8080/firstWeb/
