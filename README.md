<!-- ![](my logo?)  -->
# TABLE OF CONTENTS
1. [Introduction](#intro)
2. [UX](#ux)<br>
  2.1 [User Stories](#user-stories)
3. [Features and design](#features-design)<br>
  3.1. [Existing features](#existing-features)<br>
  3.2. [Features left to implement](#left-to-implement)
4. [Technologies](#technologies)<br>
  4.1. [Languages used](#languages)<br>
  4.2. [Frameworks, libraries and programs used](#libraries-and-programs)
5. [Testing](#testing)
6. [Deployment](#deployment)
7. [Credits](#credits)

## <a name="intro"></a>Translate it!

![Responsive Mockup](https://github.com/Koko-66/Translate_it/blob/main/data/am-i-responsive.png)
Link to the deployed app: https://translate-it7.herokuapp.com/

Translate it! is a translation service engine that allows the user to compare pricing, timings, rating and experience of linguists translating into their selected language. They can then select the linguist and place an order for translating their text.
The service is easy to use but it is used mostly aimed at youth or adults, considering it involves a purchase.

## <a name="ux"></a>UX
Considering the program is written using Python only, the UX is restricted to the functionality of the program, its features and ease of use.
In terms of the visual aspects, the instructions and on-screen feedback are arranged in a way that makes them easier to read and is as aesthetically pleasing as possible. This is achieved with the use of new lines and characters such as underscores and dashes.

### Functionality design
The functionality of the program was initially designed using a process flowchart (available [here](https://github.com/Koko-66/Translate_it/blob/main/data/Translate_it!_flow-chart.pdf)) and a graphical representation of the data model (available [here](https://github.com/Koko-66/Translate_it/blob/main/data/Translate-it!_data-model.pdf)).

### <a name="user-stories"></a>User Stories
As a user:
  1. I know what is the purpose of the service and can follow instructions on how to use it.
  2. I can see the languages available and select the one into which I want to translate my file.
  3. I can copy the text for translation to get the word count.
  4. I can see a list of linguists available in my selected language along with their information.
  5. I am given information about how much the translation into my selected language would cost and how long it would take depending on the linguist.
  6. I can select the language I wish to translate into and correct my selection if I made a mistake.
  7. I can sort the linguists depending on the selection criterion that is most important to me.
  8. I can place an order and receive confirmation on the screen and via e-mail that it has been placed. 
  9. I know what process is running in the background at all times and can confirm my selections at different points.
  10. I want the program to run smoothly, not take too long and not crash when my input is not correct.

## <a name="features-design"></a>Features and Design
The program takes the user through the process step by step, continuously providing feedback and asking for confirmation of choices made.

### <a name="existing-features"></a>Existing Features

#### Google Sheet database
The program exchanges linguist and order data with a Google Sheet acting as a database ([database link](https://docs.google.com/spreadsheets/d/14nIJVg9JECtkHeYSg42bjcTiKdKcvbqxtreLCXIFVU0/edit?usp=sharing). Language and Rating data in the Google Sheet are validated using its in-build validation features.
The program retrieves the linguist and language data from the Google Sheet and pushes the order data back to the Order_data worksheet.
_Note: all data in the database is fictional though realistic._

#### Language selection
When run, the program prints introduction to Translate it and a list of the available languages pulled from the database and asks the customer to make a selection. Once the selection is made they are asked to confirm their choice and are given an opportunity to correct their selection if they made a mistake.

![Language selection](https://github.com/Koko-66/Translate_it/blob/main/data/depl-intro-and-languages.png)
![Language selection confirmation](https://github.com/Koko-66/Translate_it/blob/main/data/depl-confirm-lang-selection.png)

_Note: During the development, the representation of the language in the Google Sheet database was changed to be in one cell rather than separate. Considering the size of the database and the list of available languages, this seemed a more efficient solution, removing the need to join and split the language/locale combination to retrieve and manipulate data._

#### Word counter
The program allows the customer to paste the text into the program directly and performs a word count later used to calculate costs for translation depending on the linguist's price. The user can paste in multiple lines or pieces of texts until they indicate they are ready but entering a specified combination of keys.

![Text input](https://github.com/Koko-66/Translate_it/blob/main/data/depl-text-input.png)
![Word count](https://github.com/Koko-66/Translate_it/blob/main/data/depl-word-counter.png)

#### Calculation of the total price and approximate turnaround time
The program calculates the total price for the project depending on the per word price for each linguist, as well as the time needed to complete the translation that is based on the number of words the linguist is able to translate a day. The minimum turnaround time is set to 1 day, to be more realistic.

#### Sorting of linguists
The program first prints a list of linguists available for the selected language in their order of appearance in the database. It then allows the customer to sort the results by price, turnaround, rating and years of experience, which would be helpful as the database grows, or not sort at all. If sorting is selected, linguists are printed again according to the sorting criteria: 
  - for price: from cheapest to most expensive;
  - for turnaround: from quickest to slowest;
  - for experience and rating: from highest to lowest.
If no sorting is selected, the program moves to the next step.

![Linguists listing](https://github.com/Koko-66/Translate_it/blob/main/data/depl-inital-linguist-listings.png)

Here is an example of listings sorted by Price:

![Linguists_sorted](https://github.com/Koko-66/Translate_it/blob/main/data/depl-linguists-sorted-price.png)

The user can also re-sort the linguists according to a different criterion if they choose not to confirm the order and want to select the linguist once again.

#### Order generation and e-mail confirmation 
Once the user selects their linguist, they are presented with the quote:

![Quote](https://github.com/Koko-66/Translate_it/blob/main/data/depl-quote.png)

Once the user confirms their selection, they are asked for their name and e-mail address.

![Customer information](https://github.com/Koko-66/Translate_it/blob/main/data/depl-user-details-input.png)

The order number is generated based on the last order number in the Google Sheet. If no number is present, a preset number is used instead.
The order and user information are then pushed into the database, and the order confirmation is sent from a dedicated e-mail account to user's the indicated e-mail address. The E-mail address is validated for correct format only.

![Sample email](https://github.com/Koko-66/Translate_it/blob/main/data/email_confirmation.png)

#### Confirmation of selections / ability to change selection
The users have the opportunity to confirm their selection of language and the linguist and change it if needed. Similarly, the user is asked to confirm their order and if "no" is selected the user is given an option to either go back to the selection of linguist and their sorting or can exit the program.

![Order not confirmed options](https://github.com/Koko-66/Translate_it/blob/main/data/depl-cancel-order-and-exit.png)

#### Validation of Data Input and handling errors
At points requiring user input, the input data is appropriately validated. 
  1. Language selection and selection of the sorting criteria validates against the key value in the dictionary holding languages/criteria using the try/except method.

  ![Language selection validation](https://github.com/Koko-66/Translate_it/blob/main/data/depl-language-selection-vlidation.png)

  2. Word counting function checks for lack of data i.e. the word count being equal to 0. 

  ![Word count validation](https://github.com/Koko-66/Translate_it/blob/main/data/depl-word-count-validation.png)

  3. Selection of linguists checks for value and index errors to ensure the user inputs correct value using the try/except method.

  ![Linguist selection validation](https://github.com/Koko-66/Translate_it/blob/main/data/depl-linguist-selection-validation.png)

  4. Functions asking to confirm selection validate for input equal to allowed values ('y' and 'n') using if statements.

  ![Confirm selection](https://github.com/Koko-66/Translate_it/blob/main/data/depl-confirm-selection-validation.png)

  5. The value for the last order number present in the database is checked for correct value and returns 101 as the first number if no order is present.
  5. The format of the e-mail is validated with the use of Regex.

  ![Customer e-mail validation](https://github.com/Koko-66/Translate_it/blob/main/data/depl-email-validation.png)

  To account for situations where the e-mail address provided is not correct, the program includes a message instructing the user to contact support at translateit7@gmail.com in case they don't receive a confirmation e-mail.

  6. Connection to the Google Sheet is wrapped in a try/except to handle errors when accessing the database. This way, if the link to the database is broken, a message appears.

  ![Error connecting to the database](https://github.com/Koko-66/Translate_it/blob/main/data/depl-error-connecting-to-database.png)

  7. Similarly, the main function is wrapped in a try/except to handle EOF and KeyboardInterrupt errors.

### <a name="left-to-implement"></a>Features Left to Implement

#### File upload
The program would ideally include a feature allowing the user to upload the file for word counting and translation. This is would require the implementation of file handling and storage, which fall outside of the scope of this project.

#### E-mail validation using OAuth2
Implementation of a more secure way of accessing the e-mail using OAuth2 credentials.

#### E-mail address validation
In the future, a more thorough validation of the e-mail address, confirming that the e-mail is not only formatted correctly but is correct and exists, could be implemented.


## <a name="technologies"></a>Technologies used
### <a name="languages"></a>Languages
- HTML and CSS (provided in Code Institute's template)
- Python
- json (files storing credentials)

### <a name="libraries-and-programs"></a>Frameworks, Libraries and Programs used
- VS Code: used as the primary code editor and debugger
- GitPod: used as a backup code editor
- Git: used for version control
- Git Hub: used to store project files
- [Python Tutor](https://pythontutor.com/): used to help with debugging
- yEd: to create the algorithm for the program and its data model 
- Google Sheets to store the database of linguists and Google mail to send confirmation e-mails.
- Python Libraries: 
  - gspread: used for working with the data from Google Sheet
  - re: used in splitting input text into individual words and validation of customer e-mail address
  - google.oauth2.service_account to connect to the Google Sheet
  - operator: used in function sorting the list with linguists by their attributes
  - yagmail: used for sending an order confirmation to the user via e-mail
- Heroku: used to deploy the live version of the project
- [Am I Responsive?](http://ami.responsivedesign.is/#) site to generate the responsive mockup

## <a name="testing"></a>Testing 
Information about testing is available in a separate file [here](https://github.com/Koko-66/Translate_it/blob/main/TESTING.md).

## <a name="deployment">Deployment
- The program was deployed to Heroku and is available here: The steps to deploy are as follows: 

1. Updated the contents of the requirements file using the `pip3 freeze > requirements.txt` command in VS Code.
2. Checked the project structure and run the program to ensure all is working as expected.
3. Created the Translate it! project on Heroku, giving it the name 'translate-it7' (translate-it was not available).
4. In the Settings tab set the environment variables in the Config Vars section to set up credentials to access the Google Sheet with the database, set port and credentials to access e-mail account for sending e-mails.
5. Added the python and nodejs buildpacks (in that order).
6. In the Deployment tab selected GitHub as deployment method, selected Connect, authorised Heroku to access the GitHub account, searched for Translate_it repository and connected to it.
7. First time deployed the app using the manual Deploy Branch button and then enabled automatic deploys.
8. After deployment tested app functionality and resolved encountered issues.

The app has been deployed to: https://translate-it7.herokuapp.com/
 
## Requirements
The program requires Python 3 or higher. 

## <a name="credits">Credits 
A great thank you to: 
- My mentor, Caleb Mbakwe, for extremely valuable pointers on how to visualise the movement on the board, make decisions on the best UX approaches and organise the code, and his support throughout the whole project. 

- Stackoverflow, its users and their previous posts to help me find solutions to problems I encountered and specifically Ned Batchelder for his suggestion on how to sort linguists listings according to a specific attribute available [here](https://stackoverflow.com/questions/4010322/sort-a-list-of-class-instances-python#comment4297852_4010333) and operator module's [official documentation](https://docs.python.org/3/library/operator.html) for information on how to apply it.

- [Python Examples](https://pythonexamples.org/python-split-string-by-regex/) for tips on how to use regex for splitting the content.

- [W3 schools](https://www.w3schools.com) for tips on the usage of various in-built functions and methods.

- [Geeks for Geeks](https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/) for code for e-mail validation using Regex.

- [Programiz](https://www.programiz.com/python-programming/docstrings) for notes on how to write docstrings for modules and classes.

- Creators of Python and Heroku documentation.

Content of the css, xterm.css and xterm.js provided with the Code Institute template, originally forked from [Fabrice Bellard's javascript vt100 for jslinux](http://bellard.org/jslinux/)