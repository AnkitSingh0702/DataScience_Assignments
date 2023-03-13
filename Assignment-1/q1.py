salaries = [(83000, 8.7), (88000, 8.1), (48000, 0.7), (76000, 6), 
            (69000, 6.5), (76000, 7.5), (60000, 2.5), (83000, 10), 
            (48000, 1.9), (63000, 4.2)]

# Group the salaries based on their tenure
less_than_two = []
between_two_and_five = []
more_than_five = []

for salary, tenure in salaries:
    if tenure < 2:
        less_than_two.append(salary)
    elif tenure >= 2 and tenure <= 5:
        between_two_and_five.append(salary)
    else:
        more_than_five.append(salary)

# Compute the average salary for each group
avg_salary_less_than_two = sum(less_than_two) / len(less_than_two)
avg_salary_between_two_and_five = sum(between_two_and_five) / len(between_two_and_five)
avg_salary_more_than_five = sum(more_than_five) / len(more_than_five)

# Print the messages based on the average salary for each group
if avg_salary_less_than_two > avg_salary_between_two_and_five and avg_salary_less_than_two > avg_salary_more_than_five:
    print("Users with less than two years of experience have the highest average salary.")
elif avg_salary_between_two_and_five > avg_salary_less_than_two and avg_salary_between_two_and_five > avg_salary_more_than_five:
    print("Users with between two and five years of experience have the highest average salary.")
else:
    print("Users with more than five years of experience have the highest average salary.")

print("Average salary for users with less than two years of experience:", avg_salary_less_than_two)
print("Average salary for users with between two and five years of experience:", avg_salary_between_two_and_five)
print("Average salary for users with more than five years of experience:", avg_salary_more_than_five)
