# these are called dictionaries

# 0) it all start with asking user for the date of their session
# to be replaced by actual date time?
r_date_input = input("\nPlease select the date of your session ")

# 1) there is a constant availability
# there is a function that adjusted the availability
# "schedule" dictionary needs work. it has to keep track of status
# i.e. there could be list of requests, or it can be open/closed

# schedule to be renamed to time_slots
availability = {"date": "a", "time_slots": [["open", "1 pm - 2 pm"], [
    "booked", "2 pm - 3 pm"], ["open", "3 pm - 4 pm"], ["open", "4 pm - 5 pm"]]}

# 2) requests keeps track of users submitting requests for particular times slots
# the admin will have the ability to look through the requests, and for
# a particular user, accept it. This will adjust the schedule for the times the
# request was for, and reject the requests that were for similar times
requests = {"date": "a", "user_requests": [["user1", ["1 pm - 2 pm", "3 pm - 4 pm", "4 pm - 5 pm"], "pending"], [
    "user3", ["1 pm - 2 pm", "4 pm - 5 pm"], "pending"], ["user4", ["4 pm - 5 pm"], "pending"]]}

# create a request function
# user is presented with available dates
# then user indicates whether they are interested in any


def add_request(date):
    if (availability["date"] == date):
        i = 0
        print("\nHERE ARE THE AVAILABLE TIMES: \n")
        while i < len(availability["time_slots"]):
            if (availability["time_slots"][i][0] == "open"):
                print(availability["time_slots"][i][1])
            i = i + 1
        proceed = input(
            "\nwould you like to proceed with booking these? indicate with 'yes' or 'no': ")

        if (proceed == "yes"):
            i = 0
            req = ["user2", [], "pending"]
            print("\nplease indicate which time slots are you interested in: ")
            while i < len(availability["time_slots"]):
                day = availability["time_slots"][i][1]

                if (availability["time_slots"][i][0] != "open"):
                    i = i + 1

                if (availability["time_slots"][i][0] == "open"):
                    # prompt here
                    choice = input(
                        f"would you like to book {day} ? indicate with 'yes' or 'no': ")

                    if (choice == "no"):
                        i = i + 1
                    # create a request dictionary
                    # store requeqst day, and stores list of lists indicating preference

                    if (choice == "yes"):
                        req[1].append(availability["time_slots"][i][1])
                        i = i + 1
            i = 0
            print("\nYou requested: ")
            while i < len(req[1]):
                print(req[1][i])
                i = i + 1
            booking_confirm = input(
                "\nwould you like to submit this booking request? indicate with 'yes' or 'no': ")

            if (booking_confirm == "yes"):
                requests["user_requests"].append(req)
            print("\nawesome, thanks!")
            print("we'll get back to you shortly about confirmation!")
            # conditional statement -- if yes then we store the request for that time slot
            # inside the availability object, specifically for the

    else:
        print("we don't have schedule for this day")


add_request(r_date_input)

# function that let's admin look at all requests, and provided
# a username, books that request via accept_request(). also calls invalidate requests
# and accept request.


def book_date(date):
    # first part returns all requests
    if (availability["date"] == date):
        i = 0
        print("\nHERE ARE ALL THE REQUESTS FOR TIMES: \n")
        while i < len(requests["user_requests"]):
            print(
                f'{requests["user_requests"][i][0]} has requested these slots \n{requests["user_requests"][i][1]}\n')
            i = i + 1
        proceed = input(
            "\nwould you like to proceed with booking these? indicate with 'yes' or 'no': ")

        if (proceed == 'yes'):
            user = input(
                "\nwhich request would you like to accept? please provide the user name: ")
            accept_request(user)
            # check if provided user matches any of the requests


def notify_user(user):
    print(
        f'hey {user} we have denied your request. please try booking another time.')

    # have to write a invalidate_requests function
    # because there is overlap in accepted requests
    # time slots that are affected need to be deleted


def invalidate_requests(accepted_request):
    # loop through accepted request time slots
    i = 0
    while i < len(requests["user_requests"]):
        j = 0
        # print(f'{requests["schedule"][i][1]}')
        # go through requested time slots
        while j < len(requests["user_requests"][i][1]):
            # print(f'{requests["schedule"][i][1]}')
            k = 0
            # check if there is a match with a time slot that is open
            while k < len(accepted_request[1]):
                if (requests["user_requests"][i][1][j] == accepted_request[1][k]):
                    if (requests["user_requests"][i][0] != accepted_request[0]):
                        requests["user_requests"][i][2] = "denied"
                        if (requests["user_requests"][i][2] == "denied"):
                            notify_user(requests["user_requests"][i][0])
                    k = k + 1
                k = k + 1
            j = j + 1
        i = i + 1

# second part -- if admin proceeds, then ask him which request
# displays all requests and tag specific one.
# tagged one changes the availability object
# also discards all requests that also had similar times


def accept_request(user):
    i = 0
    while i < len(requests["user_requests"]):
        if (requests["user_requests"][i][0] == user):
            # once the user matches, we get their request and replace open
            # schedule slot with closed ones
            j = 0
            accepted_req = requests["user_requests"][i]
            print(accepted_req)
            # go through requested time slots
            while j < len(requests["user_requests"][i][1]):
                k = 0

                # check if there is a match with a time slot that is open
                while k < len(availability["time_slots"]):
                    if (availability["time_slots"][k][0] == "open"):
                        if (availability["time_slots"][k][1] == requests["user_requests"][i][1][j]):
                            print(
                                f'Booking this time slot {availability["time_slots"][k][1]}')
                            availability["time_slots"][k][0] = "booked"
                    k = k + 1
                j = j + 1
            i = i + 1
        i = i + 1
    print(f'\nhere is the old availability{requests["user_requests"]}\n')
    invalidate_requests(accepted_req)
    print('\ninvalidate request done')
    print(f'\nhere is the new availability{requests["user_requests"]}')


print("\n\nADMIN ACCEPT REQUEST")
r_date_input = input(
    "Select the date for which you want to see the requests: ")

book_date(r_date_input)


# create a program that will process the request versus availability
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
