import flask_restful as restful
from flask import request
import sys
import json

class clsinfo(restful.Resource):     


    def post(self):

        self.data = request.get_json()
        self.contactno = self.data['contactno']
        self.myid= self.data['myid']
        

        try:
            ansible_cmd = '/etc/ansible/myansible/ansible-playbook -i %s, /home/shivam/myplaybook.yml -e myid=%s -e contactno=%s ' % (self.contactno, self.contactno, self.myid)
            os.system(ansible_cmd)
        except Exception as e:
            print(e)

#Check app.py for function call.
