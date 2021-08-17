import instaloader
from datetime import date

USER = "gibb.kleinanzeigen"  # User acc which can acces instagram...
acc_target = "m_aexu"

# Get instance
L = instaloader.Instaloader()
L.load_session_from_file(USER)  # Load the created Session // Create a session -> "instaloader -l USERNAME"
tarAcc = instaloader.Profile.from_username(L.context, acc_target)  # Load Target profile

# Print list of followers into text file
follow_list = []
fileN = "Followers-" + acc_target + "-" + str(date.today())
file = open(fileN + ".txt", "a+")  # Name of the output File
for followee in tarAcc.get_followees():
    username = followee.username
    file.write(username + "\n")
    print(username)

file.close()
