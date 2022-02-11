import json
from fpdf import FPDF

with open('jubilo_resume.json') as data_jsonfile:
    raw_details = json.load(data_jsonfile)

name = raw_details["_name"]
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
year_1 = raw_details["year1"]

skill_1 = raw_details["skills"][0]
skill_2 = raw_details["skills"][1]
skill_3 = raw_details["skills"][2]
skill_4 = raw_details["skills"][3]
skill_5 = raw_details["skills"][4]
skill_6 = raw_details["skills"][5]
skill_7 = raw_details["skills"][6]

ojt = raw_details["ojt"]
company = raw_details["company"]
place = raw_details["place"]
year_2 = raw_details["year2"]

grad = raw_details["_grad"]
summary1 = raw_details["summary_s1"]
summary2 = raw_details["summary_s2"]

#PDF 
#headerandformat
_resume = FPDF('P', 'cm', 'A4')
_resume.add_page()
_resume.set_margins(0,0,0)
_resume.set_font("helvetica", "B", 25)
_resume.set_text_color(0,0,0)
_resume.set_fill_color(102,178,255)
_resume.set_draw_color(0,0,102)
_resume.cell(0,4.5, name, align='C', ln=2, fill=1, border='LTB')
_resume.image('2x2.jpg',0,1,4.5)

_resume.set_fill_color(255,255,255)
_resume.cell(0,0.3, ln=1, fill=1)

#personal info
_resume.set_font("helvetica", "B", 14)
_resume.set_text_color(255,255,255)
_resume.set_fill_color(0,0,102)
_resume.cell(0,0.7, "          Personal Information", align='L', ln=1, fill=1, border='TB')

_resume.set_fill_color(255,255,255)
_resume.cell(0,0.1, ln=1, fill=1)

_resume.set_font("helvetica", "", 11)
_resume.set_text_color(0,0,0)
_resume.set_fill_color(255,255,255)
_resume.set_draw_color(0,0,0)
_resume.cell(0,0.5, "                    Sex: " + sex, align='L', ln=1, fill=1)
_resume.cell(0,0.5, "                    Age: " + age, align='L', ln=1, fill=1)
_resume.cell(0,0.5, "                    Address: " + address, align='L', ln=1, fill=1)

_resume.set_fill_color(255,255,255)
_resume.cell(0,0.2, ln=1, fill=1)

_resume.set_font("helvetica", "B", 14)
_resume.set_text_color(255,255,255)
_resume.set_fill_color(0,0,102)
_resume.cell(0,0.7, "          Contact Information", align='L', ln=1, fill=1, border='TB')

_resume.set_fill_color(255,255,255)
_resume.cell(0,0.1, ln=1, fill=1)

_resume.set_font("helvetica", "", 11)
_resume.set_text_color(0,0,0)
_resume.set_fill_color(255,255,255)
_resume.set_draw_color(0,0,0)
_resume.cell(0,0.5, "                    Contact Number: " + phone, align='L', ln=1, fill=1)
_resume.cell(0,0.5, "                    Email Address: " + email, align='L', ln=1, fill=1)

_resume.set_fill_color(255,255,255)
_resume.cell(0,0.2, ln=1, fill=1)

_resume.set_font("helvetica", "B", 14)
_resume.set_text_color(255,255,255)
_resume.set_fill_color(0,0,102)
_resume.cell(0,0.7, "          Accounts", align='L', ln=1, fill=1, border='TB')

_resume.set_fill_color(255,255,255)
_resume.cell(0,0.1, ln=1, fill=1)

_resume.set_font("helvetica", "", 11)
_resume.set_text_color(0,0,0)
_resume.set_fill_color(255,255,255)
_resume.set_draw_color(0,0,0)
_resume.cell(0,0.5, "                    Network: " + network_1, align='L', ln=1, fill=1)
_resume.cell(0,0.5, "                                   " + username_1, align='L', ln=1, fill=1)
_resume.cell(0,0.5, "                                   " + link_1, align='L', ln=1, fill=1)
_resume.cell(0,0.5, "                    Network: " + network_2, align='L', ln=1, fill=1)
_resume.cell(0,0.5, "                                   " + username_2, align='L', ln=1, fill=1)
_resume.cell(0,0.5, "                                   " + link_2, align='L', ln=1, fill=1)

_resume.set_fill_color(255,255,255)
_resume.cell(0,0.2, ln=1, fill=1)

_resume.set_font("helvetica", "B", 14)
_resume.set_text_color(255,255,255)
_resume.set_fill_color(0,0,102)
_resume.cell(0,0.7, "          Education", align='L', ln=1, fill=1, border='TB')

_resume.set_fill_color(255,255,255)
_resume.cell(0,0.1, ln=1, fill=1)

_resume.set_font("helvetica", "", 11)
_resume.set_text_color(0,0,0)
_resume.set_fill_color(255,255,255)
_resume.set_draw_color(0,0,0)
_resume.cell(0,0.5, "                                   " + course, align='L', ln=1, fill=1)
_resume.cell(0,0.5, "                                   " + university, align='L', ln=1, fill=1)
_resume.cell(0,0.5, "                                   " + year_1, align='L', ln=1, fill=1)

_resume.set_fill_color(255,255,255)
_resume.cell(0,0.2, ln=1, fill=1)

_resume.set_font("helvetica", "B", 14)
_resume.set_text_color(255,255,255)
_resume.set_fill_color(0,0,102)
_resume.cell(0,0.7, "          Skills", align='L', ln=1, fill=1, border='TB')

_resume.set_fill_color(255,255,255)
_resume.cell(0,0.1, ln=1, fill=1)

_resume.set_font("helvetica", "", 11)
_resume.set_text_color(0,0,0)
_resume.set_fill_color(255,255,255)
_resume.set_draw_color(0,0,0)
_resume.cell(0,0.5, "                                   " + skill_1, align='L', ln=1, fill=1)
_resume.cell(0,0.5, "                                   " + skill_2, align='L', ln=1, fill=1)
_resume.cell(0,0.5, "                                   " + skill_3, align='L', ln=1, fill=1)
_resume.cell(0,0.5, "                                   " + skill_4, align='L', ln=1, fill=1)
_resume.cell(0,0.5, "                                   " + skill_5, align='L', ln=1, fill=1)
_resume.cell(0,0.5, "                                   " + skill_6, align='L', ln=1, fill=1)
_resume.cell(0,0.5, "                                   " + skill_7, align='L', ln=1, fill=1)

_resume.set_fill_color(255,255,255)
_resume.cell(0,0.2, ln=1, fill=1)

_resume.set_font("helvetica", "B", 14)
_resume.set_text_color(255,255,255)
_resume.set_fill_color(0,0,102)
_resume.cell(0,0.7, "          Experience", align='L', ln=1, fill=1, border='TB')

_resume.set_fill_color(255,255,255)
_resume.cell(0,0.1, ln=1, fill=1)

_resume.set_font("helvetica", "", 11)
_resume.set_text_color(0,0,0)
_resume.set_fill_color(255,255,255)
_resume.set_draw_color(0,0,0)
_resume.cell(0,0.5, "                    On-the-Job Training: ", align='L', ln=1, fill=1)
_resume.cell(0,0.5, "                                   " + ojt, align='L', ln=1, fill=1)
_resume.cell(0,0.5, "                                   " + company, align='L', ln=1, fill=1)
_resume.cell(0,0.5, "                                   " + place, align='L', ln=1, fill=1)
_resume.cell(0,0.5, "                                   " + year_2, align='L', ln=1, fill=1)

_resume.set_fill_color(255,255,255)
_resume.cell(0,0.2, ln=1, fill=1)

_resume.set_font("helvetica", "B", 14)
_resume.set_text_color(255,255,255)
_resume.set_fill_color(0,0,102)
_resume.cell(0,0.7, "          Summary", align='L', ln=1, fill=1, border='TB')

_resume.set_font("helvetica", "B", 11)
_resume.set_text_color(0,0,0)
_resume.set_fill_color(255,255,255)
_resume.set_draw_color(0,0,0)
_resume.cell(0,1, "                    " + grad, align='L', ln=1, fill=1)

_resume.set_font("helvetica", "", 11)
_resume.set_text_color(0,0,0)
_resume.set_fill_color(255,255,255)
_resume.set_draw_color(0,0,0)
_resume.cell(0,0.5, "                                " + summary1, align='L', ln=1, fill=1)
_resume.cell(0,0.5, "                    " + summary2, align='L', ln=1, fill=1)

#output
_resume.output("JUBILO_DENISEIRA.pdf")