from flask import Flask, render_template, request, jsonify
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    text = request.form['text']
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save("static/output.mp3")
    return jsonify({'success': True, 'audio_url': 'static/output.mp3'})

if __name__ == "__main__":
    app.run(debug=True)
