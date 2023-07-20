import time
from tkinter import *
# from PIL import ImageTk, Image
from time import ctime
import pickle
from client_class import Send
from pickler import ShoppingSystem
from tkinter import messagebox
import threading

root = Tk()
root.title("Cyber Crypto")
root.geometry("1000x600+180+40")
root.iconbitmap("myicon.ico")
root.resizable(False, False)
# root.config(bg="#405334")
# id_txt = "UsernamePass"

# copyright bar
copyright_bar = Label(root, text=" ©Copyright Cyber Father Group, 2023", bd=1, relief=SUNKEN, anchor=E)
copyright_bar.place(x=793, y=580)


#                   FUNCTIONS
def clear(page):
    slaves = page.place_slaves()
    for x in slaves:
        x.destroy()


def sign_in_funct_thread():
    thread = threading.Thread(target=sign_in_func())
    thread.start()


def welcome_win_thread():
    thread = threading.Thread(target=welcome_win())
    thread.start()


def communicate(message, switch):
    HOST = 'localhost'
    PORT = 5005
    BUFSIZE = 1024

    if switch == 0:
        means = Send(HOST, PORT, BUFSIZE)
        means.send(message, 0)
    else:
        means = Send(HOST, PORT, BUFSIZE)
        message1 = means.send(message, 1)
        return message1

#   Coin Images
#     btc = PhotoImage(Image.open("bitcoin.jpg"), )
#     # btc_lbl = Label(investnow_frame, image=btc)
#     # btc_lbl.place(x=100, y=700)


def investnow():
    clear(welcome_win_frame)

    #   Frame
    investnow_frame = Frame(root, width=1000, height=600)
    investnow_frame.grid(row=0, column=1)

    image = Frame(investnow_frame, width=1000, height=200, bg="black")
    image.place(x=0, y=0)
    # btc = PhotoImage(file="backgroundimage.png")
    # btc_label = Label(investnow_frame, image=btc)
    # btc_label.place(x=0, y=0)

    t_head = LabelFrame(investnow_frame, height=30)
    t_head.place(x=0, y=200, width=1001)

    name = Label(t_head, text="Name", font=("Arial", 12))
    name.place(x=50, y=0)

    price = Label(t_head, text="Price", font=("Arial", 12))
    price.place(x=325, y=0)

    chart = Label(t_head, text="Chart", font=("Arial", 12))
    chart.place(x=590, y=0)

    buy = Label(t_head, text="Buy", font=("Arial", 12))
    buy.place(x=840, y=0)

    sell = Label(t_head, text="Sell", font=("Arial", 12))
    sell.place(x=940, y=0)

    def buy(buy_cmd):
        def confirm_n_pay_btn(win, amount, value):
            clear(win)
            crypto_name = Label(win, text=f"Cryptocurrency: {buy_cmd}", font=("Arial", 16))
            crypto_name.pack()
            date = Label(win, text=f"Date: {ctime()}", font=("Arial", 16))
            date.pack()
            option = Label(win, text=f"Buy or Sell: Buy", font=("Arial", 16))
            option.pack()
            quantity = Label(win, text=f"Amount: {amount}", font=("Arial", 16))
            quantity.pack()
            cost = Label(win, text=f"Value: {value} pounds", font=("Arial", 16))
            cost.pack()

        def inner_buy(win, amount):
            amount = amount.get()
            user_input = int(amount)
            value = user_input * 100
            clear(win)
            message = Label(win, text=f"You are about to buy {user_input} {buy_cmd}\n worth {value} pounds.\n "
                                  f"Do you want to proceed with the order?", font=("Arial", 16))
            message.place(x=10, y=40)

            cancel = Button(win, text="Cancel")
            cancel.place(x=260, y=200, width=120)
            edit = Button(win, text="Edit")
            edit.place(x=40, y=200, width=120)
            confirm_n_pay = Button(win, text="Confirm and Pay",
                                   command=lambda: confirm_n_pay_btn(win, amount, value))
            confirm_n_pay.place(x=110, y=320, width=150)

        def buy_command():
            new = Toplevel(master=investnow_frame)
            new.title("Purchase Crypto")
            new.iconbitmap("myicon.ico")
            new.geometry("400x400+480+160")
            new.resizable(False, False)

            mesg = Label(new, text=f"Purchase {buy_cmd}?", font=("Arial", 22))
            mesg.place(x=100, y=20)

            option = StringVar()
            option.set("Choose an Option")
            drop = OptionMenu(new, option, "By quantity", "By amount")
            drop.place(x=100, y=110, width=200)

            entry = Entry(new, width=35)
            entry.place(x=95, y=180)
            # entry.insert(0, buy_cmd + "\t\t")

            proceed_buy = Button(new, text="BUY", font=("Arial", 15), bg="#3EA438",
                                  command=lambda: inner_buy(new, entry))
            proceed_buy.place(x=120, y=310, width=150)

        return buy_command

    def sell(sell_cmd):
        def confirm_n_pay_btn(win, amount, value):
            clear(win)
            crypto_name = Label(win, text=f"Cryptocurrency: {sell_cmd}", font=("Arial", 16))
            crypto_name.pack()
            date = Label(win, text=f"Date: {ctime()}", font=("Arial", 16))
            date.pack()
            option = Label(win, text=f"Buy or Sell: Buy", font=("Arial", 16))
            option.pack()
            quantity = Label(win, text=f"Amount: {amount}", font=("Arial", 16))
            quantity.pack()
            cost = Label(win, text=f"Value: {value} pounds", font=("Arial", 16))
            cost.pack()

        def inner_sell(win, amount):
            amount = amount.get()
            user_input = int(amount)
            value = user_input * 100
            clear(win)
            message = Label(win, text=f"You are about to sell {user_input} "
                                      f"{sell_cmd}\n worth {value} pounds.\n "
                                      f"Do you want to proceed with the order?",
                                      font=("Arial", 16))
            message.place(x=10, y=40)

            cancel = Button(win, text="Cancel")
            cancel.place(x=260, y=200, width=120)
            edit = Button(win, text="Edit")
            edit.place(x=40, y=200, width=120)
            confirm_n_pay = Button(win, text="Confirm and Pay",
                                   command=lambda: confirm_n_pay_btn(win, amount, value))
            confirm_n_pay.place(x=110, y=320, width=150)

        def sell_command():
            new = Toplevel(master=investnow_frame)
            new.title("Purchase Crypto")
            new.iconbitmap("myicon.ico")
            new.geometry("400x400+480+160")
            new.resizable(False, False)

            mesg = Label(new, text=f"Sell your {sell_cmd}?", font=("Arial", 22))
            mesg.place(x=100, y=20)

            option = StringVar()
            option.set("Choose an Option")
            drop = OptionMenu(new, option, "By quantity", "By amount")
            drop.place(x=100, y=110, width=200)

            entry = Entry(new, width=35)
            entry.place(x=95, y=180)
            # entry.insert(0, sell_cmd+"\t\t")

            proceed_sell = Button(new, text="SELL",
                                  font=("Arial", 15),
                                  bg="#E01717",
                                  command=lambda: inner_sell(new, entry))
            proceed_sell.place(x=120, y=310, width=150)

        return sell_command

    #   Investment List
    crypto = ["Bitcoin(BTC)", "Ethereum(ETH)", "Dogecoin(DGC)", "Cardano(ADA)",
              "Polkadot(DOT)", "Litecoin(LTC)", "Bitcoin Cash(BCH)", "Solana(SOL)"]
    prices = ["£30,463.91", "£1,884.00", "£0.06472", "£0.2885",
              "£5.18", "£95.63", "£281.40", "£22.24"]
    commands = [("BTC", "BTC"),
                ("ETH", "ETH"),
                ("DGC", "DGC"),
                ("ADA", "ADA"),
                ("DOT", "DOT"),
                ("LTC", "LTC"),
                ("BCH", "BCH"),
                ("SOL", "SOL")]

    i = 240  # loop variable
    j = 240
    k = 240
    control = True
    while control:
        for coin in crypto:
            coin = Label(investnow_frame, text=coin, font=("Arial", 13))
            coin.place(x=30, y=i)
            i += 45

        for price in prices:
            price = Label(investnow_frame, text=price, font=("Arial", 13))
            price.place(x=310, y=j)
            j += 45

        for buy_cmd, sell_cmd in commands:
            buy_btn = Button(investnow_frame, text="Buy", width=8, bg="#3EA438", command=buy(buy_cmd))
            buy_btn.place(x=825, y=k)
            sell_btn = Button(investnow_frame, text="Sell", width=8, bg="#E01717", command=sell(sell_cmd))
            sell_btn.place(x=925, y=k)
            k += 45
        control = False


def port_view():
    clear(welcome_win_frame)
    port_view_frame = Frame(root, width=1000, height=600)
    port_view_frame.grid(row=0, column=1)

    label = Label(port_view_frame, text="Portfolio Viewing page")
    label.pack()


def deposit_withdraw():
    clear(welcome_win_frame)
    deposit_withdraw_frame = Frame(root, width=1000, height=600)
    deposit_withdraw_frame.place(x=300, y=50)

    invest_msg = Label(deposit_withdraw_frame, text="Welcome aboard \nInvest", font=("Arial", 18))
    invest_msg.place(x=90, y=20)

    amount_msg = Label(deposit_withdraw_frame, text="Enter an amount", font=("Arial", 16))
    amount_msg.place(x=120, y=105)

    amount = Entry(deposit_withdraw_frame, width=18, font=("Arial", 15))
    amount.place(x=100, y=155)
    amount.insert(0, "£")

    card = Button(deposit_withdraw_frame, text="Card", width=15)
    card.place(x=45, y=210)

    bank = Button(deposit_withdraw_frame, text="Bank Transfer", width=15)
    bank.place(x=250, y=210)

    next_page = Button(deposit_withdraw_frame, text="Proceed ", width=30, bg="#3EA438", command=welcome_win_thread)
    next_page.place(x=100, y=280)

    client = Label(deposit_withdraw_frame, text="Client ID")
    client.place(x=80, y=348)

    client_id = Entry(deposit_withdraw_frame, font=("Arial", 13))

    # client_id.insert(0, id_txt)
    client_id.config(state=DISABLED)
    client_id.place(x=145, y=349)


def welcome_win():
    action = ShoppingSystem()
    action.add_item("action1")
    action = action.show_basket()
    message = communicate(action, 1)
    id_txt = message
    invest_now.destroy()
    messagebox.showinfo("CLIENTID", f"Your client ID is {id_txt}")
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


def payment(button0, button1, entry):

    button0.config(state=DISABLED, relief=SUNKEN, bg="#35732C")
    button1.config(state=DISABLED)
    page = ShoppingSystem()
    page.add_item("page2")
    page = page.show_basket()
    communicate(page, 0)
    cash = entry.get()
    cash = cash[1:]
    send_payment = ShoppingSystem()
    send_payment.add_item(cash)
    send_payment = send_payment.show_basket()
    communicate(send_payment, 0)


def sign_in_func():
    page = ShoppingSystem()
    page.add_item("page1")
    page = page.show_basket()
    communicate(page, 0)
    details = ShoppingSystem()
    details.add_item(user_email.get())
    details.add_item(user_name.get())
    details.add_item(user_pass.get())
    details = details.show_basket()
    communicate(details, 0)
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

    card = Button(invest_now, text="Card", width=15, command=lambda: payment(card, bank, amount))
    card.place(x=45, y=210)

    bank = Button(invest_now, text="Bank Transfer", width=15, command=lambda: payment(bank, card, amount))
    bank.place(x=250, y=210)

    next_page = Button(invest_now, text="Proceed ", width=30, bg="#3EA438", command=welcome_win_thread)
    next_page.place(x=100, y=280)


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
