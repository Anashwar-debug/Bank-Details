from django.shortcuts import render,redirect
import urllib.request
import json
from django.contrib import messages
from urllib.error import HTTPError, URLError

def index(request):
    ifsc=''
    data={}
    if request.method=='POST':
        ifsc=request.POST['code']
        if ifsc:
            try:
                ifsc=ifsc.replace(" ","").upper()
                res=urllib.request.urlopen('https://bank-apis.justinclicks.com/API/V1/IFSC/'+ifsc)
                if res.status==404:
                    messages.info(request,"IFSC does not exist")
                json_data=json.load(res)
                data={
            "address":str(json_data['ADDRESS']),
            "bank":str(json_data["BANK"]),
            "branch":str(json_data['BRANCH']),
            "centre":str(json_data['CENTRE']),
            "city":str(json_data['CITY']),
            "contact":str(json_data['CONTACT']),
            "ifsc":str(json_data['IFSC']),
            "state":str(json_data['STATE'])

            
        }
                return render(request, 'index.html', {'data': data})
            except HTTPError as e:
                if e.code==404:
                    messages.info(request,"invalid ifsc")

        else:
            
            messages.info(request,"ifsc cannot be empty")



    return render(request,'index.html',{'data':data})








        









# Create your views here.
