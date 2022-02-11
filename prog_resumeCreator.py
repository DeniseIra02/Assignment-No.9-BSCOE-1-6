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
_resume.set_font("helvetica", "B", 25)
_resume.set_text_color(0,0,102)
_resume.set_fill_color(255,255,153)
_resume.set_draw_color(0,0,102)
_resume.cell(0,4.5, name, align='C', ln=2, fill=1, border='LTB')
_resume.image('2x2.jpg',0,1,4.5)

_resume.set_fill_color(255,255,255)
_resume.cell(0,0.3, ln=1, fill=1)

#personal info
_resume.set_font("helvetica", "B", 14)
_resume.set_text_color(255,255,255)
_resume.set_fill_color(0,0,102)
_resume.cell(0,0.5, "          Personal Information", align='L', ln=1, fill=1, border='TB')

_resume.set_font("helvetica", "", 11)
_resume.set_text_color(0,0,0)
_resume.set_fill_color(255,255,255)
_resume.set_draw_color(0,0,0)
_resume.cell(0,0.7, "                    Sex: " + sex, align='L', ln=1, fill=1)
_resume.cell(0,0.7, "                    Age: " + age, align='L', ln=1, fill=1)
_resume.cell(0,0.7, "                    Address: " + address, align='L', ln=1, fill=1)




#output
_resume.output("JUBILO_DENISEIRA.pdf")