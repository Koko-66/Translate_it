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

![Responsive Mockup]()
Translate it! is a translation service engine that allows the user compare pricing, timings, rating and experience of lingusits translating into their selected langauge. They can then select the lingusit, and place an order for translating their text. 
The service is easy to use and even though it is simple enough to use by children, considering the the type of service, it is mostly aimed at adults and young adults.

## <a name="ux"></a>UX
Considering the program is written using Python only, the UX is restricted to the functionality of the program, its features and ease of use.
In terms of the visual aspects, care was taken to make instructions and on-screen feedback easy to read and understand and arrange it in as easthetically pleasing way as possible by manipulating the arrangement of lines and usage of new lines, underscoores and dashes. 

The program's process flowchart is available [here](https://github.com/Koko-66/Translate_it/blob/main/data/Translate_it!_flow-chart.pdf) and the representation of the data model [here](https://github.com/Koko-66/Translate_it/blob/main/data/Translate-it!_data-model.pdf).

### <a name="user-stories"></a>User Stories
As a user:
  1. I know what is the purpose of the service and can follow instructions on how to use it.
  2. I can see the languages available and select the one into which I want to translate my file.
  3. I can copy the text for translation to get the word count.
  4. I can see a list of linguists available in my selected language along with their information.
  5. I am given the information about how much the translation into my selected language would cost and how long it would take depending on the linguist.
  6. I can select the language I wish to translate into and correct my selection if I made a mistake.
  7. I can sort the linguists depending on the selection criteria that is most important to me.
  8. I can place an order and receive confirmation on screen and via e-mail that it has been placed. 
  9. I know what process is running in the background at all times and can confirm my selections at different points.
  10. The program runs smoothly, does not take to long and does not crash when my input is not correct.

## <a name="features-design"></a>Features and Design
Program takes the user through the process step by step, continuously providing feedback and asking for confirmation of choices made.

### <a name="existing-features"></a>Existing Features

#### Google Sheet database
The program exchanges linguist and order data from a Google Sheet that is acting as a database (link to the database [here]()). Language and Rating data in the Google Sheet is validated using it's in-build validation features.
The program retreives the linguits and language data from the Google Sheet and pushes the order data back to the Order_data worksheet.
_Note:&nbsp;all&nbsp;data&nbsp;in&nbsp;the&nbsp;database&nbsp;is&nbsp;fictional._

#### Language selection
When run, the program prints a list of the available languages from the database, asks the customer to make a selection and confirm their choice, giving them opportunity to correct their selection if they make a mistake.

_Note: During the development the representation of the language in the Google Sheet database was changed to be in one cell rather than separate. Considering the size of the database and the list of available languages, this seemed a more efficient solution, removing the need to join and split the language/locale combination to retrieve and manipulate data._

#### Word counter
The program allows the customer to paste in the text into the program directly and performs a word count later used to calculate costs for translation depending on the linguist's price. The user can paste in multiple lines or pieces of texts, until they indicate they are ready but entering specified combination of keys. 

#### Calcuation of total price and approximate turnaround time
The program calculates the total price for the project depending on the per word price for each linguist, as well as the time needed to complete the translation that is based on the number of words the linguist is able to translate a day. The minimum turnaournd time is set to 1 day, to be more realistic.

#### Sorting of linguists
The program prints a list of linguists available for the selected language first in their order of appearance in the database. It then allows the customer to sort the results by price, turnaround, rating and years of experience, which would be helpful as the database grows, or can not sort at all. If sorting is selected, linguists are printed again according to the sorting criteria: 
  - from cheapest to most expensive;
  - quickest to slowest in terms of turnaround;
  - from ones with the highest to lowest rating or years of experience.
If no sorting is selected, the program moves to the next step.

The user can also re-sort the lingusits according to a different criteria if they choose not to confirm the order and want to select the linguist once again.

#### Order generation and e-mail confirmation 
Once the user confirms their selection of the linguist they are asked for their name and e-mail address. This information is then pushed into the database, along with the order number and value for future tracking, and the order confirmation is sent from dedicated e-mail account to the indicated e-mail address. E-mail address is validated for correct format only.
Order number is generated based on the last number present in the Google Sheet. If no number is present, a preset number is used instead.

#### Confirmation of selections / ability to change selection
The users have the opportunity to confirm their selection of language and the linguist and change it if needed. Similarly, the user is asked to confirm their order and if "no" is selected is given an option to either go back to selecting the linguuist again or can exit the program.

#### Validation of Data Input
At points requiring user input, the input data is appropriately validated. 
  1. Language selection and selection of the sorting crtieria validates against the key value in the dictionary holding langauges using the try/exept method.
  2. Word counting function checks for lack of data i.e. the word count being equal to 0. 
  3. Selection of linguist checks for Value and Index Errors to ensure the user inputs correct value using try/except method as well.
  4. Functions asking to confirm selection validate for input equal to allowed values using if statements.
  5. The value for last order number present in the database is checked for correct value and returns 101 as first number if no order is present.
  5. The format of the e-mail is validated with the use of Regex.

### <a name="left-to-implement"></a>Features Left to Implement

#### File upload
The program would ideally include a feature allowing the user to upload the file for word counting and translation. This is would require implementation of file-handling and storage, which fall outside of scope for this project.

#### E-mail validation using Oauth2
Implementation of a more secure way of accessing the e-mail using Oauth2 credentials.

#### E-mail address validation
For a real-life application, it would be good to implement a more thorough validation of the e-mail address, confirming that the e-mail is not only formatted correctly, but is correct and exists.

## <a name="technologies"></a>Technologies used
### <a name="languages"></a>Languages
- HTML and CSS (provided in Code Institute's template)
- Python
- json (files storing credentials)

### <a name="libraries-and-programs"></a>Frameworks, Libraries and Programs used
- VS Code: used as the primary code editor and debugger
- GitPod: used as a back up code editor
- Git: used for version control
- Git Hub: used to store project files
- [Python Tutor](https://pythontutor.com/): used to help with debugging
- yEd: to create the algorithm for the porgram and it's data model 
- Google Sheets to store the database of linguists and Google mail to send confirmation e-mails.
- Python Libraries: 
  - gspread: used for wokrking with the data from Google Sheet
  - re: used in spliting input text into individual words and validation of customer e-mail address;
  - google.oauth2.service_account to connect to the Google Sheet.
  - operator: used in function sorting the list with lingusits by their attributes;
  - yagmail and yagmail.creds: used for sending order confirmation to the user via e-mail
- Heroku: used to deploy the live version of the project
- [Am I Responsive?](http://ami.responsivedesign.is/#) site to generate the resposivene mockup

## <a name="testing"></a>Testing 
Information about testing is available in a separate file [here](https://github.com/Koko-66/Translate_it/blob/main/TESTING.md)

## <a name="deployment">Deployment
- The program was deployed to Heroku and is available here: The steps to deploy are as follows: 
 

The program requires Python 3 and higher. 

## <a name="credits">Credits 
A great thank you to: 
- My mentor, Caleb Mbakwe, for extremely valuable pointers on how to visualise the movement on the board, make decisions on the best UX approaches and organise the code, and his support throughout the whole project. 

- Stackoverflow, its users and their previous posts to help me find solutions to problems I encountered. Specifically: 
  - Ned Batchelder for his [suggestion](https://stackoverflow.com/questions/4010322/sort-a-list-of-class-instances-python#comment4297852_4010333) on how to sort linguists listings according to specific attribute and operator module's [official documentation](https://docs.python.org/3/library/operator.html) for information on how to apply it.

- [Python Examples](https://pythonexamples.org/python-split-string-by-regex/) for tips on how to use regex for spliting the content.

- [W3 schools](https://www.w3schools.com) for tips on usage of various in-built functions and methods.

- [Geeks for Geeks](https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/) for code for e-mail validation using Regex.
<!-- - https://stackoverflow.com/questions/37201250/sending-email-via-gmail-python) for tips on how to apply Auth2 with- -->

Content of the css, xterm.css and xterm.js provided with the Code Institute template, orirginally forked from [Fabrice Bellard's javascript vt100 for jslinux](http://bellard.org/jslinux/)