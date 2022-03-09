
# funcion para calcular horas minutos y segundos para una funcion

#def print_seconds(hours, minutes, seconds):
#    print(3600*hours+60*minutes+seconds)
#
#print_seconds(1,2,3)

#months

#def month_days(month,days):
#    print(month + " has " + str(days) + " days.")
#month_days("June","30")
#month_days("July","31")


#def rectangle_area(base,height):
#	area=base*height  # the area is base*height
#	print("The area is " + str(area))
#rectangle_area(5,6)

def is_positive(number):
    if number>0:
        return (True)
    else:
        return(False)

#### chequear si un numero es positivo o negativo


def number_group(number):
  if number>0:
    return ("Positive")
  elif number<0:
    return ("negative")
  else:
    return ("Zero")

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative


####  Calcular tamaño de archivo


def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize//block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize%block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return block_size*(full_blocks+1)
    return full_blocks*block_size

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192


###


def color_translator(color):
	if color == "red":
		hex_color = "#ff0000"
	elif color == "green":
		hex_color = "#00ff00"
	elif color == "blue":
		hex_color = "#0000ff"
	else:
		hex_color = "unknown"
	return hex_color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown


####



def exam_grade(score):
	if score>95:
		grade = "Top Score"
	elif score>=60 and score<100:
		grade = "Pass"
	else:
		grade = "Fail"
	return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail



####


def format_name(first_name, last_name):
	# code goes here
	if first_name== '' and last_name=='':
		string=""
	elif last_name == "":
		string = "Name: "+first_name
	elif first_name=="":
		string = "Name: "+last_name
	else:
		string = "Name: "+last_name+", "+first_name
	return string 

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string



##### WHILE LOOPS ####


def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
    
attempts(5)



#### count down ####


def count_down(start_number):
  current=3
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)



### not infinitive loop ###


def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= end:
		print(n)
		n=n+1

print_range(1, 5)  # Should print 1 2 3 4 5




### 