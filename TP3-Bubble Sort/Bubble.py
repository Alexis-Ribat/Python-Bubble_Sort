'''
Created on 26 nov. 2019

@author: alrib
'''
#MyStack = []

StackSize= 10

def DisplayStack(MyStack):

    print("Stack currently contains:")

    for Item in MyStack:

        print(Item)

def Push(MyStack, Value):

    if len(MyStack) < StackSize:

        MyStack.append(Value)

    else:

        print("Stack is full!")

def Pop(MyStack):

    if len(MyStack) > 0:

        MyStack.pop()

    else:

        print("Stack is empty.")

MyStack = []

Push(MyStack,1)

Push(MyStack,2)

Push(MyStack,3)

DisplayStack(MyStack)

 
def bubbleSort(arr):

    n = len(arr)


    # Traverse through all array elements

    for i in range(n):


        # Last i elements are already in place

        for j in range(0, n-i-1):


            # traverse the array from 0 to n-i-1

            # Swap if the element found is greater

            # than the next element

            if arr[j] > arr[j+1] :

                arr[j], arr[j+1] = arr[j+1], arr[j]

               
# Driver code to test above

arr = [64, 34, 25, 12, 22, 11, 90]


bubbleSort(arr)


print ("Sorted array is:")

for i in range(len(arr)):

    print ("%d" %arr[i]),
    
    # 1. Jack's dictionary

jack = { "name":"Jack Frost",

         "assignment" : [80, 50, 40, 20],

         "test" : [75, 75],

         "lab" : [78.20, 77.20]

       }

        
# 2. James's dictionary

james = { "name":"James Potter",

          "assignment" : [82, 56, 44, 30],

          "test" : [80, 80],

          "lab" : [67.90, 78.72]

        }

# 3. Dylan's dictionary

dylan = { "name" : "Dylan Rhodes",

          "assignment" : [77, 82, 23, 39],

          "test" : [78, 77],

          "lab" : [80, 80]

        }

# 4. Jessica's dictionary

jess = { "name" : "Jessica Stone",

         "assignment" : [67, 55, 77, 21],

         "test" : [40, 50],

         "lab" : [69, 44.56]

       }

# 5. Tom's dictionary

tom = { "name" : "Tom Hanks",

        "assignment" : [29, 89, 60, 56],

        "test" : [65, 56],

        "lab" : [50, 40.6]

      }

# Function calculates average 

def get_average(marks):

    total_sum = sum(marks)

    total_sum = float(total_sum)

    return total_sum / len(marks)

  

# Function calculates total average

def calculate_total_average(students):

    assignment = get_average(students["assignment"])

    test = get_average(students["test"])

    lab = get_average(students["lab"])

  

    # Return the result based

    # on weightage supplied

    # 10 % from assignments

    # 70 % from test

    # 20 % from lab-works

    return (0.1 * assignment +

            0.7 * test + 0.2 * lab)

# Calculate letter grade of each student

def assign_letter_grade(score):

    if score >= 90: return "A"

    elif score >= 80: return "B"

    elif score >= 70: return "C"

    elif score >= 60: return "D"

    else : return "E"

 

# Function to calculate the total

# average marks of the whole class

def class_average_is(student_list):

    result_list = []

  

    for student in student_list:

        stud_avg = calculate_total_average(student)

        result_list.append(stud_avg)

        return get_average(result_list)

  

# Student list consisting the

# dictionary of all students

students = [jack, james, dylan, jess, tom]

  
# Iterate through the students list

# and calculate their respective

# average marks and letter grade

Max=[]

for i in students :

    #calculate_total_average(i)

    print(i["name"])

    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")

    print("Average marks of",i["name"], "is :", calculate_total_average(i))

    print("Letter Grade of",i["name"], "is :", assign_letter_grade(calculate_total_average(i)))

# Calculate the average of whole class

class_av = class_average_is(students)

print( "Class Average is %s" %(class_av))

print("Letter Grade of the class is %s "

        %(assign_letter_grade(class_av)))