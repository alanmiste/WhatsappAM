import pywhatkit as kit

def check_is_digit(input_str):
    if input_str.strip().isdigit():
        print("The Mobile Number is: +"+input_str)
    else:
        print("User input is string")

print("Please enter the mobile number with the country ZIP code without + or 00. e.g. if you are in Germany the mobile number will be: 49xxxxxxxxxx")
x = input()
num=check_is_digit(x)       
kit.sendwhatmsg("+4915789032747","Test Test",15,35)
