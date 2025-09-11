


#IF statement in single line
"""food = input("food: ")

print("Sweet") if food == "cake" or food == "jalebi" else print("not sweet")"""







#IF statement in single line


"""food = input("food : ")

eat = "Yes" if food == "rice" else "No"

print(eat)"""



#Clever IF

"""age = int(input("Enter your age : "))
vote = ("no","yes")[age>=18]

print(vote)"""






#IF statement in single line

"""age = int(input("Enter your age = "))
vote = "yes" if age >= 18 else "no"

print(vote)"""



#Arthimetic operator

"""a = 10
b = 20

print(a==b)"""




#str = "apna"
#print(len(str))





#IF elif program 


"""marks = int(input("Enter your Marks:"))

if(marks>=90):
  print("Your grade is A+")

elif(marks>=80 and marks<90):
   print("Your grade is A")

elif(marks>=70 and marks<80):
    print("Your grade is B")   
else: 
   print("Your grade is C")"""  


#Dictionary update method

"""student = {
    
    "name" : "vamshi",
    "subjects" : {
        
       "chem" : 96,
       "phy"  : 95,
       "math" : 92
    }
}

student.update({"city" : "Hyderabad"})
print(student)"""


#Multiplication of a number

"""i=1;

while(i<=10):
    print("3 *",i,"=",3*i)
    i+=1"""

#Multiplication of a number with user input

"""num = int(input("Enter a integer to multiply : "))
i=1

while i<=10 :
    print(num,"*",i,"=",num*i)
    i+=1"""


"""i=1

while(i<=10):
    if(i%2== 0):
        i+=1
        continue
    print(i)
    i+=1"""


"""str = "pythn"

for char in str:
    
   if(char == 'o'):
        print("o found")
        break
   print(char)
else:
   print("END")"""


"""num = (1,4,9,16,25,36,49,64,81,100)

x=49
i=0

for el in num:
   if(el==x):
        print(f"found {x} at index value = {i}")
   i+=1"""


"""num = (1,4,9,16,25,36,49,64,81,100)

i=0
for el in num:
        print(i,el)
        i+=1"""


"""def average(a,b,c):
   total = (a+b+c)/3
   return total 


avg = average(56,89,32)

print(avg)"""


"""cities =["Hyderabad", "Bangalore", "Mumbai", "chennai", "Delhi"]
heros = ["Iron man", "spider man", "thor", "Hulk"]

def length(list1=cities,list2=heros):
    print(len(list1))
    print(len(list2))
    
length()"""


print("Hello python")