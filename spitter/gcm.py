import requests

from spitter import logger


class GCM

    @staticmethod
    def send_notificatin(body, token):
        config = {
            "Content-Type": "application/json",
            "Authorization": "key=AIzaSyCaenkjxddv7_rjNdXnzw4M6Ri-mstPW4Q"
        }
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
