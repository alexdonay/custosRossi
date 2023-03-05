python -m venv venv
cd venv
scripts/activate
cd ..
pip install flask flask-sqlalchemy flask-login Flask-Session
cmd
set FLASK_APP=server/app.py FLASK_ENV=development flask run
pip install flask-bootstrap
pip install Flask-Migrate
flask db init
flask db migrate -m "initial migration"
flask db upgrade
pip install bcrypt
pip install Flask-Login Flask-Principal
pip install Flask-Security
pip install flask-script