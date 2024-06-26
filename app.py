from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os

app = Flask(__name__)

line_bot_api = LineBotApi('uLGaElupG37Bss5I/R3olOyHxhS9fIhP6N4NT+Pi3coiTEj7p9RPxXFXy82cioCQPLFMY1/rg+tAUHZhkTOZyt+k+OrTZHvu9Rc0M4l4jK2eSRnuHRHqV67qK8pXEtLA7Dy3xZpXh0GaWYq329equwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f2a16670cf220b7b8cb8ed8637ade43b')


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)