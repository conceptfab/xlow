# Projekt Testowy Railway

To jest prosta aplikacja w Pythonie (FastAPI) przygotowana do przetestowania hostingu na [Railway.app](https://railway.app/).

## Struktura

- `main.py`: Kod aplikacji (FastAPI).
- `static/`: Pliki interfejsu (HTML/CSS).
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

1. Miej kod w repozytorium GitHub.
2. W panelu Railway stwórz projekt z repozytorium ("Deploy from GitHub repo").

## Jak aktualizować?

Skoro połączyłeś Railway z GitHubem, aktualizacja odbywa się przez wysłanie zmian do repozytorium:

1. Zapisz zmiany.
2. Wyślij je na GitHuba:
   ```bash
   git add .
   git commit -m "Nowy interfejs UI"
   git push
   ```
3. Railway automatycznie wykryje nowy commit i rozpocznie budowanie nowej wersji (Deploy).
