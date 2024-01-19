#3-4
names_to_invite = ["Kim Kardashian", "Bradley Cooper", "Michael Jackson"]

for names in names_to_invite:
    print(f"Hi {names}! Would you like to join me and my guests for dinner?")

#3-5
print(f"\nLooks like {names_to_invite[2]} couldn't make it!\n")

names_to_invite[2] = "Oskar Westerlin"

for names in names_to_invite:
    print(f"Hi {names}! Would you like to join me and my guests for dinner?")

#3-6
print("\nLooks like we found a bigger table! I'll invite more people to the dinner.\n")

names_to_invite.insert(0, "Kris Jenner")
names_to_invite.insert(3, "Kylie Jenner")
names_to_invite.append("Donald Trump")

for names in names_to_invite:
    print(f"Hi {names}! Would you like to join me and my guests for dinner?")

#3-7
print("\nSeems like my table won't come in time. I can only invite two people.\n")

revoked_invite = names_to_invite.pop()
print(f"Sorry to inform you {revoked_invite}, but you're invitation have been revoked.")

revoked_invite = names_to_invite.pop()
print(f"Sorry to inform you {revoked_invite}, but you're invitation have been revoked.")

revoked_invite = names_to_invite.pop()
print(f"Sorry to inform you {revoked_invite}, but you're invitation have been revoked.")

revoked_invite = names_to_invite.pop()
print(f"Sorry to inform you {revoked_invite}, but you're invitation have been revoked.\n")

for name in names_to_invite:
    print(f"Don't worry {name}! You're still invited.")

del names_to_invite[1]
del names_to_invite[0]

print(names_to_invite)