########### BASE IMPORTS ###############################
from flask import Flask, Response
import base64
import flask_restful as restful

app = Flask(__name__)
apy = restful.Api(app)


from myinfodir.info import clsinfo                       #myinfodir contains info.py which has class clsinfo inside it.
apy.add_resource(clsinfo, '/api/v0.1/clsinfo')           #specifying end point url


if __name__ == '__main__':
    #app.run(host='0.0.0.0', debug=True,threaded=True)
    app.run()

#Reference
#https://buildmedia.readthedocs.org/media/pdf/flask-restful/latest/flask-restful.pdf
