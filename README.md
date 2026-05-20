# 🗂️ Smart Downloads Folder Organizer

Ek simple Python tool jo automatically aapki files ko unke type ke hisaab se alag-alag folders mein organize karta hai.

---

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [File Categories](#file-categories)
- [How It Works](#how-it-works)
- [Example Output](#example-output)
- [Frontend UI](#frontend-ui)

---

## ✨ Features

- **Auto Categorization** — File extension dekh ke automatically sahi folder mein move karta hai
- **Dry Run Mode** — Pehle preview dekho, phir decide karo
- **Live Mode** — Actually files move karo
- **Undo Support** — Agar galti ho jaye toh sab wapas original jagah
- **Duplicate Handling** — Same naam ki files ko `_1`, `_2` se safely rename karta hai
- **Any Folder** — Sirf Downloads nahi, koi bhi folder organize kar sakte ho
- **Frontend UI** — Browser mein chalane wala HTML interface bhi available hai

---

## 📁 Project Structure

```
downloads-organizer/
│
├── organizer.py          # Main Python script
├── downloads_organizer.html  # Frontend UI (browser mein open karo)
└── README.md             # Ye file
```

---

## ⚙️ Requirements

- Python 3.6 ya usse upar
- Koi extra library install karne ki zaroorat nahi — sirf built-in modules use hote hain:
  - `os`
  - `shutil`
  - `pathlib`

---

## 🚀 Installation

**1. Repository clone karo ya file download karo:**

```bash
git clone https://github.com/yourname/downloads-organizer.git
cd downloads-organizer
```

**2. Ya seedha file download karo aur run karo:**

```bash
python organizer.py
```

Bas! Koi `pip install` nahi karna.

---

## 🖥️ Usage

### Python Script Chalao

```bash
python organizer.py
```

Program chalane ke baad ye puchega:

```
🗂️  Smart Downloads Folder Organizer
--------------------------------------
Default folder: C:/Users/YourName/Downloads

Kis folder ko organize karna hai? (Enter = Downloads): 

Kya karna chahte ho?
  1. Dry Run (sirf preview dekho)
  2. Organize karo (actually files move karo)
  3. Undo (sab wapas original jagah)

Option chunno (1/2/3):
```

### Option 1 — Dry Run (Safe Preview)

Koi bhi file move nahi hogi. Sirf dikhayega ki kaun si file kahan jayegi.

```
[PREVIEW]  photo.jpg       → Images/
[PREVIEW]  notes.pdf       → Documents/
[PREVIEW]  song.mp3        → Audio/
```

### Option 2 — Live Organize

Files actually move hongi. Confirm karna padega:

```
⚠️  Files actually move honge. Pakka? (yes/no): yes
```

### Option 3 — Undo

Sabhi category folders se files wapas root folder mein aa jayengi aur khali folders delete ho jayenge.

---

## 📂 File Categories

| Category | Extensions |
|---|---|
| 🖼️ Images | `.jpg` `.jpeg` `.png` `.gif` `.bmp` `.svg` `.webp` `.ico` |
| 🎬 Videos | `.mp4` `.mkv` `.mov` `.avi` `.wmv` `.flv` `.webm` |
| 🎵 Audio | `.mp3` `.wav` `.aac` `.flac` `.ogg` `.m4a` |
| 📄 Documents | `.pdf` `.doc` `.docx` `.xls` `.xlsx` `.ppt` `.pptx` `.txt` `.odt` |
| 📦 Archives | `.zip` `.rar` `.7z` `.tar` `.gz` `.bz2` |
| 💻 Code | `.py` `.js` `.html` `.css` `.java` `.cpp` `.c` `.ts` `.json` `.xml` |
| ⚙️ Executables | `.exe` `.msi` `.dmg` `.pkg` `.deb` `.apk` |
| 📎 Others | Baaki sab jo upar ki list mein nahi hain |

---

## 🔍 How It Works

**Step 1** — Folder ke andar ki sabhi files dhundho

**Step 2** — Har file ka extension nikalo (jaise `.jpg`, `.mp3`)

**Step 3** — `get_category()` function extension match karke category return karta hai

**Step 4** — Category ke naam ka folder banao (agar exist nahi karta)

**Step 5** — File us folder mein move karo

**Step 6** — Agar same naam ki file already exist karti hai toh `filename_1.ext`, `filename_2.ext` etc. se rename karo

```
Downloads/
├── photo.jpg          →   Downloads/Images/photo.jpg
├── notes.pdf          →   Downloads/Documents/notes.pdf
├── song.mp3           →   Downloads/Audio/song.mp3
├── app.exe            →   Downloads/Executables/app.exe
└── project.zip        →   Downloads/Archives/project.zip
```

---

## 📊 Example Output

```
==================================================
📁 Organizer: C:/Users/Rahul/Downloads
Live Mode | 5 files mili
==================================================

  [MOVING]  photo.jpg → Images/
  [MOVING]  resume.pdf → Documents/
  [MOVING]  song.mp3 → Audio/
  [MOVING]  setup.exe → Executables/
  [MOVING]  archive.zip → Archives/

✅ Done! 5 files move hue, 0 skip hue.
```

---

## 🌐 Frontend UI

Browser mein chalane ke liye `downloads_organizer.html` file open karo.

**Features:**
- Drag & Drop se files preview karo
- Teen modes: Dry Run, Live, Undo
- Real-time log aur progress bar
- Color-coded category badges

> **Note:** HTML frontend sirf preview ke liye hai. Actually files move karne ke liye Python script use karo.

---

## 🛠️ Customize Karna

`organizer.py` mein `CATEGORIES` dictionary edit karke apni khud ki categories add kar sakte ho:

```python
CATEGORIES = {
    "Images": [".jpg", ".png", ...],
    "MyCustomFolder": [".xyz", ".abc"],  # ← apni category add karo
    ...
}
```

---

## 📄 License

MIT License — Free to use, modify, and distribute.
