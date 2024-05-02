from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from app.models import *

from django.db.models.functions import Length

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
        QLTO = Topic.objects.all().order_by('topic_name')#orders topic_name colun accroding to ASCII values in ascending order

        QLTO = Topic.objects.filter(topic_name = 'Cricket').order_by('topic_name') # filters all Cricket topics 

        QLTO = Topic.objects.all().order_by('-topic_name')#orders topic_names column in descending order based on ASCII Values

        QLTO = Topic.objects.order_by(Length('topic_name'))#orders in asc order based on length 

        QLTO = Topic.objects.order_by(Length('topic_name').desc())#orders based on length in descending order 
        QLTO = Topic.objects.exclude(topic_name='Cricket')

        
        d = {'QLTO':QLTO}

        return render(request,'display_topics.html',d)
    
def display_webpages(request):

    QLWO=Webpage.objects.all().order_by('topic_name')
    QLWO = Webpage.objects.all().order_by('topic_name')#orders topic_name colun accroding to ASCII values in ascending order
    QLWO = Webpage.objects.filter(topic_name='Cricket').order_by('topic_name') #filters all Cricket topics accroding to ASCII values in ascending order
    QLWO = Webpage.objects.filter(topic_name='Hockey').order_by('topic_name') # filters all hockey topics 
    QLWO = Webpage.objects.filter(topic_name ='Football').order_by('id')
    QLWO = Webpage.objects.order_by(Length('name'))#orders in asc order based on length  of name column
    QLWO = Webpage.objects.order_by(Length('url'))#orders in asc order based on length  of url column
    QLWO = Webpage.objects.order_by(Length('name').desc())#orders in desc order based on length  of name column
    QLWO=Webpage.objects.filter(topic_name = 'Chess').order_by('name')
    QLWO = Webpage.objects.exclude(topic_name='Cricket')


    d={'QLWO':QLWO}
    return render(request,'display_webpages.html',d)

def display_access(request):

    QLAO=AccessRecord.objects.all()
    QLAO = AccessRecord.objects.all().order_by('date')#orders date column in ascending order
    QLAO = AccessRecord.objects.all().order_by('-author') # order in desc order based on author 
    QLAO=AccessRecord.objects.all()[::-1] #in reverse order using slicing on list
    QLAO=AccessRecord.objects.all()[3:5:] # get only 4,5
    QLAO=AccessRecord.objects.order_by(Length('name').desc())
    QLAO=AccessRecord.objects.filter(author='msd').order_by('id')
    #QLAO=AccessRecord.objects.filter(name='dhoni').order_by('name')
    QLAO = AccessRecord.objects.exclude(author='msd')
    d={'QLAO':QLAO}
    return render(request,'display_access.html',d)

