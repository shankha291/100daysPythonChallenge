#Randomization
import random
print(random.randint(12,14))#inclusive of a and b means a<=n<=b
print(random.random()*10)#0.0<=x<1.0
print(random.uniform(9,30))#0.0<=n<=b
toss=random.randint(0,1)
if(toss==0):
    print("Head")
else:
    print("Tail")
    
#Lists
list1=["item1",23]#Different data types allowed
print(list1[0])
print(list1[-1])
list1[1]=13330
print(list1[1])#Item can be changed 
list1.append("New")#Appending on a list
list1.extend(["A1","A2"])#appending more than one items
print(list1)

friend=["Alice","Jenny","John","Shaan"]
victim=random.choice(friend)#1st way
print(victim," Will pay the bill")
random_index=random.randint(0,3)
victim2=friend[random_index]#2nd way
print(victim2," Will pay the bill")
#Error->IndexError{Index goes out of the range}
#len() function
len1=len(friend)
print(friend[len1-1])#last item
#Nested lists
list2=["a","b","c","d"]
list3=[1,2,3,4]
list4=[list2,list3]
print(list4)