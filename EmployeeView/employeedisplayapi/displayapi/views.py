from urllib import response
from django.shortcuts import render
import requests
import pandas as pd
# Create your views here.

def get_employee_relation():
    response_employee=requests.get('http://127.0.0.1:8000/api/employee/').json()
    response_department = requests.get('http://127.0.0.1:8000/api/department/').json()
    big_employee_dict = {'id':[], 'name':[], 'email':[], 'depart':[]}
    big_department_dict = {'id':[], "name":[]}
    for e in response_employee:
        big_employee_dict['id'].append(e.get('id'))
        big_employee_dict['name'].append(e.get('Empname'))
        big_employee_dict['email'].append(e.get('email'))
        big_employee_dict['depart'].append(e.get('depat'))
    for d in response_department:
        big_department_dict['id'].append(d.get('id'))
        big_department_dict['name'].append(d.get('depatName'))
    df_department = pd.DataFrame.from_dict(big_department_dict)
    df_employee = pd.DataFrame.from_dict(big_employee_dict)
    df_merge = pd.merge(right=df_department, left=df_employee, right_on="id", left_on="depart")
    df_merge.drop(columns=['id_x', 'depart', 'id_y'], inplace=True)
    df_merge.rename(columns={'name_x': 'name', 'name_y': 'department'}, inplace=True)
    return df_merge.values.tolist()

def index(request):
    employees = get_employee_relation()
    print(employees)
    return render(request,'index.html',{'employees':employees,})