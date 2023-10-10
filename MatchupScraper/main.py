from matchupScraper import *
from datetime import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib

def main():
    #Creates log file to store the stack trace and errors
    curr_path = os.path.dirname(__file__)
    log_path = curr_path + '\Logs\load_' + str(date.today()) +'.txt'
    log_file = open(log_path, 'w')

    #Starts the program
    print('Starting matchup scraper...')
    log_file.write('Starting matchup scraper...\n')
    ret = matchupScraper(log_file)
    if (ret == -1):
        print('Process completed with errors.')
        log_file.write('Process completed with errors.\n')
    else:
        print('Process completed successfully!')
        log_file.write('Process completed successfully!\n')
    log_file.close()
    
    #Instanciate the email credentials for sftp connection
    curr_dir = os.path.dirname(__file__)
    path = os.path.join(curr_dir, 'Env/email.env')
    load_dotenv(path)

    email_sender = os.getenv('email_sender')
    email_password = os.getenv('email_password')
    email_port = os.getenv('email_port')
    email_receiver = os.getenv('email_receiver')

    #Connects to the SFTP server
    server = smtplib.SMTP('smtp.gmail.com', email_port)
    server.starttls()
    server.login(email_sender, email_password)

    #Instanciates the messahe as an object
    msg = MIMEMultipart()
    msg['Subject'] = 'Matchup Scraper Output ' + str(date.today())
    msg['From'] = email_sender
    msg['To'] = email_receiver

    #Reads the log file and attaches to the email
    with open(log_path, 'rb') as file:
        attachment = MIMEText(file.read(), 'plain', 'uft-8')
        attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(log_path))
        msg.attach(attachment)

    #Sends the email
    server.sendmail(email_sender, email_receiver, msg.as_string())

    #Disconnects from the server
    server.quit()
    
    return 0
        
#Main Method
if __name__ == '__main__':
    main()