from flask import app
from flask.wrappers import JSONMixin
from application.Blockchain import Blockchain


@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in Blockchain.chain:
        chain_data.append(block.__dict__)
    return JSONMixin.dumps({"length": len(chain_data),
                       "chain": chain_data})