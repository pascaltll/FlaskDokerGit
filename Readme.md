> Initial steps
* source envfraskDock/bin/activate 
* python view.py

> Docker steps 
* pip freeze > requirements.txt
* docker image build -t flask_docker .
* docker run -d -p 5001:5001 flask_docker

> manager Docker
* docker ps
* docker stopp
* http://localhost:5001

> data base mangment
* flask db init
* flask db migrate -m "users table"
* flask db upgrade
* flask db migrate -m "posts table"

> flask shell
* from app import db
* from app.models import User, Post
* db.drop_all()
* db.create_all()

u = User(username='john', email='john@example.com')
db.session.add(u)
db.session.commit()

