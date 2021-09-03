### <a name="bugs-and-fixes"></a>Bugs and Fixes
Bugs and Fixes 
1. In word_counter module copy/pasting text that contains new line causes shell to interpret the new line text as a new command rather than part of text, breatking the program.
__FIXED__ Used method that creates a list to which pasted text is appended line by line, and then converted to a string using join() method. Solution found on [Stackoverflow](https://stackoverflow.com/questions/34889012/how-to-paste-multiple-lines-of-text-into-python-input). This also allows the user to input mutliple texts.
2. word_counter module runs input request before printing instructions, even if this function is called later. Same happens when imported module to the main run.py file, even though no function is called in the module.
__FIXED__ Removed @split_text decorator and used the function with get_user_input as an argument instead.
_Note: During the development changed the representation of the language in the Google Sheet database to be in one cell rather than separate. Considering the size of the database and the list of available languages, this seemed a more efficient solution._
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
8. The select_linguist function does not account for input that is not an integer and raises an ValueError. 
__FIXED__ Add ValueError to exception handling within the function.
9. Removing sorting criteria '0 - none' from the dictionary to prevent it from printing, causes an exeption (Invalid input) to be raised when user input is '0', since it is no loger a dictionary key.
__FIXED__ Added if statement to the function to handle case with '0' as input separately and adjusted sort_by_criterium function to reflect the new input value.
10. Adding print to the select_sort_criteria function prints not sorted listings of lingusits, since it happens before listings is sorted. Sorting by experience does not sort double digit values as expected. 
__FIXED__ Created a new function to print after sorting the list that checks for sorting criteria and does not print anything if no sorting is selected. Changed the function creating linguist object to convert experience value to an integer.
11. Sorting of the lingusits' listings is from lower to higher, since all criteria are treated the same way. 
__FIXED__ Added an if statement to handle specific sorting criteria and reversing sorting for those that require sorting from higher to lower. Sorting by turnaround required addition of function returning the float value to allow sorting.
12. Use of itertools to create order number does not work as expected, since restarting the program clears all instances of the class and resets the count to 0. 
__FIXED__ Replaced with function pushing a specified number for first order and then incrementing that each time a new order is created.

### <a name="unfixed-bugs"></a>Unfixed Bugs
<!-- Ctrl+d to exit text for translation input does not always work and requires Enter. Might need to change instructions to account for that. Not sure how this would behave once on Heroku. -->
<!-- 3. Order number restarts each time the program is run, since it is a new session. Generate from the sheet instead? -->