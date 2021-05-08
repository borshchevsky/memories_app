FROM python:3.8.2
WORKDIR /code
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUDDERED 1
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /code/