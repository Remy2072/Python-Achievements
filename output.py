Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2 + 2

4
>>> 3 * 10

30
>>> 100 - 10

90
>>> 25 / 5

5.0
>>> 10 / 3

3.3333333333333335
>>> 10 // 3

3
>>> print('Mijn naam is <Remy>')
Mijn naam is <Remy>
>>> naam = '<Remy>'
>>> print(naam)

<Remy>
>>> print(naam.upper())

<REMY>
>>> print(naam[0:2])

<R
>>> print(naam[::-1])

>ymeR<
>>> leeftijd = 17
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')

Hallo <Remy> ben je al 17 jaar?
>>> leeftijd = leeftijd + 1

>>> leeftijd
18
>>> leeftijd-=1

>>> leeftijd
17
>>> if leeftijd < 18:
    hoelang_tot18jaar = 18 - leeftijd
    print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')

    
Over 1 jaar wordt je 18
>>> elif leeftijd > 18:
    hoelang_al18jaar = leeftijd - 18
    print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
    
SyntaxError: invalid syntax
>>> if leeftijd < 18:
    hoelang_tot18jaar = 18 - leeftijd
    print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
    elif leeftijd > 18:
    hoelang_al18jaar = leeftijd - 18
    print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')

SyntaxError: invalid syntax
>>> if leeftijd < 18:
    hoelang_tot18jaar = 18 - leeftijd
    print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
elif leeftijd > 18:
    hoelang_al18jaar = leeftijd - 18
    print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
else:
    print('Je bent precies ' + str(leeftijd) + ' jaar')

Over 1 jaar wordt je 18
>>> from random import randint
>>> randint(0,1000)

872
>>> willekeurig_getal = randint(0,1000)

>>> willekeurig_getal
36
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))

Willekeurig getal tussen 0 en 1000: 36
>>> from datetime import datetime

>>> datum = datetime.now()

>>> print(datum)

2020-09-09 13:02:44.854066
>>> datum.strftime('%A %d %B %Y')

'Wednesday 09 September 2020'
>>> import locale

>>> locale.setlocale(locale.LC_TIME, 'nl_NL')

'nl_NL'
>>> datum.strftime('%A %d %B %Y')

'woensdag 09 september 2020'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')

'it_IT'
>>> datum.strftime('%A %d %B %Y')

'Mercoledì 09 Settembre 2020'
>>> 