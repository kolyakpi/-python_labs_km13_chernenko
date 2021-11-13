def salary():
    salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]
    indexing_list = list(map(lambda i: round(i*30/100, 2), salary_list))
    new_salary = list(map(lambda x, y: round(x + y, 2), salary_list, indexing_list))
 
    print("Salary table: ")
    for i in range(len(salary_list)): print(str(salary_list[i]) + " " + str(new_salary[i]) + " " + str(indexing_list[i]))
salary()



































