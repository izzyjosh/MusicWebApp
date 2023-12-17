# build_files.sh

pip install -r requirements.txt
PYTHON=3.11.6
python3.11.6 manage.py collectstatic --no-input --clear

