from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from app.models import *

def insert_topic(request):
    tn=input('enter topic_name : ')

    TO=Topic.objects.get_or_create(topic_name=tn)[0]

    TO.save()
    d={'QLTO':Topic.objects.all()}
    return render(request,'display_topics.html',d)



def insert_webpage(request):
    tn=input('enter topic_name : ')
    

    #TO=Topic.objects.get(topic_name=tn)
    '''We can use get method to get the Parent Table Object but if parent table object is 
    not available it throws an error'''
    TO=Topic.objects.filter(topic_name=tn)
    if TO:
        n=input('enter name :')
        u=input('enter url :')
        e=input('enter email :')
      
        WO=Webpage.objects.get_or_create(topic_name=TO[0],name=n,url=u,email=e)[0]
        WO.save()
        d={'QLWO':Webpage.objects.all()}
        return render(request,'display_webpages.html',d)
    else:
        return HttpResponse('Given Topic is Not present in My Parent Table')



def insert_access(request):
    name = input('Enter webpage name: ')
    
    # Check if the Webpage exists
    WO = Webpage.objects.filter(name=name)
    
    if WO:
        # If Webpage exists, use the first one found
        wp = WO[0]
        
        date = input('Enter date: ')
        author = input('Enter  author: ')
        
        # Create AccessRecord using get_or_create
        ARO = AccessRecord.objects.get_or_create(name = wp, date=date, author=author)[0]
        ARO.save()
        d={'QLAO':AccessRecord.objects.all()}
        return render(request,'display_access.html',d)
   
    else:
        return HttpResponse('Given webpage is not present in the database')
    


def display_topics(request):
        QLTO = Topic.objects.all()
        d = {'QLTO':QLTO}

        return render(request,'display_topics.html',d)
    
def display_webpages(request):

    QLWO=Webpage.objects.all()
    d={'QLWO':QLWO}
    return render(request,'display_webpages.html',d)

def display_access(request):

    QLAO=AccessRecord.objects.all()
    d={'QLAO':QLAO}
    return render(request,'display_webpages.html',d)

