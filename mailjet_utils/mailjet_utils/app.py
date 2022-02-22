
import logging
from fastapi import FastAPI
from . import models

app = FastAPI()
logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

@app.get("/{version}/send")
def send_mail(send_data: models.SendData):
    for message in send_data:
        logger.info((
            f"Send email to {message.To} "
            f"from {message.From}. "
            f"\"{message.Subject}\" "
            f"({len(message.HTMLPart)} characters)"
            ))

