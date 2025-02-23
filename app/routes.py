from flask import Blueprint, jsonify, current_app
# from app.consumer import ForkliftDataConsumer

monitoring_bp = Blueprint('monitoring', __name__)


@monitoring_bp.route('/get-forklift-status/<string:forklift_id>',
                     methods=['GET'])
def get_forklift_status(forklift_id: str):
    try:
        loader_manager = current_app.loader_manager
        loader = loader_manager.get_loader_by_id(forklift_id)
        print(loader.loader_id)
        return jsonify({
            'forklift_id': loader.loader_id,
            'name': 'KoneKranes',
            'status': loader.status
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@monitoring_bp.route('/get-all-forklifts', methods=['GET'])
def get_all_forklifts():
    try:
        all_forklifts = []
        for forklift_id in ['loader_001', 'loader_002']:
            all_forklifts.append({
                'forklift_id': forklift_id,
                'name': 'KoneKranes',
                'status': 'full'
            })
        return jsonify(all_forklifts), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
