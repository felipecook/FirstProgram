my_shopping_list = ['apples', 'bananas', 'eggplant']


# iterates through the above list.
def my_program():
    for i in my_shopping_list:
        print(i)


my_program()

test_text = "hello world"


# this slices the above test from the sixth character onward.
def my_second_program():
    print(test_text[6:])


# this grabs a portion of the above text from the 2nd position (inclusive) to the 5th position exclusive
def my_third_program():
    print(test_text[2:5])


my_second_program()
my_third_program()
