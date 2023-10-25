FROM python:3.8-slim-buster
COPY . .
WORKDIR /app
EXPOSE 5001
ADD main.py .
RUN pip3 install Flask
RUN pip3 install requests
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]