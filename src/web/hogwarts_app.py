from flask import Flask, request, jsonify
from openai_api import assistant
from openai_api import chat

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello World'


@app.route('/list_message')
def list_message():
    message_id = 'msg_BAqba4QIq3877Fz2OJmkkDTz'
    thread_id = 'thread_9s3MhO8HhGAmGb5tlOtrdNWw'
    message_list = assistant.get_thread_by_id(thread_id)
    for msg in message_list:
        print(msg.type())


@app.route('/chat_send_msg', methods=['POST'])
def chat_send_msg():
    msg = request.form['msg']
    content = chat.send_msg(msg).content

    return content


@app.route('/json/chat_send_msg', methods=['POST'])
def chat_send_msg_json():
    data = request.json  # 获取 JSON 数据
    # 进行其他处理...
    return jsonify(data)  # 发送回 JSON 响应


if __name__ == '__main__':
    app.run(debug=True)
