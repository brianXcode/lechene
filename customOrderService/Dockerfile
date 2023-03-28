FROM python:3.7-alpine
ADD . /app
WORKDIR /app
COPY requirements.txt /app
RUN python3 -m pip install -r requirements.txt
COPY . .
EXPOSE 5003
ENV FLASK_APP=app
ENV FLASK_DEBUG=1
CMD ["flask", "run", "--host", "0.0.0.0"]