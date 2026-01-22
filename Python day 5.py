#1 Declare an empty list
food=[]

#2. Declare a list with more than 5 items
ages=[22,21,10,18,17,16,19,20, 22]


#3.Find the length of your list

print(len(ages)) #9

#4 Get the first item, the middle item and the last item of the list

first_item= ages[0]
middle_item= ages[4]
last_item= ages[-1]

#5= Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_type= ['Samuel',28,'5ft7','Single','Nigeria']

#6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#7 Print the list using print()

print(it_companies)

#8. Print the number of companies in the list

print(len(it_companies)) #7

#9 Print the first, middle and last company
print(it_companies[0])
print(it_companies[3])
print(it_companies[-1])

#10 Print the list after modifying one of the companies

it_companies[0]= 'Tiktok'
print(it_companies)

#11 Add an IT company to it_companies

it_companies.append('Intel')

#12 Insert an IT company in the middle of the companies list
print(len(it_companies))

it_companies.insert(3,'Tecno')
print(it_companies)

#13 Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[-1]= it_companies[-1].upper()
print(it_companies)

#14 Join the it_companies with a string '#;

joining='#;'.join(it_companies)
print(joining)

#15 Check if a certain company exists in the it_companies list.

print( 'Tecno' in it_companies)


#16. Sort the list using sort() method
it_companies.sort()
print(it_companies)



#17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

it_companies=['Amazon', 'Apple', 'Google', 'IBM', 'INTEL', 'Microsoft', 'Oracle', 'Tecno', 'Tiktok']

#18. Slice out the first 3 companies from the list
first_three= it_companies[0:3]
print(first_three)

#19. Slice out the last 3 companies from the list
last_three= it_companies[-3:]
print(last_three)

#20 Slice out the middle IT company or companies from the list

middle= it_companies[4]
print(middle)

#21 Remove the first IT company from the list

del it_companies[0]
print(it_companies)

#22 Remove the middle IT company or companies from the list
del it_companies[3:5]
print(it_companies)

#23 Remove the last IT company from the list

del it_companies[-1]
print(it_companies)

#24 Remove all IT companies from the list

print(it_companies.clear())

#25 Destroy the IT companies list

del it_companies

#26 Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

coding= front_end + back_end 
print(coding)

#27 After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stck= coding.copy()
print(full_stck)

full_stck.insert(5,'Python')
full_stck.insert(6,'SQL')

print(full_stck)

 # Exercises: Level 2: The following is a list of 10 students ages:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
print(ages)             #[19, 19, 20, 22, 24, 24, 24, 25, 25, 26]

min=19
max=26

# Add the min age and the max age again to the list

ages.insert(0,min)
ages.insert(-1,max)

#Find the median age (one middle item or two middle items divided by two)
print(len(ages))  #12


mid1=ages[-7]
mid2= ages[-6]

median= (mid1+ mid2) /2
print(f'Median age is: {median}')

#Find the average age (sum of all items divided by their number )
import math
average= sum(ages[0::]) / len(ages)

print(f'The averaage age is:{average}')

#Find the range of the ages (max minus min)

print('Range:',(max - min))


#Compare the value of (min - average) and (max - average), use abs() method

value1= min- average
value2= max- average

if abs(value1)> abs(value2) :
    print(f'{value1} is greater')
else:
    print(f'{value2} is greater')



countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

# Find the middle country(ies) in the countries list
print(len(countries))   #195

mid= countries[97]
print(mid)    #Lesotho

#Divide the countries list into two equal lists if it is even if not one more country for the first half

first_half= countries[0 : 98]
second_half= countries[98::]

print(len(first_half))
print(len(second_half))



#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

task= ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

country1= task[0]
country2= task[1]
country3= task[2]
scandic_country= task[3::]

print(country1)
print(country2)
print(country3)
print(f'scandic Countries:{scandic_country}')