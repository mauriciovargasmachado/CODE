from io import StringIO


documento = open("lineas.txt")
cuenta = 0
for line in documento:
    cuenta = cuenta +1 
print ("number of lines: "+ str(cuenta) )