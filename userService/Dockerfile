FROM python:3.7-alpine
ADD . /app
WORKDIR /app
RUN apk add --no-cache gcc musl-devlinux-headers
RUN python3 -m pip install -r requirements.txt
COPY requirements.txt /app
COPY . .
EXPOSE 5001
ENV FLASK_APP=app
ENV FLASK_DEBUG=1
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5001"]


