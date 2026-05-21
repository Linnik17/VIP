import phonenumbers
from phonenumbers import geocoder, carrier

def phone_scan(phone):
    try:
        p = phonenumbers.parse(phone, None)

        country = geocoder.description_for_number(p, "en")
        oper = carrier.name_for_number(p, "en")
        valid = phonenumbers.is_valid_number(p)

        return f"""
phone report

number: {phone}
country: {country}
carrier: {oper or "unknown"}
valid: {valid}

google:
https://www.google.com/search?q={phone}

open source only
"""
    except:
        return "invalid phone"
