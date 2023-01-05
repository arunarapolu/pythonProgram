#message="First python program using vs code"
#print(message)

#greating="welcome"
#print(greating)
#message=greating.lower()
#print(message)

#i=1
#j=2
#while(i<=10):
    #table=j*i
    #print(j,'*',i, '=' ,table)
    #i=i+1
    
#print(bytes(4))

#mylist=[1,2,3,4,5,6]
#for i in range(len(mylist)):
    #print(mylist)
    
#print(int('101',2))
#Dictionaries
#animals={'a': 'dog','b':'cat','c':'tiger','d':'moose'}
#animals['e']='elephant'
#print(animals)
#print(animals.keys())
#print(animals.values())
#for(i in range(animals.keys())):
#converting map to list
#listvalies=list(animals.keys())
#print(listvalies)
#animals['g']=['geraf','goat','gorilla']
#print(animals)


#mylist=[1,2,3,4,5,6]
#mylist2=[2*item for item in mylist]
#print(mylist2)

#mylist=list(range(100))
#mylist2=[item for item in mylist if item % 10!=0]
#print(mylist2)

#entername=input('enter your name')
#print(entername,'hello')
mylist=[('fruit1','apple'),('animal1','cat'),('flower1','rose')]
mylist2={key: values for key,values in mylist}
print(mylist2)


