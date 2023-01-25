from flask import Flask, request, jsonify

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import os
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL=os.environ['DATABASE_URL']
DATABASE_PORT=os.environ['DATABASE_PORT']
DATABASE_NAME=os.environ['DATABASE_NAME']
DATABASE_USER=os.environ['DATABASE_USER']
DATABASE_PASS=os.environ['DATABASE_PASS']

application = Flask(__name__)

application.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{DATABASE_USER}:{DATABASE_PASS}@{DATABASE_URL}:{DATABASE_PORT}/{DATABASE_NAME}"

db = SQLAlchemy(application)
migrate = Migrate(application, db)
application.app_context().push()

class UserModel(db.Model):
    __tablename__ = 'userdata'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, id,name):
        self.id = id
        self.name = name

db.create_all()
@application.route('/')
def index():
    return jsonify({'hello': 'world'})

@application.route('/user',methods=['GET','POST'])
def userDetails():

    if request.method == 'GET':

       if 'id' not in request.form:
          resp = jsonify({'message' : 'No Id to query'})
          resp.status_code = 400
          return resp

       result = UserModel.query.filter_by(id=request.form.get('id')).first()
       if result is None:
          resp = jsonify({'message' : 'User Not Found'})
          resp.status_code = 404
          return resp
       
       resp = jsonify({'id':result.id,'name':result.name})
       resp.status_code = 200
       return resp

    if request.method == 'POST':

       if 'id' not in request.form or 'name' not in request.form:
          resp = jsonify({'message' : 'No id or name field. Both necessary.'})
          resp.status_code = 400
          return resp

       name = request.form.get('name')
       id = request.form.get('id')
       entry = UserModel(id=id,name=name)
       db.session.add(entry)
       db.session.commit()
       resp = jsonify({'message' : 'User Added Successfully'})
       resp.status_code = 201
       return resp

    resp = jsonify({'message' : 'Unsupported Method'})
    resp.status_code = 400
    return resp

if __name__=="__main__":
    application.run()