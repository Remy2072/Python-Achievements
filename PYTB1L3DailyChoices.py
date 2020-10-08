print("De dagelijkse keuzes van Remy Duivesteijn")
def vraag1():
    print("\nvraag 1")    # vraag 1
    print("Je wordt wakker en gaat je brood smeren wat eet je op je brood?")
    print("kies antwoord 1 of 2") 
    print("1=kipfilet")
    print("2=pindakaas")
    vraag=input("Type een cijfer >")
    if vraag == '1':
        print("\n Hmm lekker kippie")
        vraag2()
    if vraag == '2':
        print("\nHeerlijk een broodje pindakaas")
        vraag2()

def vraag2():      
    print("\nvraag 2")    # vraag 2
    print("Je hebt je aan gekleed en je hebt een keuze ga je langer reizen en pak je de bus voor je deur of kies je de metro en de bus wat sneller is.")
    print("kies antwoord 1 of 2") 
    print("1=Bus voor de deur") # naar vraag 3
    print("2=Metro en bus") # naar vraag 4
    vraag=input("Type een cijfer >")
    if vraag == '1':
        print("Geweldig 40m in de bus\n")
        vraag3()
    if vraag == '2':
        print("Dat was snel\n")
        vraag4()

def vraag3():
    print("\nvraag 3")  # vraag 3
    print("Je bent op tijd op school maar nu hoor je net at je een studie dag hebt wat doe je?")
    print("kies antwoord 1 of 2")
    print("1=Naar werk gaan") # naar vraag 5
    print("2=Met vrienden naar buiten") # naar vraag 5
    vraag=input("Type een cijfer >")
    if vraag == '1':
        print("\nlekker zak centje verdienen")
        vraag5()
    if vraag == '2':
        print("\nLekker voetballen")
        vraag5()

def vraag4():
    print("Geweldig in een half uur op school")
    print("\nvraag 4")    # vraag 4
    print("\nJe komt te laat op school en mag de les niet in wat doe je?")
    print("kies antwoord 1 of 2") 
    print("1=Naar huis gaan") # naar vraag 5
    print("2=Wachten tot je van de docent naar huis mag") # naar vraag 5
    vraag=input("Type een cijfer >")
    if vraag == '1':
        print("Is dit wel een verstandige keuzen?")
        vraag5()
    if vraag == '2':
        print("Volgende keer niet te laat komen")
        vraag5()

def vraag5():
    print("\nvraag 5") # vraag 5
    print("Uiteindelijk ben je thuis en kan je kiezen huiswerk maken of gamen wat kies je?")
    print("kies antwoord 1 of 2")
    print("1=Huiswerk maken") # naar het einde
    print("2=Gamen") # naar het einde
    vraag=input("Type een cijfer >")
    if vraag == '1':
        print("Succes met huiswerk nerd")
    if vraag == '2':
        print("Game verslaafde")

vraag1()
