FROM alpine:3.18
RUN apk --no-cache add python3 py3-pip
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8080
ENV FLASK_APP=app.py \ 
    RDS_MYSQL_HOST='database-1.cxgmewciebc6.ap-south-1.rds.amazonaws.com'\
    RDS_MYSQL_PORT=3306 \
    RDS_MYSQL_USER='root' \
    RDS_MYSQL_PASSWORD='#99Cmt88' \
    RDS_MYSQL_DATABASE='fuel' \
    AWS_ACCESS_KEY_ID='AKIAYTLER366LDBL4QMS' \
    AWS_SECRET_ACCESS_KEY='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' \
    AWS_REGION='ap-south-1' 
    # RDS_MYSQL_HOST=$RDS_MYSQL_HOST \
    # RDS_MYSQL_PORT=$RDS_MYSQL_PORT \
    # RDS_MYSQL_USER=$RDS_MYSQL_USER \
    # RDS_MYSQL_PASSWORD=$RDS_MYSQL_PASSWORD \
    # RDS_MYSQL_DATABASE=$RDS_MYSQL_DATABASE \
    # AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
    # AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
    # AWS_REGION=$AWS_REGION

CMD ["python", "app.py"]