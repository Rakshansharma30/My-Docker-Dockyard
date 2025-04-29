FROM mysql:8
ENV MYSQL_USER=user
# The MYSQL_PASSWORD should be passed securely as an environment variable during runtime
# ENV MYSQL_PASSWORD=rakshan
ENV MYSQL_DATABASE=mydb
COPY database.sql /docker-entrypoint-initdb.d/
