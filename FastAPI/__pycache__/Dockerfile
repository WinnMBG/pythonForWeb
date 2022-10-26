FROM python:3.8
SHELL ["/bin/bash","-c"]

WORKDIR /FastAPI

COPY . /FastAPI

RUN source bin/activate
RUN pip install -r app/requirements.txt
RUN pip install "uvicorn[all]"

EXPOSE 80

CMD ["uvicorn", "app.main:app","--host","0.0.0.0","--port","8000", "--reload"]
