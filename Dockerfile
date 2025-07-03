FROM python:3.10-slim

WORKDIR /app

copy requirement.txt requirement.txt

RUN pip install -r requirement.txt

copy . .


EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]