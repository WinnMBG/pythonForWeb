FROM python:3.8

WORKDIR /ProjetStreamlit

COPY . /ProjetStreamlit

RUN pip install cmake
RUN pip install -r requirements.txt

EXPOSE 8051

ENTRYPOINT ["streamlit", "run", "projet.py", "--server.port=8501", "--server.address=0.0.0.0"]

