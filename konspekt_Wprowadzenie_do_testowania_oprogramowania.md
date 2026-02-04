# Wprowadzenie do testowania oprogramowania — konspekt zajęć

## Wstęp

Konspekt ten przeznaczony jest na jedno lub dwugodzinne zajęcia wprowadzające dla studentów kierunków technicznych. Celem zajęć jest przedstawienie podstaw testowania oprogramowania, jego roli w procesie wytwarzania oraz zaprezentowanie najważniejszych pojęć i podziałów stosowanych przez praktyków i standard ISTQB.

## Cele zajęć
- Poznać podstawowe terminy i cele testowania.
- Zrozumieć różne rodzaje i poziomy testów.
- Zapoznać się z podziałami i technikami rekomendowanymi przez ISTQB.
- Przećwiczyć krótkie przykłady testów (lab/ćwiczenia).

## Plan zajęć (proponowany)
- 0–10 min: Wstęp, cele i znaczenie testowania.
- 10–35 min: Poziomy testów — unit, integration, system, acceptance.
- 35–55 min: Typy testów — funkcjonalne, niefunkcjonalne, regresyjne.
- 55–75 min: Podziały ISTQB: techniki testowe i proces testowy.
- 75–90 min: Ćwiczenie praktyczne + krótkie podsumowanie.


## Historia nr 1 Ariane 5
Ariane 5: 64-bit vs 16-bit, czyli rakieta za pół miliarda 💥🚀

W 1996 roku Europejska Agencja Kosmiczna odpaliła Ariane 5. Rakieta miała wynieść satelity naukowe, koszt całego przedsięwzięcia to ok. 500 milionów dolarów.

Co poszło nie tak?
W oprogramowaniu systemu inercyjnego (napisanego w Ada) była linijka, która:
konwertowała 64-bitową liczbę zmiennoprzecinkową na 16-bitową liczbę całkowitą
bez sprawdzenia zakresu (bo „w Ariane 4 to zawsze działało”)

Ariane 5 miała inne parametry lotu → wartość wyszła poza zakres → exception → system nawigacji padł.
Efekt domina:
Główny komputer nawigacyjny się wyłączył
System zapasowy… miał ten sam błąd
Rakieta dostała losowe dane o położeniu
Po 37 sekundach system bezpieczeństwa uznał, że rakieta oszalała
Autodestrukcja

💸 Koszt naprawy błędu: brak — bo nie dało się naprawić. Rakieta przestała istnieć. 500 milionów USE do kosza.

Dlaczego to jest tak dobry przykład „produkcyjnego” koszmaru?
kod był przetestowany (ale w starym kontekście)
błąd był znany i udokumentowany jako „nieistotny”
system zapasowy nie był niezależny
jedna linijka kodu > pół miliarda 

## Historia nr 2 Toyota
Toyota: „niekontrolowane przyspieszanie” i miliardy strat 🚗⚠️

Lata 2009–2011. Toyota musi wycofać ~9 milionów samochodów na całym świecie. Oficjalnie: problem z niekontrolowanym przyspieszaniem.
Koszt całościowy:
- akcje serwisowe
- pozwy zbiorowe
- kary regulacyjne

👉 ~5–6 miliardów USD

Co było w sofcie?
System ETCS (Electronic Throttle Control System):
- embedded C
- brak systemu operacyjnego (bare metal / prosty RTOS)
- ~280 000 linii kodu
- jeden task robił „wszystko”
- Kod miał m.in.:
    - globalne zmienne
    - brak izolacji tasków
    - brak stack protection
    - brak watchdogów na logikę

„Ten jeden if”

Uproszczony schemat:
```c++
if (pedal_position > threshold)
    throttle_open();
```

Ale:
- był race condition
- nadpisanie pamięci (stack overflow w innym tasku)
- flaga bezpieczeństwa mogła zostać losowo skasowana

Efekt:
- system „myślał”, że pedał gazu jest wciśnięty
- brak fail-safe
- brake override nie zawsze działał

Dlaczego naprawa była koszmarem?
- Nie dało się odtworzyć błędu
- losowy
- zależny od timingów
- Auta były już u klientów
- Nie było OTA
- Regulatory (NHTSA) wymagali dowodu, nie przypuszczeń

Toyota:
przepisała fragmenty systemu
dodała watchdogi i redundancję
fizycznie wzywała auta do serwisów

Najbardziej bolesna lekcja

***„Jeśli nie potrafisz udowodnić, że twój system jest bezpieczny,
to nie jest bezpieczny — nawet jeśli działał latami.”***

I jeszcze:

*** Testy nie udowadniają że system działa ... Testy udowadniają że system nie działa. ***

## Jak brak testów spowalnia software developement.

### 1. Brak szybkiego feedbacku
Bez testów błąd wychodzi późno (QA / produkcja), a nie po minutach.
Im później wykryty błąd, tym droższy i wolniejszy fix.

---

### 2. Manualna regresja zamiast automatu
Każda zmiana wymaga ręcznego sprawdzania.
Czas weryfikacji rośnie wraz z rozmiarem systemu.

---

### 3. Strach przed zmianami
Brak testów = brak siatki bezpieczeństwa.
Kod się omija, kopiuje i dokleja zamiast poprawiać.

---

### 4. Debugowanie zjada czas
Zamiast pisać feature’y:
- szukanie repro
- debugowanie
- hotfixy

Więcej gaszenia pożarów niż rozwoju.

---

### 5. Velocity dąży do zera
Na początku szybciej.
Z czasem każda zmiana trwa dłużej i niesie większe ryzyko.

---

### Podsumowanie
**Brak testów nie spowalnia od razu —  
on systematycznie zabiera przyszłą prędkość zespołu.**

---

## Dlaczego testowanie oprogramowania jest ważne
- Zapewnienie jakości: wykrywanie defektów przed wydaniem produktu.
- Redukcja kosztów: naprawa błędów wcześnie jest tańsza niż po wdrożeniu.
- Bezpieczeństwo i niezawodność: krytyczne systemy muszą działać poprawnie.
- Spełnianie wymogów prawnych/branżowych.
- ***Redukowanie strachu przed zmianami w sofcie.***

## Podziały i terminologia ISTQB (International System Testing Qualification Board)

- Poziomy w kontekście ISTQB:
  - Foundation: podstawowa terminologia i techniki testowe.
  - Advanced/Expert: głębsze aspekty zarządzania testami, projektowania testów i technik specyficznych.

- Typowe kategorie według ISTQB:
  - Poziomy testów: unit, integration, system, acceptance (jak powyżej).
  - Testy funkcjonalne vs niefunkcjonalne.
  - Techniki projektowania testów:
    - Black-box (techniki oparte na wymaganiach): ekwiwalencja, analiza wartości brzegowych, techniki tabel decyzyjnych.
    - White-box (strukturalne): pokrycie instrukcji, pokrycie ścieżek, testy jednostkowe.
    - Experience-based: testy eksploracyjne, oparte na wiedzy eksperckiej.

- Proces testowy (wg ISTQB) — kluczowe etapy:
  1. Planowanie i kontrola testów.
  2. Analiza i projektowanie testów.
  3. Implementacja i wykonanie testów.
  4. Ocena kryteriów zakończenia i raportowanie.
  5. Zamykanie testów i lekcje wyniesione.

## Metody i narzędzia — przykłady
- Automatyzacja testów: frameworki (np. JUnit, pytest, Selenium) — kiedy się opłaca.
- Narzędzia do zarządzania testami i śledzenia defektów: JIRA, TestRail.
- CI/CD: integracja testów w potoku (GitHub Actions, GitLab CI, Jenkins).

## Ćwiczenia praktyczne (propozycje)
- Proste zadanie: napisać 3 testy jednostkowe dla małej funkcji (np. walidacja danych).
- Ćwiczenie integracyjne: sprawdzić współpracę dwóch komponentów (mocki/stuby).
- Krótkie testy eksploracyjne: znaleźć 3 błędy w przykładowej aplikacji webowej.

## Materiały i literatura
- Podręcznik ISTQB Foundation Level — sylabus i skróty pojęć.
- Artykuły i blogi o testowaniu: Martin Fowler, Ministry of Testing.
- Dokumentacja narzędzi: pytest, JUnit, Selenium.

## Ocena i ewaluacja
- Krótkie zadanie praktyczne oceniane na podstawie poprawności i pokrycia przypadków testowych.
- Dyskusja/quiz: pytania sprawdzające zrozumienie istotnych pojęć (poziomy testów, techniki projektowania).



