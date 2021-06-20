friends_list=[]

while True:
    friend_id=input("Enter your friend's ID, or type start to generate the output:  ")
    if friend_id != "start":
        friends_list.append(friend_id)
    else:
        break

for i in friends_list:
    print(f"cat_pl_add_id {i}")

print("\n process ended")
    
