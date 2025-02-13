from flask import Flask, jsonify
from flask_cors import CORS
from environment import *
from visual_crossing.controller.visual_crossing_controller import VisualCrossingController

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={
    r'/*': {
        'origins': '*'
    },
})

app.app_context().push()


@app.route('/', methods=["GET"])
def home():
    return {"message": "HOME CLIMA"}, 200


@app.route('/clima', methods=["GET"])
def index():
    return {"message": "API DASH CLIMA"}, 200


@app.route('/clima/<cidade>', methods=["GET"])
def get_clima(cidade):
    try:
        result = VisualCrossingController()
        return jsonify(result.get_clima_by_city(cidade)), 200
    except Exception as ex:
        print('Erro ao buscar dados', ex, flush=True)
        return {"message": "Erro ao buscar dados"}, 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
    # app.run(host=config.get('APP_FLASK_HOST'), port=config.get(
    #     'APP_FLASK_PORT'), debug=config.get('APP_FLASK_DEBUG'))
