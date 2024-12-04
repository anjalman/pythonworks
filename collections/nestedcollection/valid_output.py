

user_input=input("enter bracket paris:")

symbol=("{}","[]","()","<>")

# for br in symbol:
    
#     if user_input in symbol:

#         print("valid output")

#         break

#     else:

#         print("not valid output")

#         break

bracket_paris={br:symbol for br in user_input if user_input in symbol }


