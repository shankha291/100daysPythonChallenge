#LOOPS
#for-in loop
fruits=["apple","mango","lemon"]
for fruit in fruits:
    print(fruit)
score=[12,43,21,2,1,2]
print(sum(score))#sum() funcion
print(max(score))#max() function
sum=0
for s in score:
    sum+=s
print(sum)
max=0
for s in score:
    if(s>max):
        max=s
print(max)
for number in range(1,10):#excludes the last one
    print(number)
for number in range(1,6,2):
    print(number)