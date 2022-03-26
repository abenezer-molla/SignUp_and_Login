from flask import Flask, request, jsonify

from flask_restx import Api, Resource, fields
from config import DevConfig
from models import User
from exts import db
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, jwt_required

#from models import Recipe,User
#from exts import db
#from flask_migrate import Migrate
#from recipes import recipe_ns
#from auth import auth_ns
#from flask_cors import CORS
#jwt_required()



def create_app(config):


    app=Flask(__name__)
    app.config.from_object(config)

    #CORS(app)

    db.init_app(app)

    migrate=Migrate(app,db)
    JWTManager(app)



    api=Api(app,doc='/docs')


    #model (serializer)
    @app.shell_context_processor
    def make_shell_context():
        return {
            "db":db,
            "user":User
        }



    signup_model = api.model(
        'SignUp', 
        {
            "username": fields.String(),
            "email": fields.String(), 
            "password": fields.String()
        }
    )

    login_model = api.model(

        'Login', 
        {
            'username': fields.string(), 
            'password': fields.string(),
        }
    )

    @api.route('/signup')

    class SignUp(Resource):
        #@api.marshal_with(signup_model)
        @api.expect(signup_model)
        def post(self):
            data = request.get_json()

            username = data.get('useername')
            db_user = User.query.filter_by(username = username).first()

            if db_user is not None:
                return jsonify("This username already exists")

            new_user = User(
                username = data.get('username'),
                email = data.get('email'), 
                password = generate_password_hash(data.get('password'))
            )


            new_user.save()

            return jsonify({"message": "User Created Successfully!"})


    
    @api.route('/login')

    class Login(Resource):
        @api.expect(signup_model)
        def post(self):
            data = request.get_json() 

            username = data.get('username')
            password = data.get('password')

            db_user = User.query.filter_by(username = username).first()

            if db_user and check_password_hash(db_user.password, password):
                access_token = create_access_token(identity = db_user.username)
                refresh_token = create_refresh_token(identity = db_user.username)

                return jsonify(
                    {
                        "access_token" : access_token, 
                        "refresh_token": refresh_token
                    }
                )



    return app

