import re

def validate_pin(pin):
    return True if re.findall(r'^\d{4}\Z|^\d{6}\Z', pin) else False
