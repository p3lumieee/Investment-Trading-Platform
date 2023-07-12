from tkinter import *

root = Tk()
root.title("Cyber Crypto")
root.geometry("1000x600+180+40")
root.iconbitmap("myicon.ico")
root.resizable(False, False)
# root.config(bg="#405334")
id_txt = "UsenamePass"

# copyright bar
copyright_bar = Label(root, text=" ©Copyright Cyber Father Group, 2023", bd=1, relief=SUNKEN, anchor=E)
copyright_bar.place(x=793, y=580)


#                   FUNCTIONS
def clear(page):
    slaves = page.place_slaves()
    for x in slaves:
        x.destroy()


def investnow():
    clear(welcome_win_frame)
    i = 1   # loop variable

    #   Inner Frame
    investnow_frame = Frame(root, width=1000, height=600)
    investnow_frame.grid(row=0, column=1)

    #   Investment List
    crypto = ["Bitcoin(BTC)", "Ethereum(ETH)", "Dogecoin(DGC)", "Cardano(ADA)",
              "Polkadot(DOT)", "Litecoin(LTC)", "Monero(XMR)", "Shiba Inu(SHIB)"]
    for coin in crypto:
        if i <= 8:
            coin = Label(investnow_frame, text=coin, font=("Arial", 13))
            coin.grid(row=i, column=0)
            i += 1


def port_view():
    clear(welcome_win_frame)
    port_view_frame = Frame(root, width=1000, height=600)
    port_view_frame.grid(row=0, column=1)

    label = Label(port_view_frame, text="Portfolio Viewing page")
    label.pack()


def deposit_withdraw():
    clear(welcome_win_frame)
    deposit_withdraw_frame = Frame(root, width=1000, height=600)
    deposit_withdraw_frame.grid(row=0, column=1)

    label = Label(deposit_withdraw_frame, text="Transaction page")
    label.pack()


def welcome_win():
    invest_now.destroy()
    clear(loginframe)
    # Portfolio Frame
    global welcome_win_frame
    welcome_win_frame = Frame(root, width=1000, height=600)
    welcome_win_frame.grid(row=0, column=1)

    #   CLIENT ID SECTION
    clientid_frame = LabelFrame(welcome_win_frame, padx=5, pady=5)
    clientid_frame.place(x=0, y=0, width=200, height=250)
    ID = Label(clientid_frame, text=f"Your Client ID is: \n{id_txt}", font=("Consolas", 12))
    ID.place(x=8, y=90)

    #   PROFIT / LOSS SECTION
    pr_los_frame = LabelFrame(welcome_win_frame, padx=5, pady=5)
    pr_los_frame.place(x=0, y=300, width=200, height=310)
    profit = Label(pr_los_frame, text=f"Profit:\t£10.23", font=("Consolas", 14))
    profit.place(x=8, y=45)
    loss = Label(pr_los_frame, text=f"Loss:\t£2.18", font=("Consolas", 14))
    loss.place(x=8, y=150)

    ##   USER OPTIONS
    options_frame = LabelFrame(welcome_win_frame, padx=5, pady=5)
    options_frame.place(x=700, y=0, width=310, height=583)
    loss = Label(options_frame, text=f"Make a Trade?", font=("Consolas", 20))
    loss.place(x=40, y=100)

    #   Invest Now
    invest_label = Label(options_frame, text="➤", font=("Arial", 33))
    invest_label.place(x=27, y=205)
    invest = Button(options_frame, text="Invest Now", width=22, height=2, command=investnow)
    invest.place(x=100, y=210)

    #   Portfolio Viewing
    prtfolio_lab = Label(options_frame, text="➤", font=("Arial", 33))
    prtfolio_lab.place(x=27, y=300)
    view = Button(options_frame, text="View Portfolio", width=22, height=2, command=port_view)
    view.place(x=100, y=308)

    #   Deposit/Withdraw
    prtfolio_lab = Label(options_frame, text="➤", font=("Arial", 33))
    prtfolio_lab.place(x=27, y=390)
    view = Button(options_frame, text="Deposit/Withdraw", width=22, height=2, command=deposit_withdraw)
    view.place(x=100, y=396)

    #   Total Investment Value
    TIV = Label(welcome_win_frame, text="Total Investment Value", font=("Arial", 22))
    TIV.place(x=320, y=200)

    value = 500
    amount = Label(welcome_win_frame, text=f"£{value}", font=("Arial", 22))
    amount.place(x=410, y=270)


def sign_in_func():
    global invest_now
    invest_now = Toplevel(master=root)
    invest_now.title("Invest now")
    invest_now.iconbitmap("myicon.ico")
    invest_now.geometry("400x400+480+160")
    invest_now.resizable(False, False)

    invest_msg = Label(invest_now, text="Welcome aboard \nInvest now to proceed", font=("Arial", 18))
    invest_msg.place(x=90, y=20)

    amount_msg = Label(invest_now, text="Enter an amount", font=("Arial", 16))
    amount_msg.place(x=120, y=105)

    amount = Entry(invest_now, width=18, font=("Arial", 15))
    amount.place(x=100, y=155)
    amount.insert(0, "£")

    card = Button(invest_now, text="Card", width=15)
    card.place(x=45, y=210)

    bank = Button(invest_now, text="Bank Transfer", width=15)
    bank.place(x=250, y=210)

    next_page = Button(invest_now, text="Proceed ", width=30, bg="#3EA438", command=welcome_win)
    next_page.place(x=100, y=280)

    client = Label(invest_now, text="Client ID")
    client.place(x=80, y=348)

    client_id = Entry(invest_now, font=("Arial", 13))

    client_id.insert(0, id_txt)
    client_id.config(state=DISABLED)
    client_id.place(x=145, y=349)


# Welcome Message
loginframe = Frame(root, width=1000, height=600)        # Frame
loginframe.grid(row=0, column=1)
wlcm_message = Label(loginframe, text="Welcome to Cyber Crypto Investment Platform", font=("Arial", 20))

# Applying Welcome Message
wlcm_message.place(x=210, y=50)

# CREATING SIGN UP FRAME
frame = LabelFrame(loginframe, padx=5, pady=5)

# Contents
open_acct = Label(frame, text="Open an account", font=("Arial", 15))

Email = Label(frame, text="E-mail")
user_email = Entry(frame, width=35)
user_email.insert(0, "Enter your email address")

Username = Label(frame, text="Username")
user_name = Entry(frame, width=35)
user_name.insert(0, "Enter a username")

Userpass = Label(frame, text="Password")
user_pass = Entry(frame, width=35)
user_pass.insert(0, "Enter a password")

Userpass_confirm = Label(frame, text="Confirm Password")
user_pass_confirm = Entry(frame, width=35)
user_pass_confirm.insert(0, "Confirm your password")

sign_up = Button(frame, text="Sign Up", command=sign_in_func, width=10)  # Sign Up button
sign_in = Label(frame, text="Already have an account? Sign In")  # Sign Up link

# APPLYING FRAME'S WIDGET
# Sign Up Frame
frame.place(x=270, y=120, width=450, height=360)

open_acct.place(x=145, y=20)

Email.place(x=70, y=80)
user_email.place(x=125, y=80)

Username.place(x=50, y=120)
user_name.place(x=125, y=120)

Userpass.place(x=53, y=160)
user_pass.place(x=125, y=160)

Userpass_confirm.place(x=6, y=200)
user_pass_confirm.place(x=125, y=200)

sign_up.place(x=180, y=240)  # Sign Up button
sign_in.place(x=120, y=290)  # Sign In link


#   Mainloop
root.mainloop()
