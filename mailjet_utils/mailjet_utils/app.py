
import logging
from fastapi import FastAPI
from . import models

app = FastAPI()
logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

@app.post("/{version}/send")
def send_mail(send_data: models.SendData):
    for message in send_data.Messages:
        users = ", ".join([u.Email for u in message.To])
        logger.info((
            f"Send email to {users} "
            f"from {message.From.Email}. "
            f"\"{message.Subject}\" "
            f"({len(message.HTMLPart)} characters)"
            ))

