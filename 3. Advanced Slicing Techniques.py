# Task 1: Given the list of temperatures

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

second_week = temperatures[7:14]
#print(second_week)


# Task 2: Extract all the temperatures above 100

over_100 = []
for temp in temperatures:
    if temp > 100:
        over_100.append(temp)

#print(over_100)


# Task 3: Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.

temperatures.reverse()
day_5_to_10_from_rev = temperatures[4:10]

#print(day_5_to_10_from_rev)