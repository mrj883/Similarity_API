FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip intstall --no-cache-dir -r requirements.txt
RUN pip instal ./en_core_web_sm_1.2.0.tar.gz
COPY . .
CMD ["python", "run.py"]