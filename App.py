from flask import Flask, send_file, request, jsonify
from config import Settings
from video_service import VideoService

app = Flask(__name__, static_folder='../frontend/public', static_url_path='/')
video_service = VideoService()

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/video', methods=['POST'])
def get_video():
    data = request.json
    file_id = data.get('file_id')
    if not file_id:
        return jsonify({'error': 'file_id required'}), 400
    try:
        file_path = video_service.save_video(file_id)
        return jsonify({'url': f"/videos/{file_id}.mp4"}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/videos/<filename>')
def serve_video(filename):
    return send_file(f"videos/{filename}", mimetype='video/mp4')

if __name__ == '__main__':
    app.run(host=Settings.FLASK_HOST, port=Settings.FLASK_PORT)
                
