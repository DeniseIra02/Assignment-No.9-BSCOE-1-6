import json
from fpdf import FPDF

with open('jubilo_resume.json') as data_jsonfile:
    raw_details = json.load(data_jsonfile)

name = raw_details["_name"]
job = raw_details["_job"]
summary = raw_details["_summary"]
sex = raw_details["_sex"]
age = raw_details["_age"]
address = raw_details["_address"]

phone = raw_details["contact_number"]
email = raw_details["email_address"]

network_1 = raw_details["network1"] 
username_1 = raw_details["username1"]
link_1 = raw_details["link1"]
network_2 = raw_details["network2"]
username_2 = raw_details["username2"]
link_2 = raw_details["link2"]

course = raw_details["study_course"]
university = raw_details["university"]

skill_1 = raw_details["skills"][0]
skill_2 = raw_details["skills"][1]
skill_3 = raw_details["skills"][2]
skill_4 = raw_details["skills"][3]
skill_5 = raw_details["skills"][4]
skill_6 = raw_details["skills"][5]
skill_7 = raw_details["skills"][6]

#PDF 
#header
_resume = FPDF('P', 'cm', 'Letter')
_resume.add_page()
_resume.set_margins(0,0,0)
_resume.set_font("helvetica", "B", 22)
_resume.set_text_color(0,0,0)
_resume.set_fill_color(137,148,153)
_resume.cell(19.7,4.5, name , align="C", ln=1, fill=1, border=1)
_resume.image('2x2.jpg',16,1.3,4)

#output
_resume.output("JUBILO_DENISEIRA.pdf")