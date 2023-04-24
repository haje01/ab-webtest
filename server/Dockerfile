FROM python:3.10-slim-bullseye

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY templates templates
COPY --chown=python:python server.py .

EXPOSE 5000

CMD ["python", "server.py"]