 # Python program to find the number of characters  
# in the longest word in the sentence.  
  
def longestWordLength(string): 
      
    length = 0
      
    # Finding longest word in sentence 
    for word in string.split(): 
        if(len(word) > length): 
            length = len(word) 
      
    return length  
  
# Driver Code 
string = "I am an intern at geeksforgeeks"
print(longestWordLength(string)) 

#2 
# Python program to find the number of characters  
# in the longest word in the sentence.  
  
def longestWordLength(string): 
      
    length = 0
      
    # Finding longest word in sentence 
    for word in string.split(): 
        if(len(word) > length): 
            length = len(word) 
      
    return length  
  
# Driver Code 
string = "I am an intern at geeksforgeeks"
print(longestWordLength(string)) 

