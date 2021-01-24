# Cyaphe
A cypher-based encrypted safe for all your passwords

Welcome to your own personal Cyaphe!
A secure cypher-based encrypted safe for all your hard to remember passwords.
No cross-platform syncing, no stealing your data, no backdoors, full control.

OPENING YOUR CYAPHE:
Simply run the python file from the terminal or use the provided bash script ./cyaphe.sh
(In order to run the bash script you'll have to run the following command:
"chmod +x cyaphe.sh"
Note: command must be run in same directory as the script)

Upon opening the cyaphe it will ask you for a cypher.
This cypher is the password to protect all your passwords.
(I recommend not forgetting this one)
Your Cyaphe will then open to the table where all your passwords are shown.

ADDING PASSWORDS TO YOUR CYAPHE:
The Cyaphe acts like its own little simulated terminal and works with commands.
To not overload users, commands do not require any arguments as they will prompt you for additional input.
Type the command: "add" or just "a", then press enter.
Follow the prompts.
Congrats! You've just added your first password.

ADDITIONAL COMMANDS:
    () : shortcut identifier
    (a)dd     ->    add and save a new entry to the table
    (d)elete  ->    removes an entry from the table
    (e)dit    ->    change table values for a line
    (s)ort    ->    sorts the table alphabetically by the app name
    (c)ypher  ->    re-encrypts the table with a new cypher (can destroy table if user logs in with incorrect cypher)
    (h)elp    ->    you are here
    e(x)it    ->    closes application

TROUBLESHOOTING:
Q: How can I find the commands while in the Cyaphe?
A: Just type "help" or "h" to list all commands above the table

Q: I'm getting an IndexError on line 96 from python!
A: This is caused when there is a phantom newline in the epsf.txt file. This can be fixed by removing any empty lines at the beginning or end of the file. (Note: This should never happen unless you try to edit the epsf.txt file outside of the Cyaphe.

Q: All my passwords display as gibberish in the table!
A1: You may have put in the wrong cypher at startup. Cyaphe doesn't save your cypher, that's your job. Unfortunately adding a backdoor to recover your passwords defeats the whole point.
A2: If you change your cypher while logged in under a bad cypher, it will completely destroy all your passwords.
A3: If you edited the epsf.txt file outside of the Cyaphe, check to make sure there are exactly four spaces between each segment of gibberish on each line.

Enjoy your Cyaphe!
