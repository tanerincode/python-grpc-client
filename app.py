from flask import Flask, jsonify
from project_services.health_check_service import health_check_service
app = Flask(__name__)

@app.route('/healthcheck')
def healthcheck():
    # Call the gRPC client to check the health of the gRPC server
    status, message = health_check_service.check_health('localhost:9000')
    return jsonify({'status': status, 'message': message})

if __name__ == '__main__':
    app.run(debug=True)
