<!-- ![](my logo?)  -->

# Translate it!

![Responsive Mockup]()
Translate it! is a translation service engine allowing the user to compare pricing and timings from different lingusits and place an order for translating their file in selected language. The engine 

## Deployed at

## UX

### User Stories
1. As a user:
  - I know what is the purpose of the service and can follow instructions on how to use it.
  - I can see the languages available and select the one into which I want to translate my file.
  - I can copy the text for translation to get the word count.
  - I can see a list of linguists available in my selected language.
  - I am given the information about how much the translation into my selected language would cost and 
    how long it would take depending on the linguist.
  - I can compare different linguists depending on the selection criteria that is most important to me.
  - I can place an order and receive confirmation that it has been placed. 
  - I know what process is running in the background.

## Features and Design
- Selection from different languages. During the development changed the representation of the language in the Google Sheet database to be in one cell rather than separate. Considering the size of the database and the list of available languages, this seemed a more efficient solution.
- Selection from different linguists
- Selection of comparison criteria - price, completion time, experience average customer rating and presentation of results.
   <!-- Solutions for graphs: 
   1. none and just printing according to the sorting selected by the user 
   2. one graph opening as a separate HTML page with all criteria (if possible due to data ranges); 
   3. separate graph for each criteria placed on the same page -->
- 

### Existing Features

### Features Left to Implement

## Technologies Used

### Languages
- HTML and CSS (provided in Code Institute's template)
- Python

### Frameworks, Libraries and Programs used
- VS Code: used as the primary code editor
- Git: used for version control
- Git Hub: used to store project files
- yEd: to create the algorithm for the porgram and it's data model 
- Google Sheets to store the database of linguists
- Python Libraries 
- Heroku: used to deploy the live version of the project
- [Am I Responsive?](http://ami.responsivedesign.is/#) site to generate the resposivene mockup

## Testing 

### User Story Testing
1. As a user:
  - I know what is the purpose of the service and how can follow instructions on how to use it.
  - I can see the languages available and select the one into which I want to translate my file.
  <!-- - I can upload the file for a word count-->
  - I can see a list of linguists available in my selected language
  - I am given the information how much the translation into my selected language would cost and how long it would take depending on the linguist.
  - I can compare different linguists depending on the selection criteria that is most important to me.
  - I can place an order and receive confirmation that it has been placed.
  - I know what process is running in the background.
  

### Validator Testing 
- Run through [Pep 8 online check](http://pep8online.com/) validator
  

<!-- ### Performance Testing -->

### Bugs and Fixes
1. In word_counter module copy/pasting text that contains new line causes shell to interpret the new line text as a new command rather than part of text, breatking the program.
__FIXED__ Used method that creates a list to which pasted text is appended line by line, and then converted to a string using join() method. Solution found on [Stackoverflow](https://stackoverflow.com/questions/34889012/how-to-paste-multiple-lines-of-text-into-python-input). This also allows the user to input mutliple texts.
2. word_counter module runs input request before printing instructions, even if this function is called later. Same happens when imported module to the main run.py file, even though no function is called in the module.
__FIXED__ Removed @split_text decorator and used the function with get_user_input as an argument instead.
3. Creating Linguist instance from Google Sheet data in the linguist_selector.py required importing sheet data from the main run.py module, causing circular import issues. 
__FIXED__ Moved the function to the main module (run.py).
4. The creation of the linguists listing and sorting required some consideration and testing different methods on how best to approach this. 
__FIXED__ Adjusted the function to return a list of objects instead of a dictionary, thus allowing the use of operand.getattribute to sort returned lists.
5. Initial idea of creating a dictonary with row number as key and the object returned as string caused issues applying the sorting method. In the sorting function, when sorted list assigned to another variable returned None object.
__FIXED__ Adjusted sort_by_criterium function to reassign the sorted list to the same variable as that passed in the function.
6. sort_by_criteria function returns exception when selecting 0.
__FIXED__ Added 0 to the criteria dictionary and if statement to the sorting function to pass when no sorting is selected.
7. Printing quotation after selection of the linguist throws an error due to incorrect data types. 
__FIXED__ Converted class attributes to floats in functions calculating total price and turnaround time and changed return_word_count function in word_counter module to return word_count rather than a string. 

### Unfixed Bugs

## Deployment
- The program was deployed to Heroku and is available here: The steps to deploy are as follows: 
 

## Credits 
<!-- A great thank you to: 
- My mentor, Caleb, for extremely valuable pointers on how to visualise the movement on the board, make decisions on the best UX approaches and support throughout the whole project. 
- -->
<!-- - Stackoverflow, its users and their previous posts to help me find solutions to problems I encountered.
- https://pythonexamples.org/python-split-string-by-regex/ for tips on how to use regex for spliting the content.
- https://www.w3schools.com for tips on usage of various in-built functions and methods.
- https://stackoverflow.com/questions/4010322/sort-a-list-of-class-instances-python#comment4297852_4010333: for solution on how to sort the linguists listings according to specific attribute and https://docs.python.org/3/library/operator.html for information on how to apply it-->

### Content
- css, xterm.css and xterm.js provided with the Code Institute template, orirginally forked from [Fabrice Bellard's javascript vt100 for jslinux](http://bellard.org/jslinux/)
- 