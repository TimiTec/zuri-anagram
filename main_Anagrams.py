# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


    
Userinput1 = input("Enter the first word: ")
Userinput2 = input("Enter the second word: ")

def find_anagram(word, anagram):
    # [assignment] Add your code here
    
    str1 = Userinput1
    str2 = Userinput2

    str1 = str1.lower()
    str2 = str2.lower()

    if(len(str1) == len(str2)):
        sorted_str1 = sorted(str1)
        sorted_str2 = sorted(str2)
    
    if(sorted_str1 == sorted_str2):
        print(str1 + " and " + str2 + " are anagram. True")

    if(sorted_str1 != sorted_str2):
        print(str1 + " and " + str2 + " are not anagram. False")

    return True

find_anagram(1,2)