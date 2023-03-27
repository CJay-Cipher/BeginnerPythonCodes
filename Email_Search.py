def email_search(text):
    """ Checks all the email in a string or text and return as a list. """

    import re
    temp_list = re.split(r"[ ,\n]+", text)

    return [check for check in temp_list if "@" in check and ".com" in check]


abc = "my name is Trust, you can contact me at trust@gmail.com. www.gmail.com My company's email sdf@kdj \n" \
      "is trustglobal@yahoomail.com but my friend's email is careerguru99@hotmail.com \n" \
      "guru99@google.com, careerguru99@hotmail.com, users@yahoomail.com i live my job @the office"


print(email_search(abc))