
# AI Developer Task - Oxido Recruitment

## Opis projektu
To repozytorium zawiera rozwiązanie zadania rekrutacyjnego na stanowisko Junior AI Developer dla firmy Oxido. Aplikacja została stworzona w Pythonie i korzysta z API OpenAI do przetworzenia artykułu na strukturalny kod HTML, zgodnie ze specyfikacją zadania.

## Funkcjonalności aplikacji
1. **Integracja z API OpenAI** – Aplikacja łączy się z modelem GPT-4, aby przetworzyć dostarczony artykuł na kod HTML.
2. **Generowanie HTML** – Wygenerowany kod HTML zawiera odpowiednie tagi strukturalne (`<h1>`, `<p>`, `<img>` itp.) oraz miejsca na obrazy, oznaczone tagami `<img src="image_placeholder.jpg" alt="opis grafiki">`.
3. **Zapis do pliku** – Wygenerowany kod HTML zapisywany jest w pliku `artykul.html`.
4. **Dodatkowy szablon do wizualizacji** – Szablon HTML (`szablon.html`) jest gotowy do wklejenia treści artykułu, a plik `podglad.html` zawiera pełny podgląd artykułu.

## Struktura plików
```
AI-Developer-Task/
├── .env                  # Plik środowiskowy zawierający klucz API 
├── main.py               # Główny plik z kodem aplikacji, który łączy się z API OpenAI
├── article.txt           # Plik z tekstem artykułu, który będzie przetwarzany
├── artykul.html          # Wygenerowany plik HTML z przetworzoną treścią artykułu
├── szablon.html          # (Opcjonalny) pusty szablon HTML do wizualizacji treści artykułu
├── podglad.html          # (Opcjonalny) pełny podgląd artykułu z osadzonym kodem artykułu
├── test/                 # Folder zawierający przykłady artykułów wygenerowanych przez różne modele OpenAI
│   ├── artykul_gpt-4-turbo.html
│   ├── artykul_gpt3.5-turbo.html
│   ├── artykul_gpt4o.html
│   └── artykul_gpt4.html
└── README.md             # Plik z opisem projektu i instrukcją uruchomienia

```

## Testy generacji HTML dla różnych modeli OpenAI
W folderze `test` znajdują się cztery pliki HTML wygenerowane przez różne modele OpenAI. Każdy z plików reprezentuje wynik przetworzenia artykułu przez inny model. Oto krótki opis różnic między modelami:

- **artykul_gpt-4-turbo.html** i **artykul_gpt4o.html**: Modele GPT-4-turbo oraz GPT-4o wygenerowały poprawny HTML, ale dodały dodatkowy znacznik ```html```, co było niezgodne ze specyfikacją. Kod HTML jest dobrze strukturyzowany, a prompty do generowania obrazków są konstruktywne i dokładne.

- **artykul_gpt3.5-turbo.html**: Model GPT-3.5-turbo okazał się najszybszy spośród przetestowanych modeli, jednak generowane przez niego opisy promptów dla obrazków były mniej konstruktywne i mało precyzyjne. Mimo to, struktura HTML była zgodna z oczekiwaniami.

- **artykul_gtp4.html**: Model GPT-4 generował dobrze zorganizowany kod HTML bez dodatkowych zbędnych znaczników. Wygenerowane prompty były szczegółowe i odpowiednie dla zamierzonego użycia, ale czas przetwarzania był dłuższy niż w przypadku GPT-3.5.

### Instrukcje do podglądu artykułu
1. Otwórz plik `podglad.html` w przeglądarce, aby zobaczyć pełny podgląd artykułu z osadzonym HTML-em.
2. Możesz również wkleić wygenerowany HTML do `szablon.html`, aby zobaczyć, jak wygląda w ramach szablonu.

## Dodatkowe informacje
- **Szablon HTML**: Plik `szablon.html` został przygotowany jako czysty szablon, który zawiera style i struktury pozwalające na wizualizację treści artykułu.
- **Podgląd HTML**: Plik `podglad.html` jest pełnym podglądem artykułu z wygenerowanym HTML-em wstawionym do struktury szablonu.
- **Do struktury plików należy dołączyć plik środowiskowy `.env` zawieierający klucz API w zmiennej `OPENAI_API_KEY`**
