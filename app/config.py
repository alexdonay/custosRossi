
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
    '/admin': ['admin'],
    '/manager': ['admin', 'manager'],
    '/user': ['admin'],
    '/user/register': ['admin',],
    '/company': ['admin'],
    '/company/register': ['admin']
}