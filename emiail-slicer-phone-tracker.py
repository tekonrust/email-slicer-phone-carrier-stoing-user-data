# email-slicer-phone-carrier-stoing-user-data
def emailusername():
    import phonenumbers
    from phonenumbers import geocoder,carrier
    store={}                                                                                                                          #empty dictionary
    user=[]                                                                                                                           #empty list
    dom=[]                                                                                                                            #EMPTY LIST
    email=input("enter your email id : ").strip()
    number=input("enter your valid phone number with country code :")                                                                 
    username = email[:email.index("@")]                                                                                               #email slicing
    domain = email[email.index("@")+1:]                                                                                               #domain slicing
    mob_number = phonenumbers.parse(number)                                                                                           
    a=(geocoder.description_for_number(mob_number, "en"))                                                                             #geotracker
    b=(carrier.name_for_number(mob_number,"en"))                                                                                      #service provider
    print(F" country : '{a}' carrier/provider : '{b}' username : '{username}' domain : '{domain}'")                                   #printing all info
    user.append(username)                                                                                                             #list appeneded
    dom.append(domain)                                                                                                                #list appended
    store=dict(zip(user,dom))                                                                                                         #storing username and domain in dict
    print(store)
emailusername()



"""
drawback is havent put in the loop to check if the number is a number or not valid numbers(i.e string)
"""
