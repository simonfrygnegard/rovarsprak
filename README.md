# Rövarspråk

Ni ska bygga en översättare från svenska till  [rövarspråk](https://sv.wikipedia.org/wiki/R%C3%B6varspr%C3%A5ket)  och tvärtom.

Börja med att forka projektet och under arbetet ska ni committa och pusha upp det färdiga programmet.

Innan ni börjar med koda, gör en lösning i psuedokod eller flödesschema.

Det finns färdigskrivna tester, för att testa funktionaliteten, skrivna i pytest. Använd requirements.txt för att installera dessa. För att det ska fungera måste ni skriva koden i `rovare.py` i avsedda funktionerna och returnera rätt svar.

pytest använder ni lättast från en terminal ```pytest -v``` där -v står för verbose. kör pytest i samma katalog som ni har program och testfilerna.

#### TIPS
Ni kan begränsa vilka tester som körs genom att fylla på med filnamnet, ex

```
pytest -v test_rovare.py
```
Ni kan begränsa ännu mer genom att lägga till -k, där -k står för keyword, ex för att endast köra tester innehållandet namnet translate i filen test_rövare.py

```
pytest -v -k "translate" test_rövare.py

```


**Happy hacking**

*glöm inte att comitta och pusha*
