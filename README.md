# Testing tools
This is a small recopilation of several testing methods I find interesting.

## Special mention for:
From whom I took several ideas (Almost copy them) and taught me the necessary
to create this resources and share them with the community by repetition.



Hillel Wayne Twitter: @hillelogram  Github: hwayne

Austin Bingham Twitter: @austin_bingham Github: abingham



From whom I have learned how to present Python content/code and are the role
models I follow to improve in my presentation/workshop skills.


James Powell Twitter: @dontusethiscode http://seriously.dontusethiscode.com/

Raymond Hettinger Twitter: @raymondh Github: rhettinger



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
