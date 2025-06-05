import os
import re

# Configuration
SOURCE_DIR = "./source"
DEST_DIR = "./migrated"

# Ensure destination exists
os.makedirs(DEST_DIR, exist_ok=True)

# Helper function to extract title from AsciiDoc first line
def extract_title(lines):
    if lines[0].startswith("= "):
        return lines[0][2:].strip()
    else:
        raise ValueError("Cannot find title line.")

# Helper function to extract date from filename
def extract_date(filename):
    match = re.match(r'(\\d{4}-\\d{2}-\\d{2})-.*', filename)
    if match:
        return match.group(1)
    else:
        raise ValueError("Cannot extract date from filename.")

# Helper function to clean body

def clean_body(lines):
    body = []
    for line in lines[1:]:
        if line.startswith("Author:"):
            continue
        if line.startswith("v") and re.match(r'v\\d+\\.\\d+', line.strip()):
            continue
        body.append(line)
    return body

# Main interactive migration loop
for filename in os.listdir(SOURCE_DIR):
    if not filename.endswith(".adoc"):
        continue

    filepath = os.path.join(SOURCE_DIR, filename)
    print(f"\nProcessing: {filename}")

    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    try:
        title = extract_title(lines)
        date = extract_date(filename)
        body = clean_body(lines)
    except Exception as e:
        print(f"Error: {e}")
        continue

    # Ask user for category
    category = input("Category (Adventures / Reflections): ").strip()
    if not category:
        category = "Reflections"

    # Ask user for tags
    default_tags = []
    if "linkedin" in filename.lower():
        default_tags.append("LinkedIn")
    if "medium" in filename.lower():
        default_tags.append("Medium")

    tag_input = input(f"Tags [{', '.join(default_tags)}]: ").strip()
    if tag_input:
        tags = [tag.strip() for tag in tag_input.split(",")]
    else:
        tags = default_tags

    # Build YAML front matter
    front_matter = ["---\n"]
    front_matter.append(f"title: \"{title}\"\n")
    front_matter.append(f"date: {date}\n")
    front_matter.append(f"category: {category}\n")
    front_matter.append(f"tags: [{', '.join(tags)}]\n")
    front_matter.append("---\n\n")

    # Show preview
    print("\n--- Preview ---")
    print("".join(front_matter + body))
    confirm = input("Save migrated file? (y/n): ").strip().lower()
    if confirm != "y":
        print("Skipped.")
        continue

    # Write migrated file
    dest_path = os.path.join(DEST_DIR, filename)
    with open(dest_path, "w", encoding="utf-8") as out_f:
        out_f.writelines(front_matter)
        out_f.writelines(body)

    print(f"Saved to {dest_path}")
