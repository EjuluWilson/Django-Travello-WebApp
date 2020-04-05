from django.shortcuts import render

def home(request): 
    return render(request,"home.html") #launch the home.html template

# this functio requests/launches/calls the input.html template
def calc(request):
    return render(request,"inputs.html")


#function returns a sum on the the  template results.thml
def add(request):
    x = request.POST["num1"]
    y = request.POST["num2"]
    sum = int(x)+int(y)
    #seend to results.html
    return render(request,"results.html",{"result":sum})
