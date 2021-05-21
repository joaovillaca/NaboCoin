from flask.blueprints import Blueprint
from application.blockchain import blockchain
import json

blockchain_json_dump = Blueprint('jsonpage', __name__, template_folder='templates')

@blockchain_json_dump.route('/jsondump', methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return json.dumps({"length": len(chain_data),
                       "chain": chain_data})

from flask_restful import Resource

class Blockchain_api_dump(Resource):

    def get(self):
        return get_chain()