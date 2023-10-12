FROM python:3.11.3-slim
ENV PYTHONDONTWRITEBYTECODE 1 \
ENV PIP_NO_CACHE_DIR off
ENV PYTHONUNBUFFERED 1
ENV PIP_DISABLE_PIP_VERSION_CHECK on

WORKDIR /bewise
COPY . /bewise

RUN apt-get update
RUN apt-get -y install libpq-dev gcc

RUN pip install -r requirements.txt \
 && chmod -R 777 "/bewise/logs/"

EXPOSE 8000
