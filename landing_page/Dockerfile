FROM python:3.11
COPY . .
ADD main.py .
RUN pip install Flask
RUN pip install requests
CMD ["python3", "./main.py"]
EXPOSE 5001