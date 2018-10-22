#################################################################################
# Author: Ela Jamali, Emely Alfaro Zavala
# Username: Jamalie, Alfarozavalae
#
# Assignment: T09: Mad Libs
# Purpose: Additional practice breaking a larger problem down into smaller "pieces" using functions.
# Gain practice using strings.
#################################################################################
# Acknowledgements:
#
#
#################################################################################


def story_time(answers):
    """
    Docstring for function_1
    """
    print('''Dear professor, {0}
    
    I wanted to let you know that I will not be able to attend class today because I broke my {1}.
    When I was {2} on the sofa. I feel very {3} because I will miss your lecture.
    Also, last week, I did not submit the homework in Github because my {4} ate the paper I was working the algorithm on.
    
    "I apologize for being such a {5} student.
    
    Best,
    {6}'''.format(*answers))


def function_2():
    """
    Docstring for function_2
    """
    pass
    # ...


def main():
    """
    Docstring for main
    """
    input_user = ["last_name", "body_part", "ing_verb", "adjective", "animal", "adjective_2", "your_name"]
    answers = []
    for i in range(7):
        answers.append((str(input("Please enter " + input_user[i]))))
    story_time(answers)


main()
