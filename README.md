# MachEight

# Intructions
### Mach Eight Sample Project

Thank you for taking the time to complete this sample project. We're a tech
first company and we value our engineers tremendously. We're are looking for
hard working, smart engineers with either excellent experience or lots of
potential.


## Project

The project is to write a function that searches through NBA player heights
based on user input. The raw data is taken from
[here](https://www.openintro.org/data/index.php?data=nba_heights).  The data is
served in json format by the endpoint
[here](https://mach-eight.uc.r.appspot.com/).

The task is to create an application that takes a single integer input. The
application will download the raw data from the website above
(https://mach-eight.uc.r.appspot.com) and print a list of all pairs of players
whose height in inches adds up to the integer input to the application. If no
matches are found, the application will print "No matches found"

Sample output is as follows:
```
> app 139

- Brevin Knight         Nate Robinson
- Nate Robinson         Mike Wilks
```

The algorithm to find the pairs must be faster than O(n^2). All edge cases
should be handled appropriately. Though not strictly required, demonstrating
comfort in writing unit tests will make your submission stand out. This is
_not_ a closed book test. You are encouraged to reach out with any questions
that you come across.

## Submission

The preferred form of submission is by publishing a public repo on github with
your code and a README file explaining how to run the code. I also can accept
an emailed zip file with the same contents.

# Execution

## App

To execute the app first of all it is necesarry to have python installed in your PC. Then follow the following steps

#### 1. Install dependencies:
The modules used in the app are the following:
requests
unittest
json

#### 2. Run App:
On the command prompt enter the MachEight directory and run the following command:
py app.py

#### 3. Input:
Enter valid input (the app will not accept 0 or non-integer values as input)

#### 4. Output:
The app will print in console the corresponding message or list of players pairs.

## Tests

#### 1. Run Unit Tests:
On the command prompt enter the MachEight directory and run the following command:
python -m unittest tests
