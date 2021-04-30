# STG Certification 1 Python

## Challenge 1
Within test_challenge1.py, write a new test that does the following:

Go to google.com
Assert that the results page that loads has “google” in its title


## Challenge 2
Create test_challenge2.py and write a test that does the following:

Go to copart.com
Search for "exotics"
Assert "PORSCHE" is in the list of cars on the Results Page


## Challenge 3
Create test_challenge3.py and write a test that does the following:

Go to copart.com
On the Home Page, under Most Popular Items, there is a Makes/Models section. For each Make or Model in this section, print the name of the Make or Model with its URL (aka href) next to it
Example Output: SILVERADO - https://www.copart.com/popular/model/silverado


## Challenge 4
Fibonacci (recursion)

Create test_challenge4.py and write a test that does the following:

Displays the fibonnaci sequence for N numbers
However, print the number(s) as English words
Example: If the sequence is 18, then print "Eighteen"

Example: If the seqence value is 120, then print "One Hundred Twenty"

This challenge starts the use of a helper file


## Challenge 5
Part 1 - Create test_challenge5.py and write a test that does the following:

Go to copart.com
Search for "porsche"
Change Show Entries to 100
Print the number of occurrences for each Model
Example: There might be x3 PANAMERA T and x11 CAYENNE

Part 2 - Using the same, first three steps of Part 1, write a test that then does the following:

Count the number of occurrences of each Damage type
However, you need to map the Damage types to these:
REAR END
FRONT END
MINOR DENT/SCRATCHES
UNDERCARRIAGE
Any Damage type that does NOT match the above types should be grouped into a MISC Damage type
Example: SIDE and ALL OVER would each count towards MISC

Example Output: REAR END: 2, FRONT END: 7, MINOR DENT/SCRATCHES: 22, UNDERCARRIAGE: 0, MISC: 4

This file uses the class Cars found in the library/libs folder


## Challenge 6
Create test_challenge6.py and write a test that does the following:

Go to copart.com
Search for 'nissan'
Then for the Model, search 'skyline'. This is a rare car that might not exist
If it doesn't exist, catch the exception and take a screenshot

This file uses the class Cars found in the library/libs folder


## Challenge 7
Create test_challenge7.py and write a test that does the following:

Go to copart.com
Look at the Makes/Models section of the page
Create a two-dimensional list that stores the names of the Make/Model as well as their URLs
Check that each element in this list navigates to the correct page

This file uses the class Cars found in the library/libs folder
