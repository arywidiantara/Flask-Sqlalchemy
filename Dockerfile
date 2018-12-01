FROM python:3.7-alpine
MAINTAINER arywidiantara33@gmail.com
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "flaskexample.py"]
