"""Alle commando's dienen ingetypt te worden zonder hoofdletters"""

hostname = input("Geef de gewenste hostname: ")
secret = input("Geef het gewenste secret wachtwoord: ")
console = input("Geef het gewenste console wachtwoord: ")
vty = input("Geef het gewenste vty wachtwoord: ")

while True:

    keuze = input("Typ router of switch: ")

    if keuze == 'router':
        r = open("router.txt", "w")

        interface = input("Geef de gewenste interface: ")
        ip = input("Geef het gewenste IP-adres: ")
        sub = input("Geef det gewenste subnetmasker: ")
        description = input("Geef een description op van de interface: ")
        username = input("Geef de gewenste gebruikersnaam voor ssh: ")
        wachtwoord = input("Geef het gewenste wachtwoord voor ssh: ")

        encryptie = str
        while True:
            encryption = input("Wilt u encryptie toepassen, ja of nee? ")
            if encryption == 'ja':
                encryptie = "service password-encryption"
                break
            elif encryption == 'nee':
                encryptie = "no service password-encryption"
                break
            else:
                print("Ongeldige invoer")
                continue

        banner = input("Geef de gewenste banner: ")


        r.write("enable\nconf t\n!\nhostname " + hostname + "\n!\n"
                "enable secret " + secret + "\n!\n"
                "banner motd # " + banner + " #\n!\n"
                "username " + username + " privilege 15 password 0 " + wachtwoord + "\n!\n"
                "interface " + interface + "\n"
                "description " + description +"\n"
                "ip address " + ip + " " + sub + "\n"
                "no sh\n!\n"
                "line con 0\n"
                "exec-timeout 0 0\n"
                "privilege level 15\n"
                "password " + console + "\n"
                "login\n"
                "logging synchronous\n!\n"
                "line vty 0 15\n"
                "password " + vty + "\n"
                "login local\n"
                "transport input ssh\n!\n"
                "crypto key generate rsa 2048\n"
                "ip ssh version 2\n!\n" + encryptie + "\n!\n")

        lijst = []
        r.write("router rip\nversion 2\n")
        while True:
            routing = input("Geef de gewenste netwerk(en) op voor de routing configuratie. Typ 'einde' om te stoppen: ")
            if routing == "einde":
                break
            else:
                lijst.append(str(routing))

        for item in lijst:
            r.write("network " + item + "\n")

        while True:
            static = input("Wilt u (nog) een static route instellen? Ja of nee? ")
            if static == "ja":
                staticIP = input("Geef een IP-adres voor de static route op: ")
                staticSub = input("Geef een subnetmasker op voor de static route: ")
                nextHop = input("Geef een next-hop adres of interface op voor de static route: ")
                r.write("!\nip route " + staticIP + " " + staticSub + " " + nextHop + "\n")
            elif static == "nee":
                break
            else:
                continue

        r.write("!")
        r.close()
        break

    elif keuze == 'switch':
        s = open("switch.txt", "w")
        s.write("enable\nconf t\n!\nhostname " + hostname + "\n!\n"
                "enable secret " + secret + "\n!\n"
                "line con 0\n"
                "exec-timeout 0 0\n"
                "privilege level 15\n"
                "password " + console + "\n"
                "login\n"
                "logging synchronous\n!\n"
                "line vty 0 15\n"
                "password " + vty + "\n"
                "login local\n"
                "transport input ssh\n!\n")

        vlan = []
        naam = []
        while True:

            try:
                vlaninput = int(input("Geef het vlan-id op. Typ '0' om te stoppen: "))
            except ValueError:
                print("Geef een cijfer op!")
                continue

            if vlaninput < 0:
                continue
            elif vlaninput == int(0):
                break
            else:
                naaminput = input("Geef de naam van het vlan: ")
                vlan.append(vlaninput)
                naam.append(naaminput)

        zipped = zip(vlan, naam)
        lists = list(zipped)
        for i in lists:
            s.write("vlan " + str(i[0]) + "\n")
            s.write("name " + i[1] + "\n!\n")

        while True:
            layer = input("Geef aan met het getal 2 of 3 wat voor soort layer switch: ")

            s.write("crypto key generate rsa\n2048\nip ssh version 2\n!\n")

            if layer == '2':
                while True:
                    bereik = input("Wil je (nog) een range opgeven? Ja of nee? Typ 'einde' om te stoppen: ")
                    if bereik == "ja":
                        interfaces = input("Geef de range op: ")
                        s.write("interface range " + interfaces + "\nduplex full \n")
                    elif bereik == "nee":
                        interface = input("Geef een interface op: ")
                        s.write("interface " + interface + "\nduplex full \n")
                    elif bereik == "einde":
                        break
                    else:
                        print("Geen van de mogelijke opties gekozen. Probeer het opnieuw")
                        continue

                    switchport = input("Geef aan of dit access of trunk moet worden: ")
                    if switchport == "access":
                        s.write("switchport mode access \n")
                        access = input("Geef het vlan-id op die toegestaan is op deze interfaces: ")
                        s.write("switchport access vlan " + access + "\n!\n")
                    elif switchport == "trunk":
                        s.write("switchport trunk encapsulation dot1q \n")
                        s.write("switchport mode trunk \n!\n")
                    else:
                        print("Verkeerde waarde. Probeer het opnieuw")
                        s.write("!\n")
                        continue
                break

            elif layer == '3':
                s.write("ip routing \n!\n")
                while True:
                    try:
                        vlanID = int(input("Geef het VLAN-id voor de interface op. Typ '0' om te stoppen: "))
                    except ValueError:
                        print("Geef een cijfer op!")
                        continue

                    if vlanID < 0:
                        continue
                    elif vlanID == int(0):
                        break
                    else:
                        s.write("interface vlan " + str(vlanID) + "\n")
                        description = input("Geef een description op: ")
                        s.write("description " + description + "\n")
                        ipAddress = input("Geef het IP-adres op: ")
                        sub = input("Geef het subnetmasker op: ")
                        s.write("ip address " + ipAddress + " " + sub + "\n!\n")

                while True:
                    static = input("Wilt u (nog) een static route instellen? Ja of nee? ")

                    if static == "ja":
                        staticIP = input("Geef een IP-adres voor de static route op: ")
                        staticSub = input("Geef een subnetmasker op voor de static route: ")
                        nextHop = input("Geef een next-hop adres of interface op voor de static route: ")
                        s.write("ip route " + staticIP + " " + staticSub + " " + nextHop + "\n")
                    elif static == "nee":
                        break
                    else:
                        print("Geen van de mogelijke opties gekozen. Probeer het opnieuw")
                        continue
                break
            else:
                print("Geen van de mogelijke opties gekozen. Probeer het opnieuw")
                continue

        s.close()
        break

    else:
        print("Geen van de mogelijke opties gekozen. Probeer het opnieuw")
        continue



