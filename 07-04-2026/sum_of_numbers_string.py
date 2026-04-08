#counting sum of numbers in a string
def num_counter(str):
    counter=0
    for i in str:
        if ord(i)>=48 and ord(i)<=57:
            counter=counter+1
    return counter

str=input("Enter a string: ")
print(f"count of numbers in {str} is : {num_counter(str)}")
