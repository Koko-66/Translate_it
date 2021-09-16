# TESTING
The program was tested at each step of the development within the development environment as well as on Heroku after deployment. The testing process included:
1. [User Stories testing](#user-stories-testing)
2. [Validation testing](#validation-testing)
3. [Performance testing](#performance-testing)
4. [Development testing](#bugs-and-fixes)
5. [Deployment testing](#deployement-testing)

## <a name="user-stories-testing"></a>User Story testing
1. I know what is the purpose of the service and can follow instructions on how to use it.<br>
    On running the program the user is presented with an introduction to the service and its purpose. Each step of the program is accompanied by relevant instructions.
2. I can see the languages available and select the one into which I want to translate my file.<br>
    The list of available languages is retrieved from the database and printed at the start of the program, below introduction. 
3. I can copy the text for translation to get the word count.<br>
    The user can copy lines or pieces of text to translate and receives feedback from the program about the word count.
4. I can see a list of linguists available in my selected language along with their information.<br>
    A list of linguists matching the selected language is printed once the word count is finished. 
5. I am given information about how much the translation into my selected language would cost and how long it would take depending on the linguist.<br>
    The listings include the linguists' ID, name, language, experience, rating, price per word, the total price for the text and its estimated turnaround time.
6. I can select the language into which I wish to translate and correct my selection if I made a mistake.<br>
    The user is asked to select the language and then confirm their selection. If selection is not confirmed, the user is asked to select the language again.
7. I can sort the linguists depending on the selection criterion that is most important to me.<br>
    The user can sort the listings of linguists according to the linguist's price, the time needed to complete the translation (turnaround time), their experience and their rating.<br>
8. I can place an order and receive confirmation on the screen and via e-mail that it has been placed.<br>
    Once the linguist is selected and confirmed, the user receives feedback on the screen and email with order details.
9. I know at what stage in the process I am, what process is running in the background and can confirm my selections at different points.<br>
    Throughout the program, the user receives feedback on their input and the program's background activities, instructions on expected input and is asked to confirm their choices.
10. I want the program to run smoothly and without delays, and not crash when my input is not correct.<br>
    Testing has shown that the program runs quickly with only the functions that retrieve the data from the database causing very minor delays. Various input validation methods are implemented throughout the program to handle exceptions and errors that might be caused by the user input.
  
## <a name="vlaidator-testing"></a>Validator testing 
Each module has been checked with [Pep 8 online check](http://pep8online.com/) validator and developed in an environment with enabled linters: flakes and cornflakes-linter (VS Code extensions). 

## <a name="performance-testing"></a>Performance testing
Performance testing was done by running the program on various devices.  

## <a name="bugs-and-fixes"></a>Development Testing
Each feature was tested while being developed to ensure correct and error-free functionality.
Bugs encountered during the development and their fixes are listed below.

1. In the *word_counter* module new lines in the copy/pasted text are interpreted by the shell as a new command rather than part of the text, which results in an error.<br>
__FIXED__: Used a method that creates a list to which the pasted text is appended line by line and then converted into a string using the `join()` method. This solution, which also allows the user to input multiple texts, was found on [Stackoverflow](https://stackoverflow.com/questions/34889012/how-to-paste-multiple-lines-of-text-into-python-input).

2. *word_counter* module runs input request before printing instructions, even if this function is called later. The same happens when run in the `main()` function in the *run* module after importing *word counter*, despite the `get_user_input()` input request function not being called in that module.<br>
__FIXED__: Removed `@split_text` decorator which was causing this issue and used the function with `get_user_input()` as an argument instead.

3. Creating a Linguist instance from the database data in the *linguist_selector* module requires importing the sheet data from the main *run* module, causing circular import issues.<br>
__FIXED__: Moved the function creating an instance of the Linguist to the *run* module to avoid setting up the worksheet access in the *linguist_selector* module as well. All functions needing direct access to the data from the database are in the *run.py* for the same reason.

4. Initial idea of creating a dictionary with the row number as key and the linguist instance returned as a string using the `__str__` method caused issues when applying the sorting function.<br>
After passing through the sorting function, the sorted list returned a `None` object if assigned to another variable.<br>
__FIXED__: Adjusted the program to return a list of objects (Linguists retrieved from the database based on their language attribute) instead of a dictionary, thus allowing the `operand.getattribute` to be used to sort the returned lists. 
Adjusted the `sort_by_criterion()` function to reassign the sorted list to the same variable as that passed in the function, which resolved the issue with a variable being returned as `None`.

5. The `generate_quote` linguist method, after selection of the linguist, raises an error due to incorrect data types.<br>
__FIXED__: Converted class attributes to floats within the functions that calculate total price and turnaround time and changed the `return_word_count()` function in the *word_counter* module to return a `word_count` variable, rather than a string of text. 

6. The `select_linguist()` function in the *linguist_selector* module does not account for input that is not an integer and raises ValueError.<br>
__FIXED__: Added ValueError to exception handling within the function.

7. Removing '0 - none' from the dictionary with sorting criteria in the `select_sort_criteria()` function (*linguist_selector module*) to prevent the linguists listing from printing when 'none' is selected raises KeyError when the user inputs '0' because it is no longer in the dictionary.<br>
__FIXED__: Added an if statement to the function to handle a case with '0' as input separately and adjusted `sort_by_criterion()` function to reflect the new input value. 

8. In order to prevent the linguists' listings from re-printing when no sorting criterion is selected the `print_linguists()` function was moved out of the `main()` function in the  *run* module. But when moved to the `select_sort_criterion()` function within the *linguist_selector* module, the listings that are printed are not sorted.<br>
__FIXED__: Created a separate function that checks for sorting criterion and prints sorted list only if the criterion is not equal to 'none' ('0').

9. Sorting of the linguists' listings sorts them from lower to higher irrespective of the criteria, because all are treated the same way.<br>
__FIXED__: Added an if statement to the `sort_by_criterion()` function in the *linguitst_selector* module to handle specific sorting criteria and reversing sorting for those that require sorting from higher to lower.

10. Sorting linguists by experience does not sort double-digit values correctly. The same issue occurs when sorting by turnaround.<br>
__FIXED__: Changed the `return_linguist()` function that builds an instance of a Linguist class in the *run* module to convert all numerical values retrieved from the database to numbers (integers and the price as float).

11. The use of `itertools` external library to create the order number does not work as expected - restarting of the program clears all instances of the class and resets the count to 0.<br>
__FIXED__: Replaced with a function that grabs the last order number from the database instead and pushes a specified number (101) if there is no order number in the database yet.

12. Attempted e-mail authentication using OAuth2, however, the simple configuration suggested in yagmail documentation does not work as expected.<br>
__NOT FIXED__: Implementation of this feature requires more detailed research and implementation of a more complex code as suggested in a [blog by Macuyiko](https://blog.macuyiko.com/post/2016/how-to-send-html-mails-with-oauth2-and-gmail-in-python.html).

## <a name="deployement-testing"></a>Deployment Testing 
Testing after deployment to Heroku revealed several issues as well.

1. The hidden module with credentials for accessing e-mail, since not pushed to git cannot be used in Heroku.<br>
__FIXED__: Set up account and password values as Config Vars in Heroku and adjusted the code in *confirmation_mailer* module accordingly.
 
2. After deploying to Heroku, `get_user_input()` function does not work - the keyboard shortcut does not force the EOF error and the program does not move forward. Tried adding KeyboardInterrupt but this does not solve the issue.<br>
__FIXED__: Changed function to check for user's input equal to 'DONE' to indicate they are finished inputting data. 'DONE' is not case sensitive for ease of use. Changed instructions to reflect the change in the code and adjusted the word counting formula to reduce the word count by one to exclude 'DONE', which is the last typed string.

3. The `total_price` in the printed listings is rounded to one instead of two decimal places when the last digit is '0'.<br>
__FIXED__: Added number formatting to the calculation of the `total_price` in the `__str__` linguist method to print with 2 decimal places.

4. Linguist selection recognises 0 and negative selection as a valid input, treating it as index `[-1] [-2]` etc.<br>
__FIXED__: Added an if statement to the `select_lingusit()` function in the *linguist_selector* module to handle inputs that are 0 or lower.