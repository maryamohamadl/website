from flask import Flask, jsonify, request
app = Flask(__name__)

items=[]

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/api/items', methods=['POST'])
def add_item():
    data=request.get_json()
    name=data.get('name','')
    items.append(name)
    return jsonify({"added":name})

@app.route('/health')
def health():
    return "ok"

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)
