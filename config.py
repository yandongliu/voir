_obj = {
    'database.username': 'tornado_application_user',
    'database.password': 'qwerty123!',
    'database.database': 'tornado_application',
    'database.url': 'postgresql://tornado_application_user:qwerty123!@localhost:5432/tornado_application',
}

def load():
    pass

def get(key):
    return _obj.get(key)
