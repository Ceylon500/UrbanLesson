#Словарь
my_dict={"Honda":250, "Yamaha":450}
print(my_dict)
print("Existing key:", my_dict["Honda"])
print("Non existing key:", my_dict.get("Suzuki"))
my_dict.update({"KTM":350, "Kawasaki":450})
pop = my_dict.pop("KTM")
print(my_dict)
print(pop)
#Множество
my_set={1, 2, 3, 4, 4, 5, True, True, "Yes", "yes", "yeS", "yes"}
print(my_set)
print(my_set.add(7))
print(my_set.add("ADDED"))
print(my_set.remove(3))
print(my_set)