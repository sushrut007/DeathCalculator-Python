import random
import tkinter as tk
from datetime import datetime

def calculate_age(date_of_birth):
    current_date = datetime.now()
    birth_date = datetime.strptime(date_of_birth, "%d-%m-%Y")
    age = current_date.year - birth_date.year

    # Check if the current month and day are earlier than the birth month and day
    if current_date.month < birth_date.month or (current_date.month == birth_date.month and current_date.day < birth_date.day):
        age -= 1

    # Calculate the number of full years, months, and days
    years = age
    months = current_date.month - birth_date.month
    days = current_date.day - birth_date.day

    # Adjust the months and days if they are negative
    if months < 0:
        years -= 1
        months += 12
    if days < 0:
        months -= 1
        days += 30  # Assuming 30 days in a month

    return years+1, months, days

def calculate_death_time():
    birth_date = entry_dob.get()
    sex = var_sex.get()
    smoke = var_smoke.get()
    smoke_packs = var_smoke_packs.get()
    smoke_years = var_smoke_years.get()
    bmi = entry_bmi.get()
    outlook = var_outlook.get()
    alcohol = var_alcohol.get()
    death_age=0
    years, months, days = calculate_age(birth_date)
    output = "You are {} years, {} months, and {} days old.".format(years, months, days)
    # Calculate the death time based on the input values
    #sex if-else
    if sex == "Male":
        death_age = 65.8
    else:
        death_age = 68.9
    #smoke if-else    
    if smoke :
        if smoke_packs == "0" :
            smoke_packs=1
        if smoke_packs=="5+":
            smoke_packs = random.randrange(5,8)
        else:
            smoke_packs= int(smoke_packs)
    #smoke years if-else
    if smoke_years == "20+":
        yrs = random.randrange(20,26)
    else: 
        for i in range(0,len(smoke_years)):
            if smoke_years[i] == "-":
                two=int(smoke_years[i+1:])
                one=int(smoke_years[:i])
        yrs= random.randrange(one,two+1)
        if yrs==0:
            yrs=1
    death_age -= (int(smoke_packs) *  0.000822 * 365 * yrs)
    #BMI if-else
    if bmi=="<19":
        death_age-=random.randrange(1,4)
    elif bmi =="19-25":
        death_age+=random.randrange(0,3)
    elif bmi== "26-30":
        death_age-=random.randrange(3,6)
    elif bmi== "30+":
        death_age-=random.randrange(5,7)
    
    #Outlook if-else
    if outlook== "Optimistic":
        death_age+=random.randrange(1,3)
    elif outlook== "Neutral":
        pass
    elif outlook== "Suicidal":
        death_age-=random.randrange(1,5)
    
    #Alcohol if-else
    if alcohol == "Never":
        death_age+=random.randrange(0,3)
        if random.randrange(0,2):
            death_age+=0.5
    elif alcohol == "Once in month":
        death_age-=random.randrange(2,5)
    elif alcohol == "2-4 times a month":
        death_age-=random.randrange(4,6)
    elif alcohol ==  "2 times a week":
        death_age-=random.randrange(5,8)
    elif alcohol == "Daily":
        death_age-=random.randrange(8,11)
    if years > death_age:
        death_age+=(years-(round(death_age)))+random.randrange(1,3)
    #result_label.configure(text="Your predicted death time is: {}".format(death_date.strftime("%d-%m-%Y")))
    output1 = "You will live for another {} years, {} months, and {} days & You will Die at age of {} 💀".format((round(death_age)-years),random.randrange(1,12), random.randrange(1,30),round(death_age))
    Current_label.config(text=output)
    result_label.config(text=output1)

def validate_inputs():
    if entry_dob.get() and var_sex.get() and (not var_smoke.get() or (var_smoke.get() and var_smoke_packs.get() and var_smoke_years.get())) and entry_bmi.get() and var_outlook.get() and var_alcohol.get():
        calculate_button.config(state="normal")
    else:
        calculate_button.config(state="disabled")
def BMI_Cal():
    h=height_var.get()/100
    w=weight_var.get()
    BMI=0
    if h or w:
        BMI=w/(h**2)
        out="BMI value : {:.1f}".format(BMI)
        BMI_label = tk.Label(window,
                    text=out,fg="#00FF00",background="black",font=("Ink Free",10,"bold")).place(x=H*9,y=V*12)

window = tk.Tk()
H=50;V=35 #for horizontal and vertical spacing
window.title("Death Time Calculator")
window.config(background="black")
window.geometry("650x670+400+20")
window.resizable(False,False)

tital_label = tk.Label(window,
                        text="Death Time Calculator 💀",fg="#00FF00",background="black",font=("Ink Free",24,"bold"))
tital_label.place(x=H*3,y=V*0)

label_dob = tk.Label(window,
                     text="Date of Birth (dd-mm-yyyy):",fg="#00FF00",background="black",font=("Ink Free",12,"bold"))
label_dob.place(x=H*2,y=V*2)
entry_dob = tk.Entry(window,fg="#00FF00",background="black",font=("Ink Free",12,"bold"),insertbackground="#00FF00")
entry_dob.place(x=H*7,y=V*2)
entry_dob.bind("<KeyRelease>",
               lambda event: validate_inputs())

label_sex = tk.Label(window, text="Sex:",fg="#00FF00",background="black",font=("Ink Free",12,"bold"))
label_sex.place(x=H*2,y=V*3)
var_sex = tk.StringVar()
var_sex.set("Male")
radio_button_male = tk.Radiobutton(window, 
                                   text="Male", 
                                   variable=var_sex,
                                   value="Male",
                                   command=lambda: validate_inputs(),fg="#00FF00",background="black",font=("Ink Free",12,"bold"),
                                   activeforeground="#00FF00",activebackground="black")
radio_button_male.place(x=H*3,y=V*3)
radio_button_female = tk.Radiobutton(window, text="Female",
                                     variable=var_sex, value="Female",
                                     command=lambda: validate_inputs(),
                                     fg="#00FF00",background="black",font=("Ink Free",12,"bold"),
                                     activeforeground="#00FF00",activebackground="black")
radio_button_female.place(x=H*5,y=V*3)

label_smoke = tk.Label(window, 
                       text="Do you smoke?",fg="#00FF00",background="black",font=("Ink Free",12,"bold"))
label_smoke.place(x=H*2,y=V*4)
var_smoke = tk.BooleanVar()
check_button_smoke = tk.Checkbutton(window,
                                    text="Yes", 
                                    variable=var_smoke,
                                    command=lambda: toggle_smoke_inputs(),fg="#00FF00",background="black",font=("Ink Free",12,"bold"),
                                    activeforeground="#00FF00",activebackground="black")
check_button_smoke.place(x=H*5,y=V*4)

label_smoke_packs = tk.Label(window, 
                             text="How Many Packs Per Day?",fg="#00FF00",background="black",font=("Ink Free",12,"bold"))
label_smoke_packs.place(x=H*2,y=V*5)
var_smoke_packs = tk.StringVar()
drop_down_smoke_packs = tk.OptionMenu(window, 
                                      var_smoke_packs, 
                                      "0", "1", "2", "3", "4", "5+")
var_smoke_packs.set("0")
drop_down_smoke_packs.place(x=H*4,y=V*6)
drop_down_smoke_packs.config(state="disabled",fg="#00FF00",background="black",font=("Ink Free",9,"bold"),activeforeground="#00FF00",activebackground="black")

label_smoke_years = tk.Label(window, 
                             text="For How Many Years? (Approx)",fg="#00FF00",background="black",font=("Ink Free",12,"bold"))
label_smoke_years.place(x=H*2,y=V*7)
var_smoke_years = tk.StringVar()
drop_down_smoke_years = tk.OptionMenu(window, 
                                      var_smoke_years, 
                                      "0-5", "6-10", "11-15", "16-20", "20+")
var_smoke_years.set("0-5")
drop_down_smoke_years.place(x=H*4,y=V*8)
drop_down_smoke_years.config(state="disabled",fg="#00FF00",background="black",font=("Ink Free",9,"bold"),activeforeground="#00FF00",activebackground="black")

Bmical = tk.Label(window,text="BMI Calculator",fg="#00FF00",background="black",font=("Ink Free",10,"bold")).place(x=H*9,y=V*8)
label_height=tk.Label(window,text="Height(cm):",fg="#00FF00",background="black",font=("Ink Free",10,"bold")).place(x=H*9,y=V*9)
height_var=tk.IntVar()
height=tk.Entry(window,fg="#00FF00",textvariable=height_var,background="black",width=7,insertbackground="#00FF00",font=("Ink Free",10,"bold")).place(x=H*10.6,y=V*9)
label_weight=tk.Label(window,text="Weight(kg):",fg="#00FF00",background="black",font=("Ink Free",10,"bold")).place(x=H*9,y=V*10)
weight_var=tk.IntVar()
weight=tk.Entry(window,fg="#00FF00",textvariable=weight_var,background="black",width=7,insertbackground="#00FF00",font=("Ink Free",10,"bold")).place(x=H*10.6,y=V*10)

cal_button = tk.Button(window,text="Calculate",command=BMI_Cal,
                             fg="#00FF00",background="black",font=("Ink Free",10,"bold"),state="active",
                             activeforeground="#00FF00",activebackground="black").place(x=H*9,y=V*11)


label_bmi = tk.Label(window, 
                     text="BMI value:",fg="#00FF00",background="black",font=("Ink Free",12,"bold"))
label_bmi.place(x=H*2,y=V*9)
entry_bmi = tk.StringVar()
drop_down_entry_bmi = tk.OptionMenu(window, 
                        entry_bmi, 
                        "<19", "19-25", "26-30", "30+")
drop_down_entry_bmi.config(fg="#00FF00",background="black",font=("Ink Free",9,"bold"),activeforeground="#00FF00",activebackground="black")
entry_bmi.set("<19")
drop_down_entry_bmi.place(x=H*3,y=V*10)



label_outlook = tk.Label(window,
                         text="Outlook:",fg="#00FF00",background="black",font=("Ink Free",12,"bold"))
label_outlook.place(x=H*2,y=V*11)
var_outlook = tk.StringVar()
drop_down_outlook = tk.OptionMenu(window,
                                  var_outlook, 
                                  "Optimistic", "Neutral", "Suicidal")
var_outlook.set("Optimistic")
drop_down_outlook.config(fg="#00FF00",background="black",font=("Ink Free",9,"bold"),activeforeground="#00FF00",activebackground="black")
drop_down_outlook.place(x=H*3,y=V*12)


label_alcohol = tk.Label(window, text="Alcohol consumption:",fg="#00FF00",background="black",font=("Ink Free",12,"bold"))
label_alcohol.place(x=H*2,y=V*13)
var_alcohol = tk.StringVar()
drop_down_alcohol = tk.OptionMenu(window,
                                  var_alcohol,
                                  "Never", "Once in month", "2-4 times a month", "2 times a week", "Daily")
var_alcohol.set("Never")
drop_down_alcohol.config(fg="#00FF00",background="black",font=("Ink Free",9,"bold"),activeforeground="#00FF00",activebackground="black")
drop_down_alcohol.place(x=H*4,y=V*14)

calculate_button = tk.Button(window,
                             text="Calculate",
                             command=calculate_death_time,
                             state="disabled",fg="#00FF00",background="black",font=("Ink Free",12,"bold"),
                             activeforeground="#00FF00",activebackground="black")
calculate_button.place(x=H*6,y=V*16)

Current_label = tk.Label(window,
                        text="",fg="#00FF00",background="black",font=("Ink Free",12,"bold"))
Current_label.place(x=H*2,y=V*17)

result_label = tk.Label(window,
                        text="",fg="#00FF00",background="black",font=("Ink Free",11,"bold"))
result_label.place(x=H*0,y=V*18)



    


def toggle_smoke_inputs():
    if var_smoke.get():
        drop_down_smoke_packs.config(state="normal")
        drop_down_smoke_years.config(state="normal")
    else:
        drop_down_smoke_packs.config(state="disabled")
        drop_down_smoke_years.config(state="disabled")

    validate_inputs()

window.mainloop()
