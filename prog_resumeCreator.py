import json
from fpdf import FPDF

with open('_resume.json') as data_jsonfile:
    raw_details = json.load(data_jsonfile)

#retrieving data
#Pesonal Details
name = raw_details["_name"]
job = raw_details["_job"]
summary = raw_details["_summary"]
sex = raw_details["_sex"]
age = raw_details["_age"]
address = raw_details["_address"]

#Contacts
phone = raw_details["contact_number"]
email = raw_details["email_address"]

#Accounts
network_1 = raw_details["network1"] 
username_1 = raw_details["username1"]
link_1 = raw_details["link1"]
network_2 = raw_details["network2"]
username_2 = raw_details["username2"]
link_2 = raw_details["link2"]

#Education
course = raw_details["school_course"]
university = raw_details["university"]

#Skills
Skill_1 = raw_details["skills"][0]
Skill_2 = raw_details["skills"][1]
Skill_3 = raw_details["skills"][2]
Skill_4 = raw_details["skills"][3]
Skill_5 = raw_details["skills"][4]
Skill_6 = raw_details["skills"][5]
Skill_7 = raw_details["skills"][6]