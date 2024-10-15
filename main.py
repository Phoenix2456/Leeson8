"""
Create a function that determines if a string contains any digits and returns that information to the function call. 

Summary: function that returns whether or not a string contains any digits.
Input: a string (not from user)
Edge case: Empty string
Output: True/False

Coding tools needed: return, print, for loop, if

More info needed: How do we define the condition of being a digit? .isdigit()
"""


def contains_digits(a_string):
    for character in a_string:
      if character.isdigit():
        return True
      return False
    
text_1 = contains_digits("Bye")
text_2 = contains_digits("Hello")
text_3 = contains_digits("ABC easy as 123")

print(f"Test 1: {text_1}")
print(f"Test 2: {text_2}")
print(f"Test 3: {text_3}")
  


"""
def contains_digits(a_string): <---sample code given

  FOR character in string
    IF character = a digit
      RETURN True
  RETURN False

function call var = function call with string argument
PRINT function call var


"""