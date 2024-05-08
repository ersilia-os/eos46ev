FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install rdkit==2021.3.5
RUN pip install git+https://github.com/gadsbyfly/PyBioMed.git@45440d8a70b2aa2818762ceadb499dd3a1df90bc
RUN pip install git+https://github.com/bp-kelley/descriptastorus.git@9b133e2c91bb6a67df53db4cba992776db219ab7
RUN pip install scikit-learn==0.23.2
RUN pip install pandas==1.3.5
RUN pip install xgboost==0.90

WORKDIR /repo
COPY ./repo
