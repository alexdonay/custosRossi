
HOST="localhost"
PORT="4000"
DEBUG=True
PORT = 8087
HOST = "0.0.0.0"
DEBUG = True
THREADED = True
STATIC_FOLDER = "static"
TEMPLATES_FOLDER = "views"
ROUTES_FOLDER = "routes"
SRC_FOLDER ="src"
SECRET_KEY = "rossi"
SQLALCHEMY_DATABASE_URI = "sqlite:///banco.db"
USER_ROLES = ['admin', 'manager', 'user']
PERMISSIONS = {
    '/': ['admin', 'manager', 'user'],
    '/user/': ['admin'],
    '/user/register/': ['admin'],
    '/user/delete/': ['admin'],
    '/user/update/':['admin'],
    '/user/salary/': ['admin'],
    '/company/': ['admin'],
    '/company/register/': ['admin'],
    '/company/delete/': ['admin'],
    '/company/details/': ['admin'],
    '/company/update/': ['admin'],
    '/client/': ['admin'],
    '/client/register/': ['admin'],
    '/client/delete/': ['admin'],
    '/client/details/': ['admin'],
    '/client/update/': ['admin']
}
