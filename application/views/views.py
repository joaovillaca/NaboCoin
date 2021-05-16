<<<<<<< Updated upstream:application/views/views.py
from application import app
import json
=======
from flask import app, render_template
from flask.wrappers import JSONMixin
from application.Blockchain import Blockchain
>>>>>>> Stashed changes:application/routes.py

@app.route("/", methods=['GET'])
def homepage():
    
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
<<<<<<< Updated upstream:application/views/views.py
    return json.dumps({"length": len(chain_data),
                       "chain": chain_data})
=======
    
    JSONMixin.dumps({"length": len(chain_data),
                       "chain": chain_data})

    return render_template('homepage.html') 
    
>>>>>>> Stashed changes:application/routes.py
