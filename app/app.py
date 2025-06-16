from flask import Flask, render_template, request, redirect
from dns_manager import create_txt_record, get_original_url
from dotenv import load_dotenv
import hashlib
import os

load_dotenv(dotenv_path='.env')

app = Flask(__name__)
DOMAIN_NAME = os.getenv('DOMAIN_NAME')

def shortener_url(original_url):
    return hashlib.sha256(original_url.encode()).hexdigest()[:6]

@app.route('/url-shortener', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['url']
        short_url = shortener_url(original_url)
        if create_txt_record(short_url, original_url):
            short_link = f"https://{DOMAIN_NAME}/{short_url}"
            return render_template('index.html', short_url=short_link, original_url=original_url)
        return "Error creating DNS TXT record", 500
    return render_template('index.html')

@app.route('/<short_url>')
def redirect_url(short_url):
    original_url = get_original_url(short_url)
    if original_url:
        return redirect(original_url)
    return "Short url not found", 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
