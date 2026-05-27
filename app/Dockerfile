FROM python:3.13-slim
WORKDIR /app
RUN pip install flask
COPY app.py .
EXPOSE 8098
CMD ["python", "app.py"]
