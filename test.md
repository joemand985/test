Teorijski deo
---

Dati sto konciznije odgvore u formi prosto prosirenih recenica na svako od sledecih pitanja.

01. Sta je to JSON?
02. Sta je to XML?
Extensible Markap Lenguage, jezik za opisno obelezavanje teksta
03. Sta je to URL?
Uniform Resource Locator - adresa (referenca) nekog resursa na Internetu
04. Sta je to HTTP?
Hyper Text Transfer Protocol, protokol za prenos hiperteksta putem mreze
05. Sta je to RESTful API?
06. Koje HTTP metode imamo?
GET, POST, HEAD, PUT, DELETE, CONNECT, OPTIONS, TRACE, PATCH
07. Sta je to DNS?
Domain Name System 
08. Sta je to private IP?
Adresa rezervisana za unutrasnju upotrebu recimo u okviru LAN
09. Sta je to AJAX?
10. Sta je to TCP/IP?
Internet Protokol
11. Sta je to kes memorija?
12. Koja je razlika izmedju klase i objekta?

Backend
---

1. U `models.py` fajlu implementirati `Comment` model (klasu) u Python-u koja sadrzi atribute:
- `text`: sam komentar, i
- `date`: datum komentara u formatu `YYYY-MM-DD`
"Override"-ovati `__repr__` metod.

2. U `models.py` fajlu definisati `COMMENTS` varijablu koja sadrzi niz od 3 elementa koji su tipa `Comment`. 

3. U `app.py` fajlu napraviti Flask applikaciju koja ima `index` "view" funkciju koja handle-uje `/` route. Funkcija bi trebalo da vraca HTML string koji u `body`-ju sadrzi heading "Welcome!".

4. U `app.py` dodati `comments` "view" funkciju koja handle-uje `/comments` route. Funkcija bi trebalo da vraca HTML koji u `body`-ju sadrzi tabelu komentara. Koristiti Flask template.

5.  U `app.py` dodati `api_comments` "view" funkciju koja handle-uje `/api/v1.0/comments` route. Funkcija bi trebalo da vraca JSON reprezentaciju `COMMENTS` niza.

Frontend
---

U `home.html` fajlu imlementirati jednostavnu klijent aplikaciju kojom moze da testira prethodno implementirani API end point. Koristiti `form` i `iframe`.

Algoritmi
---

Napisati i JavaScript i Python funkciju koja predstavlja resenje sledeceg zadataka:

Write a program that prints the numbers from 1 to 100. But for multiples of three print `Fizz` instead of the number and for the multiples of five print `Buzz`. For numbers which are multiples of both three and five print `FizzBuzz`.

Uputstvo
---

Resenja i odgovore predati u okviru GitHub repozitorijuma.
Python:

def numbers():
  num = 1
  nums = 100
  while num <= nums:
    if num%3 == 0:
      if num%5 == 0:
        print 'FizzBuzz'
      else:
        print 'Fizz'
    elif num%5 == 0:
      print 'Buzz'
    else:
      print num
    num = int(num)
    num += 1

JavaScript:

function numbers(){
  num = 1;
  for (num; num<=100; num++){
    if((num%3 == 0) && (num%5 == 0)){
      console.log("FizzBuzz");
    } else if(num%3 == 0){
       console.log("Fizz");
    } else if(num%5 == 0){
      console.log("Buzz");
    } else {
      console.log(num)
    }
   
  }
}
