import smtplib
def mail_id(name,score): 
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("ravikantisunil14@gmail.com", "8985422340")
    message = "This is the a message regarding your score in the SHORT ANSWER EVALUATION program created by Group N-1 of CSE-D 3rd year of GRIET.\nYou have secured "+str(score)+" marks out of 5.\nThank you!All the best!!"
    s.sendmail("ravikantisunil14@gmail.com", name, message)
    s.quit()
#mail_id("chinnabathinikarunakar1729@gmail.com",3)
