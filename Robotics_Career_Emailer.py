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

Hi, I'm Aditya Sen. A grade 12 student in Canada. For our Grade 12 Robotics class, we have an assignment to research potential career paths in Robotics, and interview an industry professional.
The career path a choose to research is Electrical Engineer.
If it is not too much of a hassle, may you, or someone in your company (preferably an electrical engineer or a similar discipline), answer 12 questions for my assignment.
You, or they, may answer the questions to any degree they see fit.

The Questions: 

1. What is your job title? 
2. What are the duties and responsibilities of your job? 
3. How many hours per day or week do you work? Do you work shifts? 
4. Can you tell me about your background and how you got into this field? 
5. 	a) What do you like the most about your work? 
    b) What do you like the least about your work?
6 	a) What education or training is needed for this occupation? 
    b) What training have you completed since starting the job? 
    c) What personal characteristics are required for someone to be successful in this job? 
7. Is there a steady demand for workers in this field? How much job security is there? 
8. What should people do to get started in this career? (i.e. experience, training, education) 
9. How might this job change in the future? 
10. What other jobs could you do with the skills/education you have gained in this field. 
11. How are new employees hired for this position? 
12. What supplementary skills/knowledge, that is not engineering-related, are handy for this job? (e.g interpersonal skills, accounting, knowledge of equity and shares)

Again, feel free answer the questions to however much specificity you deem comfortable. One-sentence answers are fine. 

Thank you so much!
Looking forward to hearing from you!

---
Best Regards,
{NAME}
{EMAIL}
    """)

    #ATTACHING TO EMAIL
    #attach resume & cover letter to email
    #resume
    # with open('AdityaSen_Resume.pdf', 'rb') as content_file:
    #     content = content_file.read()
    #     message.add_attachment(content, maintype='application', subtype='pdf', filename='AdityaSen_Resume.pdf')


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
job_csv = open("")
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