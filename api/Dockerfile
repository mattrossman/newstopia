FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m nltk.downloader punkt

COPY . .
ENV FLASK_APP api.py
EXPOSE 5000
CMD flask run --host=0.0.0.0