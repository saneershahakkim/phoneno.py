import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

phoneNumber = phonenumbers.parse("+91 8075111576")

Carrier = carrier.name_for_number(phoneNumber, "en")

Region = geocoder.description_for_number(phoneNumber, "en")

print(f"| Counrty | Supplier |\n|----------------|\n| {Region} | {Carrier} |")