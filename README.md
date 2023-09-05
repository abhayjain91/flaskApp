# flaskApp
Python Flask App

## Deploy with Gunicorn - gunicorn service file
```
[Unit]
Description=Gunicorn instance to serve the api
After=network.target

[Service]
User=ubuntu
Group=ubuntu
WorkingDirectory=/home/ubuntu/flaskApp
Environment="PATH=/home/ubuntu/flaskApp/venv/bin"
ExecStart=/home/ubuntu/flaskApp/venv/bin/gunicorn --workers 4 --bind 0.0.0.0:5000 app:app

[Install]
WantedBy=multi-user.target
```

## To run locally in Docker
```
# To build the image
docker build -t flask-app .

# Something else runs on 5000 port in mac, so running on 8080
docker run -p 8080:8080 flask-app

# Some useful docker commands
docker ps -a
docker stop <container_id>
docker rm <container_id>
```

## Steps to Build on DockerHub and Deploy to AWS via GitHub Actions
https://blog.devops.dev/continuous-deployment-with-github-actions-dockerhub-and-aws-ec2-a-hands-on-tutorial-b01656a27963