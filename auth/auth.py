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

    def add_user(self, username, hash_, salt):
        if username not in self.db:
            self.db[username] = (hash_, salt)
        else:
            raise ValueError('User already in db!')

    def authenticate(self, username, hash_, salt):
        return (username, (hash_, salt)) in self.db.items()

    def get_salt(self, username):
        try:
            hash_, salt = self.db[username]
            return salt
        except KeyError:
            raise KeyError('User unknown!')

def get_credentials():

def pwhash(pass_text, salt):
    hash_ = 0
    full_pass_text = pass_text + salt
    for idx, char in enumerate(full_pass_text):
        # use idx as a multiplier, so that shuffling the characters returns a
        # different hash
        hash_ += (idx+1)*ord(char)
    return hash_

def get_salt():
    salt_chars = random.choices(CHARS, k=10)
    return ''.join(salt_chars)

if __name__ == '__main__':
    pwdb_path = tempfile.gettempdir() / PWDB_FLNAME
    try:
        pwdb_file = open(pwdb_path, 'rb+')
    except FileNotFoundError:
        pwdb_file = open(pwdb_path, 'wb+')

    username, password = get_credentials()
    pwdb = read_pwdb(pwdb_file)

    if authenticate(username, password, pwdb):
        print('Authentication succeeded!')
        print(pwdb)
    else:
        print('Wrong username or password')
        ans = input('Create new user [y/n]? ')
        if ans == 'y':
            salt = get_salt()
            add_user(username, password, salt, pwdb, pwdb_file)
        else:
            print('Exit!')
