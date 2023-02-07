from django.shortcuts import render


# Create your views here.
import datetime
def filters (request):
    t=datetime.datetime.now()
    d={'filter':'My Name BHEEMAsena','t':t,'a':5}
    

    return render(request,'filters.html',d)
