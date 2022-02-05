from O365 import Account, MSOffice365Protocol
import datetime as dt

        credentials = ('xxxxxxxxxxxxxxxxxxxx', 'xxxxxxxxxxxxxxxxxxxxxxxx')
        account = Account(credentials, auth_flow_type='credentials', tenant_id='xxxxxxxxxxxxxxxxxxxxxxxxxxx') #Authentication check
        if account.authenticate():
                print('Mailbox Authenticated!')
                mailbox = account.mailbox(resource='mymail@xyz.com')
                test_mailbox = mailbox.get_folder(folder_name="Inbox")
                query = test_mailbox.new_query().on_attribute('isRead').equals(False)  # get unread messages
                #for message in test_mailbox.get_messages(): #Looping through all  messages
                for message in test_mailbox.get_messages(query=query, limit=50): #Looping through messages limit to read last 50
                        mail_time = message.received
                        mail_ID = message.internet_message_id
                        mail_sender = message.sender
                        mail_cc = message.cc
                        mail_subject = message.subject
                        mail_content = message.get_body_text()
                        message.mark_as_read()
                        if 'Shivam Malhotra' in mail_subject:
                                print(str(mail_subject))
                                message.mark_as_read()


#You need to make sure you have Mail.Read permissions.
#Reference links: 
#https://docs.microsoft.com/en-us/graph/auth-register-app-v2
#https://pypi.org/project/O365/
