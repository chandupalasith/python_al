############# String Formatting #################

print("%s"%"Chandupa")
print()
#output is normal as me ;)

print("%8s"%"Chandupa")
print()
#in that case there are 8 letters in the string nothing special happens


print("%15s"%"Chandupa")
print()
#it keeps the spaces now! | output:       Chandupa

print("%0.4s"%"Chandupa")
print()
#cuts off the by 4th letter | output:Chan


print("%15.4s"%"Chandupa")
print()
#cuts off the by 4th letter and keeps 15 charaters in total | output:       Chan

