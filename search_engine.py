import instaloader
import csv
import os
import time
import sys
from datetime import date


def menu():
    print("=" * 10 + " MENU " + "=" * 10)
    print("Press 1: Create list of all followers from {0}\n".format(tarAcc) +
          "Press 2: Create list of followees from {0}\n".format(tarAcc) +
          "Press 3: Download Content\n"
          "Press 4: instaMapper\n"
          "Press 99: End Script\n\n")

    print("Please type in a Number: ")
    usr_in = int(input())

    def getFollowers():
        loadTarAcc = instaloader.Profile.from_username(s.context, tarAcc)
        fileN = "Followers-" + tarAcc + "-" + str(date.today())
        file = open(fileN + ".txt", "a+")  # Name of the output File
        for followee in loadTarAcc.get_followers():
            username = followee.username
            file.write(username + "\n")
            print(username)

        file.close()
        print("The File: " + fileN + ".txt" + " has been saved.")
        print("\n")
        menu()

    def getFollowees():
        loadTarAcc = instaloader.Profile.from_username(s.context, tarAcc)
        fileN = "Followers-" + tarAcc + "-" + str(date.today())
        file = open(fileN + ".txt", "a+")  # Name of the output File
        for followee in loadTarAcc.get_followees():
            username = followee.username
            file.write(username + "\n")
            print(username)

        file.close()
        print("The File: " + fileN + ".txt" + " has been saved.")
        print("\n")
        menu()

    def downloadSubmenu():
        print("Please enter path (to file with account names): ")
        fileName = str(input())
        pathValid(fileName)
        print("Download will start any moment. This can take a lot of time...")
        print("""
        IMPORTANT: 
        1. Please respect the creators privacy. Especially when downloading content from private accounts.
           I do not take any responsibility for anything.
           
        2. If you download a lost of content, the API might start to give timeouts.
        
        3. Do not use Instagram while fetching content.         
        
        """)
        u = input("Press enter to continue: ")
        time.sleep(2)
        readFile(fileName)

    def instaMapper():
        print(4)

    def default():
        print("Incorrect option...")

    def endScript():
        print("Sending Kill signal...")
        sys.exit()

    dict = {
        1: getFollowers,  # DONE
        2: getFollowees,  # DONE
        3: downloadSubmenu, # DONE
        4: instaMapper,
        99: endScript,

    }
    dict.get(usr_in, default)()


def pathValid(fileName):
    if os.path.exists(fileName):
        pass
    else:
        while True:
            print("Path or Filename not found...Try again: ")
            fileName = str(input())
            if os.path.exists(fileName):
                return fileName


def readFile(fileName):
    with open(fileName, "r") as fileContent:  # opens the file in read mode
        content = fileContent.readlines()
        contentList = []

        for u in content:
            sp = u.split(",")
            contentList.append(sp[0].replace("\n", ""))

    download_post(contentList)


def download_post(contentList):
    print(" ===== Download Start ===== ")
    for u in contentList:
        po = instaloader.Profile.from_username(s.context, u).get_posts()
        print(" - User: " + u)
        for post in po:
            print("Fetching Content from: " + u + "...")
            s.download_post(post, u)


def tarA():
    global tarAcc
    tarAcc = str(input("Please enter the account name from which you want to retrieve data: "))


def loadSession():
    global s
    print("Please enter your account name (to access Instagram): ")
    u = input()
    u = "gibb.kleinanzeigen"  # todo Delete when done... its just so i don't have to type it every time
    s = instaloader.Instaloader()
    s.load_session_from_file(u)  # Load the created Session


# todo figure out that in prompt login... it just does not wanna work... >(
"""
    print(" Please enter a Target Account (from which you like to retrieve Data): ")
    userInput = str(input())
    tarAcc = instaloader.Profile.from_username(L.context, userInput)  # Target profile

    # L.login(USER, PASSWORD)  # (login)
    # L.interactive_login(USER)  # (ask password on terminal)
    # L.load_session_from_file(USER
"""


def start():  # Whole welcome text ect.
    print("""
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
Welcome to Insta_mapper! By Greenwavemonster
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
This tool can:
    - Map your instaconnections (Gephi needed for visualisation)
    - Download Followerlist / Followeelist from Accounts
    - Download Content from Accounts
    - more...
----------------------------------------------
IMPORTANT DISCLAIMER:
These scripts are for educational purpose only! 
Use at your own risk, I take no responsibility for anything or anyone!
----------------------------------------------
By continuing to use this Script you agree.


    """)
    wait = input('Press Enter to agree and continue... ')
    print("""
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
Please create a valid session which the script can use to access instagram.
Execute following command on the cmd to create a session:

'instaloader -l USERNAME'
    
and Login (2FA should work but can cause problems...)

*If you have already done that once, just continue.

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=# 
    """)
    wait = input('Press Enter to continue... ')


def main():
    start()
    loadSession()
    tarA()
    menu()


if __name__ == "__main__":
    main()

