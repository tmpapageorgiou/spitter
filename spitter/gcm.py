import grequests

from spitter import logger


def send_notification(body, tokens):
    config = {
        "Content-Type": "application/json",
        "Authorization": "key=AIzaSyCaenkjxddv7_rjNdXnzw4M6Ri-mstPW4Q"
    }

    payload = {"data": {"message": body}, "registration_ids": tokens}

    url = "https://gcm-http.googleapis.com/gcm/send"
    response = irequests.post(url, json=payload, headers=config)

    logger.info("sending notification - %s", str(response))

    if not response.status_code == 200:
        logger.warn("notification not sent - %s", str(response.text))

    logger.info("notification sent - %s", str(response.text))
