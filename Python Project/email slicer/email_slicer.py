import re

def email_slicer(email_address):


  match = re.search(r'^([^@]+)@([^@.]+)\.([a-z]{2,6})$', email_address)
  if match:
    return match.group(1), match.group(2), match.group(3)
  else:
    return None


email_address = "om2213500@gmail.com"
username, domain, tld = email_slicer(email_address)

print("Username:", username)
print("Domain:", domain)
print("TLD:", tld)
