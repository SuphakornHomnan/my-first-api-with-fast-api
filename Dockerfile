FROM python:3.8.2

WORKDIR /dir

COPY ./requirements.txt /dir/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /dir/requirements.txt

COPY ./app /dir/app

ENTRYPOINT ["uvicorn", "app.main:app", "--reload","--proxy-headers","--host","0.0.0.0", "--port", "80"]