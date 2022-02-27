from app import db
from typing import List, Dict


class User(db.Model):
    """
    This class is used for creating the table and adding data to SQLite database.

    Attributes
    ----------
    email: str
        email of the user
    password: str
        password of the user
    name:
        name of the user


    Methods
    -------
    def addUsers():
        Adds a user to the database.

    def getUsers()
        Return all users in the database.

    """
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)

    def __init__(self, name, email, password):
        """
        Constructs all attributes for the user object.
        :param name: str
                the name of the user
        :param email:
                the email of the user
        :param password:
                the password of the user
        """
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self) -> None:
        return "Name : "+self.name+", Email : "+self.email+", Password : "+self.password

    def addUsers(self) -> None:
        """
        Adds the new user to the database.

        :return:
        None
        """
        db.session.add(self)
        db.session.commit()

    def getUsers() -> List[Dict]:
        """
        Finds all the users present in the
        :return: response: List[dict]
        Returns all the information for all users in database.
        """
        users = User.query.all()
        result = []
        for user in users:
            obj = {
                'user_id': user.user_id,
                'email': user.email,
                'password': user.password,
                'name': user.name,
            }
            result.append(obj)
        return result

    def deleteUser(email) -> None:
        """
        Deletes the user.

        :return:
        None
        """
        user = User.query.filter(User.email == email).first()
        db.session.delete(user)
        db.session.commit()
