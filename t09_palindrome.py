######################################################################
# Author: Scott Heggen & Emily Lovell      TODO: Change this to your names
# Username: heggens & lovelle             TODO: Change this to your usernames
#
# Assignment: T09: Mad Libs
#
# Purpose: A palindrome is a word, phrase, number, or other sequence of characters
# which reads the same backward and forward.  This program tests phrases
# to determine if they are or are not palindromes.
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Jan Pearce
#
# Modified from the remove punctuation function
#   from http://www.ict.ru.ac.za/Resources/cspw/thinkcspy3/thinkcspy3_latest/strings.html
#
# Palindromes from http://www.buzzfeed.com/fjelstud/the-21-best-palindromes
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import sys


def testit(did_pass):
    """
    Print the result of a unit test.

    :param did_pass: a boolean representing the test
    :return: None
    """
    # This function works correctly--it is verbatim from the text
    linenum = sys._getframe(1).f_lineno         # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def is_palindrome_test_suite():
    """
    The test_suite function utilizes the testit() function and
    is designed to test the is_palindrome() function.

    :return: None
    """
    print("\nRunning is_palindrome_test_suite().")

    print("\n----------------------------------")
    # Testing that non-palindrome's fail
    print("Testing non-palindromes")
    testit(is_palindrome("This is a palindrome--NOT!") == False)
    testit(is_palindrome("No") == False)

    print("\n----------------------------------")
    # Testing that actual palindromes pass
    print("Testing palindromes")
    testit(is_palindrome("Nurses RUN!!!") == True)
    testit(is_palindrome("Mr. Owl ate my metal worm...") == True)
    testit(is_palindrome("Ogre, flog a golfer. GO!") == True)
    testit(is_palindrome("Was it a car or a cat I saw?") == True)
    testit(is_palindrome('A dog! A panic in a pagoda!') == True)

    print("\n----------------------------------")
    # Testing that punctuation gets removed properly
    print("Testing punctuation remover")
    testit(remove_punctuation("No Punctuation!") == "NoPunctuation")
    testit(remove_punctuation("h!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ i") == "hi")

    print("\nRun of is_palindrome_test_suite() complete.\n")


def remove_punctuation(s):
    """
    Returns a string with all punctuation removed from input

    :param s: Any string
    :return: A string with no punctuation
    """
    # modified from http://www.ict.ru.ac.za/Resources/cspw/thinkcspy3/thinkcspy3_latest/strings.html

    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "     # space added
    s_sans_punct = ""           # empty string
    for letter in s:
        if letter not in punctuation:
            s_sans_punct += letter          # s_sans_punct = s_sans_punct + letter
    return s_sans_punct


def is_palindrome(the_str):
    """
    Takes a string input, converts to lowercase, removes punctuation, and
    returns true if the string is a palindrome

    :param the_str: a string suspected of palindrome-ness
    :return: A Boolean representing if the string is a palindrome or not
    """
    lower_input = the_str.lower()
    no_punct_input = remove_punctuation(lower_input)
    # print(nopunctinput)                         # for testing purposes only --remove comment to see nopunctinput
    return no_punct_input == no_punct_input[::-1]    # this is a fancy way to traverse the string forward and backwards


def interactive_test_mode_1():
    """
    Interactive mode 1 requests two inputs from the user and runs a sentence through is_palindrome()
    tester. This method of testing is NOT as effective as a test_suite.  Do you see why?

    :return: None
    """

    input1 = input("Enter a three letter name: ")
    input2 = input("Enter a three letter name: ")

    build_sentence = "'{0}, {1}, note: I dissent! A fast never prevents a fatness. I diet on {1}, {0}!!'".format(input1, input2)

    if is_palindrome(build_sentence):
        print(build_sentence + ' is a palindrome.')
    else:
        print(build_sentence + ' is not a palindrome.')


def interactive_test_mode_2():
    """
    Another interactive mode for testing palindromes. Still, not as effective as the test suite. Do you agree?

    :return: None
    """

    build_sentence = input('Enter possible palindrome for testing:\n')

    if is_palindrome(build_sentence):
        print(build_sentence + ' is a palindrome.')
    else:
        print(build_sentence + ' is not a palindrome.')


def main():
    """
    The main() function is used to demonstrate a couple of methods of testing.

    :return: None
    """
    is_palindrome_test_suite()        # Uncomment this line to run the test suite
    # interactive_test_mode_1()  # Uncomment this line to run the interactive mode 1
    # interactive_test_mode_2()  # Uncomment this line to run the interactive mode 2


if __name__ == "__main__":
    main()          # calls the main() function
