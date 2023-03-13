x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
print(x)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = "Bryant"
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = "Andres"
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)

students = [
            {'first_name':  'Michael', 'last_name' : 'Jordan'},
            {'first_name' : 'John', 'last_name' : 'Rosales'},
            {'first_name' : 'Mark', 'last_name' : 'Guillen'},
            {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def defiterateDictionary(some_list):
    for dict in some_list:
        output=""
        for info in dict:
            output += f"{info} - {dict[info]}, "
        print(output)
defiterateDictionary(students)

def iterateDictionary2(key_first_name, some_list):
    for dict in some_list:
        print(f"{dict[key_first_name]}")
iterateDictionary2('first_name', students)

def  iterateDictionary2(key_last_name, some_list):
    for dict in some_list:
        print(f"{dict[key_last_name]}")
iterateDictionary2('last_name', students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(list):
    for key in list:
        print(len(list[key]), key.upper())
        for key_info in list[key]:
            print(key_info)
print_info(dojo)