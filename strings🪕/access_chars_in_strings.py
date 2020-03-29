################# Accessing Characters in a string by index ######################

'syntax: stringname(index)'

s= 'I love python'

'''

I   l o v e   p y t h o n
0 1 2 3 4 5 6 7 8 9 10 11 12

'''

print(s[0])
#output = I


#!  Lower Bound


print('lower bound:',s[4:]) #lower bound prints

#!  Upper Bound

print('upper bound:',s[:4]) #upperbound do not print


print(s[2:6])
#prints a range form the string
