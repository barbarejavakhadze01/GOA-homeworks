# # Classwork 4: List Manipulation and Aggregation
# 1. Create a list named temperatures that contains the following values representing daily temperatures: [72, 68, 75, 70, 78, 74, 71].
# 2. Calculate and print the highest temperature using the max() function.
# 3. Calculate and print the lowest temperature using the min() function.
# 4. Calculate and print the average temperature using the sum() function divided by the length of the list.
# 5. Use a list comprehension to create a new list named above_70 that contains only the temperatures above 70 degrees.
# 6. Print the above_70 list. - ?

temperatures = [72, 68, 75, 70, 78, 74, 71]

highest_temp = max(temperatures)

lowest_temp = min(temperatures)

average_temp = sum(temperatures) / len(temperatures)

print("Highest Temperature:", highest_temp)
print("Lowest Temperature:", lowest_temp)
print("Average Temperature:", average_temp)
