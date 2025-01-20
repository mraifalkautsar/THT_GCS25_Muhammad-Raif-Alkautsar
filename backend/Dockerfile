FROM python:3.11-slim
WORKDIR /app
COPY . .
ENV PYTHONPATH=/app
RUN pip install -r requirements.txt
CMD ["python", "app/main.py"]