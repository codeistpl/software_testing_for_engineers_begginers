# Błędy w Aplikacji Task Manager

Dokument ten zawiera listę celowo wprowadzonych błędów do aplikacji Task Manager w celu testowania manualnego.

## Błąd 1: Pole Priorytetu Się Nie Resetuje
**Lokalizacja:** `gui/main.py` - metoda `add_task()`

**Opis:** Po dodaniu nowego zadania, pole listy rozwijanej priorytetu nie resetuje się do wartości domyślnej "3". Zachowuje wartość, która była używana do utworzenia poprzedniego zadania.

**Jak go Odkryć:**
1. Otwórz aplikację
2. Wpisz tytuł i wybierz priorytet "1"
3. Kliknij "Add"
4. Lista rozwijana priorytetu nadal pokazuje "1" zamiast powrócić do "3"

**Wpływ:** Zamieszanie użytkownika - niejasne, jaki priorytet będzie przypisany do następnego zadania

---

## Błąd 2: Przełączenie Zrobione Nie Aktualizuje Interfejsu
**Lokalizacja:** `gui/main.py` - metoda `toggle_done()`

**Opis:** Gdy klikniesz "Toggle Done" na zadaniu, stan wewnętrzny jest aktualizowany, ale wyświetlanie tabeli nie jest odświeżane. Wizualny wskaźnik (zielone podświetlenie) nie pojawi się, dopóki lista nie zostanie ręcznie odświeżona w inny sposób.

**Jak go Odkryć:**
1. Otwórz aplikację
2. Wybierz zadanie z listy
3. Kliknij "Toggle Done"
4. Tabela nadal pokazuje zadanie bez zielonego podświetlenia (stan ukończenia)

**Wpływ:** Użytkownik nie widzi, czy przełączenie się powiodło

---

## Błąd 3: Usunięcie Się Zawiesza Bez Zaznaczenia
**Lokalizacja:** `gui/main.py` - metoda `delete_task()`

**Opis:** Jeśli użytkownik kliknie "Delete" bez zaznaczenia zadania, aplikacja się zawiesza, ponieważ `selected_id()` zwraca `None`, które jest następnie przekazywane do `remove()` powodując TypeError.

**Jak go Odkryć:**
1. Otwórz aplikację
2. Kliknij "Delete" bez zaznaczenia żadnego zadania
3. Aplikacja się zawiesza z TypeError

**Wpływ:** Niestabilność aplikacji i kiepskie doświadczenie użytkownika

---

## Błąd 4: Tytuł i Opis Zamienione w Tabeli
**Lokalizacja:** `gui/main.py` - metoda `refresh_list()`

**Opis:** Wartości wstawiane do kolumn tabeli są zamienione - tytuł pojawia się w kolumnie opisu i vice versa.

**Jak go Odkryć:**
1. Otwórz aplikację
2. Dodaj zadanie z tytułem "Moje Zadanie" i opisem "Mój Opis"
3. Spójrz na tabelę - "Mój Opis" pojawia się w kolumnie Tytuł, a "Moje Zadanie" w kolumnie Opis

**Wpływ:** Zamieszanie z danymi - użytkownicy widzą nieprawidłowe informacje w interfejsie

---

## Błąd 5: Brak Wiadomości Potwierdzenia Zapisania
**Lokalizacja:** `gui/main.py` - metoda `save()`

**Opis:** Gdy klikniesz "Save", zadania są zapisywane do magazynu, ale użytkownikowi nie jest wyświetlana żadna wiadomość potwierdzająca. Użytkownik nie ma żadnego sprzężenia zwrotnego, że zapis był pomyślny.

**Jak go Odkryć:**
1. Otwórz aplikację
2. Dodaj zadanie
3. Kliknij "Save"
4. Nie pojawia się żadna wiadomość potwierdzająca zapis

**Wpływ:** Niepewność użytkownika dotycząca tego, czy dane zostały zapisane

---

## Błąd 6: Nieprawidłowy Format Daty Zawiesza Aplikację
**Lokalizacja:** `app/model.py` - metoda `add_task()`

**Opis:** Jeśli użytkownik wpisze nieprawidłowy format daty w polu "Due Date" (coś innego niż YYYY-MM-DD), aplikacja zgłasza ValueError i zamyka się bez ostrzeżenia.

**Jak go Odkryć:**
1. Otwórz aplikację
2. Wpisz tytuł
3. Wpisz nieprawidłową datę taką jak "2025-13-45" lub "01/02/2025"
4. Kliknij "Add"
5. Aplikacja zamyka się natychmiast bez komunikatu o błędzie

**Wpływ:** Utrata danych i kiepskie doświadczenie użytkownika - aplikacja kończy się bez wyjaśnienia
