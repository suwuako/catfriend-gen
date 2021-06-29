#!/usr/bin/env python3
#

friends_list = []
friend_id = input("Enter your friend's ID, or type start to generate the output:  ")

while (friend_id != "start"):
    friends_list.append(friend_id)
    friend_id = input("Enter your friend's ID, or type start to generate the output:  ")

for i in friends_list:
    print(f"cat_pl_add_id {i}")

print("\n process ended")
    
