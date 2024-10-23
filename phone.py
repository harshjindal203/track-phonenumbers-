import phonenumbers
from phonenumbers import geocoder, carrier
def track_phone_number(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        
        # Get the country name
        country = geocoder.description_for_number(parsed_number, "en")
        print("Country:", country)
        
        # Get the carrier name
        carrier_name = carrier.name_for_number(parsed_number, "en")
        print("Carrier:", carrier_name)
        
        # Check if the number is valid
        is_valid = phonenumbers.is_valid_number(parsed_number)
        print("Valid Number:", is_valid)
        
        # Check if the number is possible
        is_possible = phonenumbers.is_possible_number(parsed_number)
        print("Possible Number:", is_possible)
    except phonenumbers.phonenumberutil.NumberParseException:
        print("Invalid phone number")

# Example usage
phone_number = "+917073074852"
track_phone_number(phone_number)

