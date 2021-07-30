FROM python:3.8
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY model /model/
COPY load_data.py .
RUN pip install -e model

CMD [ "python", "model/api.py" ]
