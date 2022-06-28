FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install -c conda-forge rdkit
RUN pip install git+https://github.com/ersilia-os/PyBioMed.git
RUN pip install git+https://github.com/bp-kelley/descriptastorus.git
RUN python3 -m pip install sklearn
RUN pip install pandas
RUN pip install xgboost

WORKDIR /repo
COPY ./repo
