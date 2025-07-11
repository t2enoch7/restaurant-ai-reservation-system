FROM python:3.11-slim

WORKDIR /app


RUN apt-get update && \
  apt-get install -y git build-essential && \
  apt-get clean


RUN pip install --upgrade pip


# Dockerfile
ARG GITHUB_PAT
ENV GITHUB_PAT=${GITHUB_PAT}

RUN git config --global url."https://${GITHUB_PAT}:x-oauth-basic@github.com/".insteadOf "https://github.com/"
RUN pip install --no-cache-dir \
  git+https://github.com/aws-samples/aws-strands-sdk.git@main#egg=aws-strands-sdk



COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
