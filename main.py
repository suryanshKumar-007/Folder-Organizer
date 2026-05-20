import os
import shutil
from pathlib import Path


CATEGORIES = {
    "Images":     [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".ico"],
    "Videos":     [".mp4", ".mkv", ".mov", ".avi", ".wmv", ".flv", ".webm"],
    "Audio":      [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Documents":  [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".odt"],
    "Archives":   [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
    "Code":       [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".ts", ".json", ".xml"],
    "Executables":[".exe", ".msi", ".dmg", ".pkg", ".deb", ".apk"],
    "Others":     []  
}

def get_category(extension: str) -> str:
    """File extension se category dhundho"""
    ext = extension.lower()
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category
    return "Others"

def organize_folder(folder_path: str, dry_run: bool = False):
    """
    folder_path: jis folder ko organize karna hai
    dry_run: True = sirf preview dikhao, actually move mat karo
    """
    folder = Path(folder_path)
    
    if not folder.exists():
        print(f"❌ Folder nahi mila: {folder_path}")
        return
    
    files = [f for f in folder.iterdir() if f.is_file()]
    
    if not files:
        print("📂 Folder already empty hai!")
        return
    
    print(f"\n{'='*50}")
    print(f"📁 Organizer: {folder_path}")
    print(f"{'Dry Run Mode' if dry_run else 'Live Mode'} | {len(files)} files mili")
    print(f"{'='*50}\n")
    
    moved = 0
    skipped = 0
    
    for file in files:
        ext = file.suffix
        category = get_category(ext)
        dest_folder = folder / category
        dest_file = dest_folder / file.name
        
        # Agar same name ka file already exist kare
        if dest_file.exists():
            base = file.stem
            counter = 1
            while dest_file.exists():
                dest_file = dest_folder / f"{base}_{counter}{ext}"
                counter += 1
        
        print(f"  {'[PREVIEW]' if dry_run else '[MOVING] '} {file.name}")
        print(f"           → {category}/{dest_file.name}")
        
        if not dry_run:
            dest_folder.mkdir(exist_ok=True)
            shutil.move(str(file), str(dest_file))
        
        moved += 1
    
    print(f"\n✅ Done! {moved} files {'preview dikhe' if dry_run else 'move hue'}, {skipped} skip hue.\n")

def undo_organize(folder_path: str):
    """Sabhi category folders se files wapas root mein le aao"""
    folder = Path(folder_path)
    print(f"\n🔄 Undo kar raha hoon: {folder_path}\n")
    
    for category in CATEGORIES:
        cat_folder = folder / category
        if cat_folder.exists():
            for file in cat_folder.iterdir():
                if file.is_file():
                    dest = folder / file.name
                    if not dest.exists():
                        shutil.move(str(file), str(dest))
                        print(f"  ↩️  {file.name} wapas aaya")
            # Khali folder hatao
            if not any(cat_folder.iterdir()):
                cat_folder.rmdir()
    
    print("\n✅ Undo complete!\n")


# ─── Main Program ────────────────────────────────────────────
if __name__ == "__main__":
    import sys
    
    # Default: user ki Downloads folder
    home = Path.home()
    downloads = str(home / "Downloads")
    
    print("🗂️  Smart Downloads Folder Organizer")
    print("--------------------------------------")
    print(f"Default folder: {downloads}")
    
    folder = input("\nKis folder ko organize karna hai? (Enter = Downloads): ").strip()
    if not folder:
        folder = downloads
    
    print("\nKya karna chahte ho?")
    print("  1. Dry Run (sirf preview dekho)")
    print("  2. Organize karo (actually files move karo)")
    print("  3. Undo (sab wapas original jagah)")
    
    choice = input("\nOption chunno (1/2/3): ").strip()
    
    if choice == "1":
        organize_folder(folder, dry_run=True)
    elif choice == "2":
        confirm = input("⚠️  Files actually move honge. Pakka? (yes/no): ").strip().lower()
        if confirm == "yes":
            organize_folder(folder, dry_run=False)
        else:
            print("❌ Cancel kar diya.")
    elif choice == "3":
        undo_organize(folder)
    else:
        print("❌ Galat option!")