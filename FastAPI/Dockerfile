FROM python:3.8

WORKDIR /FastAPI

COPY . /FastAPI

RUN pip install -r requirements.txt
RUN pip install "uvicorn[all]"

EXPOSE 80

ENTRYPOINT ["uvicorn", "main:app", "--reload"]

