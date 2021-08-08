<!-- ![](my logo?)  -->

# Translate it!

![Responsive Mockup]()
Translate it! is a translation service engine allowing the user to compare pricing and timings from different lingusits and place an order for translating their file in selected language. The engine 

## Deployed at

## UX

### User Stories
1. As a user:
  - I know what is the purpose of the service and how can follow instructions on how to use it.
  - I can see the languages available and select the one into which I want to translate my file.
  - I can copy the text for translation to get the word count.
  - I can see a list of linguists available in my selected language.
  - I am given the information how much the translation into my selected language would cost and 
    how long it would take depending on the linguist.
  - I can compare different linguists depending on the selection criteria that is most important to me.
  - I can place an order and receive confirmation that it has been placed. 
  - I know what process is running in the background.

## Features and Design
- Selection from different languages
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
1. During the development of the word_counter module noticed that pasting text that includes new line causes shell to mistake the new line text as a command rather than part of text.
__FIXED__ Used method that creates a list with text that is appended to it by line and then converted to string using join() method. Solution found on [Stackoverflow](https://stackoverflow.com/questions/34889012/how-to-paste-multiple-lines-of-text-into-python-input).
2. word_counter module runs input request before printing instructions, even if this function is called later. Same happens when imported module to the main run.py file, even though no function is called in the module.
__FIXED__ Removed @split_text decorator and used the function with get_user_input as an argument instead.


### Unfixed Bugs

## Deployment
- The program was deployed to Heroku and is available here: The steps to deploy are as follows: 
 

## Credits 
<!-- A great thank you to: 
- My mentor, Caleb, for extremely valuable pointers on how to visualise the movement on the board, make decisions on the best UX approaches and support throughout the whole project. 
- -->
<!-- - Stackoverflow, its users and their previous posts to help me find solutions to problems I encountered.
- https://pythonexamples.org/python-split-string-by-regex/ for tips on how to use regex for spliting the content. -->

### Content
- css, xterm.css and xterm.js provided with the Code Institute template, orirginally forked from [Fabrice Bellard's javascript vt100 for jslinux](http://bellard.org/jslinux/)
- 