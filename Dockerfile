# usar imagem base oficial do Python
FROM python:3.11-slim-buster

# definir diretório de trabalho
WORKDIR /usr/src/app

# definir variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# instalar dependências do sistema
RUN apt-get update \
  && apt-get install -y libpq-dev gcc \
  && apt-get clean 

# instalar dependências do Python
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./app /usr/src/app/
