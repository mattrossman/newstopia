FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m nltk.downloader punkt

COPY . .
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "api.py" ]