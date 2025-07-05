# 🎯 Projekt Python

Krótki opis

---

## 📦 Spis treści
- [Opis](#opis)
- [Instalacja](#instalacja)
- [Użycie](#użycie)
- [Struktura projektu](#struktura-projektu)
- [Technologie](#technologie)
- [Autor](#autor)
- [Licencja](#licencja)

---

## 📝 Opis

- funkcje,
- zastosowania,
- docelowi użytkownicy,
- etapy rozwoju.

---

## Deployment

Projekt jest wdrażany automatycznie za pomocą GitHub Actions.

Pipeline obejmuje:
- Automatyczne testy
- Budowanie aplikacji
- Sprawdzanie jakości kodu
- Symulowane wdrożenie

### Konfiguracja środowiska

Należy dodać do repozytorium w **Settings > Secrets** następujące sekrety:

- `TEST_SECRET` – przykładowy sekret używany podczas wdrożenia.

### Monitoring

Aplikacja udostępnia endpoint `/health`, który zwraca status 200 OK. Pipeline wykonuje prosty test tego endpointu po wdrożeniu.


## ⚙️ Instalacja

Instrukcja, jak uruchomić projekt lokalnie:

```bash
git clone https://github.com/Boroowka/repo86983.git
cd repo86983
python main.py

