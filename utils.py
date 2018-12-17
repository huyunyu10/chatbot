import requests
import os

GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAEO1XPWFa4BAE7C0DlmZAKhjBCcLkqu2eSRv2rSH6zbqxXeOtV7ZC1qdZAxa8ZCNpENHHqfti03aSSHtnRUopnJYPhxStIkjowPr40JO15mLLgn51rGfg3920mtZCzBLnIPrFB2OoBHfGd8Sb8RKzxQFsEPcif5Vq7cklLLwinuhB2oj1TbK"
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
