users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" },
   
]
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]



# create a dictionary with each user's id and an empty list of friends
network = {user["id"]: [] for user in users}

# populate the lists of friends using the friendship pairs
for i, j in friendship_pairs:
    network[i].append(j)
    network[j].append(i)

# calculate the total number of connections
total_connections = sum(len(friends) for friends in network.values())

# calculate the average number of connections
num_users = len(network)
avg_connections = total_connections / num_users

print("Total connections:", total_connections)
print("Average connections:", avg_connections)

# create a list of tuples with each user's id and number of friends
num_friends = []
for user_id, friends in network.items():
    if isinstance(friends, list):
        num_friends.append((user_id, len(friends)))

# sort the list by number of friends in descending order
sorted_num_friends = sorted(num_friends, key=lambda x: x[1], reverse=True)

# print the sorted list
for user_id, num_friends in sorted_num_friends:
    user_name = [user["name"] for user in users if user["id"] == user_id][0]
    print(user_name, "has", num_friends, "friends")

# find the friends of friends for user with id 0
user_id = 0
friends_of_friends = set()
for friend in network[user_id]:
    for friend_of_friend in network[friend]:
        if friend_of_friend != user_id and friend_of_friend not in network[user_id]:
            friends_of_friends.add(friend_of_friend)

# print the set of friends of friends
print(friends_of_friends)
