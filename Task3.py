import random
def check_mail(mail,domain): 
    """This function check the email and return back where it comes from."""
    if mail.index("@") >=2 and domain in mail: # it checks the mail
        return True
    elif domain not in mail: # it check domain is in mail or not
        return False
    else:
        return False

def output(name):
    """This function shows the output of the program."""
    robot = ["Honey","Lily","Rose","Mary","Jisny","Jenny","Anny"]
    network = [True,True,False,True,False,True,True]
    replies = ["Hmmm","Oh","yes","I see","Tell me more","Like?"]
    print(f"\nHello, {name}! Thank you, and welcome to Pop Chat!")
    print(f"My name is {random.choice(robot)}, and it will be my pleasure to help you.")
    if random.choice(network) == True:   # it check the network error
        while True: #it loops the program
            question = input("---->")
            if question == "bye" or question == "exit": # it check the condition 
                break
            elif "library" in question: #it execute if condition is fulfilled
                print("The library is closed today.")
            elif "wifi" in question:    #it execute if condition is fulfilled
                print("WiFi is excellent across the campus.")
            elif "deadline" in question:    #it execute if condition is fulfilled
                print("Your deadline has been extended by two working days.")
            elif "coffee" in question:  #it execute if condition is fulfilled
                print("Teekee is open until 9pm this evening.")
            elif "fee" in question: #it execute if condition is fulfilled
                print("Contact to the Administration.")
            elif "hoilday" in question: #it execute if condition is fulfilled
                print("You can ask to the SSD department.")
            elif "teacher" in question: #it execute if condition is fulfilled
                print("Teacher will be back soon.")
            else:      #if condition doesnot match it print random values
                print(f"{random.choice(replies)}")
    else: # it print if network error
        print("Network Error")
    print(f"Thanks, {name}, for using PopChat. See you again soon!\n")


print("Welcome to pop chat")
print("One of our operators will be please to help you today.")
mail = input("Please enter your Poppleton email address: ")
domain = "@pop.ac.uk"

if mail == "":  # it check email id provided or not
    print("Email not provided")
elif check_mail(mail,domain) == True: # it pass the email if email id provided 
    n = mail.index("@")
    name = mail[:n]
    output(name)
else: 
    print("Invalid mail")
