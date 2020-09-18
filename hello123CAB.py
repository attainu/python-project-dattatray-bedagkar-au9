import sys
import random
import time
import smtplib
import math

#  account verification


def account(x):
    if x == 1:
        y = input("enter the valid  e-mail id :")
        OTP = generateOTP()
        messeage = ("welcome to hellocabs123 ")
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("hellocabs123@gmail.com", "789845651232")
        server.sendmail("hellocabs123@gmail.com", y, messeage)
        server.sendmail("hellocabs123@gmail.com", y, OTP)
        server.quit()
        while True:
            try:
                verify = input("enter the otp received : ")
                if verify == OTP:
                    print("user_mail registerd")
                    break
                elif verify != OTP:
                    print("wrong  OTP")
            except Exception as e:
                print(e)

    elif x == 2:
        z = input("enter the valid e-mail id :")
        messeage = ("welcome to hellocabs123 ")
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("hellocabs123@gmail.com", "789845651232")
        server.sendmail("hellocabs123@gmail.com", z, messeage)
        server.quit()
        print("driver_mail verified", z)
    else:
        print("enter the valid choice : 1 or 2")

# location of user


def position(city):
    city = int(input("1:mumbai,2:bangluru : "))
    while city == 1:
        print("select the locality you are currently in :")
        m_1 = int(input("1:DADAR , 2:MATUNGA , 3:BANDRA , 4:CHURCGATE : "))
        print("select the destination you want to go :")
        m_2 = int(input("1:DADAR , 2:MATUNGA , 3:BANDRA , 4:CHURCGATE : "))
        dict_1 = {1: 'DADAR', 2: 'MATUNGA', 3: 'BANDRA', 4: 'CHURCGATE'}
        dict_2 = {1: 'DADAR', 2: 'MATUNGA', 3: 'BANDRA', 4: 'CHURCGATE'}
        if m_1 == m_2:
            print(" please select valid destiantion")
        else:
            # this function will throw the random values in range of 0 to 10.
            key = random.randrange(0, 10)
            if key == 0:
                print("oops ! no rides available try again in few seconds.")
            else:
                print("the nearest ride is at a distance of km : ", key)
                # average speed is assumed to be 40kmph
                period = key/40
                # this is to convert the time into minutes.
                time_min = period*60
                print("your ride will arrive in min", time_min)
                confirmation = int(input("enter 1 to confirm ride : "))
                if confirmation == 1:
                    print("ride", dict_1[m_1], "to", dict_2[m_2], "confirmed")
                    time.sleep(time_min)
                    print("your ride has arrived")
        break

    while city == 2:
        print("select the locality you are currently in :")
        b_1 = int(input("1:M G Road , 2:MYSORE ROAD , 3:MANTRI SQUARE "))
        print("select the destination you want to go :")
        b_2 = int(input("1:M G Road , 2:MYSORE ROAD , 3:MANTRI SQUARE "))
        dit_1 = {1: '1:M G Road', 2: 'MYSORE ROAD', 3: 'MANTRI SQUARE'}
        dit_2 = {1: '1:M G Road', 2: 'MYSORE ROAD', 3: 'MANTRI SQUARE'}
        if b_1 == b_2:
            print(" please select valid destiantion")
        else:
            key = random.randrange(0, 10)
            if key == 0:
                print("oops ! no rides available try again in few seconds.")
            else:
                print("the nearest ride is at a distance of km : ", key)
                period = key/40
                time_min = period*60
                print("your ride will arrive in min", time_min)
                confirmation = int(input("enter 1 to confirm ride : "))
                if confirmation == 1:
                    print("ride ", dit_1[b_1], "to", dit_2[b_2], "confirmed")
                    time.sleep(time_min)
                    print("your ride has arrived")
        break

# driver loaction and availbilty


def driver(start_ride):

    if start_ride == 1:
        city = int(input("update the location,1:MUMBAI,2:BANGLURU"))
        if city == 1:
            print("searching for rider in MUMBAI ")
        if city == 2:
            print("searching for rider in BANGLURU")

    elif start_ride == 0:
        print("location has been turned off and no rides are made availabe")

# otp generation for user verification


def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


if __name__ == "__main__":
    arg = sys.argv
    while True:
        try:
            signup = int(input("press 1 for rider and 2 for driver  : "))
            if signup == 1:
                account(signup)

                location = print("select the city : ")
                position(location)
            elif signup == 2:
                account(signup)
                ride = int(input("1:new ride 0:turn off loaction : "))
                driver(ride)
            elif signup != 1 and signup != 2:
                print("enter valid key ! ")
        except Exception as e:
            print(e)
            break