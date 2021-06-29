from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'quotes':'i am not in danger, i am the danger, now say my name','number':10}
    return render(request,'urlapp/index.html',my_dict)

def other(request):
    my_dict = {'quotes':'i am not in danger, i am the danger, now say my name'}
    return render(request,'urlapp/other.html',my_dict)

def relative(request):
    return render(request,'urlapp/relative_url.html')
    