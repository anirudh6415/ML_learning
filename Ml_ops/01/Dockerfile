FROM python:3.11.7-slim-bookworm

WORKDIR /opt/src

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt && rm -rf /root/.cache/pip

COPY . .

ENTRYPOINT ["python", "inference.py" ]