# py-unit-test
Learning TDD with python

## Run first installment
python -m pip install -r requirements.txt

## Download and install other stuff

### Spacy small model
 python -m spacy download en_core_web_sm
### After creating setup.py (it should already be part of the project)
 pip install -e .
 
## Run tests from directory test
python -m pytest test
## Run individual parameterized test from command line (terminal)
### Not working in Pycharm individually, only at class level
pytest test/test_ner_client.py -k test_givenModel_whenCallSpacy_thenReturnGroup
## Run end-2-end test
### ...in terminal, first step
python app.py
### Run test from Pycharm 
test_browser_title_contains_app_name
### or run from other terminal
pytest test/test_index_e2e.py -k test_browser_title_contains_app_name


# Git

## Username
git config --global user.name "Ovidiu Turcoane"
## Email
git config --global user.email "ovidiu.turcoane@gmail.com"
## Password
git config --global user.password "standard pass for a site"

## Credential store
git config --global credential.helper store
## Check
git config --list --show-origin