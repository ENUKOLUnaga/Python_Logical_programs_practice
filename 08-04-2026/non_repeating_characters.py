def non_repeating_character(str):

    for i in str:
        count=0
        for j in str:
            if i==j:
                count+=1
            
            if count>1:
                break
        if count==1:
            return i
        
str=input("Enter a string: ")
print(f"non repeating character from a string {non_repeating_character(str)}")
