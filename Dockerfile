# start by pulling the python image
FROM python:3.10.13-slim-bookworm

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# Environment variables
ENV PYTHONUNBUFFERED True

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
#ENTRYPOINT [ "python" ]

# CMD ["app.py" ]
CMD exec gunicorn --workers 2 --bind 0.0.0.0:8080 app:app --timeout 0
