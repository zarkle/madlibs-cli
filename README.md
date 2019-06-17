# Mad Libs CLI version

Create `madlibs.py` and `test_madlibs.py` files.  Keeping in mind the concept of Single Responsiblity Principle, build a command line tool which will perform the following:
- Print a welcome message to the user, explaining the Madlib process and command line interactions
- Read a template Madlib file and parse that file into usable parts. You need to decide what components of this file are useful, and how to break those useful pieces apart
- Once you know what parts of the template need user input, such as `Adjective`, prompt the user to submit a series of words to fit each of the required components of the Madlib template
- With the collected user inputs, populate the template such that each provided input is placed into the correct position within the template
- After the resulting Madlib has been completed, provide the completed response back to the user in the command line.
- Write the completed template to a new file on your file system (in the repo).

*Testing*  Every bit of functionality that you add should be tested. As a general rule at this time, you should have a test for valid, invalid, and edge case variants for every function that you define (there are exceptions).
