FROM python:3.9-slim
RUN apt update && apt install -y build-essential git python3-pip python3-dev libssl-dev libffi-dev
WORKDIR /bot
COPY ./requirements.txt /config/
RUN pip install -r /config/requirements.txt

EXPOSE 3141 3142
