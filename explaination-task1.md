Förklaring task1:

* Börjar med att räkna antalet förekomster av varje bokstav i katalogen, fuskar lite och använder collections.Counter men kan även iterera över strängen själv och skapa en dictionary som åstadkommer samma resultat.

* max_copies är variabel för att hålla koll på det maximala antalet kopior som kan skapas för ett visst namn.

* itererar över varje namn i listan L och räknar antalet kopior som kan skapas för det namnet.

* återigen, fuskar och använder collections.Counter för att räkna antalet förekomster av varje bokstav i namnet.

* lokal variabel copies är för att hålla koll på det maximala antalet kopior som kan skapas för ett visst namn.

* itererar över dictionary name_counter 

* kollar om nuvarande bokstav finns i katalogen, om inte sätts copies till 0 och avslutar loopen eftersom vi inte kan skapa några kopior.

* räknar hur många kopior som kan skapas för det nuvarande namnet genom att dela antalet förekomster av bokstaven i katalogen med antalet förekomster av bokstaven i namnet. 

* uppdaterar lokala variabeln copies med det minimala antalet kopior som kan skapas för det nuvarande namnet, copies sätts initialt till oändligheten. Detta görs eftersom antalet kopior är begränsat av det minsta antalet kopior som kan skapas för en bokstav.

* om antalet kopior för det nuvarande namnet är högre än max_copies sätts max_copies till det nya antalet kopior.

* returnerar max_copies