import instaloader
from datetime import date

USER = "foo"  # User acc which can access instagram...
acc_target = "foo2"

# Get instance
L = instaloader.Instaloader()
L.load_session_from_file(USER)  # Load the created Session // Create a session -> "instaloader -l USERNAME"
tarAcc = instaloader.Profile.from_username(L.context, acc_target)  # Load Target profile

# Print list of followees
follow_list = []
fileN = "Followees-" + acc_target + "-" + str(date.today())
file = open(fileN + ".txt", "a+")  # Name of the output File
for follower in tarAcc.get_followers():
    username = follower.username
    file.write(username + "\n")
    print(username)

file.close()

