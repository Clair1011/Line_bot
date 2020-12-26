from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('3dPSSPHHhol/LUyjueTC1FV16R1/piYT8SBnloI6feDNOUN5JaTKNy61adQ433I6yPo07KYzAedknw7GNwug6uAgOw/BakyUdo2uQILeumDGnJYLdHEQWSW4B5g/rJFprKZp+INHnETtwQT2OklSpwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('da408c8950ee12ac7ab11386fea56c01')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='你吃飯了嗎'))


if __name__ == "__main__":
    app.run()