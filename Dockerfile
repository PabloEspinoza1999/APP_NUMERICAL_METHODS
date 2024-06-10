FROM python:3.10-alpine

WORKDIR /app

#Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#Copy source code
COPY src/ ./

#Copy environment file
COPY .env ./

EXPOSE 8000

#CMD [ "python", "python manage.py runserver 0.0.0.0:8000" ]
