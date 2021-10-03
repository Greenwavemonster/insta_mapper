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
        print("Creating list of followers...")
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
        print("Creating list of followees...")
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
        fileName = input()
        if os.path.exists(fileName):
            pass
        else:
            while True:
                print("Path or Filename not found...Try again: ")
                fileName = input()
                if os.path.exists(fileName):
                    break
        print("Download will start any moment. This can take a lot of time...")
        print("""
        IMPORTANT: 
        1. Please respect the creators privacy. Especially when downloading content from private accounts.
           I do not take any responsibility for anything.

        2. If you download a lot of content, the API might start to give timeouts.

        3. DO NOT use Instagram on a other Device while fetching content. The API will throw errors...      

        """)
        u = input("Press enter to continue: ")
        time.sleep(2)
        readFile(fileName)

    def instaMapper():
        print(4)
        firstRun()
        secondRun()

    def default():
        print("Incorrect option...")

    def endScript():
        print("Sending Kill signal...")
        sys.exit()

    dict = {
        1: getFollowers,  # DONE
        2: getFollowees,  # DONE
        3: downloadSubmenu,  # DONE
        4: instaMapper,
        99: endScript,

    }
    dict.get(usr_in, default)()

def firstRun():  # This is to fetch data from the tarAcc
    t1 = time.time()
    os.mkdir(r'C:\Users\XXXX\PycharmProjects\instaread2.0\csv-files\followers-files')
    cPaths = r'C:\Users\XXXX\PycharmProjects\instaread2.0\csv-files\followers-files'

    acc = tarAcc + '-' + "followers" + '.csv'
    tmpPath = os.path.join(cPaths, acc)

    users = instaloader.Profile.from_username(s.context, tarAcc)  # Load Target profile

    h = ['Account', 'Followers', 'Followees']

    with open(tmpPath, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(h)

        i = 0
        count = 0
        pause = 0
        for f in users.get_followers():
            uName = str(f.username)
            uLoad2 = instaloader.Profile.from_username(s.context, uName)
            uCon1 = str(uLoad2.get_followers().count)
            uCon2 = str(uLoad2.get_followees().count)
            csvContent = [uName, uCon1, uCon2]
            writer.writerow(csvContent)
            i += 1
            if (i == 10):
                csvFile.flush()
                count += 10
                print("Flushed")
                if (count == 60):
                    print("Waiting 15min to avoid \"To many request\"")
                    time.sleep(900)
                    count = 0
                    pause += 1

        csvFile.flush()
        csvFile.close()
    t2 = time.time()
    total = t2 - t1
    print("TOTAL RUNTIME Follower Download {}".format(total))
    print("TOTAL RUNTIME Follower Download without API Breaks {}".format(total - (pause*15)))

def secondRun():  # This is to fetch data from the tarAcc
    print("Waiting 15min to avoid \"To many request\"") # Just to make sure nothing happends
    time.sleep(900)

    t1 = time.time()
    os.mkdir(r'C:\Users\XXXX\PycharmProjects\instaread2.0\csv-files\followees-files')
    cPaths = r'C:\Users\XXXX\PycharmProjects\instaread2.0\csv-files\followees-files'

    acc = tarAcc + '-' + "followees" + '.csv'
    tmpPath = os.path.join(cPaths, acc)

    users = instaloader.Profile.from_username(s.context, tarAcc)  # Load Target profile

    h = ['Account', 'Followers', 'Followees']

    with open(tmpPath, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(h)

        i = 0
        count = 0
        pause = 0
        for f in users.get_followees():
            uName = str(f.username)
            uLoad2 = instaloader.Profile.from_username(s.context, uName)
            uCon1 = str(uLoad2.get_followers().count)
            uCon2 = str(uLoad2.get_followees().count)
            csvContent = [uName, uCon1, uCon2]
            writer.writerow(csvContent)
            i += 1
            if (i == 10):
                csvFile.flush()
                count += 10
                print("Flushed")
                if (count == 60):
                    print("Waiting 15min to avoid \"To many request\"")
                    time.sleep(900)
                    count = 0
                    pause += 1

        csvFile.flush()
        csvFile.close()
    t2 = time.time()
    total = t2 - t1
    print("TOTAL RUNTIME Followees Download {}".format(total))
    print("TOTAL RUNTIME Followees Download without API Breaks {}".format(total - 15 - (pause*15))) # The first 15 is from the 15min wait befor this cycle starts


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

