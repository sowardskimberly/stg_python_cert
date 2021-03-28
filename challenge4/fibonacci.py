# Define list values for number conversion
ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
            'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']
twenties = ['', 'tens', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety',
                'one hundred']
thousands = ['zero', 'hundred', 'thousand', 'million', 'billion']


# Create function to solve the nth value of the fibonacci sequence
def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


# Convert an int (num) into words where  1,000 > num > 0
def num2words_conversion(num):
    len_num = len(str(num))
    if num <= 20:  # ones
        o = ones[num]
        return o
    elif 20 < num < 100:  # tens
        ten_split = divmod(num, 10)
        t = twenties[ten_split[0]]
        o = ones[ten_split[1]]
        to = t + " " + o
        return to
    elif len_num == 3:  # hundreds
        div_ten = divmod(num, 100)
        h = ones[div_ten[0]] + " hundred and "
        if div_ten[1] <= 20:
            t = ones[div_ten[1]]
            return h + t
        else:
            ten_split = divmod(div_ten[1], 10)
            t = twenties[ten_split[0]]
            o = " " + ones[ten_split[1]]
            return h + t + o


# Convert an int (num) into words where 1,000,000 > num > 999
def thousands2words(num):
    thousand_hundreds = divmod(num, 1000)
    thousand = num2words_conversion(thousand_hundreds[0]) + " thousand "
    hundreds = num2words_conversion(thousand_hundreds[1])
    return thousand + hundreds


# Convert an int (num) into words where 1,000,000,000 > num > 999,999
def millions2words(num):
    millions_thousands = divmod(num, 1000000)
    million = num2words_conversion(millions_thousands[0]) + " million "
    thousand = thousands2words(millions_thousands[1])
    return million + thousand


# Convert an int (num) into words where 1,000,000,000,000 > num > 999,999,999
def billions2words(num):
    billions_millions = divmod(num, 1000000000)
    billions = num2words_conversion((billions_millions[0]) + " billion ")
    millions = millions2words(billions_millions[1])
    return billions + millions


# Convert any int (num) from 0 < num < 1,000,000,000,000 into words
def words2numgreat3(num):
    num_length = len(str(num))

    if num_length <= 3:  # hundreds or less length
        hundreds_words = num2words_conversion(num)
        return hundreds_words

    elif 3 < num_length < 7:   # thousands
        return thousands2words(num)

    elif 6 < num_length < 10:  # millions
        return millions2words(num)

    elif 9 < num_length < 13:  # billions
        return billions2words(num)
    else:
        print(str(num) + ' Number is too big')
