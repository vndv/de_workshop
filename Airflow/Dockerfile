FROM apache/airflow:2.2.2

ENV AIRFLOW_HOME=/opt/airflow

WORKDIR $AIRFLOW_HOME

USER root
RUN apt-get update

COPY requirements.txt .

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install --no-cache-dir -r requirements.txt


COPY scripts scripts
RUN chmod +x scripts

USER $AIRFLOW_UID