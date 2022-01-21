"""
# ------ 1-----
age= int(input("Enter your age"))
print("her age is" + age)

# -------- 2--------
import random
number = random.randint(1, 25)

for i in range(5):
    print("enter a number between 1 to 25")
    guess = int(input())

    if guess < number:
        print("Your guess is low")
    if guess > number:
        print("Your guess is high")
    if guess == number :
        print("on point!!!!")
        break;

if guess == number:
    print("Correct answer")

else :
    print("better luck next time")
    
# Output 2:
enter a number between 1 to 25
23
Your guess is high
enter a number between 1 to 25
15 Your guess is low
enter a number between 1 to 25
18
Your guess is low
enter a number between 1 to 25
20
Your guess is high
enter a number between 1 to 25
19
on point!!!!
Correct answer  

# ------------ 3 ----------
number = int(input("Enter number"))
print(float(number))


#--------------- 4 addition ------------
first = int(input("First"))
second = int(input("second"))
sum = first + second
print(sum)
print("enter sum is" + str(sum))

 Output :
First4
second5
9
enter sum is9

#------------ 5 String --------
name = "Atharva Mulay"
print(name)
print(name.upper())
print(name.find('a')) #3
print(name.find("lay")) #10
print(name.find("mulay")) #-1
print(name.replace("Atharva", "At")) #At Mulay
print('v' in name) # True
print("at" in name) # False
print("Atharva" in name) # True


#------ 6 Arithmatic opearators --------
print(5+2) #7
print(5-2) #3
print(5*2) #10
print(5/2) #2.5
print(5//2) #2
print(5**2) #25 power opearator


# ------ 7 Logical operators ------
print( 2 > 3 and 2 > 1) #False
print(2 > 3 or 2 > 1) # True
a = 2 > 3
print(a) #False
print(not a) #True
print(not 2>3) #True


#------- 8 If else ----------
age = 16
if age>=18 :
    print("You are adult")
elif age<18 and age>3:
    print("You are in school")
else :
    print("You are kid")

print("Ty")



#------ 9 Range -------
numbers = range(5) #0,1,2,3,4
print(numbers) #range(0, 5)


#-------10 While loops -----
i = 1
while i <=5:
    print(i)
    i += 1
Output : 
1
2
3
4
5

i = 5
while i>=0 : 
    print(i*"*")
    i = i - 1
*****
****
***
**
*


# ------ 11 For loop ---------
for i in range(5):
    print(i)
0
1
2
3
4


#------ 12 List -------
marks = [90, 92, 98, 94, 97, 93]
print(marks) #[90, 92, 98, 94, 97, 93]
print(marks[0]) # 90
print(marks[-1]) # 93
print(marks[1:5]) # [92, 98, 94, 97]

marks.append(76) #insertion of element at last
print(marks) # [90, 92, 98, 94, 97, 93, 76]

marks.insert(4, 67) #insert 67 at index 4
print(marks) # [90, 92, 98, 94, 67, 97, 93, 76]

print(76 in marks) # True
print(len(marks)) # 8



i=0
while i < len(marks): # Gives error if we write i<= len(marks)
    print(marks[i])
    i = i + 1 

for i in range(len(marks)):
    print(marks[i])


print("sorted list")
marks.sort()
print(marks) #[67, 76, 90, 92, 93, 94, 97, 98]
print("reverse list")
marks.reverse()
print(marks) #[98, 97, 94, 93, 92, 90, 76, 67]

""" 
