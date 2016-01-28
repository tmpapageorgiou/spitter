import requests

from spitter import logger


def send_notification(body, tokens):
    config = {
        "Content-Type": "application/json",
        "Authorization": "key=AIzaSyCaenkjxddv7_rjNdXnzw4M6Ri-mstPW4Q"
    }

    for token in tokens:
        payload = {
            "data": {"message": body},
            "to": token}

        logger.info("sending notification - %s", payload)

        resp = requests.post("https://gcm-http.googleapis.com/gcm/send",
                                json=payload,
                                headers=config)

        if not resp.status_code == 200:
            logger.warn("notification not sent - %s", str(resp.text))

        logger.info("notification sent - %s", str(resp.text))
