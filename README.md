# Projekt Testowy Railway

To jest prosta aplikacja w Pythonie (FastAPI) przygotowana do przetestowania hostingu na [Railway.app](https://railway.app/).

## Struktura

- `main.py`: Kod aplikacji.
- `requirements.txt`: Lista zależności.
- `Procfile`: Instrukcja startowa dla Railway.

## Uruchomienie lokalne

1. Zainstaluj zależności:
   ```bash
   pip install -r requirements.txt
   ```
2. Uruchom aplikację:
   ```bash
   python main.py
   ```
3. Otwórz w przeglądarce: `http://localhost:8000`

## Wdrożenie na Railway

1. Wrzuć ten kod na GitHub.
2. W panelu Railway wybierz "New Project" -> "Deploy from GitHub repo".
3. Wybierz to repozytorium.
4. Railway automatycznie wykryje Pythona i plik `Procfile`.
5. Po chwili aplikacja będzie dostępna pod wygenerowaną domeną.
