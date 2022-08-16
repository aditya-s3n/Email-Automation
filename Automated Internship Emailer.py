import smtplib
import csv
from dotenv import load_dotenv
import os

from email.message import EmailMessage


#initialize .env file
load_dotenv()
#get email and password from .env file
NAME = "Aditya Sen"
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


#send email function (takes care of everything to send)
#can change content of cover letter and email body + subject
def send_email_companies(subject_email_address, subject_name) -> None:
    #change subject each specific company TODO Change subject name
    subject = f"Summer Internship - {subject_name}"
    #INFO OF EMAIL
    #set where credentials of email, TO, FROM, SUBJECT
    message = EmailMessage()
    message["From"] = NAME
    message["To"] = subject_email_address
    message["Subject"] = subject

    #BODY OF EMAIL
    #change content to specificy each company
    #Add email formatting and content
    message.set_content(
    f"""\
Hello {subject_name},

I'm Aditya, a Grade 11 student in GTA Toronto. 

For the summer I am looking for a tech internship. As I was searching through the internet for tech companies around Canada, {subject_name} caught my eye.

I was wondering if I am able to apply for an internship to your company as a developer. I've attached my resume to this email if you want to look into that. 

I also have a personal blog website, that I made with the MERN tech stack, if you want to learn more about me :)
I'm always looking for opportunities to learn more about this industry, be it web-development or any other.

LinkedIN: https://www.linkedin.com/in/aditya-s3n/
Github: https://github.com/aditya-s3n
Personal Blog Website: https://sol-thoughts.web.app

I'm looking forward to hearing from you!
---
{NAME}
{EMAIL}
    """)

    #ATTACHING TO EMAIL
    #attach resume & cover letter to email
    #resume
    with open('AdityaSen_Resume.pdf', 'rb') as content_file:
        content = content_file.read()
        message.add_attachment(content, maintype='application', subtype='pdf', filename='Aditya Sen Resume - High School.pdf')


    #send the email
    message = message.as_string()
    # Logs in and sends mail
    #NOTE after with statement STMP quits automatically 
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls() #starts TLS (security)

        server.login(EMAIL, PASSWORD) #login to my google gmail
        server.sendmail(EMAIL, subject_email_address, message) #send the message

    return "Successful"


#array to check if all emails when through
email_check = []
#get company name and emails
#iterate through all the rows in the csv file
job_csv = open("Round 3 - Sheet1.csv")
job_csv.readline()
job_csv = csv.reader(job_csv)
#change company email to each specfic company
for data in job_csv:
    subject_name_global = data[0] #company name

    if data[3] != '': #company email
        company_email = data[3]
        # company_email = "1senadi@hdsb.ca"

        #send email & check if it went successfully through
        temp_list = []
        temp_list.append(subject_name_global)
        temp_list.append(send_email_companies(company_email, subject_name_global))
    else:
        #no email address to send to - Unsuccessful
        temp_list = []
        temp_list.append(subject_name_global)
        temp_list.append("Unsuccessful")

    

    email_check.append(temp_list)


#prints out how many emails were successfully sent
for email in email_check:
    print(f'{email[0]:<40}: {email[1]:>30}')