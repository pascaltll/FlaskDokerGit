> Initial steps
* source new-env/bin/activate 
* python view.py

> Docker steps 
* pip freeze > requirements.txt
* docker image build -t flask_docker .
* docker run -d -p 5000:5000 flask_docker

> manager Docker
* docker ps
* docker stopp
* http://localhost:5001