import win32com.client as win32

# Create Outlook application object
outlook = win32.Dispatch('Outlook.Application')

# Create a new mail item
mail = outlook.CreateItem(0)  # 0 represents olMailItem, indicating a new email

# Set email properties
mail.Subject = 'Your subject'
mail.Body = 'Your email body'
mail.To = 'recipient@example.com'
mail.CC = 'cc@example.com'

# Send the email
mail.Save()

mail.Send()
