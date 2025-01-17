FROM python:3.13

WORKDIR /app

COPY ./src/ /app/
COPY ./requirements.txt /app/

RUN pip install --no-cache-dir -r /app/requirements.txt

CMD [ "/app/userimport.py"]
