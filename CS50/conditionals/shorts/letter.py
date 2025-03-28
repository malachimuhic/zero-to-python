"""
This program goes over how to use 'For Loops' and range
i = iterate

"""

def main():
    guestlist = ["Mario", "Luigi", "Daisy", "Yoshi"]
    for name in guestlist:
        print(write_letter(name, "Princess Peaches"))
        

def write_letter(receiver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        Dear, {receiver},

        you are cordially invited to a ball at
        Peach's Castle this evening, 7:00 PM.

        Sincerely,
        {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
"""

main()