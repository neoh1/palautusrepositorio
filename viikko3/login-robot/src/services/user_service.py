import sys
import pdb
import re
from entities.user import User



class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):

        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)
        user = self._user_repository.create(User(username, password))
        return user

    def validate(self, username, password):
        """
        Käyttäjätunnuksen on oltava merkeistä a-z koostuva
        vähintään 3 merkin pituinen merkkijono, joka ei ole vielä käytössä.

        Salasanan on oltava pituudeltaan vähintään 8 merkkiä
        ja se ei saa koostua pelkästään kirjaimista

        """
        if not username or not password:
            raise UserInputError("Username and password are required")
        if self._user_repository.find_by_username(username):
            raise UserInputError("Username already exists")
        if len(username) < 3:
            raise UserInputError("Username too short; less than 3 letters")
        if not re.match("^[a-z]+$", username):
            raise UserInputError("Username should only consists of characters [a-z]")
        if re.match("^[a-z]+$", password):
            raise UserInputError("Password has to have non-letter characters")
        if len(password) < 8:
            raise UserInputError("Password should be 8 characters or more")

