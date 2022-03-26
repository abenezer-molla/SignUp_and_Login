from flask import Flask

from flask_restx import Api, Resource, fields
from config import DevConfig
from models import User
from exts import db
from flask_migrate import Migrate


#from models import Recipe,User
#from exts import db
#from flask_migrate import Migrate
#from flask_jwt_extended import JWTManager
#from recipes import recipe_ns
#from auth import auth_ns
#from flask_cors import CORS



'''
app = Flask(__name__)

app.config.from_object(DevConfig)

db.init_app(app)

migrate = Migrate(app, db)

api=Api(app,doc='/docs')


@api.route('/hello')

class HelloResources(Resource):
    def get(self):
        return {"message":"Aben is Here"}




@app.shell_context_processor

def make_shell_context():
    return {

        "db": db, 
        "User": User
    }

@api.route('/signup')

class SignUp(Resource):
    def port(Self):
        pass

@api.route('/login')

class Login(Resource):
    def post(self):
        pass

if __name__ == "__main__":
    app.run()



'''


def create_app(config):


    app=Flask(__name__)
    app.config.from_object(config)

    #CORS(app)

    db.init_app(app)

    migrate=Migrate(app,db)
    #JWTManager(app)



    api=Api(app,doc='/docs')

    #api.add_namespace(recipe_ns)
    #api.add_namespace(auth_ns)

    #model (serializer)
    @app.shell_context_processor
    def make_shell_context():
        return {
            "db":db,
            "user":User
        }



    return app

