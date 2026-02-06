#Dictionary
emp1={
    "name":"Rahul Das",
    "id":"23je21s",
    "age":20,
}
print(emp1["name"])
#keyerror:Proper key name is  not given
emp1["salary"]=30000#add a new key
print(emp1)
empty_dict={}
empty_dict["added"]="yes"
print(empty_dict)
#clear the dictionary
empty_dict={}
print(empty_dict)
#edit dictionary
emp1["age"]=30
print(emp1)
#loops
for things in emp1:
    print(things)#things represent the key names
    print(emp1[things])#this represents the value
#nested dictionaries
capitals={
    "India":"New Delhi",
    "France":"Paris",
}
travel_log={
    "France":["Paris","Little","Dijon"]
}
print(travel_log["France"])
nested_list=["a","b",["c","d"]]
print(nested_list[2][1])#d
#dictionary inside dictionary
nested_dict={
    "France":{
        "num":1,
        "city":"Paris",
    },
    "India":{
        "num":2,
        "city":["Kolkata","Nasik"]
    }
    
}
print(nested_dict["India"]["city"][0])#Kolkata
#max ()==>> 
frutis={"apple":2,"pear":90,"mango":4}
print(max(frutis, key=frutis.get))
