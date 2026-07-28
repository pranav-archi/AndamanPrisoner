from django.shortcuts import render

# Create your views here.
def home(request):
    result=andaman_prisoners(10)
    return render(request,'app1/index.html',{'param1':result})
prisons=[]
def andaman_prisoners(total_prisons):
    f1=open('letter1.txt','w')
    f2=open('letter2.txt','w')
    
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

    f1.write("Prisoners from these cells will be released today:\n")
    f2.write("Prisoners from these cells will be released after 4 weeks:\n")

    lucky=[]
    unlucky=[]
    for i in range(len(prisons)):   
        if prisons[i]=='O':
            lucky.append(i+1)
        else:
            unlucky.append(i+1)

    for cell in lucky:
        f1.write(f"{cell}\n")

    for cell in unlucky:
        f2.write(f"{cell}\n")
    f1.close()
    f2.close()

