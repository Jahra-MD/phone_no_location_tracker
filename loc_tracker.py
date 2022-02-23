import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

number =input("enter the phone no with (+country code) \n")
country_name =phonenumbers.parse(number,"CH") #country history
print(geocoder.description_for_number(country_name,"en"))
#for service provider name
service_no=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_no,"en"))
