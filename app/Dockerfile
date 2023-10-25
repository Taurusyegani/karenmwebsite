FROM python:3.8-slim-buster
COPY . .
ADD main.py .
RUN pip install Flask
RUN pip install requests
CMD ["python3", "./main.py", "--host=0.0.0.0"]
EXPOSE 5001