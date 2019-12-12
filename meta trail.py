import exifread

print " _______  _______ _________ _______  ______   _______ _________ _______ ".center(75)
print "(       )(  ____ \\__   __/(  ___  )(  __  \ (  ___  )\__   __/(  ___  )".center(75)
print "| () () || (    \/   ) (   | (   ) || (  \  )| (   ) |   ) (   | (   ) |".center(75)
print "| || || || (__       | |   | (___) || |   ) || (___) |   | |   | (___) |".center(75)
print "| |(_)| ||  __)      | |   |  ___  || |   | ||  ___  |   | |   |  ___  |".center(75)
print "| |   | || (         | |   | (   ) || |   ) || (   ) |   | |   | (   ) |".center(75)
print "| )   ( || (____/\   | |   | )   ( || (__/  )| )   ( |   | |   | )   ( |".center(75)
print "|/     \|(_______/   )_(   |/     \|(______/ |/     \|   )_(   |/     \|".center(75)
print""
print""
print"Coded By : Mohammed Banyamer ".center(75)
print""
print '{IMAGE REVERSE LOOKUP JO}'.center(75)
print""
print""

def mainMenu():
    print("SELECT A Meta-Data")
    print("")
    print("e1- Get Image Meta-Data ")
    print("e2- Get vioce Meta-Data")
    print("e3- Exit")
    print("")

    while True:

        selection = input("Enter a choice: ")

        if(selection == "e1"):
            e1()
            break
        elif(selection == "e2"):
            e2()
            break
        elif(selection == "e3"):
            print("Goodbye")
            break
        else:
            print("Invalid choice. Enter 'e1'-'e3'")
            print("")
            mainMenu()
def e1():

                           
