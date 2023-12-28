

import requests
import datetime

def EmailSender(sender,receips,subject,body,number):
    
    # MailGun Configuration
    with open('.\\Resources\\mailGun.txt','r') as b:
        n = b.readlines()
        data=[]
        for i in n:
            f = i.replace('\n','')   
            data.append(f)
    b.close()
        
    domain_name=data[0]
    api_key=data[1]

    
    def send_simple_message(rec):
        return requests.post(
            f"https://api.mailgun.net/v3/{domain_name}/messages",
            auth=("api",api_key),
            data={"from": sender,
                "to": rec,
                "subject": subject,
                "text": body})
    
    for i in receips:
        response = send_simple_message(i)
        print(response.text)
        timestamp=datetime.datetime.now()
        timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
        if 'Thank you.' in response.text:
            with open('Log.txt','a') as l:
                l.write(f'Success,\n\t Recipient {i} Received the email with number {number}, Time stamp {timestamp}\n')
        else:
            with open('Log.txt','a') as l:
                l.write(f'Failed,\n\t Cant deliver to Recipient {i} Time stamp {timestamp}\n')
    with open('Log.txt','a') as l:
        l.write('\n')
        
    l.close()
        