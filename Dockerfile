FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install -c conda-forge rdkit
RUN conda install openbabel
RUN pip install git+https://github.com/ersilia-os/PyBioMed.git
RUN pip install git+https://github.com/bp-kelley/descriptastorus.git
RUN python3 -m pip install scikit-learn==1.1.1
RUN pip install pandas==1.4.3
RUN pip install torch==1.11.0
RUN pip install xgboost==0.90

WORKDIR /repo
COPY ./repo
