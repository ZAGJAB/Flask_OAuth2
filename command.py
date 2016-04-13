import requests
from flask_script import Manager
from app import app

manager=Manager(app)

@manager.command
def test_token():
    r = requests.get('http://127.0.0.1:5000/client/login')
    print '=======r.text======='
    print r.text
    print '=======r.history======='
    print r.history
    print '=======r.url======='
    print r.url
    print '=======r2.text======='
    uri_login = r.url.split('?')[0] + '?user=magigo&pw=123456'
    r2 = requests.get(uri_login)
    print '=======r.text======='
    r = requests.get('http://127.0.0.1:5000/test1', params={'token': r2.text})
    print r.text

if __name__=="__main__":
    manager.run()
