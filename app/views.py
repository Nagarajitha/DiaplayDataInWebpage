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

        QLTO = Topic.objects.all()

        #LOOKups

        #for pattern searching we go for startswith,endswith,contains --> its not case sensitive

        QLTO = Topic.objects.filter(topic_name__startswith = 'a') # its like a pattern searching LIKE operator in sql
        QLTO = Topic.objects.filter(topic_name__startswith = 'c')
        QLTO = Topic.objects.filter(topic_name__startswith = 'h')
        QLTO = Topic.objects.filter(topic_name__endswith = 'c')
        QLTO = Topic.objects.filter(topic_name__endswith = 'ey')
        QLTO = Topic.objects.filter(topic_name__endswith = 't')
        QLTO = Topic.objects.filter(topic_name__contains = 'c')
        QLTO = Topic.objects.filter(topic_name__contains = 'a')
    #in lookup
        QLTO = Topic.objects.filter(topic_name__in=('Chess','Cricket'))





        
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


#LOOKups

    #for pattern searching we go for startswith,endswith,contains --> its not case sensitive

    QLWO = Webpage.objects.filter(name__startswith = 'a') # its like a pattern searching LIKE operator in sql
    QLWO = Webpage.objects.filter(name__startswith = 'r')
    QLWO = Webpage.objects.filter(url__startswith = 'a')
    QLWO = Webpage.objects.filter(url__endswith = 'in')
    QLWO = Webpage.objects.filter(url__contains = 'a')
    QLWO = Webpage.objects.filter(url__contains = 'o')
    #QLWO = Webpage.objects.filter(topic_name__startswith ='h')
    #QLWO=Webpage.objects.all()

    #In lookup
    QLWO = Webpage.objects.filter(name__in =('Dhoni','Virat'))

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


#LOOKups

    #for pattern searching we go for startswith,endswith,contains --> its not case sensitive

    #QLAO = AccessRecord.objects.filter(name__startswith = 'a')-->it is foreign key column we can't use lookupd coz its object
     # its like a pattern searching LIKE operator in sql
    QLAO = AccessRecord.objects.filter(author__startswith = 'r')
    QLAO = AccessRecord.objects.filter(author__endswith ='d')
    QLAO = AccessRecord.objects.filter(author__contains ='d')
    QLAO = AccessRecord.objects.all()
    #__year lookup
    QLAO = AccessRecord.objects.filter(date__year ='1999')

    #__month lookup
    QLAO = AccessRecord.objects.filter(date__month =9)
    #__day lookup
    QLAO = AccessRecord.objects.filter(date__day =17)

    #IN lookup
    QLAO = AccessRecord.objects.filter(author__in =('msd','virat'))

    #__gt lookup(greater than > )
    QLAO = AccessRecord.objects.filter(date__year__gt=1990)

    #__lt lookup(lessthan <)
    QLAO = AccessRecord.objects.filter(date__year__lt=1990)
    #__gte lookup(greater thanequalsto >= )
    QLAO = AccessRecord.objects.filter(date__year__gte=1990)
    #__lte lookup(lessthan equal to <=)
    QLAO = AccessRecord.objects.filter(date__year__lte=1990)

    #Foreign Key columns
    #QLAO = AccessRecord.objects.filter(name__startswith ='v')

    d={'QLAO':QLAO}
    return render(request,'display_access.html',d)




#Lookups --> helps to fetch the data based on conditions precisely
    #__startswith - > fetch the data which starts with given value
    #__endswith - > fetch the data which ends with given value
    #__contains - > fetch the data which contains (means if data have the value wherever) it returns
    # ---> startswith,endswith,contains are case insensitive
