from flask.blueprints import Blueprint
from application.blockchain import blockchain
import json

blockchain_json_dump = Blueprint('apipage', __name__, template_folder='templates')

@blockchain_json_dump.route('/api', methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return json.dumps({"length": len(chain_data),
                       "chain": chain_data})