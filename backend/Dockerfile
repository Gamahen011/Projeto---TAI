FROM python:3.12-slim

WORKDIR /Projeto---TAI

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY rotas.py .

COPY Classes/ ./Classes/

EXPOSE 5000

CMD ["python3", "rotas.py", "0.0.0.0:5000"]
