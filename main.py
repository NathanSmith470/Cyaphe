import os
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '?', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', ':', ';', '\'', '|', '<', '>', '/', '_', '+', '[', ']', '{','}', '\"', '\\', ' ', '`', '~']

# FILE LOCATION TO SAVE ENCRYPTED PASSWORD DATA
pswd_file = "epsf.txt"

# COLORS
t_WHITE = "\033[0;37m"
t_GREEN = "\033[1;32m"
t_BLUE = "\033[1;34m"
t_YELLOW = "\033[1;33m"
t_RED = "\033[1;31m"
t_PURPLE = "\033[1;35m"

# FUNCTIONS
def encrypt(cyp,pswd):
    encpass = ""
    while True:
        if len(cyp) < len(pswd):
            cyp += cyp
        else:
            break

    summ = 0
    for j in range(0, len(pswd)):
        letter = ''
        flem = chars.index(pswd[j]) + chars.index(cyp[j]) + summ
        summ += chars.index(cyp[j])

        while True:
            try:
                letter = chars[flem]
                break
            except IndexError:
                flem -= len(chars)
                continue
        encpass += letter

    return encpass

def decrypt(cyp,pswd):
    decpass = ""
    temp_pass = ""
    while True:
        if len(cyp) < len(pswd):
            cyp += cyp
        else:
            break

    summ = 0

    for k in range(0, len(pswd)):
        letter = ''
        summ += chars.index(cyp[k])
        flem = chars.index(pswd[k]) + chars.index(cyp[k]) - summ

        while True:
            try:
                letter = chars[flem]
                break
            except IndexError:
                flem += len(chars)
                continue
        temp_pass += letter

    for d in range(0,len(temp_pass)):
        letter = chars.index(temp_pass[d]) - chars.index(cyp[d])
        decpass += chars[letter]

    return decpass

# MAIN
if __name__ == "__main__":
    running = True
    # LOGIN
    usr_cypher = input("Please Enter Your Cypher: ")
    top_msg = "Welcome to your Cyaphe!"

    # APPLICATION LOOP
    while running:
        print("\n" * 50)
        os.system("clear")
        print(t_GREEN + top_msg)
        print(t_WHITE+" _______________________________________________________________\n"+"|"+t_GREEN+" # "+t_WHITE+"|"+t_BLUE+"   Application   |"+t_YELLOW+"   Username   |"+t_RED+"   Password   |"+t_PURPLE+"   Notes   "+t_WHITE+"|\n|_______________________________________________________________|")
        p_database = open(pswd_file,"r+")

        # DISPLAY DATA
        line_num = 0
        while True:
            p_data = p_database.readline()
            line_num += 1
            if p_data == "":
                break
            secs = p_data.split("    ")
            secs[0] = decrypt(usr_cypher,secs[0].replace("\n",""))
            secs[1] = decrypt(usr_cypher, secs[1].replace("\n",""))
            secs[2] = decrypt(usr_cypher, secs[2].replace("\n",""))
            secs[3] = decrypt(usr_cypher, secs[3].replace("\n", ""))
            print("| "+t_GREEN+str(line_num)+t_WHITE+" |"+t_BLUE, str(secs[0]), "|"+t_YELLOW, str(secs[1]), "|"+t_RED, str(secs[2]), "|"+t_PURPLE, str(secs[3]),t_WHITE)
        p_database.close()

        # NEXT STEPS
        usr_inp = input(">: ").lower()

        # EXIT
        if usr_inp == "exit" or usr_inp == "x":
            running = False
            os.system("clear")
            os.system("exit")

        # ADD
        elif usr_inp == "add" or usr_inp == "a":
            app_name = input("Application Name: ")
            usr_name = input("Username: ")
            while True:
                passd = input("Password: ")
                passd_2 = input("Retype Password: ")
                if passd == passd_2:
                    break
                else:
                    print("Password Fields Do Not Match. Try Again.")
                    continue
            xtra_notes = input("Notes: ")
            if xtra_notes == "":
                xtra_notes = "---"
            p_database = open(pswd_file,"a")
            data_line = encrypt(usr_cypher,app_name) + "    " + encrypt(usr_cypher,usr_name) + "    " + encrypt(usr_cypher,passd) + "    " + encrypt(usr_cypher,xtra_notes) + "\n"
            p_database.write(data_line)
            p_database.close()
            top_msg = "Line Successfully Added"

        # DELETE
        elif usr_inp == "delete" or usr_inp == "d":
            while True:
                try:
                    del_line = int(input("Line # of Entry to Remove: "))
                    usr_inp = input("Are You Sure You Want to Delete Line #" + str(del_line)+" ? ").lower()
                    if usr_inp == "yes" or usr_inp == "y":
                        p_database = open(pswd_file, "r")
                        lines = p_database.readlines()
                        p_database.close()
                        p_database = open(pswd_file,"w")
                        for l in lines:
                            if l != lines[del_line-1]:
                                p_database.write(l)
                        p_database.close()
                        top_msg = "Line Successfully Deleted"
                        break
                    else:
                        top_msg = "Line Deletion Aborted"
                        break
                except ValueError:
                    print("Line # Must be a Number!")

        # EDIT
        elif usr_inp == "edit" or usr_inp == "e":
            edit_line = 0
            try:
                edit_line = int(input("Line # of Entry to Edit: "))
                while True:
                    p_database = open(pswd_file, "r")
                    lines = p_database.readlines()
                    p_database.close()
                    secs = lines[edit_line - 1].split("    ")
                    secs[0] = decrypt(usr_cypher, secs[0].replace("\n", ""))
                    secs[1] = decrypt(usr_cypher, secs[1].replace("\n", ""))
                    secs[2] = decrypt(usr_cypher, secs[2].replace("\n", ""))
                    secs[3] = decrypt(usr_cypher, secs[3].replace("\n", ""))
                    print("| " + t_GREEN + str(edit_line) + t_WHITE + " |" + t_BLUE, str(secs[0]), "|" + t_YELLOW, str(secs[1]), "|" + t_RED, str(secs[2]), "|" + t_PURPLE, str(secs[3]), t_WHITE)

                    try:
                        usr_inp = input("Overwrite: (a)pplication, (u)sername, (p)assword, (n)otes or e(x)it? ").lower()
                        if usr_inp == "app" or usr_inp == "a":
                            new_appname = input("New App Name: ")
                            p_database = open(pswd_file, "r")
                            lines = p_database.readlines()
                            p_database.close()
                            p_database = open(pswd_file, "w")
                            for l in lines:
                                if l != lines[edit_line - 1]:
                                    p_database.write(l)
                                else:
                                    prts = l.split("    ")
                                    l = encrypt(usr_cypher, new_appname) + "    " + prts[1] + "    " + prts[2] + "    " + prts[3]
                                    p_database.write(l)
                            p_database.close()
                            top_msg = "Line Successfully Edited"
                        elif usr_inp == "user" or usr_inp == "u":
                            new_user = input("New Username: ")
                            p_database = open(pswd_file, "r")
                            lines = p_database.readlines()
                            p_database.close()
                            p_database = open(pswd_file, "w")
                            for l in lines:
                                if l != lines[edit_line - 1]:
                                    p_database.write(l)
                                else:
                                    prts = l.split("    ")
                                    l = prts[0] + "    " + encrypt(usr_cypher, new_user) + "    " + prts[2] + "    " + prts[3]
                                    p_database.write(l)
                            p_database.close()
                            top_msg = "Line Successfully Edited"
                        elif usr_inp == "pass" or usr_inp == "p":
                            while True:
                                new_pass = input("New Password: ")
                                new_pass2 = input("Retype Password: ")
                                if new_pass == new_pass2:
                                    break
                                else:
                                    print("Passwords Do Not Match! Try Again.")
                                    continue
                            p_database = open(pswd_file, "r")
                            lines = p_database.readlines()
                            p_database.close()
                            p_database = open(pswd_file, "w")
                            for l in lines:
                                if l != lines[edit_line - 1]:
                                    p_database.write(l)
                                else:
                                    prts = l.split("    ")
                                    l = prts[0] + "    " + prts[1] + "    " + encrypt(usr_cypher, new_pass) + "    " + prts[3]
                                    p_database.write(l)
                            p_database.close()
                            top_msg = "Line Successfully Edited"
                        elif usr_inp == "notes" or usr_inp == "n":
                            new_notes = input("New Notes: ")
                            p_database = open(pswd_file, "r")
                            lines = p_database.readlines()
                            p_database.close()
                            p_database = open(pswd_file, "w")
                            for l in lines:
                                if l != lines[edit_line - 1]:
                                    p_database.write(l)
                                else:
                                    prts = l.split("    ")
                                    l = prts[0] + "    " + prts[1] + "    " + prts[2] + "    " + encrypt(usr_cypher, new_notes) + "\n"
                                    p_database.write(l)
                            p_database.close()
                            top_msg = "Line Successfully Edited"

                        else:
                            top_msg = "Line Editing Ended"
                            break
                    except ValueError:
                        print("An Internal Error Occured!")
            except IndexError:
                top_msg = "Line Does Not Exist"
            except ValueError:
                top_msg = "Line # Must be a Integer"

        # CHANGE CYPHER
        elif usr_inp == "cypher" or usr_inp == "c":
            print("Change Cypher? (DO NOT Change Cypher if Table is Unreadable!) ")
            usr_inp = input("(yes or no?) ")
            if usr_inp == "yes" or usr_inp == "y":
                usr_inp = input("Enter Old Cypher: ")
                if usr_inp == usr_cypher:
                    new_cypher = input("Enter New Cypher: ")
                    new_cypher2 = input("Re-Enter New Cypher: ")
                    if new_cypher == new_cypher2:
                        p_database = open(pswd_file, "r")
                        lines = p_database.readlines()
                        p_database.close()
                        p_database = open(pswd_file, "w")
                        for l in lines:
                            secs = l.split("    ")
                            secs[0] = decrypt(usr_cypher, secs[0].replace("\n", ""))
                            secs[1] = decrypt(usr_cypher, secs[1].replace("\n", ""))
                            secs[2] = decrypt(usr_cypher, secs[2].replace("\n", ""))
                            secs[3] = decrypt(usr_cypher, secs[3].replace("\n", ""))
                            n_line = encrypt(new_cypher,secs[0]) + "    " + encrypt(new_cypher,secs[1]) + "    " + encrypt(new_cypher,secs[2]) + "    " + encrypt(new_cypher,secs[3]) + "\n"
                            p_database.write(n_line)

                        p_database.close()
                        usr_cypher = new_cypher
                        top_msg = "Cypher Successfully Changed"
                    else:
                        top_msg = "Cyphers Do Not Match! Cypher Change Aborted."
                else:
                    top_msg = "Incorrect Cypher! Cypher Change Aborted."

        # SORT
        elif usr_inp == "sort" or usr_inp == "s":
            p_database = open(pswd_file, "r")
            lines = p_database.readlines()
            p_database.close()
            new_lines = []
            for l in lines:
                secs = l.split("    ")
                secs[0] = decrypt(usr_cypher, secs[0].replace("\n", ""))
                secs[1] = decrypt(usr_cypher, secs[1].replace("\n", ""))
                secs[2] = decrypt(usr_cypher, secs[2].replace("\n", ""))
                secs[3] = decrypt(usr_cypher, secs[3].replace("\n", ""))
                n_line = secs[0] + "    " + secs[1] +"    " + secs[2] +"    " + secs[3]
                new_lines.append(n_line)
                new_lines.sort()
            p_database = open(pswd_file, "w")
            for n in new_lines:
                secs = n.split("    ")
                w_line = encrypt(usr_cypher, secs[0]) + "    " + encrypt(usr_cypher, secs[1]) + "    " + encrypt(usr_cypher, secs[2]) + "    " + encrypt(usr_cypher, secs[3]) + "\n"
                p_database.write(w_line)
            p_database.close()
            top_msg = "Table Sorted!"

        # HELP MENU
        elif usr_inp == "help" or usr_inp == "h":
            top_msg = "HELP SECTION _______________________________________\n() : shortcut identifier\nCOMMANDS:\n(a)dd     ->    add and save a new entry to the table\n(d)elete  ->    removes an entry from the table\n(e)dit    ->    change table values for a line\n(s)ort    ->    sorts the table alphabetically by the app name\n(c)ypher  ->    re-encrypts the table with a new cypher (can destroy table if user logs in with incorrect cypher)\n(h)elp    ->    you are here\ne(x)it    ->    closes application"

        else:
            top_msg = "Command Not Recognized! (Type 'help' for a list of commands)"
