# Förklaring task2:

* börjar med att räkna antalet förekomster av varje siffra i strängen S, skulle kunna använt Counter här också men valde att göra det själv för att vara mer grundlig.

*  specialfall ifall alla siffror i S är 0, returnerar "0" direkt.

* middle är variabel för att hålla koll på vilken siffra som ska placeras i mitten av palindromet.

* loopar från 9 till 0 för att hitta den största siffran som har en udda frekvens. Siffran som ska placeras i mitten av palindromet måste ha udda frekvens eftersom för att använda så många siffror som möjligt i S.

* Kollar om siffran finns i S och om frekvensen är udda. Dekrementerar frekvensen med 1 för att markera att den har använts.
Eftersom vi itererar från 9 till 0 kan vi avbryta loopen vid första matchning. Detta skulle egentligen kunna göras mer effektivt genom att använda ett set av S och kolla om siffran finns i setet så att man inte behöver kolla siffror som inte finns i S.

* nu skapar vi första halvan av palindromet, itererar från 9 till 0. Om listan half är tom och siffran är 0 skippar vi den, eftersom vi inte kan ha ett palindrom med 0 i början.

* om siffran finns i S, räknar vi antalet par av siffror som kan skapas, delar med 2 för att få antalet par och använder floor för att få det hela antalet par. Lägger till paret av siffran så många gånger som antalet par i half-listan. Återigen, effektiverare att bara kolla siffror som finns i S.

* Om både half-listan och middle är tom, returnerar vi den största siffran i S, eftersom det är ett korrekt palindrom. Här kan vi också göra typ max(S) för att returnera det största talet i S, vilket är effektivare. 

* till sist skapar vi palindromet genom att konkatenera half-listan med middle och half-listan baklänges.

* returnerar palindromet.