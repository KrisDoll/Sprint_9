FROM python:3.10-slim  # ← 3.13 ещё не стабилен, лучше 3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .