############### Fuctions in Strings ################



# ( ͡° ͜ʖ ͡°) Length Function len()

'This function is used to cout the number of characters in a string'

s='''Does Ranil still holds the leadership?'''
print(len(s))
#output: (count the characters including letters, spaces,and those !@#$%%^&* , you may find it ¯\_(ツ)_/¯ )





# ( ͡° ͜ʖ ͡°)  Strip Function strip()

'This function resturns a string which the leading(infront) & trailing(behind) wide spaces removed'


# Enter your name with trailing and leading white spaces

x=input("Who is your Valentine?").strip()
print(x)

# output : Who is your Valentine?
#        : ______sushi________ ('_' stands for spaces you type)
#        : sushi

'use lstrip() to remove leading white spaces and rstrip() to remove trailing white spaces'





# ( ͡° ͜ʖ ͡°)  Count Function count()

'This returns a number of occurances of substring of a given string'

m='I still love my ex!'

occurance_of_l = m.count("l")

print(occurance_of_l)

#output: l repeats 3 times so the output is 3






# ( ͡° ͜ʖ ͡°)  Uppr,Lower and Capitalize Function   upper() | lower() | capitalize()


text1= 'I am working at CID!'


'upper()'
'This converts whole lowercase characters into uppercase and returns it'

print(text1.upper())
#output: I AM WORKING AT CID!


'lower()'
'This converts whole upper characters into lowercase and returns it'

print(text1.lower())
#output: i am working at cid!!


'capitalize()'
'This convert first letter of a sring into uppercase and others to lowercase'

text2='i am your worst friend'
print(text2.capitalize())
#Output : I am your worst friend









