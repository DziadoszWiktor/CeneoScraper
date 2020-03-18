# CeneoScraper
## Etap 1 - pobranie pojedynczej opinii 
- opinia: li.review-box
- identyfikator: li.review-box["data-entry-id"]
- autor: div.reviewer-name-line
- rekomendacja: div.product-review-summary > em
- liczba gwiazdek: span.review-score-count
- czy potwierdzona zakupem: div.product-review-pz
- data wystawienia: span.review-time > time["datetime"] - pierwsze wyystąpienie
- data zakupu: span.review-time > time["datetime"] - drugie wyystąpienie
- przydatna: button.vote-yes["data-total-vote"]
- nieprzydatna: button.vote-no["data-total-vote"]
- treść: p.product-review-body
- wady: div.cons-cell > ul
- zalety: div.pros-cell > ul
## Etap 2 - pobranie wszystkich opinii z pojedynczej strony
- zapis składotych opinii do złożonej struktury danych
## Etap 3 - pobranie wszystkich opinii o pojedynczym produkcie
- sposób przechodzenia po kolejnych stronach z opiniami
- eksport opinii do pliku (.csv lub .xlsx lub .json) 
