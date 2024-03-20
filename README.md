[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/PMYfDUok)

# itinf22_python_final

# FoodExpress

FoodExpress är en applikation där man kan beställa mat.

Kör main.py

När man startar applikationen möts man av en login-skärm där man ombeds att berätta vem man är, antingen med namn ELLER kundnummer, samt frågar efter lösenord.

Här finns några olika inlogg man kan använda:

Kundnummer | Användarnamn | Lösenord (Användarnamn = lösenord för enkelhetens skull))

- 0|admin|admin (logga in med denna för att kunna lista alla ordrar och "största kunden", för VG-kriterierna)
- 1|coop|coop
- 2|ica|ica
- 3|robert|robert

Om inloggningen lyckades så kommer man vidare till huvudmenyn.

Den ser ut så här:

   ------- Menu -------

1. Assortment & Prices
2. Show current cart
3. Add to cart
4. Add random item to cart
5. Remove from cart
6. Checkout # add timestamp, save to file, empty cart
7. Order history (Sorted after order value)
8. x
9. Show customer information (Logged in as Admin)
   q. Log out
   a. Admin menu

Beskrivning av menyn:

1. Assortment & Prices
   Lista sortimentet, dvs alla varor och priser.
2. Show current cart
   Visar allt som finns i din korg just nu.
3. Add to cart
   Öppnar en ny meny där man kan lägga till varor i varukorgen.
   Man kan antingen skriva varans artikelnummer (item number) eller varans namn (tex. Bread).
   I nästa steg får man välja hur många som ska läggas till.
   Det finns även lite andra funktioner här:
   List, LS, L: listar sortimentet.
   Cart, C: listar din nuvarande varukorg
   Random, R: lägger till en slumpmässig vara i korgen
   Quit, Q, 0: Avbryter och går tillbaka till huvudmenyn.
4. Add random item to cart
   Lägger till en slumpmässig vara i varukorgen.
5. Remove from cart
   Öppnar en ny meny där man kan ta bort varor från varukorgen.
   Man kan antingen skriva varans artikelnummer (item number) eller varans namn (tex. Bread)
   I nästa steg får man välja hur många som ska tas bort från varukorgen.
   Det finns även lite andra funktioner här:
   Empty, E: tömmer hela korgen
   Quit, Q: Avrbryter och går tillbaka till huvudmenyn.
6. Checkout
   Öppnar en ny meny där man kan checka ut sin varukorg när man är redo att slutföra beställningen.
   Din nuvarande varukorg listas och du blir frågad att bekräfta beställningen med ditt lösenord. Om du bekräftat ditt lösenord så sparas ordern till orderhistoriken och din korg töms. Skriv Q / Quit för att avbryta och gå tillbaka till huvudmenyn.
7. Customer order history
   Listar den inloggade kundens orderhistorik, sorterat efter största order. (Vill man se alla kunders ordrar så måste man logga in som admin, mer info nedan)
8. x
   Gör ingenting, för att fylla ut så att alla siffror används.
   (Om du är inloggad som admin så kan 8:an användas för att öppna adminmenyn, men det "officiella" sättet att öppna den menyn ser du nedan. Bara bonus.)
9. Show customer information (Logged in as {current_user})
   Listar den inloggade kundens kundinformation, dvs kundnummer, kundnamn samt lösenord.

   q. Log out

   Stänger programmet.

   a. Admin menu

   Detta alternativ visas bara när man är inloggad som admin.

   Öppnar en ny meny med tre alternativ:

   1. List biggest spenders
      Skriver ut en lista som visar vilka kunder som spenderat mest i butiken.
   2. List all orders (Sorted after total order value)
      Printar en lista med alla ordrar, sorterat efter största order.
   3. q. Quit to main menu
      Avbryter och återgår till huvudmenyn

En typisk beställning går till så här:

Logga in med kundnummer och lösenord. (Tex. admin|admin eller robert|robert)

Kolla sortimentet (1)

Lägg till några varor i din varukorg (3)

Lista din varukorg (2)

Ta bort några varor från din varukorg (4)

Checka ut din varukorg (6)

Kolla din orderhistorik (7)

Logga ut när du är färdig (q)

## Betygskriterier (och checklista)

Jag listar här beskrivningen och betygskriterierna för uppgiften samt hur de uppfylls.

I denna uppgift ska du skriva ett program som hanterar beställningar av matvaror.

Krav G:

Du kan ladda in varor från en fil eller databas (minst 10 varor) - CHECK, laddar varor items.json

Du kan lista / visa alla varor i sortimentet - Tryck 2 i huvudmenyn

Du kan lägga till en vara till varukorgen -Tryck 3 i huvudmenyn, välj någonting att lägga till

Du kan ta bort en vara från varukorgen - Tryck 5 i huvudmenyn, välj någonting att ta bort

Du kan slutföra din beställning, så att varukorgen töms - Tryck 6 i huvudmenyn, bekräfta beställningen med ditt lösenord

Dina beställningar sparas till en fil eller databas - CHECK, sparas till orders.json

Krav VG:

Du använder en klass för varukorgen, Cart - CHECK, har även en klass för Customers

Du kan lägga en slumpvis vara till varukorgen - Tryck 4 i huvudmenyn. Kan även göras under 3 (Add to cart) genom att där skriva random.

Du kan lista / visa historiska beställningar sorterat på totalbelopp - Tryck 7 i huvudmenyn för att lista den nuvarande kundens orderhistorik, sorterat efter totalbelopp. För att se alla kunders ordrar, logga in som admin, tryck A i huvudmenyn och välj sedan alternativ 2 i adminmenyn.

Du kan lista / visa kunder sorterat på totalt belopp av alla deras köp - Om du är inloggad som admin, välj A i huvudmenyn och välj sedan alternativ 1 i adminmenyn.

(Notering: jag la dessa två VG-funktioner i adminmenyn för "kundsekretessens" skull, så att inte kunder ska kunna kolla andra kunders beställningar eller se våra största kunder. Jag har tekniskt sett uppnått dessa kriterier, men "formateringen"/presentationen av datan är inte så snygg.)

Du kodar välstrukturerad och läsbar kod - CHECK ?

(Notering: Jag lyckades tyvärr inte att få till att importera klasserna och funktionerna från filer för att "gömma bort dessa" från main.py.. Trodde att jag kunde göra detta enkelt som sista steg när allt annat var färdigt, men jag fick tyvärr errors att klassernas variabler var undefined och jag lyckades inte få till det..

Försöket till detta ligger i mappen attempt_to_import_classes_and_functions_to_main

Koden jag skrev i början av veckan var väldigt välstrukturerad, men tyvärr tog saker längre tid än vad jag hade hoppats på så mot slutet blev det lite sämre.
Jag förstår vad som behöver göras och hur det ska göras, tyvärr så räckte inte riktigt tiden till för mig för att göra det 100% bra.
Hoppas du ser detta)

### För Godkänd (G) krävs att studenten får godkänt på följande kriterier

- Kunna installera, sätta upp och använda sig av en modern IDE för Pythonprogrammering
- Förstå vad objektorienterad programmering innebär och skillnaden mellan olika programspråk
- Kunna lösa enklare programmeringsuppgifter med hjälp av Python på egen hand
  innehållande till exempel variabler, arrayer, loopar, villkorskonstruktioner, klasser,objekt och metoder
- Kunna använda sig av en interaktiv debugger för felsökning och kan versionshantera kod

### För Väl Godkänd (VG) krävs att studenten får godkänt på samtliga G – respektive VG-kriterier

- Visa god förmåga i att lösa programmeringsuppgifter med hjälp av Python på egen hand
- Visa att man kan koda välstrukturerat och läsbar kod

### För G krävs det

* Koden gör åtminstone det som beskrivs i uppgiften
* Koden går att köra
* Ni beskriver i en README.md hur programmet körs
* Du kan i seminariegruppen förklara hur din lösning fungerar

### För VG är det extra noga med

* Ren och tydlig kod
* Bra variabelnamn enligt Python konventioner (t.ex. pep8)
* Korta tydliga metoder som gör en isolerad sak.

## Instruktioner

### Regler

* Slutuppgiften är enskild
* Det är ok att fråga lärare och varandra generella frågor.
* Ni ska skriva er egen kod, om ni använder er av kodbitar från webben t.ex. Stack Overflow så måste ni ange källa.
* Ni ansvarar för att Betygskriterierna är uppfyllda, kolla er kursplan.

### Inlämning

* Deadline Onsdag 26/4 09:00
* Dubbelkolla att programmet fungerar innan redovisning
* Kontrollera så att er dator fungerar med hdmi kontakt i klassrummet
* Om ni har missat något finns en extra chans på seminariet att visa vad ni kan, var förberedda.
* Seminariet äger rum i små grupper Onsdag 26/4. Det är obligatoriskt att redovisa sin lösning.

### Vilken uppgift får jag?

* Det lottas vilken uppgift ni får
* Ni kan under dagen Onsdag 19 april byta uppgift mellan varandra i klassen om ni meddelar mig innan dagen är slut.
