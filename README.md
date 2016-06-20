# emi1

## Środowisko
Pierwsze co, to trzeba włączyć sobie środowisko.  
W tym katalogu wydaj komendę:  
`source ./bin/activate`  
po niej powinno pojawić się `(emi1)` na linii komend. Ja mam tak:  
`(emi1) killme@borgemi1 $ `  

## Biblioteki
Żeby napisać to ustrojstwo co tam chciałaś to nie potrzeba de facto nic z dodatkowych bibliotek. Ale zawsze warto byc w virtualenv, żeby wyrobić sobie dobry nawyk pracy z Pythonem.

## Wersja Pythona
Kod, który napiszesz odpalisz pod Python 3 i 2.7.

## Struktura pracy
Wszystko co robisz jako programista zamyka się w słowie "tłumaczenie".  
Programista tłumaczy pewien zbiór "chciejstw" określonych ludzi - w rzeczywistości nazywa się taki zbiór zamierzonych funkcji - wymaganiami (requirements, specification albo specs) - na kod.  
Kod to nie jest sam program, który robi zamierzoną funkcję, ale też testy, które potwierdzają, że program działa. My napiszemy tylko unit testy - UTki, ale w większych projektach robi się też testy wyższego poziomu, nvm.  
Musimy zacząć zawsze od zrozumienia co chcemy zrobić, czyli zająć się tym co powiedzieli do nas "ludzie od chciejstw".  

### Ludzie od chciejstw - co mamy zrobić

zadanie:   napisz prostą grę w kości.  
Zasady: 
- gra kończy się po 3 rundach  
- jedna runda składa się z dwóch ruchów: jeden ruch to rzut kośćmi przez gracza, drugi ruch to rzut kośćmi przez komputer
- każdy z graczy rzuca dwiema kostkami sześciościennymi (można wyrzycić od 1 do 6) 
- po każdym ruchu gracza należy zsumować wynik wylosowanych oczek z poprzednimi, tak, żeby na koniec gry (po 3 rundach) dostać sumę wszystkich wyrzuconych oczek 
- wygrywa ten, kto na koniec trzeciej rundy będzie miał więcej oczek 
- możliwy jest remis +(bonus dla ambitnych) 
- w przypadku remisu należy rozpocząć grę od nowa (ponownie rozegrać 3 rundy)

### Słowa słowa słowa
Słowa kluczowe:
* gra = 3 rundy  
* runda = dwa ruchy - gracza i komputera  
* ruch = Dodać wynik rzutu 1k6 [1k6 to kostka do gry](https://pl.wikipedia.org/wiki/Ko%C5%9B%C4%87_do_gry#Nazewnictwo) do sumy poprzednich rzutów gracza
* wygrywa ten kto ma większą sumę  
* remis = równa liczba oczek = gra jeszcze raz

### Po co nam to?
Teraz mamy zasady, które łatwo przedstawić w postaci kodu.

## najpierw UTki, potem kod!
Jak chcesz sobie poczytać to tutaj masz [artykuł](http://code.tutsplus.com/tutorials/beginning-test-driven-development-in-python--net-30137) co to.
W skrócie: Przed napisaniem funkcjonalności napiszemy najpierw test do niego. Test pokaże czy to co napisaliśmy działa.  
Plusy: Nie musimy bawić się ręcznie i sprawdzać czy wszystko działa, tylko piszemy automat, który to robi.  
Minusy: Więcej pisania.  
Więcej plusów: Powoduje że w kodzie będzie mniej bugów, latwiej sie go sprawdza, jest to standard w branży i dobra praktyka

## Komendy
Po zmianie w kodzie:  
`python tests.py`

Commitowanie:  
`git add __pliki__`
`git commit -m "opis zmiany"`
`git push`



