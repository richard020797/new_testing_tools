# Testing tools
This is a small recopilation of several testing methods I find interesting.

## Special mention for:
From whom I took several ideas (Almost copy them) and taught me the necessary
to create this resources and share them with the community by repetition.



Hillel Wayne Twitter: [@hillelogram](https://twitter.com/search?q=%40hillelogram&src=typd&lang=en)  Github: hwayne

Austin Bingham Twitter: [@austin_bingham](https://twitter.com/austin_bingham?lang=en) Github: abingham



From whom I have learned how to present Python content/code and are the role
models I follow to improve in my presentation/workshop skills.


James Powell Twitter: [@dontusethiscode](https://twitter.com/dontusethiscode?lang=en) http://seriously.dontusethiscode.com/

Raymond Hettinger Twitter: [@raymondh](https://twitter.com/raymondh?lang=en) Github: rhettinger



## Previous:
### a. Install `pip`
```
  Windows:
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py

  Mac:
    brew install pip
    brew install pipenv

  Linux:
    sudo apt-get update sudo apt-get -y upgrade
    sudo apt-get install python-pip
```


## Setup instructions

1. Install Pipenv if you do not have it:
```
    pip install pipenv==2018.11.26
  or
    sudo pip install pipenv==2018.11.26
```


2. Run 
```
  pipenv sync 
```
  if you cloned the repo and go to instruction 6 or continue.


3. Install pytest:
```
  pipenv install pytest==4.0.1
```

  docs: https://docs.pytest.org/en/latest/getting-started.html


4. Install Hypothesis:
```
  pipenv install hypothesis
```

  docs: https://hypothesis.readthedocs.io/en/latest/quickstart.html#installing



5. Install dpcontracts:
```
  pipienv install dpcontracts==0.6.0
```

  docs: https://pypi.org/project/dpcontracts/


6. Activate env:
```
  pipenv shell
```
