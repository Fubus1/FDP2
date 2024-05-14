
ticket_concierto =int(input ("Ingrese numero de ticket "))


if ticket_concierto < 750 and ticket_concierto > 100:
    print ("Usted puede ingresar")
    if ticket_concierto < 750 and ticket_concierto  > 650:
        print ("Usted va a cancha")
    elif ticket_concierto > 100 and ticket_concierto < 649:
        print ("Usted va a galeria")
