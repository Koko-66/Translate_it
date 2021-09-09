# TESTING
The program was tested at each step of the development within the development environment. The testing process included:
1. [User Stories testing](#user-stories-testing)
2. [Validation testing](#validation-testing)
3. [Performance testing](#performance-testing)
4. [Development testing](#bugs-and-fixes)

## <a name="user-stories-testing"></a>User Story testing
1. I know what is the purpose of the service and can follow instructions on how to use it.<br>
    On running the code the user is presented with an introduction to the service and its brief introductions. Each step of the program is accompanied by relevant instructions
2. I can see the languages available and select the one into which I want to translate my file.<br>
    The list of available languages is extracted from the database and printed at the start of the program. 
3. I can copy the text for translation to get the word count.
    The user can copy lines or pieces of text to translate and receives feedback from the program about the word count.
4. I can see a list of linguists available in my selected language along with their information.<br>
    A list of linguists matching the selected language is printed once the word count is finished. 
5. I am given information about how much the translation into my selected language would cost and how long it would take depending on the linguist.<br>
    The listings include the linguists' ID, name, language, experience, rating, price per word, the total price for the text and its estimated turnaround time.
6. I can select the language I wish to translate into and correct my selection if I made a mistake.<br>
    The user is asked to select the language and then confirm their selection. If selection is not confirmed, the user is asked to select the language again.
7. I can sort the linguists depending on the selection criterion that is most important to me.<br>
    The user has an option to sort the listings of linguists according to their price, time needed to complete translation (turnaround time), experience and rating.<br>
8. I can place an order and receive confirmation on the screen and via e-mail that it has been placed.<br>
    Once the linguist is selected and confirmed, the user receives feedback on the screen and email with order details.
9. I know at what stage in the process I am, what process is running in the background and can confirm my selections at different points.<br>
    Throughout the program, the user receives feedback on their input and the program's background activities, instructions on expected input and is asked to confirm their choices.
10. The program runs smoothly, does not take too long and does not crash when my input is not correct.<br>
    Testing has shown that the program runs quickly and for the functions that might take a bit longer feedback message is printed informing about the background process. Various input validation methods are implemented throughout the program to handle exceptions and errors that might be caused by the user input.
  
## <a name="vlaidator-testing"></a>Validator testing 
- Run through [Pep 8 online check](http://pep8online.com/) validator
- Used flakes and cornflakes-linter VS Code extension to validate code as as it's been developed. 

## <a name="performance-testing"></a>Performance testing
Performance testing was done by running the program. 

## <a name="bugs-and-fixes"></a>Development Testing
Each feature was tested while being developed to ensure correct and error-free functionality.
Bugs encountered during the development and their fixes are listed below.

1. In the *word_counter* module copy/pasting text that contains newline causes the shell to interpret the new line text as a new command rather than part of the text and preventing it from running correctly.<br>
__FIXED__ Used method that creates a list to which pasted text is appended line by line and then converted to a string using join() method. Solution found on [Stackoverflow](https://stackoverflow.com/questions/34889012/how-to-paste-multiple-lines-of-text-into-python-input). This also allows the user to input multiple texts.

2. *word_counter* module runs input request before printing instructions, even if this function is called later. The same happens when imported module to the main *run.py* module, despite the input request function not being called in the module.<br>
__FIXED__ Removed `@split_text` decorator, which was causing this issue, and used the function with `get_user_input()` as an argument instead.

3. Creating a Linguist instance from Google Sheet data in the *linguist_selector* module requires importing sheet data from the main *run* module, causing circular import issues.<br>
__FIXED__ Moved the function to the *run* module to avoid setting up the worksheet access in the *linguist_selector* module as well. All functions needing direct access to the data from the database are in the run.py for the same reason.

4. Initial idea of creating a dictionary with row number as key and the linguist instance returned as a string using the `__str__` method caused issues when applying the sorting function. In the sorting function, when sorted list assigned to another variable returned `None` object.<br>
__FIXED__ Adjusted the program to return a list of objects (Linguists pulled in from the database based on their language attribute) instead of a dictionary, thus allowing the use of `operand.getattribute` to sort returned lists. 
Adjusted `sort_by_criterion()` function to reassign the sorted list to the same variable as that passed in the function.

5. The `generate_quote` linguist method, after selection of the linguist, raises an error due to incorrect data types.<br>
__FIXED__ Converted class attributes to floats within the functions that calculate total price and turnaround time and changed the `return_word_count()` function in the *word_counter* module to return `word_count` variable, rather than a string of text. 

6. The `select_linguist()` function in the *linguist_selector* module does not account for input that is not an integer and raises ValueError.<br>
__FIXED__ Added ValueError to exception handling within the function.

7. Removing '0 - none' from the criteria dictionary in the `select_sort_criteria()` function (*linguist_selector module*) to prevent the linguists listing from printing when 'none' is selected raises KeyError when the user inputs '0' since it is no longer in the dictionary.<br>
__FIXED__ Added an if statement to the function to handle a case with '0' as input separately and adjusted `sort_by_criterion()` function to reflect the new input value. 

8. In order to prevent the linguists' listings from re-printing when no sorting criterion is selected the `print_linguists()` function was moved out of the `main()` function in the  *run* module. When moved to the `select_sort_criterion()` function within the *linguist_selector* module, the listings that are printed are not sorted.<br>
__FIXED__ Created a new function that checks for sorting criterion and prints sorted list only if the criterion is not equal to 'none' ('0').

9. Sorting of the listings of the linguists sorts them from lower to higher irrespective of the criteria, since all are treated the same way.<br>
__FIXED__ Added an if statement to the `sort_by_criterion()` function in the *linguitst_selector* module to handle specific sorting criteria and reversing sorting for those that require sorting from higher to lower.

10. Sorting the linguists by experience does not sort double-digit values correctly. Later in the development, the same issue becomes apparent when sorting by turnaround.<br>
__FIXED__ Changed the `return_linguist()` function that builds an instance of a Linguist class in the *run* module to convert all numerical values pulled in from the database as numbers (integers and the price as float).

11. The use of `itertools` external library to create the order number does not work as expected, since restarting the program clears all instances of the class and resets the count to 0.<br>
__FIXED__ Replaced with a function that grabs the last order number from the database instead and pushes a specified number (101) if there is no order number in the database yet.

12. Attempted e-mail authentication using OAuth2, however simple configuration suggested in yagmail documentation does not work as expected. 
__NOT FIXED__ Implementation of this feature requires more detailed research and implementation of a more complex code as instructed [here](https://blog.macuyiko.com/post/2016/how-to-send-html-mails-with-oauth2-and-gmail-in-python.html).
