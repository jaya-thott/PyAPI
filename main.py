#!/usr/bin/python3

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import json

app = FastAPI()


class Student (BaseModel):
	id: Optional[int]=None
	name:str
	age:int
	location:str

with open('students.json','r') as file:
	students= json.load(file)['students']
	#print(students)

@app.get('/student/{s_id}',status_code=200)
def get_student(s_id:int):
	student=[s for s in students if s['id']==s_id]
	return student[0] if len(student) > 0 else {}



