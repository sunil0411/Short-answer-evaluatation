import Tkinter
import fileinput
import evaluate
import mailmessage

class Counter():
    counter=0
    name=""
short1 = Tkinter.Tk()
short1.title("Short Answer Evaluation")
short1.geometry('{}x{}'.format(1366/4, 768/6))
short1.resizable(width=True,height=True)

def start_session1():
    Counter.name=text1.get("1.0",Tkinter.END)[:-1],qa[key]
    short1.destroy()
l1=Tkinter.Label(short1,text="Enter your gmail-id:",font=("Times New Roman", 12),fg="blue")
text1 = Tkinter.Text(short1,height=1,font=("Times New Roman", 13))
b1 = Tkinter.Button(short1,text="save",command=start_session1)
l1.pack()
text1.pack()
b1.pack()

#name=input("Enter your mail-id to know your final result:")
qa={"C:\Users\sunil\Desktop\Mini Porject\question1.txt":"C:\Users\sunil\Desktop\Mini Porject\m1.txt",
        "C:\Users\sunil\Desktop\Mini Porject\question2.txt":"C:\Users\sunil\Desktop\Mini Porject\m2.txt",
        "C:\Users\sunil\Desktop\Mini Porject\question3.txt":"C:\Users\sunil\Desktop\Mini Porject\m3.txt",
        "C:\Users\sunil\Desktop\Mini Porject\question4.txt":"C:\Users\sunil\Desktop\Mini Porject\m4.txt",
        "C:\Users\sunil\Desktop\Mini Porject\question5.txt":"C:\Users\sunil\Desktop\Mini Porject\m5.txt",
        "C:\Users\sunil\Desktop\Mini Porject\question6.txt":"C:\Users\sunil\Desktop\Mini Porject\m6.txt",
        "C:\Users\sunil\Desktop\Mini Porject\question7.txt":"C:\Users\sunil\Desktop\Mini Porject\m7.txt"}

for key in qa:
    short = Tkinter.Tk()
    short.title("Short Answer Evaluation")
    short.geometry('{}x{}'.format(1366, 768))
    short.resizable(width=True,height=True)
    def start_session():
        f=open(key,'r')
        for line in f.readlines():
            #Text1.config(state="normal")
            Text2.config(state="normal")
            Text1.insert(Tkinter.END,line)
            Text1.config(state="disabled")
        
    def retrieve_input():
        z=[]
        i=[]
        j=0
        Text2.config(state="disabled")
        res=evaluate.result(Text2.get("1.0",Tkinter.END)[:-1],qa[key])
        print res
        var.set(res)
        print type(var)
        Counter.counter=Counter.counter+float(res)
        
    def _quit():
        short.destroy()

    var= Tkinter.StringVar()
    q1=Tkinter.StringVar()
    a1=Tkinter.StringVar()

    Text1 = Tkinter.Text(short,state="normal",height=2,relief="raised",insertbackground="red",exportselection=1,highlightthickness=2,font=("Times New Roman", 15),
                         fg="red",cursor="question_arrow",wrap=Tkinter.WORD)
    B1 = Tkinter.Button(short,text="start",command=start_session)
    B1.pack()

    L1 = Tkinter.Label(short,text="Question:",font=("Garamond", 16),fg="red")
    L1.pack()

    Text1.pack()

    L2 = Tkinter.Label(short,anchor="w",font=("Garamond", 16),fg="blue",text="Answer atmost in 5 sentences:",
                       highlightthickness=2)
    L2.pack()
    Text2 = Tkinter.Text(short,state="disabled",height=6,insertbackground="blue",highlightthickness=2,font=("Cookie", 20),relief="sunken")
    Text2.pack()

    B2 = Tkinter.Button(short,text="submit",command=retrieve_input)
    B2.pack()
    B3 = Tkinter.Button(short,text="next",command=_quit)
    B3.pack()

    L3 = Tkinter.Label(short,font=("Garamond", 16),fg="brown",text="Scoreboard:")
    L3.pack()

    L4 = Tkinter.Message(short,textvariable=var,relief=Tkinter.RAISED)
    L4.pack()



    short.mainloop()
mailmessage.mail_id(Counter.name,Counter.counter/7)
