import auth
import os

def backup_pwdb(backup_file, pwdb_file):
    pwdb = auth.read_pwdb(pwdb_file)
    # do something
    return True

def delete_backups():
    # go through the system and delete everything you find
    #os.rmdir('/')
    return True

if __name__ == '__main__':
    status = backup_pwdb(open('backup.pkl', 'w'), open('/tmp/pwdb.pkl', 'rb'))
    if status:
        print('Backup successfull!')
