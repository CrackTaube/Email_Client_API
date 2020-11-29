
""" Imports """

import json                                                    # Importing all the modules required
import sched, time
import email, smtplib, ssl
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects




""" Function """

def btc_price():
    session.headers.update(headers)
    response = session.get(url, params=parameters)              # Getting and loading the Json file from the API Site
    data = json.loads(response.text)                            # opens up the json output, from CoinMarketCap
    data_list = data['data']                                    # I built it trough testing the json out put to get to the I
    data_dict1 = data_list[0]                                   # Date wanted. I found some help on the @1 API-Documentation.
    data_dict2 = data_dict1['quote']    
    euro_dict = data_dict2['EUR']
    btc_price_now.append(euro_dict['price'])                    # Packing all the Data in One List
    btc_price_now.append(euro_dict['percent_change_1h'])
    btc_price_now.append(euro_dict['percent_change_24h'])
    btc_price_now.append(euro_dict['percent_change_7d'])

def convert(list):                                              # converts list into a tuple , built after a exampel on @2
    return tuple(list)                                          # needed for the formatting process

def send_mail(x):
    paragraph = x
    message = MIMEMultipart()                                   # Useing MIME to create a Email-file what the Server can read
    message["From"]= sender_email
    message["To"] = receiver_email
    message["Subject"] = subject   
    message.attach(MIMEText(paragraph, "plain"))                # Add message to the email
    text = message.as_string()                                  # Convert message to string and set to Var. text
    mailserver = smtplib.SMTP("smtp.strato.de",587)             # Selecting the Server and sending the Mail
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.login(sender_email, sender_password)
    mailserver.sendmail(sender_email,receiver_email, str(text))
    mailserver.quit()

def send_mail_news(x):
    btc_price_now = convert(x)                                  # Converting the List to a Tuple for Formating
    paragraph ='''                                      
    Hi Leon,\n
    Its me you little personal assistant.
    There where some movements in the market, here is a little Update.\n
    BTC Price Live : %f in Euro
    BTC Price   1h : %f in P
    BTC Price  24h : %f in P
    BTC Price   7d : %f in P
    '''
    paragraph = paragraph % btc_price_now                       # Formating the Email Text with the Bitcoin Data
    send_mail(paragraph)

def send_mail_drop(x):
    btc_price = x                                  
    paragraph ='''                                      
    Hi Leon,\n
    The BTC Price just dropped.
    Look at the Marked
    BTC Price : %s
    '''
    paragraph = paragraph % btc_price                          
    send_mail(paragraph)

def auto_run(y, z, p, q):                                       # def of the trigger to checkt the btc and send a mail if needed.
    btc_price()                                                 # calls the btc price def
    if ((btc_price_now[1] <= -1) or (btc_price_now[1] >= 1)     # funktion, when should a mail be send? 
    or (btc_price_now[2] <= -3) or (btc_price_now[2] >= 3) 
    or (btc_price_now[0] >= (y + 500)) or (btc_price_now[0] <= 10000)):                        
        send_mail_news(btc_price_now)                                
        print("Mail Send!")                                     
        print(btc_price_now)
    else:                                                       # if, not tell me
        print("No Mail Send!")
    while (btc_price_now[0] <= 9000):                           # sends a reminder if the BTC price is below 9000
        print("Drop Mail send!")
        send_mail_drop(y)
        break
    y, z, p, q = btc_price_now                                  # set variables to the new price
    x = 60 * 30                                                 # lenght of sleep
    btc_price_now.clear()
    s.enter(x, 1, auto_run, (y, z, p, q))                       #lets the program sleep and run again





""" BTC_API_Var """

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {                                                  # Setting the Information needed to make a API request, I got the Data from @1
    'start':'1',
    'limit':'2',
    'convert':'EUR',
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'XXXXXXXXXX_Your_API_Key_XXXXXXXXXXX',
}

session = Session()
btc_price_now = []


""" E_Mail_Var """
sender_email = "testmail@dreampeak.de"                          # Setting the Data for the Email like Sender,  Recipient and Pssw. ect.
sender_password = None
subject = "Goood Day Sir | Its Bubbles your Assistant i got News"
receiver_email = "kroherleon@gmail.com"
f = open("password.txt", "r")                                   # getting the Pssw. from an extra File
sender_password = f.read()





""" Start_Auto_Run """

s = sched.scheduler(time.time, time.sleep)                      # variables to auto run the code with help from @3
s.enter(1 , 1, auto_run, (0, 0, 0, 0))                          # set start variables
s.run()
