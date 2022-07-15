# these are called dictionaries

# 0) it all start with asking user for the date of their session
# to be replaced by actual date time?

r_date_input = input("Please select the date of your session ")

# 1) there is a constant availability
# there is a function that adjusted the availability
# "schedule" dictionary needs work. it has to keep track of status
# i.e. there could be list of requests, or it can be open/closed
availability = {"date": "a", "schedule": [["requested", "1 pm - 2 pm"],["open", "2 pm - 3 pm"],["open", "3 pm - 4 pm"],["open", "4 pm - 5 pm"]]}

# create a request function
# user is presented with available dates
# then user indicates whether they are interested in any
def schedule_function(date):
    if (availability["date"]==date):
        i = 0
        print("HERE ARE THE AVAILABLE TIMES: ")
        while i < len(availability["schedule"]):
            if (availability["schedule"][i][0] == "open"):
                print(availability["schedule"][i][1])
            i = i + 1
        proceed = input("would you like to proceed with booking these? indicate with 'yes' or 'no': \n")

        if (proceed == "yes"):
            i = 0
            req = availability
            print("\nplease indicate which time slots are you interested in: ")
            while i < len(availability["schedule"]):                     
                day = availability["schedule"][i][1]          

                if (availability["schedule"][i][0] != "open"):
                    req["schedule"][i][0] = "no"

                if (availability["schedule"][i][0] == "open"):
                    # prompt here
                    choice = input(f"would you like to book {day} ? indicate with 'yes' or 'no': ")          
                    
                    if (choice == "no"):
                        req["schedule"][i][0] = "no"
                    # create a request dictionary
                    # store requeqst day, and stores list of lists indicating preference

                    if (choice == "yes"):
                        req["schedule"][i][0] = "yes"
                i = i + 1g
            i = 0
            print("\nYou requested: ")
            while i < len(req["schedule"]):
                if (req["schedule"][i][0] == "yes"):
                    print(availability["schedule"][i][1])
                i = i + 1
            input("\nwould you like to submit this booking request?")

        # figure out how to deal with user submitting != n or != y
        # if (proceed != "y" or proceed != "n"):
        #     proceed = input("wrong answer. please select either y or n")


        # booking_function():
        #     booking_request = availability["schedule"]
            # loop through booking_request, ask for user input
            # print("would you like to book {availability["schedule"][i][1]}))")
    else:
        print("we don't have schedule for this day")

schedule_function(r_date_input)

# 
# def booking_function():



#create a program that will process the request versus availability
#   1) how to take user request via terminal? XX//XX
#   2) how to have function take in dictionary object?
# def request_validation():
#     if (availability["date"] == request_3["date"]):
#         if(availability["schedule"] == request_3["schedule"]):
#             print("full match!!")
#             print("changing availability to match request!!")
#         else:
#             print("only dates match!!")
#             print("please adjust selected hours!!")
#     else:
#         print("dates do not match!!")
#         print("please adjust date!!")

# request_validation()