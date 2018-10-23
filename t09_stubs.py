#################################################################################
# Author: Ela Jamali, Emely Alfaro Zavala
# Username: Jamalie, Alfarozavalae
#
# Assignment: T09: Mad Libs
# Purpose: Additional practice breaking a larger problem down into smaller "pieces" using functions.
# Gain practice using strings.
#################################################################################
# Acknowledgements:
#################################################################################


def story_time(answers):
    """
        This function alocates the user's input into the text to print an mad lib email.
    :param answers: parameter to get the user's input from main
    :return:
    """
    print('''Dear professor, {0}  
    
    I wanted to let you know that I will not be able to attend class today because I broke my {1} when I was {2} on the sofa. 
    I feel very {3} to miss your lecture.
    Also, last week, I did not submit the homework in Github because my {4} ate the paper I was working the algorithm on.
    
    "I apologize for being such a {5} student.
    Best,
    {6}'''.format(*answers))                    # this print statement contains a long string that uses {} to replace the numbers with
                                                # the input's that the user entered in main. we use format to add them in the spaces


def main():
    """
    Main function to ask the user for seven inputs that will be used in a function. uses for loop to run the same input statement and append them afterwards.
    """
    input_user = ["last_name", "body_part", "ing_verb", "adjective", "animal", "adjective_2", "your_name"]          # seven inputs that we will ask the user for
    answers = []                        # creating empty list
    for i in range(7):                  # loop to run 7 times and ask user for input
        answers.append((str(input("Please enter " + input_user[i]))))       # appending the user's input in a list
    story_time(answers)                                                     # calling story_time function


main()
