FROM python:3.7

COPY . .

ENV FLASK_APP app.py
ENV PYTHONUNBUFFERED 1
RUN pip install -r requirements.txt
CMD ["gunicorn", "run:app"]
