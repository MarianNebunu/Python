list = [ ["Mama", "Papa", "Brother", "Sister"], [23, 45, 67, 89] ]
print(list[1][2]) 
touple = ("Mama", "Papa", "Brother", "Sister")
print(touple[0])   
set = {"Mama", "Papa", "Brother", "Sister"}
print(set)  # This will raise an error because sets do not support indexing

#list[0] = "Grandma"  # This will work because lists are mutable
#touple[] = "Grandma"  # This will raise an error because tuples are immutable
list.append(1)
print(list)  # This will add the integer 1 to the end of the list
list.remove(["Mama", "Papa", "Brother", "Sister"])
print(list)  # This will remove the integer 1 from the list
set.add("Grandma")
print(set)  # This will add "Grandma" to the set
