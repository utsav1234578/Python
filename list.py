#### list excerise 1 #### 

#1 Declare an empty list.
empty_list =list()
print(empty_list)

#2 Declare a list with more than 5 items.
Fruits = ['Banana','Orange','Mango','Lemon','Apple','Guava','Pineapple']
print('Fruits:',Fruits)

#3 Find the length of your list.
print(len(Fruits))

#4 Get the first item, the middle item and the last item of the list.
first_fruit=Fruits[0]
print((first_fruit))
last_fruit = Fruits[6]
print(last_fruit)
mid=int(len(Fruits)/2)
print(Fruits[mid])

#5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address).
mixed_data_types =['Utsav',19,5.9,'Unmarried','Hostel']
print(mixed_data_types)

#6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(it_companies)

#7 Print the list using _print()_.
print(it_companies)

#8 Print the number of companies in the list.
print(len(it_companies))

#9 Print the first, middle and last company.
first =it_companies[0]
print((first))
last= it_companies[6]
print((last))
mid=int(len(it_companies)/2)
print(it_companies[mid])

# a='string'
# b='5'
# print(a*5-b)

#10 Print the list after modifying one of the companies.
it_companies[6]="tatvsoft"
print(it_companies)

#11 Add an IT company to it_companies.
it_companies.append('IT COMPANY')
print(it_companies)

#12 Insert an IT company in the middle of the companies list.
it_companies.insert(6,"Evosys")
print(it_companies)

#13 Change one of the it_companies names to uppercase (IBM excluded!).
uppercase= it_companies[2].upper()
print(uppercase)

#14 Join the it_companies with a string '#;&nbsp; '.
Join1 = "#;&nbsp;".join(it_companies)
print(Join1)

#15 Check if a certain company exists in the it_companies list.
does_exist= 'Apple' in it_companies
print(does_exist)

#16 Sort the list using sort() method.
it_companies.sort()
print(it_companies)

#17 Reverse the list in descending order using reverse() method.
it_companies.reverse()
print(it_companies)

#18 Slice out the first 3 companies from the list.
compnies=it_companies[0:3]
print(compnies)

#19 Slice out the last 3 companies from the list.
compnies1=it_companies[-3:]
print(compnies1)

#20 Slice out the middle IT company or companies from the list.
mid=int(len(it_companies)/2)
print(it_companies[mid:mid+3])

#21 Remove the first IT company from the list.
it_companies.pop(0)
print(it_companies)

#22 Remove the middle IT company or companies from the list.
mid=int(len(it_companies)/2)
remove2=it_companies.pop(mid)
print(remove2)

#23 Remove the last IT company from the list.
it_companies.pop(6)
print(it_companies)

#24 Remove all IT companies from the list.
it_companies.clear()
print(it_companies)

#25 Destroy the IT companies list.
del it_companies 


#### list excerise 2 ####

#1 The following is a list of 10 students ages.
ages=[13, 12, 17, 15, 19, 16, 24, 21, 26, 20]

#2 Sort the list and find the min and max age.
ages.sort()
print(ages)
print("Min age:",ages[0])
print("Max age:",ages[-1])

#3 Add the min age and the max age again to the list.
ages.extend([ages[0],ages[-1]])

#4 Find the median age (one middle item or two middle items divided by two).
middleindex=len(ages) //2
median_age=(ages[middleindex]) //2 
print("\nMedain age:",median_age)   

#5 Find the average age (sum of all items divided by their number ).
print("\nAverage sum:",sum(ages)/len(ages))

#6 Find the range of the ages (max minus min).
print("\nRange of ages:",max(ages)-min(ages))

#7 Compare the value of (min - average) and (max - average), use abs() method.
min_average=abs(ages[0]-(sum(ages)/len(ages)))
print("\nMin_average:",min_average)
max_average=abs(ages[-1]-(sum(ages)/len(ages)))
print("Max_average:",max_average)

#8 Find the middle country(ies) in the [countries list].
countries=['Usa','India','U.k','Dubai','England']
middle=len(countries)//2
print("\nMiddle country(ies):",countries[middle])

#9 Divide the countries list into two equal lists if it is even if not one more country for the first half.
country=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
mid=len(country)//2
firsthalf=country[:mid]
secondhalf=country[mid:]
if len(country)%2 !=0:
    firsthalf.append(secondhalf.pop(0))
print("\nFirst half:",firsthalf)
print("Second half:",secondhalf)

#10 ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
first_three,scandic_countries=country[:3],country[3:]
print("\nFirst Three countries:",first_three)
print("Scandic countries:",scandic_countries)

