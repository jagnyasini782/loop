from django.shortcuts import render

# Create your views here.

def condition(request):
    d={'name':'ritu','age':22}
    return render(request,'condition.html',context=d)



