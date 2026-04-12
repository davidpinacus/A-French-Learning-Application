# 🇫🇷 Flash Card App (Python - Tkinter + Pandas)

An interactive flashcard application to learn French vocabulary using Python Tkinter.
Flip cards, track learned words, and improve your language skills efficiently.

---

## 🎯 Features

* 📖 Random French word generation
* 🔄 Auto flip to English after 3 seconds
* ✅ Mark words as learned
* ❌ Track unknown words
* 💾 Save progress using JSON files
* 🖥️ Clean card-style UI

---

## 📁 Project Structure

```id="l2x8qa"
.
├── main.py
├── data/
│   ├── french_words.csv
│   ├── learned_words.json
│   ├── unknown_words.json
├── images/
│   ├── card_front.png
│   ├── card_back.png
│   ├── right.png
│   ├── wrong.png
```

### Files Overview

* **main.py** → Core logic, UI, and flashcard system 
* **french_words.csv** → Word dataset (French → English)
* **learned_words.json** → Stores learned words
* **unknown_words.json** → Stores difficult words
* **images/** → UI assets for cards & buttons

---

## 🎮 How It Works

* A French word appears on the card
* After 3 seconds → flips to English
* Click:

  * ✅ → Mark as learned
  * ❌ → Mark as unknown
* Progress is saved automatically
