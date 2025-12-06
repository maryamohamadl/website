import os
from flask import Flask, render_template, request, jsonify
import requests
app=Flask(__name__)
BACKEND_URL=os.environ.get("BACKEND_URL","http://backend:5000")
@app.route('/')
def index():
    try:
        r=requests.get(f"{BACKEND_URL}/api/items")
        items=r.json()
        return render_template('index.html', items=items)
    except Exception as e:
        return render_template('index.html', items=[], error=str(e))
@app.route('/submit', methods=['POST'])
def submit():
    name=request.form.get('name')
    try:
        r=requests.post(f"{BACKEND_URL}/api/items", json={'name':name})
        return jsonify({'ok':True})
    except Exception as e:
        return jsonify({'ok':False,'error':str(e)})
if __name__=='__main__':
    app.run(host='0.0.0.0', port=3000)
