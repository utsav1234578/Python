#### Tuples Excercise 1 #### 

#1 Create an empty tuple.
empty_tuple = ()
print(empty_tuple)

#2 Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine).
sisters=('Champa','Pushpa','Hetvi','Devika','Jayti','Palak','Khayati')
brothers=('Jay','Nirav','Krish','Kirtan')
print(sisters)
print(brothers)

#3 join brothers and sisters tuples and assign it to siblings.
siblings=sisters+brothers
print(siblings)

#4 How many siblings do you have?.
total=len(siblings)
print(total)

#5 Modify the siblings tuple and add the name of your father and mother and assign it to family_members.
parents=('Ashvinbhai','Harshaben')
family_members=(parents),(siblings)
print(family_members)

#### Tuples Excercise 2 #### 

#1 Unpack siblings and parents from family_members.
(parents),(siblings)=(family_members)
print(parents)
print(siblings)
print(family_members)

#2 Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits=('watermelon','Guava','Mango','Chiku','Apple')
vegetables=('potato','Cucumber','Tomato','Lemon','Potato')
animal=('Dog','Deer','Lion','Tiger','Zibra')
food_staff_tp=(fruits+vegetables+animal)
print(food_staff_tp)

#3 Change the about food_stuff_tp  tuple to a food_stuff_lt list.
food_staff_lt=food_staff_tp
print(food_staff_lt)

#4 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
mid=int(len(food_staff_lt)/2)
print(food_staff_lt[mid:mid+3])

#5 Slice out the first three items and the last three items from food_staff_lt list.
first=food_staff_lt[0:3]
print(first)
last=food_staff_lt[-3:]
print(last)

#6 Delete the food_staff_tp tuple completely.
del food_staff_lt

#7 Check if an item exists in tuple.
#print('Meat' in food_stuff_tp) ----False bcs tuple deleted

#8 Check if an item exists in  tuple.
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(nordic_countries)
if "Estoin" in nordic_countries:
    print("yes it exists")
else:
    print("No it doesn't exist")

#9 Check if 'Denmark' is a nordic country.
print(nordic_countries)
if "Denmark" in nordic_countries:
    print("yes it exists")
else:
    print("No it doesn't exist")