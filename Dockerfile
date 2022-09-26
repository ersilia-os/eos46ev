FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install rdkit
RUN pip install git+https://github.com/ersilia-os/PyBioMed.git
RUN pip install git+https://github.com/bp-kelley/descriptastorus.git
RUN pip install scikit-learn==0.23.2
RUN pip install pandas==1.3.5
RUN pip install xgboost==0.90

WORKDIR /repo
COPY ./repo
