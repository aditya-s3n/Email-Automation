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
    subject = f"Experienced, Inexpensive, and Looking: Part-Time Job {subject_name}"
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

I hope you are doing well.

Hi, I'm Aditya Sen. A passionate developer looking for a challenge, in grade 12.
Looking through top tech startups in Toronto, {subject_name} caught my eye. 

I'm currently looking for a part-time development job opportunity, and {subject_name} one of the companies that I believe can satisfy my goal.

I understand that companies are always on the lookout for talent. 
I understand that most startups are in a fast-paced pressured environment. 
I understand that startups are also bootstrapped for funds.

Unfortunately, since I am in Grade 12, I do have time constraints due to my school hours. 
But with that if you are looking for cost-effective labour, and a determined worker. I'm looking for a company to challenge me, and to learn from. Learning about the tech industry and startup/company culture.

If my resume, Github, experience, or projects don't prove to you that I have the necessary skills. Feel free to send me an assignment, or test on your tech stack. Or to set up an interview. I would be happy to satisfy your needs.

LinkedIN: https://www.linkedin.com/in/aditya-s3n/
Github: https://github.com/aditya-s3n
Personal Blog Website: https://sol-thoughts.web.app

I'm looking forward to hearing from you!

---
Best Regards,
{NAME}
{EMAIL}

Sent through personal python email script: https://github.com/aditya-s3n/Email-Automation
    """)

    #ATTACHING TO EMAIL
    #attach resume & cover letter to email
    #resume
    with open('AdityaSen_Resume.pdf', 'rb') as content_file:
        content = content_file.read()
        message.add_attachment(content, maintype='application', subtype='pdf', filename='AdityaSen_Resume.pdf')


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
job_csv = open("Email_List.csv")
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
    #print(email);
    print(f'{email[0]:<40}: {email[1]:>30}')