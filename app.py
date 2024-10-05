from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)

# Load configuration based on environment
if os.environ.get('FLASK_ENV') == 'production':
    app.config.from_object('config.ProductionConfig')
elif os.environ.get('FLASK_ENV') == 'testing':
    app.config.from_object('config.TestingConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

CORS(app)  # Enable Cross-Origin Resource Sharing

db = SQLAlchemy(app)

# Blood Pressure Model
class BloodPressure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    systolic = db.Column(db.Integer, nullable=False)
    diastolic = db.Column(db.Integer, nullable=False)
    heart_rate = db.Column(db.Integer, nullable=False)
    measurement_time = db.Column(db.DateTime, default=datetime.utcnow)

# Initialize database using app context
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
