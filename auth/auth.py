import getpass
import pathlib
import pickle
import random
import string
import tempfile

PWDB_FLNAME = pathlib.Path('pwdb.pkl')
CHARS = string.ascii_letters + string.digits + string.punctuation

class PasswordDatabase:

    def __init__(self, dbfilename):
        # this is an attribute
        self.dbfilename = dbfilename
        self.db = self.read_dbfile()

    def in_database(self, username):
        return username in self.db

    # this is a method
    def read_dbfile(self):
        try:
            dbfile = open(self.dbfilename, 'rb')
            db = pickle.load(dbfile)
            dbfile.close()
        except FileNotFoundError:
            db = {}
        return db

    def write_dbfile(self):
        dbfile = open(self.dbfilename, 'wb')
        pickle.dump(self.db, dbfile)
        dbfile.close()

    def add_user(self, username, password):
        if username not in self.db:
            self.db[username] = password
        else:
            raise ValueError('User already in db!')

    def authenticate(self, username, password):
        return self.db[username].hash == password.hash

    def get_salt(self, username):
        try:
            salt = self.db[username].salt
            return salt
        except KeyError:
            raise KeyError('User unknown!')



class PasswordHash:

    def __init__(self, pass_string, username, salt=None):
        if salt:
            self.salt = salt
        else:
            self.salt = self.create_salt()
        self.hash = self.pwhash(pass_string, self.salt)

    def create_salt(self):
        salt_chars = random.choices(CHARS, k=10)
        return ''.join(salt_chars)

    def pwhash(self,pass_text, salt):
        hash_ = 0
        full_pass_text = pass_text + salt
        for idx, char in enumerate(full_pass_text):
            # use idx as a multiplier, so that shuffling the characters returns a
            # different hash
            hash_ += (idx+1)*ord(char)
        return hash_



def get_credentials():
    username = input('Enter your username: ')
    password = getpass.getpass('Enter your password: ')
    return (username, password)

if __name__ == '__main__':
    pwdb_path = tempfile.gettempdir() / PWDB_FLNAME

    pwdb = PasswordDatabase(pwdb_path)
    username, pass_string = get_credentials()

    if pwdb.in_database(username):
        print("User in database.")
    else:
        newpassword = PasswordHash(pass_string, username)
        pwdb.add_user(username, newpassword)
        print('Created new user.')

    #now we try to authenticate
    salt = pwdb.get_salt(username)
    password = PasswordHash(pass_string, username, salt)
    if pwdb.authenticate(username, password):
        print('Authentication succeeded!')
    else:
        print('No!')
    pwdb.write_dbfile()
