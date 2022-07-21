# these are called dictionaries

# 0) it all start with asking user for the date of their session
# to be replaced by actual date time?
r_date_input = input("\nPlease select the date of your session ")

# 1) there is a constant availability
# there is a function that adjusted the availability
# "schedule" dictionary needs work. it has to keep track of status
# i.e. there could be list of requests, or it can be open/closed
availability = {"date": "a", "schedule": [["open", "1 pm - 2 pm"],["booked", "2 pm - 3 pm"],["open", "3 pm - 4 pm"],["open", "4 pm - 5 pm"]]}

# 2) requests keeps track of users submitting requests for particular times slots
# the admin will have the ability to look through the requests, and for 
# a particular user, accept it. This will adjust the schedule for the times the
# request was for, and reject the requests that were for similar times
requests = {"date": "a", "schedule": [["user1", ["1 pm - 2 pm", "3 pm - 4 pm"]], ["user3", ["1 pm - 2 pm", "4 pm - 5 pm"]], ["user4", ["4 pm - 5 pm"]]]}

# create a request function
# user is presented with available dates
# then user indicates whether they are interested in any
def schedule_function(date):
    if (availability["date"]==date):
        i = 0
        print("\nHERE ARE THE AVAILABLE TIMES: \n")
        while i < len(availability["schedule"]):
            if (availability["schedule"][i][0] == "open"):
                print(availability["schedule"][i][1])
            i = i + 1
        proceed = input("\nwould you like to proceed with booking these? indicate with 'yes' or 'no': ")

        if (proceed == "yes"):
            i = 0
            req = ["user2", []]
            print("\nplease indicate which time slots are you interested in: ")
            while i < len(availability["schedule"]):                     
                day = availability["schedule"][i][1]          

                if (availability["schedule"][i][0] != "open"):
                    i = i + 1

                if (availability["schedule"][i][0] == "open"):
                    # prompt here
                    choice = input(f"would you like to book {day} ? indicate with 'yes' or 'no': ")          
                    
                    if (choice == "no"):
                        i = i + 1
                    # create a request dictionary
                    # store requeqst day, and stores list of lists indicating preference

                    if (choice == "yes"):
                        req[1].append(availability["schedule"][i][1])
                        i = i + 1
            i = 0
            print("\nYou requested: ")
            while i < len(req[1]):
                print(req[1][i])
                i = i + 1
            booking_confirm = input("\nwould you like to submit this booking request? indicate with 'yes' or 'no': ")
            
            if (booking_confirm == "yes"):
                requests["schedule"].append(req)
            print("\nawesome, thanks!")
            print("we'll get back to you shortly about confirmation!")
            # conditional statement -- if yes then we store the request for that time slot
            # inside the availability object, specifically for the 
        
        
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


def booking_function(date):
    # first part returns all requests
    if (availability["date"]==date):
        i = 0
        print("\nHERE ARE ALL THE REQUESTS FOR TIMES: \n")
        while i < len(requests["schedule"]):
            print(f'{requests["schedule"][i][0]} has requested these slots \n{requests["schedule"][i][1]}\n')
            i = i + 1
        proceed = input("\nwould you like to proceed with booking these? indicate with 'yes' or 'no': ")

        if (proceed == 'yes'):
            user = input("\nwhich request would you like to accept? please provide the user name: ")
            accept_request(user)
            # check if provided user matches any of the requests

            # 

# print(requests["schedule"][i][1][j])
j = 0
while j < len(requests["schedule"][0][1]):
    print(requests["schedule"][0][1][j])
    j = j + 1

# have to write a invalidate_requests function
# because there is overlap in accepted requests
# time slots that are affected need to be deleted
def invalidate_requests(accepted_request):
    print(f'requests["schedule"] {requests["schedule"]}')
    print(f'requests["schedule"][1] {requests["schedule"][1]}')
    print(f'requests["schedule"][1][1] {requests["schedule"][1][1]}')
    print(f'requests["schedule"][1][1][1] {requests["schedule"][1][1][1]}')
    # loop through accepted request time slots
    i = 0
    while i < len(requests["schedule"]):
        j = 0
        #print(f'{requests["schedule"][i][1]}')
        # go through requested time slots
        while j < len(requests["schedule"][i][1]):
            #print(f'{requests["schedule"][i][1]}')
            k = 0
            #check if there is a match with a time slot that is open
            while k < len(accepted_request):
                if (accepted_request[k] == requests["schedule"][i][1][j]):
                    print(f'found a match with accepted request time at {accepted_request[k]} and other requested time {requests["schedule"][i][1][j]} from user {requests["schedule"][i][0]}')
                k = k + 1
            j = j + 1   
        i = i + 1

# second part -- if admin proceeds, then ask him which request
# displays all requests and tag specific one. 
# tagged one changes the availability object
# also discards all requests that also had similar times
def accept_request(user):
    print(availability["schedule"])
    i = 0
    while i < len(requests["schedule"]):
        if (requests["schedule"][i][0] == user):
            # once the user matches, we get their request and replace open
            # schedule slot with closed ones
            j = 0
            accepted_req = requests["schedule"][i][1]
            print(accepted_req)
            # go through requested time slots
            while j < len(requests["schedule"][i][1]):
                k = 0

                #check if there is a match with a time slot that is open
                while k < len(availability["schedule"]):
                    if (availability["schedule"][k][0] == "open"):
                        if (availability["schedule"][k][1] == requests["schedule"][i][1][j]):
                            print(f'Booking this time slot {availability["schedule"][k][1]}')
                            availability["schedule"][k][0] = "booked"
                    k = k + 1
                j = j + 1   
            i = i + 1
        i = i + 1
    print(availability["schedule"])
    invalidate_requests(accepted_req)
    print('invalidate request done')
print("\n\nADMIN ACCEPT REQUEST")
r_date_input = input("Select the date for which you want to see the requests: ")

booking_function(r_date_input)





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