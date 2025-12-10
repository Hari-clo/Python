#Dictionary
dict={"one":1, "two":2, "three":3,"four":4}
print("dictinoary",dict)

#update
dict["two"]="02"
print("updated",dict["two"])

#copy
num=dict.copy()
print(num)

#get value
t=dict.get("one")
print(t)

my_dict = {'apple': 'fruit', 'carrot': 'vegetable'}
print(my_dict['apple'])  # Outputs: fruit
print(my_dict.get('banana', 'not found'))  # Outputs: not found

print(my_dict.keys())  # Outputs: dict_keys(['apple', 'carrot'])

print(my_dict.values())  # Outputs: dict_values(['fruit', 'vegetable'])
print(my_dict.items())  # Outputs: dict_items([('apple', 'fruit'), ('carrot', 'vegetable')])

my_dict['apple'] = 'green fruit'  # Updates value
my_dict['banana'] = 'yellow fruit'  # Adds new key-value pair

print(len(my_dict))  # Outputs: 3

value = my_dict.pop('carrot')  # Removes 'carrot' and returns 'vegetable'
