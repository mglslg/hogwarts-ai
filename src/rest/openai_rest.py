from flask import request, jsonify
from openai_api import chat


def init_app(curr_app):
    @curr_app.route('/chat/single', methods=['POST'])
    def index():
        if not request.is_json:
            return jsonify({'error': 'Invalid content type'}), 400
        data = request.get_json()
        content = chat.send_msg(data['msg']).content
        return jsonify({'replay': content}), 200
