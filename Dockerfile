FROM python:3.7-slim
ENV MAX_ROWS=3000

RUN mkdir app
COPY main.ipynb app/main.ipynb
COPY utils.py app/utils.py
COPY Data_WP3_1_Geotagged_Images_v1.0.csv app/Data_WP3_1_Geotagged_Images_v1.0.csv
COPY requrements.txt app/requirements.txt
RUN pip install -r app/requirements.txt

EXPOSE 8888

CMD cd app && jupyter notebook --ip=0.0.0.0 --allow-root --no-browser
