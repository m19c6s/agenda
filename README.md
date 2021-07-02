git clone git@github.com:m19c6s/agenda.git

cd agenda

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

python manage.py migrate
