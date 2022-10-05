import re

# 1
addr = ['Room 536, Library Building, University College Dublin, Dublin 4, Ireland', 
        'Room G03, Science Centre North University College Dublin, Belfield, Dublin 4, Ireland']

newaddr = [item.replace(",", "\n") for item in addr]
print(newaddr)

# 2
emails = ['test1@ucd.ie','test2@gmail.com','test3@hotmail.com']
domains = []
for email in emails:
    domains.append(email.split("@")[1])

print(domains)

x = [email.split("@")[1] for email in emails]
print(x)

# 3

poem = str(['No man is an island, entire of itself, every man is a piece of the continent, a part of the main. If a clod be washed away by the sea, Europe is the less.'])
words = re.findall("the ", poem)

print(words)

# 4
def find_emails(x):
        emails = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", x)
        return(emails)

print(find_emails('John Koftaram <test@capahq.org> would like to connect on LinkedIn. How would you like to respond?'))