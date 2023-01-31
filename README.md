# Wallet API

## SheCodesPlus 2022-2023 | VGW Immersion day

## Project set up

1) Fork Repo

2) Clone repo locally

`git clone https://github.com/<username>/she-codes-wallet-api.git`

3) cd into the root directory `she-code-wallet-api`

4) Create virtual environment

`virtualenv env`

5) Activate virtual environment

`. venv/bin/activate`

6) Install requirements

`pip3 install -r requirements.txt`

7) cd into `webApi`

8) Create the migrations 

`python3 manage.py makemigrations`

9) Migrate to create the database

`python3 manage.py migrate`

10) Start the server and you're good to go!!

`python3 manage.py runserver`






