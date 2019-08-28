from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
#    return HttpResponse('HELLO')
    return render(request,'home.html',{'name':'i m Dinesh'})

def aboutus(request):
#    return HttpResponse('HELLO')
    return render(request,'aboutus.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    worddict = {}
    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1

        sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    name = request.GET['fname']
    age= find_age(name)
    return render(request,'count.html',{'fulltext':fulltext, 'name':name,'age':age,'Count':len(wordlist), 'worddict':sortedwords })

def fetch_age(request):
    name= request.get('fulltext')
    age= find_age(name)
    return render(request,'count.html',{'name':name,'age':age})


def find_age(name):
    emp_dict =[{'name':'Dinesh','age':25},{'name':'umesh','age':27}]
    for i in emp_dict:
        if name == i['name']:
            emp_age = i['age']
        else:
            emp_age = 1
    return emp_age
