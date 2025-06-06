from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Simulated intersection data
intersections = [
    {
        "name": "迎泽大街与建设南路",
        "location": [37.8716, 112.5624],
        "flow": 820,
        "truck_rate": 0.32,
        "suggestion": "延长绿灯15秒"
    },
    {
        "name": "长风街与滨河东路",
        "location": [37.8562, 112.5711],
        "flow": 730,
        "truck_rate": 0.28,
        "suggestion": "保持当前配时"
    },
    {
        "name": "亲贤街与平阳路",
        "location": [37.8441, 112.5789],
        "flow": 920,
        "truck_rate": 0.35,
        "suggestion": "缩短红灯10秒"
    }
]

@app.route('/api/intersections')
def get_intersections():
    return jsonify(intersections)

@app.route('/api/vehicle_types')
def get_vehicle_types():
    return jsonify({
        "labels": ["小型车", "公交车", "货车", "摩托车"],
        "data": [550, 120, 80, 30]
    })

if __name__ == '__main__':
    app.run(debug=True)
