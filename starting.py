# import requests
# from bs4 import BeautifulSoup
# import smtplib
# import datetime

# now = datetime.datetime.now() #Reason: To create email subject line that show appropriate date that email was sent.
# content = ""

# #below extracts HackerNews BlogPost/Content

# def extract_News(url):
#     print("Extracting Hacker News Story")
#     cnt = "" #This line is used to assign value to this "content" variable above
#     cnt =+("<b>HackerNews Top stories:</b> \n"+"<br>"+"-"*50+"<br>")
#     response = response.get(url)
#     content = response.content #Content here is different from the content above in the first line. Block scope only :)
#     soup = BeautifulSoup(content,"html.parser" )
#     for i, tag in enumerate(soup.find_all("td", attrs={"class": "title","valign":""})):
#         cnt += ((str(i+1)+' :: '+ '<a href="' + tag.a.get('href') + '">' + tag.text + '</a>' + "\n" + '<br>') if tag.text!='More' else '')
#                 #print(tag.prettify) #find_all('span',attrs={'class':'sitestr'}))
#         return(cnt)
    
# cnt = extract_News('https://news.ycombinator.com/')
# content += cnt
# content += ('<br>------<br>')
# content +=('<br><br>End of Message')















# print("This is week one of python for data science")

# num3 = 4
# num2 = 3
# print(2/2)
# print(str(1 + 1))

# A=(1,2,3,4,5)
# print(A[1:4])



# def collatz(number):
#     if number % 2 == 0:
#         result = number // 2
#         print(result)
#         return result
#     else:
#         result = 3 * number + 1
#         print(result)
#         return result

# while True:
#     try:
#         n = int(input("Enter a positive integer: "))
#         if n <= 0:
#             raise ValueError
#         break
#     except ValueError:
#         print("Invalid input. Please enter a positive integer.")

# while n != 1:
#     n = collatz(n)



# import matplotlib.pyplot as plt
# import numpy as np

# y = np.array([35, 25, 25, 15])

# plt.pie(y)
# plt.show() 






























# name = "Eric"
# for i in range(4):
#     print(name[i])







# from itertools import permutations











# from itertools import product

# a = [1, 2]
# b = [3, 4]
# product = product(a,b)
# print(list(product))



# dictName = {"name":"Eric", "age" : 35}

# print(dictName["name"])

# if "age" in dictName:
#     print("Yes name is available")
# else:
#     print("not found")



#Tuples

#NOTE tuples are immutable.
# list = ("this", 3, "everything")
# print(type(list))


# for i in list:
#     print(i, end=', ')
#     break

# print ("WEveything is okay")
# print(len(list))

# list = ["Dog", "Cat", "camel"]
# if "everything" in list:
#     print("Yes. It is present")
# else:
#     print("not found.")

# list.append("books")
# print(list)

# list.insert(1, "Everything")
# print(list)

# x = list.pop()
# print(x)

# print(list)

# list.reverse()
# print(list)

# newList = sorted(list)

# copyList = list.copy()
# print(copyList)
# print(newList)





# num1 = [1, 2, 3, 4, 5, 6, 7]
# numsqr = [ i * i for i in num1]
# print(numsqr)
 
# class question:
#     def __init__(self, name, age , everything):
# tuples cannot be changed after creation!!. PLEASDE TAKE NOTE!!







# name = "Eric"

# for x in name:
#     print(x)






# secreteWord = "giraffe"
# counter = 0
# guessWord = ""
# guessLimit = 3
# outOfGuesses = False

# while guessWord != secreteWord and not(outOfGuesses):
#     if counter < guessLimit:
#         guessWord = input("Enter Another Guess")
#         counter += 1
#     else: 
#         outOfGuesses = True
   
    
# if outOfGuesses:
#     print ("Out of Guesses, You Lose!")
# else:
#     print ("YOU WiN!")





















# i = 1

# while i <= 10:
#     print (i)
#     i +=1

# print ("Done")









# try:
#     num1 = float(input("Type First Number: "))
#     operator = input("Type operator: ")
#     num2 = float(input("Type Second Number: "))

# except ValueError:
#         print("That was not a number. Please try again.")

# if operator == "*" :
#     print(num1 * num2 )
# elif operator == "+" :
#     print(num1 + num2)
# elif operator == "-" :
#     print( num1 - num2)
# elif operator == "/" :
#     print (num1 / num2)

# else:
#     print ("Type the correct operation")















# def sayHi(name, age):
#     print("Hello" + name + "You are " + str(age) + " years old")
# sayHi("Eric", 78)






# color = input("What is your favorite color?: ")
# anything = input ("what is your thing?: ")
# pluralName = input("Type your name")


# print ("roses are ", color)
# print ("Violets are ", anything)
# print ( "i love ", pluralName)





# from math import *

# name = input ("Type your Name: ")

# #This is a comment in python. 

# print ("Hello \n", name[0].upper())