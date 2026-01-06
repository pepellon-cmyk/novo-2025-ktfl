from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to Kite for Life!',
        'status': 'running',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
