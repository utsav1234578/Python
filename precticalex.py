#1.Reverse the given string(You can take any string) 
x ="utsav"
print(x[::-1])

#2.Replace some character of the string with another character without using a loop.
y="hello word"
print(y.replace("h","o"))

#3.Find whether the character in the given string or not.
x = "hello"
char ='o'
if char in x:     
    print("yes")
else:
    print("no")

#4.Create tuple, list and set and convert them into the different strings.
a=("world","word","worl")
b=[1,2,3]
c=["u","t","s"]
print(str(a))
print(str(b))
print(str(c))

#5.Convert all the string characters to the upper and the lower case and split it with the different methods.
uppercase = x.upper()
splitu = uppercase.split()
print(splitu)
lowercase = x.lower()
splitl = lowercase.split()
print(splitl)

#6.Perform the following operations to the tuple and the list Find max, min, len, sum
tup =[1,2,3,4]
lis =[5,6,7,8]
print(max(tup),min(tup),len(tup),sum(tup))
print(max(lis),min(lis),len(lis),sum(lis))

#7.Copy one list to the another list without using the copy command.
list1 =[10,20,30,40]
list2 =list1[:]
print(list2)

#8 Perform below task as instructed
#	-> Create a dictionary named student with keys: 'name', 'age', and 'grade'. Assign 	values accordingly.
#	Access Dictionary Values:
#	-> Print the 'age' of the student from the dictionary created in Exercise 1.
#	Modify Dictionary Values:
#	-> Update the 'grade' of the student to a new value.
#	-> Check if the key 'gender' is present in the student dictionary. Print a message 	based on the result.
student = {'name':"utsav",'age':"19",'grade':"A"}
print(student["age"])
student["grade"] ="A+"
print(student["grade"])

#9. Perform below task as instructed
#   3-> Create two sets: set1 with elements (1, 2, 3) and set2 with elements (3, 4, 5).
#	Union of Sets:
#   -> Find the union of set1 and set2 and print the result.
#   Intersection of Sets:
#   -> Find the intersection of set1 and set2 and print the result.
#   Difference of Sets:
#   -> Find the elements that are in set1 but not in set2 and print the result.
#	Check Subset:
#   -> Check if set1 is a subset of set2. Print a message based on the result.
set1 ={1,2,3}
set2 ={3,4,5}
print(set1|set2)#union
print(set1 & set2)#insersection
print(set1 -set2)#difference
print(set1.issubset(set2))

# 10. Perform below task as instructed
# 	Create a dictionary where keys are subjects ('math', 'science') and values are sets of students who take those subjects.
# 	Update Set Values:

# 	Add a new student to the 'math' subject in the dictionary from Exercise 11.
# 	Remove Set Values:

# 	Remove a student from the 'science' subject in the dictionary from Exercise 11.
# 	Check Common Students:

# 	Find and print the students who take both 'math' and 'science'.
# 	Nested Dictionary:

# 	Create a nested dictionary where each key represents a country, and the value is 	another dictionary containing cities and their populations.
edu = {"math":
        {"krish", "kunj"},
        "science":
        {"utsav","kalpan"}
        }

edu["math"].add("yash")
print(edu)
edu["science"].remove("kalpan")
print(edu)

student = {'name': 'John', 'age': 20, 'grade': 'A', 'science': {'Alice': {'age': 22, 'grade': 'B'}, 'Bob': {'age': 21, 'grade': 'C'}}}
if 'science' in student:

    if 'Alice' in student['science']:
        removed_student = student['science'].pop('Alice')
        print("Removed student from 'science' subject:", removed_student)
    else:
        print("Student 'Alice' not found in 'science' subject.")
else:
    print("No 'science' subject found in the dictionary.")

# Print the updated dictionary
print("Updated dictionary:", student)

countries = {
    'India': {
        'Junagadh': 362001 ,
        'Delhi': 1122,
        'Bangalore': 123456
    },
    'USA': {
        'New York': 11,
        'Los Angeles': 22,
        'Chicago': 33
    },
    'China': {
        'Shanghai': 44,
        'Beijing': 55,
        'Guangzhou': 66
    }

}
print(countries)

# 11. Create two lists, one containing elements at even indices and the other containing elements at odd indices from the original list.
student = {'name': 'John', 'age': 20, 'grade': 'A', 'science': {'Alice': {'age': 22, 'grade': 'B'}, 'Bob': {'age': 21, 'grade': 'C'}}}
if 'science' in student:
    if 'Alice' in student['science']:
        removed_student = student['science'].pop('Alice')
        print("Removed student from 'science' subject:", removed_student)
    else:
        print("Student 'Alice' not found in 'science' subject.")
else:
    print("No 'science' subject found in the dictionary.")

print("Updated dictionary:", student)

# 12. Use tuple packing and unpacking to swap the values of two variables without using a temporary variable.
a = 5
b = 10
a, b = b, a

print("a after swapping:", a)
print("b after swapping:", b)

# 13. Check if a given list is a palindrome using slicing.
def is_palindrome(lst):
    return lst == lst[::-1]

test_list1 = [1, 2, 3, 4, 5]
test_list2 = [1, 2, 3, 2, 1]

print(is_palindrome(test_list1))
print(is_palindrome(test_list2))

# 14. oncatenate two tuples without using the + operator.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple(tuple1 + tuple2))