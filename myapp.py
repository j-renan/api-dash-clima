import os

from flask import Flask, jsonify
from flask_cors import CORS
from environment import *
from visual_crossing.controller.visual_crossing_controller import VisualCrossingController

app = Flask(__name__)
app.config['FLASK_RUN_PORT'] = os.environ.get('FLASK_RUN_PORT')
app.config['FLASK_RUN_HOST'] = os.environ.get('FLASK_RUN_HOST')
app.config['FLASK_RUN_DEBUG'] = os.environ.get('FLASK_RUN_DEBUG')

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
    result = VisualCrossingController()
    try:
        return jsonify(result.get_clima_by_city(cidade)), 200
    except Exception as ex:
        print('Erro ao buscar dados-----------', ex, result.get_clima_by_city(cidade).get('url'), flush=True)
        return {"message": "Erro ao buscar dados", "result": result.get_clima_by_city(cidade)}, 500


if __name__ == '__main__':
    app.run(host=app.config['FLASK_RUN_HOST'], port=app.config['FLASK_RUN_PORT'],
            debug=app.config['FLASK_RUN_DEBUG'])

