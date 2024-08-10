from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the local server!'

@app.route('/location', methods=['GET'])
def get_location():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    if lat and lon:
        return jsonify({'status': 'success', 'latitude': lat, 'longitude': lon})
    return jsonify({'status': 'error', 'message': 'No location data received'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
