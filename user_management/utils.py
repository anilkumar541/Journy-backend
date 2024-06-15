from django.core.mail import EmailMessage
import os

class Util:
    @staticmethod
    def send_email(data):
        try:
            email = EmailMessage(
                subject=data.get("subject"),
                body=data.get("body"),
                from_email=os.environ.get("EMAIL_HOST_USER"),
                to=[data.get("to_email")],
            )
            email.content_subtype= "html"
            email.send()
            print("Email sent successfully!")
        except Exception as e:
            print("Error sending email:", str(e))


# **************
# from django.core.mail import send_mail
# from django.shortcuts import render

# def send_email_(data):
#     try:
#         subject= data.get("subject"),
#         message = data.get("body"),
#         email_from = os.environ.get("DEFAULT_FROM_EMAIL"),
#         recipient_list = [data.get("to_email")]
        
#         send_mail(subject, message, email_from, recipient_list, fail_silently=False,)
#     except:
#         print("something went wrong")

#     # return render(request, 'some_template.html')
#     print("something went wrong1")