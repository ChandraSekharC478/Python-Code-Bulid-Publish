# Non promotove data types are mutbale in nature 
# 1. list 
fruits =['Apple','Mango','jackFruit','Banana'];
print(fruits);
print(fruits[3]) # To get the element  in the index value

fruits[2]= 40 # to update the  Value in Particular index 
print (fruits)

fruits.append(56); # to insert the vale at the end 
print (fruits);
print("****** lists is completed********")

# 2.Tuple : it is immuatable in nature 
t1=(1,2,3,4,5)
# t1[4]=6  # since  tuple is immutable it wont work

print (t1);
print("********Tuple  is completed ********")
# Dictonory 
students ={"name":"chandhu" ,"surname":"Kanna" ,"age":"26" ,"rollnumber":24}
print(students)

print(students["surname"]) # to get the Particular Value from Dict or objects
print(students["name"] + students["surname"]); # to append the 2 key value pairs

students.update({"pincode":12345}) # to update the the Dict or objects 

print(students)
  
person ={
    "id" : {
        "name" : "chandra",
        "age"  : "34"
    },
    "adress" :{
        "city" : "Tirupathi" ,
        "pincode" : "517520"
    },
    "work":{
        "company" : "cap",
        "city" :"india"
    }
}
print (person);
print (person["id"]["age"]) # to print an object inside the object
person["work"].update({"company": "Infosys","city":"Banglore"}) # to update the the Dict 
print(person)

person["contact"]= {"phoneNumber" : 9553394020, "email" : "chandhu@gmail.com"} # to insert the Dict

print(person)