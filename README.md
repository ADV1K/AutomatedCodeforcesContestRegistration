# Automated Contest Registration for Codeforces
A simple script which registers for contests available on codeforces which can be customized with your own needs

## Installation
### selenium
- pip install selenium

### chromedriver
- pip install chromedriver-binary  # adds chromedriver binary to the path

## Firing up the script
- git clone https://https://github.com/ADV1K/AutomatedCodeforcesContestRegistration
- cd AutomatedCodeforcesContestRegistration
- python register.py USERNAME PASSWORD  # default on windows
or
- python3 register.py USERNAME PASSWORD  # default on linux

## why do i need an additional package if have chromedriver installed and added to the path
### Short answer
You Don't.
### Long answer  
adding chromedriver to the path can be a real tricky task for a script-kiddie.
so i researched about this and came across a very helpful module.
This module takes care of all the hassle of adding chromedriver to the path
