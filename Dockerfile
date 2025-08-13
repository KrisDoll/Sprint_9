# подгружаем образ linux с python:3.13
FROM python:3.13
# создаем папку app
WORKDIR /app
# копируем содержимое проекта в папку app
COPY . .
# устанавливаем зависимости проекта
RUN pip install --no-cache-dir -r requirements.txt pytest
# при старте контейнера запускаем команду pytest с генерацией отчета в папку allure-results
CMD ["pytest", "-v", "--alluredir=allure-results"]