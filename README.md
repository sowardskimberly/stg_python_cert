# stg_python_cert
Using python and selenium to test websites

1st Challenge:
Navigate to Google and confirm the title of the page is for Google


2nd Challenge: 
Write a script that will go to copart.com, search for exotics and verify porsche is in the list of cars.  Use the hard assertion for this challenge.  


3rd Challenge: 
For this challenge, go to copart and print a list of all the “Popular Items” of vehicle Make/Models on the home page and the URL/href for each type.  This list can dynamically change depending on what is authored by the content creator but using a loop will make sure that everything will be displayed regardless of the list size.
Your output in the console would look like:
IMPREZA - https://www.copart.com/popular/model/impreza


4th Challenge:
For this challenge, we are going to write a function that display the fibonacci sequence up to a certain number.  If I want the fibonacci for the 9 order of the sequence, I should see 21.  Keep your function to calculate the fibonacci sequence separate from the file that has the unittest.main().

However, to add additional challenge to this challenge, instead of displaying the number 21, I want the string representation of twenty one.  This will require you to use string concatenation to print out the string. 


5th Challenge:
For this challenge, go to https://www.copart.com and do a search for “porsche” and change the  drop down for “Show Entries” to 100 from 20.  Count how many different models of porsche is in the results on the first page and return in the terminal how many of each type exists.  

Possible values can be “CAYENNE S”, “BOXSTER S”, etc.  

For the 2nd part of this challenge, create a switch statement to count the types of damages.
Here’s the types:
REAR END
FRONT END
MINOR DENT/SCRATCHES
UNDERCARRIAGE
And any other types can be grouped into one of MISC.  


6th Challenge:
For this challenge, go to copart site, search for nissan, and then for the model, search for “skyline”.  This is a rare car that might or might not be in the list for models.  When the link does not exist to click on, your script will throw an exception.  Catch the exception and take a screenshot of the page of what it looks like.  


7th Challenge:
For this challenge, take a look at https://www.copart.com main page.  Go to the Makes/Models section of the page.  Create a 2 dimensional array that stores all the values displayed on the page along w/ the URL for that link.  Once you have this array, you can verify all the elements in the array navigates to the correct page.  
