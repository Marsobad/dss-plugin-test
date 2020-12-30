from dataiku.customwebapp import *

# Access the parameters that end-users filled in using webapp config
# For example, for a parameter called "input_dataset"
# input_dataset = get_webapp_config()["input_dataset"]

import dataiku
import pandas as pd
from flask import request

@app.route('/post_parameter',methods=['POST'])
def get_parameter():
    data = request.form
    print(data)
    #config = json.loads(request.data)
    return json.dumps({"status": "ok", "data": 66})
