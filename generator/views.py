from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
	# return 'JAI MA SARDE'
	#like this we cannot return string we have to form it as as hhtp response
	#return HttpResponse('JAI MA SARDE')
	#this was working but now we want to return template by rendering it
	return render(request,'generator/home.html',{'password':'whaggawjh72ah'})
	#this dictionary is a passed to home.html and we can reference any item inside key by specifying its key 
	# in home page {{key_of_item}}
def milk(request):
	return HttpResponse('<h1>Milk is good for health</h1>')

def about(request):
	developer='PRASHANT THAKUR'
	return render(request,'generator/about.html',{'name':developer})
def password(request):
	characters=list('abcdefghijklmnopqrstuvwxyz')
	if request.GET.get('Uppercase'):
		characters.extend(list("ABCDEFGHIJKLMNOPQRTUVWXYZ"))
		#extend the list of charecter by uppercase charcter
		#now uppercase character will also be included
	if request.GET.get('special character'):
		characters.extend(list("!@#$%^&*()_+"))
	if request.GET.get('Number'):
		characters.extend(list("1234567890"))
	length=int(request.GET.get('length',12)) #length is name we have specified in home.html form
	#here 12 is default value ie when we dont pass any value and directly go to password without taking input from home page it take 2
	#here length is name of form in html page 
	thepassword=''
	for x in range(length):
		thepassword+=random.choice(characters)#it chose random character from list and append to thepassword
	return render(request,'generator/password.html',{'password':thepassword})
	#inside form in action specify password hence on clicking generate password it goes to password
