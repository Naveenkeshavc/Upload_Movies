import os
import re
from googletrans import Translator

def process_file_name(filename):
    # Separate extension and base name
    name, ext = os.path.splitext(filename)
    
    # Regex to find and extract language tags (Kan, Eng, Hin, Tel, Tam, Mal)
    pattern = r'\b(Kan|Eng|Hin|Tel|Tam|Mal)\b'
    
    # Search for the tag
    match = re.search(pattern, name, flags=re.IGNORECASE)
    tag = match.group(0) if match else ""
    
    # Remove the tag from the base name to prepare for translation
    cleaned_name = re.sub(pattern, '', name, flags=re.IGNORECASE).strip()
    
    return cleaned_name, tag, ext

def rename_files_to_kannada(folder_path):
    translator = Translator()
    
    # Check if folder exists
    if not os.path.exists(folder_path):
        print(f"Directory '{folder_path}' not found.")
        return

    for filename in os.listdir(folder_path):
        # Skip directories
        file_path = os.path.join(folder_path, filename)
        if os.path.isdir(file_path):
            continue

        cleaned_name, tag, ext = process_file_name(filename)

        if not cleaned_name:
            continue

        try:
            # Translate/Transliterate title into Kannada
            translated = translator.translate(cleaned_name, dest='kn')
            kannada_name = translated.text.strip()
            
            # Reconstruct the file name with the original tag retained
            if tag:
                new_filename = f"{kannada_name} {tag}{ext}"
            else:
                new_filename = f"{kannada_name}{ext}"

            new_file_path = os.path.join(folder_path, new_filename)

            # Rename the file
            os.rename(file_path, new_file_path)
            print(f"Renamed: '{filename}' -> '{new_filename}'")

        except Exception as e:
            print(f"Failed to process '{filename}': {e}")

if __name__ == "__main__":
    TARGET_FOLDER = "D:\Movie converter\Output" 
    rename_files_to_kannada(TARGET_FOLDER)