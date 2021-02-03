def keuzemenu():
    print('!!!WARNING!!!\n'
          'Gebruik alleen HOOFDLETERS of KLEINE LETTERS tenzij anders aangegeven\n'
          '!!!WARNING!!!\n')

    keuze = input(
        'Wat voor IOS script wil je creëren? \n'
        'A: Ik wil een router IOS \n'
        'B: Ik wil een L2 Switch \n'
    )
    if keuze == 'A' or keuze == 'a':
        router()
    elif keuze == 'B' or keuze == 'b':
        layer2switch()
    else:
        print('Gebruik alleen de letters uit het keuze menu!')
        print('Please try again')
        keuzemenu()


def router():
    f = open('router.txt', '+a')
    f.write('enable \nconf t\n')

    hostnamerouter = input('Wat is de naam van de router:')
    f.write('hostname' + ' ' + hostnamerouter + '\n')

    secret = input('Wil je secret toevoegen? (ja/nee) : ')
    if secret == 'ja' or secret == 'JA':
        secret2 = input('Voer secret in: ')
        f.write('enable secret 5' + ' ' + secret2 + '\n')
    else:
        if secret == 'nee' or secret == 'NEE':
            pass
    f.write('aaa new-model\n')
    f.write('no ip domain lookup \n')

    AddDomain = input('Wil je een domain toevoegen? (ja/nee) :')
    if AddDomain == 'ja' or AddDomain == 'JA':
        domain = input('Voer je domain in: ')
        f.write('ip domain name' + ' ' + domain + '\n')
    else:
        if AddDomain == 'nee' or AddDomain == 'NEE':
            pass
    f.write('no ipv6 cef \n')

    AddLogin = input('Wil een username en password toevoegen? (ja/nee) : ')
    if AddLogin == 'ja' or AddLogin == 'JA':
        username = input('Voer je username in: ')
        password = input('Voer je password in: ')
        f.write('username' + ' ' + username + ' ' + 'privilege 15' + ' ' + 'password 0' + ' ' + password + '\n')
    else:
        if AddLogin == 'nee' or AddLogin == 'NEE':
            pass

    RootLogin = input('Wil je het root account activeren? (ja/nee) : ')
    if RootLogin == 'ja' or RootLogin == 'JA':
        rootpass = input('Voer het root password in: ')
        f.write('username root privilege 15 password 0'+ ' ' + rootpass + '\n')
    else:
        if RootLogin == 'nee' or RootLogin == 'NEE':
            pass

    interface = input('Wil je een ethernet interface configureren? (ja/nee) : ')
    if interface == 'ja' or interface == 'JA':
        type = input('wat voor interface heb je?\n'
              'A: FastEthernet\n'
              'B: Ethernet\n')
        if type == 'a' or type == 'A':
            intnub = input('Welke interface: ')
            IPadd = input('Wat is het ip: ')
            subnet = input('Wat is het subnet:')
            f.write('interface FastEthernet' + intnub + '\n')
            f.write('ip address' + ' ' + IPadd + ' ' + subnet + '\n')
            f.write('no shutdown\n')
            f.write('exit\n')

        elif type == 'b' or type == 'B':
            intnub1 = input('Welke interface: ')
            IPadd1 = input('Wat is het ip: ')
            subnet1 = input('Wat is het subnet:')
            f.write('interface Ethernet' + intnub1 + '\n')
            f.write('ip address' + ' ' + IPadd1 + ' ' + subnet1 + '\n')
            f.write('no shutdown\n')
            f.write('exit\n')

        else:
            print('Verkeerde inpunt, probeer opnieuw!!')
            print(type)

    linecon = input('line con configureren? (ja/nee) :')
    if linecon == 'ja' or linecon == 'JA':
        f.write('line con 0\n')
        f.write('exec-timeout 0 0\n')
        f.write('privilege level 15\n')
        f.write('exit\n')
        print('Done!')
    else:
        pass

    f.write('logging synchronous\n')

    vty = input('Wil je VTY configureren? (ja/nee) :')
    if vty == 'ja' or vty == 'JA':
        bgint = input('Begin interface? : ')
        endint = input('Eind interface? : ')
        ww = input('Voer wachtwoord in: ')
        ssh = input('SSH configureren? (ja/nee) :')

        if ssh == 'ja' or ssh == 'JA':
            f.write('transport input ssh')
        elif ssh == 'nee' or ssh == 'NEE':
            pass
        else:
            print('Verkeerde input')
            print(vty)

        f.write('line vty' + ' ' + bgint + ' ' + endint + '\n')
        f.write('password' + ' ' + ww + '\n')
        f.write('login' + '\n')

    elif vty == 'nee' or vty == 'NEE':
        pass

    vty2 = input('nog andere vty interfaces configureren? (ja/nee) :')
    if vty2 == 'ja' or vty2 == 'JA':
        bgint = input('Begin interface? : ')
        endint = input('Eind interface? : ')
        ww = input('Voer wachtwoord in: ')
        ssh = input('SSH configureren? (ja/nee) :')

        if ssh == 'ja' or ssh == 'JA':
            f.write('transport input ssh')
        elif ssh == 'nee' or ssh == 'NEE':
            pass
        else:
            print('Verkeerde input')
            print(vty2)

        f.write('line vty' + ' ' + bgint + ' ' + endint + '\n')
        f.write('password' + ' ' + ww + '\n')
        f.write('login' + '\n')

    elif vty == 'nee' or vty == 'NEE':
        pass

def layer2switch():
    f = open('layer2switch.txt', '+a')
    f.write('enable \nconf t\n')

    hostnameswitch = input('Wat is de naam van de Switch:')
    f.write('hostname' + ' ' + hostnameswitch + '\n')

    secret = input('Wil je secret toevoegen? (ja/nee) : ')
    if secret == 'ja' or secret == 'JA':
        secret2 = input('Voer secret in: ')
        f.write('enable secret 5' + ' ' + secret2 + '\n')
    else:
        if secret == 'nee' or secret == 'NEE':
            pass
    f.write('aaa new-model\n')
    f.write('no ip domain lookup \n')

    AddDomain = input('Wil je een domain toevoegen? (ja/nee) :')
    if AddDomain == 'ja' or AddDomain == 'JA':
        domain = input('Voer je domain in: ')
        f.write('ip domain name' + ' ' + domain + '\n')
    else:
        if AddDomain == 'nee' or AddDomain == 'NEE':
            pass
    AddLogin = input('Wil een username en password toevoegen? (ja/nee) : ')
    if AddLogin == 'ja' or AddLogin == 'JA':
        username = input('Voer je username in: ')
        password = input('Voer je password in: ')
        f.write('username' + ' ' + username + ' ' + 'privilege 15' + ' ' + 'password 0' + ' ' + password + '\n')
    else:
        if AddLogin == 'nee' or AddLogin == 'NEE':
            pass

    RootLogin = input('Wil je het root account activeren? (ja/nee) : ')
    if RootLogin == 'ja' or RootLogin == 'JA':
        rootpass = input('Voer het root password in: ')
        f.write('username root privilege 15 password 0'+ ' ' + rootpass + '\n')
    else:
        if RootLogin == 'nee' or RootLogin == 'NEE':
            pass

    intfc = input('Welke interface wil je configureren? (alleen nummer) : ')
    f.write('int' + ' ' + intfc + '\n')

    duplex = input('Full of half duplex? (full/half) :' )
    if duplex == 'half' or duplex == 'Half':
        f.write('duplex half' + '\n')
    elif duplex == 'full' or duplex == 'Full':
        f.write('duplex full' + '\n')

    vlan = input('Welke vlan wil je instellen?')
    f.write('interface vlan' + ' ' + vlan + '\n')

    IP = input('Wil je IP address instellen? (ja/nee) : ')
    if IP == 'ja' or IP == 'JA':
        ipaddress = input('Geef een ip address: ')
        subnet = input('Wat is het subnet: ')
        f.write('ip address' + ' ' + ipaddress + ' ' + subnet + '\n')
        f.write('no shutdown'+ '\n')
    elif IP == 'nee' or IP == 'Nee':
        pass
    else:
        print('Verkeerde input!')


    linecon = input('line con configureren? (ja/nee) :')
    if linecon == 'ja' or linecon == 'JA':
        f.write('line con 0\n')
        f.write('exec-timeout 0 0\n')
        f.write('privilege level 15\n')
        f.write('exit\n')
        f.write('logging synchronous\n')
        print('Done!')
    else:
        pass

    vty = input('Wil je VTY configureren? (ja/nee) :')
    if vty == 'ja' or vty == 'JA':
        bgint = input('Begin interface? : ')
        endint = input('Eind interface? : ')
        ww = input('Voer wachtwoord in: ')
        ssh = input('SSH configureren? (ja/nee) :')

        if ssh == 'ja' or ssh == 'JA':
            f.write('transport input ssh'+ '\n')
        elif ssh == 'nee' or ssh == 'NEE':
            pass
        else:
            print('Verkeerde input')
            print(vty)

        f.write('line vty' + ' ' + bgint + ' ' + endint + '\n')
        f.write('password' + ' ' + ww + '\n')
        f.write('login' + '\n')

    elif vty == 'nee' or vty == 'NEE':
        pass

keuzemenu()