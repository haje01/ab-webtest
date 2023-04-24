FROM python:3.10-slim-bullseye

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install chromium --with-deps

COPY --chown=python:python client.py .

CMD ["python", "client.py"]