from django.shortcuts import render
from .models import Destination

#Create your views here.
dest1 = Destination("Atutur","my birth place","500k","destination_2.jpg",True)
dest2 = Destination("Bukedea","cool place","700k","destination_6.jpg")
dest3 = Destination("Kumi","try it out","800k","destination_4.jpg")

dests = [dest1,dest2,dest3] #object array

def launch_travello(request):

    #pass the  destination object to the HTML
    return render(request,"index.html",{"dests":dests})
    #You will thereafter be able to call these objects using {{}} in the HTML
    #call example: {{dests.0.name}} == dests.dest1.name


