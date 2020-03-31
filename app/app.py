from flask import Flask, request, render_template
from flask_restful import Resource, Api, fields, marshal, reqparse
from datetime import datetime
import dateutil.parser
import pytz 
import sys
from  pathlib import Path
_current_root = str(Path(__file__).resolve().parents[0])
sys.path.append(_current_root)
from api import auth, industry, report, kpi, comment, summary

tz = pytz.timezone('Asia/Shanghai')
app = Flask(__name__)

api = Api(app)

#api.add_resource(auth.AuthLoginApi, '/api/auth/login')
#api.add_resource(xxxApi, '/api/xxx/<string:user>/', methods = ['GET'])

@app.route('/', defaults={'path':''},   methods=['GET'])
@app.route('/<path:path>',  methods=['GET'])
def industryChain_app_index(path):
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=7089)
