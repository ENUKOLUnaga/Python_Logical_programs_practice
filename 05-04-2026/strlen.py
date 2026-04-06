def str_len(str):
    count = 0
    for i in str:
      count+=1
    return count
str=input("Enter a string: ")
print(f"length of {str} is : {str_len(str)}")
