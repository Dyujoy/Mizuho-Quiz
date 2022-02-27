from flask import request, jsonify
from models import User
from app import app
from flask_jwt_extended import (create_access_token, get_jwt_identity, jwt_required)


@app.route('/register', methods=['POST'])
def register():
    """
    Used to register a user.

    :parameter:
    email (string) : Email of the user
    password (string) : Password of the user
    name (string) : Name of the user

    :return:
    List[dict] : response
        success: bool,
        message: string

    """
    try:
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')

        check_prev_user = User.query.filter(User.email == email and User.password == password).first()

        if check_prev_user == None:
            user = User(email=email, name=name, password= password)
            user.addUsers()
            response = jsonify({'success': True, 'message': 'User registered'}), 200
        else:
            response = jsonify({'success': False, 'message': 'User already registered registered'}), 400


    except Exception as e:
        response = jsonify({'success': False, 'message': str(e)}), 400

    return response


@app.route('/login', methods=['POST'])
def login():
    """
    Used to login a preregistered user.

    :parameter:
        email (string) : Email of the user
        password (string) : Password of the user

    :return: response
    List[dict] :
        success: bool
        token: string
        message: string
    """

    try:
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter(User.email == email and User.password == password).first()

        if user == None:
            response = jsonify({'success': False, 'token': None, 'message': 'Email or/and Password wrong.'}), 404
        else:
            access_token = create_access_token(identity=user.user_id)
            response = jsonify({'success': True, 'token': access_token, 'message': 'Logged in.'}), 200

    except Exception as e:
        response = jsonify({'success': False, 'token': None, 'message': str(e)}), 400

    return response



@app.route('/getuser', methods=['GET'])
@jwt_required()
def user():
    """
    Used to retrieve user information.

    :parameter:
       JWT token: sent from headers

    :return:
    List[dict] : response
        success: bool
        message: string

    """
    try:
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        print(current_user_id, user)
        if user.name == 'Admin User' and user.email == 'admin@testing.com':
            users = User.getUsers()
            response = jsonify({'success': True, 'message': users}), 200
        else:
            result = [{
                'user_id': user.user_id,
                'email': user.email,
                'password': user.password,
                'name': user.name,
            }]
            response = jsonify({'success': True, 'message': result}), 200
    except Exception as e:
        response = jsonify({'success': False, 'message': str(e)}), 400

    return response


@app.route('/delete', methods=['POST'])
@jwt_required()
def delete():
    """
    Used to delete a users account.

    :parameter:
       JWT token: sent from headers
       email: string

    :return:
    List[dict] : response
        success: bool
        message: string

    """
    try:
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        user_email = request.form.get('email')
        delete_user = User.query.filter(User.email == user_email).first()

        if user.name == 'Admin User' and user.email == 'admin@testing.com' and delete_user and delete_user.email != user.email:
            User.deleteUser(delete_user.email)
            response = jsonify({'success': True, 'message': 'Account of '+delete_user.name+' deleted.'}), 200
        else:
            response = jsonify({'success': False, 'message': 'Unsuccessful'}), 404
    except Exception as e:
        response = jsonify({'success': False, 'message': str(e)}), 400

    return response
