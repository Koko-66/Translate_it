# <a name="bugs-and-fixes"></a>Bugs and Fixes
This file contains a list of bugs I came across during the development of the program and their fixes.

1. In the *word_counter* module copy/pasting text that contains new line causes shell to interpret the new line text as a new command rather than part of text and preventing it from running correctly.<br>
__FIXED__ Used method that creates a list to which pasted text is appended line by line, and then converted to a string using join() method. Solution found on [Stackoverflow](https://stackoverflow.com/questions/34889012/how-to-paste-multiple-lines-of-text-into-python-input). This also allows the user to input mutliple texts.

2. *word_counter* module runs input request before printing instructions, even if this function is called later. Same happens when imported module to the main run.py file, despite the input request function not being called in the module.<br>
__FIXED__ Removed @split_text decorator, which was causing this issue, and used the function with get_user_input as an argument instead.

3. Creating Linguist instance from Google Sheet data in the *linguist_selector* module requires importing sheet data from the main *run* module, causing circular import issues.<br>
__FIXED__ Moved the function to the *run* module to avoid setting up the worksheet access in the *linguist_selector* module as well. All functions needing direct access to the data from the database are in the run.py for the same reason.

4. Initial idea of creating a dictonary with row number as key and the linguist instance returned as string using *str* method caused issues when applying sorting function. In the sorting function, when sorted list assigned to another variable returned None object.<br>
__FIXED__ Adjusted the program to return a list of objects (Linguists pulled in from the database based on their language attribute) instead of a dictionary, thus allowing the use of *operand.getattribute* to sort returned lists. 
Adjusted *sort_by_criterium* function to reassign the sorted list to the same variable as that passed in the function.

5. The generate_quote lingusit method, after selection of the linguist, raises an error due to incorrect data types.<br>
__FIXED__ Converted class attributes to floats within the functions that calculate total price and turnaround time and changed the *return_word_count* function in the *word_counter* module to return word_count variable, rather than a string of text. 

6. The select_linguist function in the *linguist_selector* module does not account for input that is not an integer and raises ValueError.<br>
__FIXED__ Added ValueError to exception handling within the function.

7. Removing '0 - none' from the criteria dictionary in the select_sort_criteria function (*linguist_selector module*) to prevent the linguists listing from printing when "none" is selected raises KeyError when the user inputs '0', since it is no longer in the dictionary.<br>
__FIXED__ Added an 'if statement to the function to handle a case with '0' as input separately and adjusted sort_by_criterium function to reflect the new input value. 

8. In order to prevent the linguists listings from re-printing when no sorting criteria is slected, the the print_linguists function was moved out of the main function in the  *run*. When moved to the select_sort_criteria function within the *linguist_selector* module, the listings that are printed are not sorted.<br>
__FIXED__ Created a new function that checks for sorting criteria and prints sorted list if criterium is not 'none' ('0').

9. Sorting of the lingusits' listings sorts them from lower to higher irrespective of the criteria, since all are treated the same way.<br>
__FIXED__ Added an if statement to the sort_by_criterium function in the *linguitst_selector* module to handle specific sorting criteria and reversing sorting for those that require sorting from higher to lower. Sorting by turnaround required addition of function returning the float value to allow sorting.

10. Sorting the linguists by experience does not sort double digit values correctly. Later in developement, same issue becomes appearent when sorting by turnaround.<br>
__FIXED__ Changed the return_linguist function in the *run* module to convert all numerical values pulled in from the database as integers and the price as float.

11. The use of itertools to create the order number does not work as expected, since restarting the program clears all instances of the class and resets the count to 0.<br>
__FIXED__ Replaced with a function pushing a specified number for first order (101) and then incrementing that each time a new order is created.
