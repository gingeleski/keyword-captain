# Keyword Captain
Bot to play Boggle-style word games. This includes:
- Keyword (royalgames.com)
- Scrabble Boggle (worldwinner.com)

## Setup
The Keyword Captain repo is meant to be run from a virtual environment.
```
# if you don't have virtualenv installed...
pip install virtualenv

# son don't even talk to me if you haven't got pip

# set up a virtualenv in directory 'venv'
virtualenv venv

# activate the virtualenv (this will be different on windows)
source venv/bin/activate

# install the stuff from requirements.txt
pip install -r requirements.txt

# have fun :-o

# when you're all done, leave the virtualenv
deactivate
```
## Running the test suite
```
# get inside your virtualenv... see the above section on setup

# from the root of the repository run the following
nosetests
```
