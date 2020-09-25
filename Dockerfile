FROM python:3.8.4-alpine3.12

RUN apk update \
    && apk add --update build-base \
    && apk add --no-cache libffi-dev \
    && apk add --no-cache tzdata

RUN apk add tzdata \
    && pip install gunicorn

WORKDIR /app-run

COPY requirements.txt /app-run/requirements.txt
RUN pip install -r /app-run/requirements.txt
COPY . /app-run

#ENTRYPOINT ["gunicorn", "-w 4", "--bind", "0.0.0.0:8000", "--access-logfile", "-", "--error-logfile", "-", "server:app"]

#ENTRYPOINT ["uvicorn" "main:app" "--reload" "--port=8000" "--host=0.0.0.0"]
CMD uvicorn main:app --reload --port=8000 --host=0.0.0.0