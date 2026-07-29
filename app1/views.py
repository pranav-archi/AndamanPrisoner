from django.shortcuts import render

# Create your views here.
def home(request):
    lucky,unlucky=andaman_prisoners(100)
    return render(request,'app1/index.html',{'param1':lucky,'param2':unlucky})

def andaman_prisoners(total_prisons):
    prisons=[]
    for i in range(0,total_prisons,1):
        prisons.append('C')
    

    for i in range(0,total_prisons,1):
        prisons[i]='O'
    

    for i in range(1,len(prisons),2):
        prisons[i]='C'
    

    for j in range(2,len(prisons),1):   
        for i in range(j,len(prisons),j+1):
            if prisons[i]=='C':
                prisons[i]='O'
            else:
                prisons[i]='C'
   
    lucky=[]
    unlucky=[]
    for i in range(len(prisons)):   
        if prisons[i]=='O':
            lucky.append(i+1)
        else:
            unlucky.append(i+1)

    return lucky, unlucky

