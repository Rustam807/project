import pandas as pd
import numpy as np

#1 — You can use any type of data

#2
month_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
months = pd.Series(month_num, index = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
print(months)
#2

#3
stud_Dictionary = {"MatMIE": 35, "MatDAIS": 36, "COMIE": 37, "COMEC": 38}
students = pd.Series(stud_Dictionary)
print(students)
#3

#4
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

exam_results = pd.DataFrame(exam_data, index = labels)
print(exam_results)
#4

#5
exam_results_1 = exam_results[exam_results["attempts"] > 2]
print(exam_results_1)