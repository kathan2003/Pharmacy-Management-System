# pharma/converters.py
class FormActionConverter:
    # regex: text followed by digits, e.g. dealerformupdate3
    regex = r'[a-zA-Z]+[a-zA-Z]+[0-9]+'

    def to_python(self, value):
        # Extract the trailing digits only and convert to int
        import re
        number = re.findall(r'\d+', value)
        if number:
            return int(number[0])
        raise ValueError("Invalid format")

    def to_url(self, value):
        # Just convert int back to string, the fixed text will be in path()
        return str(value)
