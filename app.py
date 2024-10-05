from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import db, BloodPressure  # 导入 models 和 db
from datetime import datetime

app = Flask(__name__)
app.config.from_object('config.Config')

CORS(app)  # Enable Cross-Origin Resource Sharing

# 初始化 SQLAlchemy
db.init_app(app)

# 创建数据库表
with app.app_context():
    db.create_all()

# POST: Add new blood pressure record
@app.route('/api/bloodpressure', methods=['POST'])
def add_bloodpressure():
    data = request.get_json()
    new_record = BloodPressure(
        systolic=data['systolic'],
        diastolic=data['diastolic'],
        heart_rate=data['heart_rate'],
        measurement_time=datetime.strptime(data['measurement_time'], '%Y-%m-%d %H:%M:%S')
    )
    db.session.add(new_record)
    db.session.commit()
    return jsonify({"message": "Record added"}), 201

# GET: Fetch all blood pressure records
@app.route('/api/bloodpressure', methods=['GET'])
def get_bloodpressure():
    records = BloodPressure.query.all()
    result = [
        {
            "systolic": record.systolic,
            "diastolic": record.diastolic,
            "heart_rate": record.heart_rate,
            "measurement_time": record.measurement_time.strftime('%Y-%m-%d %H:%M:%S')
        }
        for record in records
    ]
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)
