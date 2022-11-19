def email_search(text):
    """ Checks all the email in a string or text. """

    new = text.split(" ")
    for check in new:
        if "@" in check and ".com" in check:
            print(check)


abc = "my name is Trust, you can contact me at trust@gmail.com. www.gmail.com My company's email sdf@kdj" \
       "is trustglobal@yahoomail.com but my friend's email is careerguru99@hotmail.com " \
      "guru99@google.com, careerguru99@hotmail.com, users@yahoomail.com i live my job @the office"


email_search(abc)