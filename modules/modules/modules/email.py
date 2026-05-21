def email_scan(email):
    domain = email.split("@")[-1]

    return f"""
email report

email: {email}
domain: {domain}

google:
https://www.google.com/search?q={email}

breach check:
https://haveibeenpwned.com/
"""
