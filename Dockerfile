FROM python:3.9-slim-buster
RUN opt update -y && opt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install requirements.txt
CMD ["python","app.py"]
