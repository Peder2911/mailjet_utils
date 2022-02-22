FROM peder2911/uvicorn-deployment:2.1.2
COPY ./mailjet_utils /home/gunicorn/mailjet_utils
RUN pip install /home/gunicorn/mailjet_utils
ENV GUNICORN_ERROR_LOG_FILE="-"
ENV GUNICORN_ACCESS_LOG_FILE="-"
ENV GUNICORN_APP="mailjet_utils.app:app"
