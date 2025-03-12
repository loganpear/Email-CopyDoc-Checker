import re
import difflib
from bs4 import BeautifulSoup

def clean_text(text):
    """
    Clean the text by removing indentation spaces but preserving multiple spaces within the text.
    """
    # Replace multiple spaces at the beginning of lines with a single space
    cleaned_text = re.sub(r'(?m)^\s+', '', text)
    return cleaned_text

def extract_text_blocks_from_html(file_path):
    text_blocks = []
    with open(file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
        for element in soup.find_all(text=True):
            text = element
            if text:
                # Split the text into lines, strip each line, and join them back together
                lines = text.splitlines()
                stripped_lines = [line.strip() for line in lines]
                cleaned_text = clean_text(" ".join(stripped_lines)).strip()  # Strip trailing spaces
                text_blocks.append(cleaned_text)
    return text_blocks

def read_text_blocks_correct(file_path):
    text_blocks = {}
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        blocks = content.split("\n\n")  # Assuming each block is separated by a double newline
        for block in blocks:
            lines = block.split("\n")
            key = lines[0].replace("\\", "").strip()
            value = " ".join(line.strip() for line in lines[1:]).strip()  # Strip trailing spaces
            text_blocks[key] = value
    return text_blocks

def compare_text_blocks(correct_blocks, email_blocks):
    discrepancies = []
    missing_blocks = {}

    for key, correct_text in correct_blocks.items():
        found = False
        for email_text in email_blocks:
            similarity = difflib.SequenceMatcher(None, correct_text, email_text).ratio() * 100
            if similarity == 100:
                found = True
                
            elif 50 <= similarity < 100:
                discrepancies.append((key, correct_text, email_text, similarity))
                found = True
                
        if not found:
            missing_blocks[key] = correct_text

    return discrepancies, missing_blocks

def find_difference_snippet(correct_text, email_text):
    """
    Find the first difference between correct_text and email_text and return a snippet around the difference.
    """
    matcher = difflib.SequenceMatcher(None, correct_text, email_text)
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag != 'equal':
            start = max(i1 - 10, 0)
            end = min(i2 + 10, len(correct_text))
            return correct_text[start:end], email_text[start:end]
    return "", ""

# Example usage
if __name__ == "__main__":
    text_file = input("Enter the copydoc TXT file: ") 
    html_file = input("Enter the HTML email file: ")   

    text_blocks_in_email = extract_text_blocks_from_html(html_file)
    text_blocks_correct = read_text_blocks_correct(text_file)

    discrepancies, missing_blocks = compare_text_blocks(text_blocks_correct, text_blocks_in_email)
    num_discrepancies = len(discrepancies)

    print(f"\n📌 SUMMARY REPORT: {num_discrepancies} Text Discrepancies Found")
    print("==================================================")
    
    if discrepancies:
        count = 1
        for key, correct_text, email_text, similarity in discrepancies:
            print(f"\n{count}) SIMILARITY:   {similarity:.2f}%  IN  {key}\n")
            print(f"🟩 EXPECTED:      {correct_text}\n")
            print(f"🟥 FOUND:         {email_text}\n")
            correct_snippet, email_snippet = find_difference_snippet(correct_text, email_text)
            print(f"🟦 DIFFERENCE:   Expected: \"{correct_snippet}\" Found: \"{email_snippet}\"\n")
            if count != num_discrepancies:
                print("--------------------------------------------------")
            else:
                print("==================================================")
            count += 1
    else:
        print("✅ No discrepancies found between the text blocks and the HTML email!")

    if missing_blocks:
        print("\n🟨 WARNING: The following text blocks from the copywriting team were not found in the HTML email:\n")
        count = 1
        for key, block in missing_blocks.items():
            print(f"   {count}) {key} \"{block}\"\n")
            count += 1
    else:
        print("\n✅ All text blocks from the copywriting team were identified at least once in the HTML email!\n")