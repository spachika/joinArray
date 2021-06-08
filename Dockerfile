FROM python:latest
WORKDIR /app
ADD ./joinArray.py /app
ADD ./__main__.py /app
ENTRYPOINT [ "python", "-m", "joinArray"]