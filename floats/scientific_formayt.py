#Scientific Notation#
"we can use pyhton to represent large numbers in scientific format"
'''syntax : print("%e"%number)'''

print("%e"%100)
#output : 1.000000e+02
"+02 shows the index of the 10th power it could be in - mark also as necessary"


print("%e"%0.098)
#output : 9.800000e-02


''' lets see the values which can rounded off using sci notation '''

print("%.e"%749.02)
#output :7e+02

print("%.e"%750.02)
#0utput :8e+02

print("%.1e"%749.02)
#output :7.5e+02

print("%.1e"%769.02)
#output :7.7e+02


print("%10.1e"%765.00)
#output :   7.6e+02


