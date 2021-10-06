salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]
new_salary_list = []
salary_indexing = []
for i in range(len(salary_list)):
    new_salary_list.append( round ( (salary_list[i] + ( (salary_list[i]*30)/100)) , 2) )
    salary_indexing.append(new_salary_list[i]-salary_list[i])

for i in range(len(salary_list)):
    print(salary_list[i], round(salary_indexing[i], 2) , new_salary_list[i])