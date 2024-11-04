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