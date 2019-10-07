# Var #1 

# Python3 program to find the 
# number of charters in the 
# longest word in the sentence. 
def LongestWordLength(str): 

	n = len(str) 
	res = 0; curr_len = 0
	
	for i in range(0, n): 
		
		# If current character is 
		# not end of current word. 
		if (str[i] != ' '): 
			curr_len += 1

		# If end of word is found 
		else: 
			res = max(res, curr_len) 
			curr_len = 0

	# We do max one more time to consider 
	# last word as there won't be any space 
	# after last word. 
	return max(res, curr_len) 

# Driver Code 
s = "I am an intern at geeksforgeeks"
print(LongestWordLength(s))                                

------------------------------------------------------------------------------------------------------------------
# Var 2 

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








