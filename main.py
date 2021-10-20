from urllib import parse
from googlesearch import search
question = input("enter question::")

for i in search(question,num=10,stop=10,pause=2):
    print(i)