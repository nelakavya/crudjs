from tkinter import *
#from PIL import Image, ImageTk
from plyer import notification
from tkinter import messagebox
from PIL import Image, ImageTk
import time
import os
from threading import Thread
class Obj:
    def __init__(self):
        self.result=True
def Task():
    # get details
    def get_details():
      get_title = title.get()
      get_msg = msg.get()
      get_time = time1.get()
    # print(get_title,get_msg, tt)
     
      if get_title == "" or get_msg == "" or get_time == "":
        messagebox.showerror("Alert", "All fields are required!")
      else:
          
          obj=Obj()
          int_time =int(float(get_time))
          min_to_sec = int_time * 60
          messagebox.showinfo("notifier set", "set notification ?")
          t.destroy()
          time.sleep(min_to_sec)
          
          def notify(obj):
              while (obj.result):
                  time.sleep(2)
                  notification.notify(title=get_title,
                                      message=get_msg,
                                      app_name="Notifier",
                                      app_icon="ico.ico",
                                      toast=True,
                                    timeout=10)
             
              
          def stop_notify(obj):
              def done(obj):
                  obj.result=False
                  root1.destroy()
              root1=Tk()
              root1_label = Label(root1, text="Do you want to stop the notifications",font=("poppins", 10))
              root1_label.place(x=12, y=70)
              button = Button(root1, text="yes", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20,
                              relief="raised",
                              command=lambda:done(obj))
              button.place(x=20,y=20)
          thread = Thread(target =notify, args = (obj, ))
          
          thread.start()
          stop_notify(obj)
          
              
             
    t = Tk()
    t.title('TASK NOTIFICATION')
    t.geometry("900x300")
    img = Image.open("notify-label.png")
    tkimage = ImageTk.PhotoImage(img)
   # img_label =Label(t, image=tkimage).grid()


    t_label = Label(t, text="Title to Notify",font=("poppins", 10))
    t_label.place(x=12, y=70)


    title = Entry(t, width="25",font=("poppins", 13))
    title.place(x=123, y=70)


    m_label = Label(t, text="Display Message", font=("poppins", 10))
    m_label.place(x=12, y=120)


    msg = Entry(t, width="40", font=("poppins", 13))
    msg.place(x=123,height=30, y=120)


    time_label = Label(t, text="Set Time", font=("poppins", 10))
    time_label.place(x=12, y=175)


    time1 = Entry(t, width="5", font=("poppins", 13))
    time1.place(x=123, y=175)


    time_min_label = Label(t, text="min", font=("poppins", 10))
    time_min_label.place(x=175, y=180)


    but = Button(t, text="SET NOTIFICATION", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20,relief="raised",command=get_details)
    but.place(x=170, y=230)

    t.resizable(0,0)
    t.mainloop()
def Event():
    os.system("taskschd")

    
root=Tk()
root.title('Remainder App')
root.geometry("700x300")
#img = Image.open("notify-label.png")
#tkimage = ImageTk.PhotoImage(img)
lab=Label(root, text="REMAINDER APP", font=("poppins", 50))
lab.place(x=12, y=12)
button = Button(root, text="TASK", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20,
             relief="raised",
             command=Task)
button1 = Button(root, text="EVENT", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20,
             relief="raised",
             command=Event)
button.place(x=200,y=230)
button1.place(x=200,y=130)
root.mainloop()

