# **Email Copy Validator**

## **Business Problem**
Ensuring that marketing emails retain the intended wording and structure from the original copywriting document is crucial for brand consistency and regulatory compliance. Small discrepancies in email content can lead to miscommunication, legal risks, or reduced engagement rates. This program automates the validation process by comparing the final HTML email against the original copywriting text, identifying discrepancies, and generating reports.

---

## **Overview of Program**
The **Email Copy Validator** extracts text from an HTML email and compares it to a reference copywriting document. It highlights differences, missing text, and similarity scores, allowing teams to quickly identify and correct issues. The program provides detailed output reports categorizing:
- **Perfect Matches** ✅
- **Partial Matches (with similarity scores)** 🔍
- **Missing or Incorrect Text Blocks** ⚠️

**Note:** This project was built using **simplified data files** and is not suited for real-world business use. Its accuracy is limited because it expects a **specific copydoc format** and may **miss errors** or even break with **more diverse email HTML**. With further testing and real-world context, it could be improved for greater reliability. 

---

## **Tools Used**  
- **Python** – Core programming language for text extraction and comparison.  
- **BeautifulSoup** – Parses and extracts text from HTML emails.  
- **difflib** – Calculates similarity between text blocks.  
- **GitHub Copilot** – Assisted in generating code and debugging.  
- **ChatGPT** – Helped create the HTML email template, copydoc example, README file
- **VS Code** – Primary code editor for development and debugging.

---

## **File Structure**
```
📂 Email-CopyDoc-Checker/
├── 📂 data/                      # Input files (original texts & emails)
│   ├── 📜 [0] copydoc.txt        # Original copywriting text
│   ├── 📜 [1] flawless_email.html # Email with no detected errors
│   ├── 📜 [2] one_error_email.html # Email with a single error
│   ├── 📜 [3] many_errors_email.html # Email with multiple discrepancies
├── 📂 outputs/                   # Results from script execution
│   ├── 📜 [1] output_flawless.txt # Report for a flawless email
│   ├── 📜 [2] output_one_error.txt # Report for an email with a single error
│   ├── 📜 [3] output_many_errors.txt # Report for an email with many errors
├── 📜 README.md                  # Documentation for the project
├── 📜 email_checker.py           # Main script that compares email content with the reference text
├── 📜 image_flawless_email.png   # Screenshot of a flawless email
```

### **Explanation of Key Files**
- **`email_checker.py`** – Main script that processes the email and text file, performs comparisons, and generates reports.
- **`[0] copydoc.txt`** – The reference document that contains the original approved email content.
- **`[1] flawless_email.html`**, **`[2] one_error_email.html`**, **`[3] many_errors_email.html`** – Sample email files with different levels of discrepancies.
- **Output files (`outputs/[X] output_*.txt`)** – Reports highlighting text mismatches and missing sections.
- **`image_flawless_email.png`** – Screenshot my AI gererated mock email advertisement 

---

## **Project Process**

This project was developed through a structured process that involved planning, coding, testing, and refining the program. Below is a step-by-step breakdown of how the **Email Copy Validator** was built.

### **1️⃣ Planning the Algorithmic Approach**
Before writing any code, I developed a clear **algorithmic plan** to solve the problem efficiently. The goal was to compare an HTML email’s text against a structured reference document (**copydoc.txt**) and identify discrepancies. Key considerations included:
- Extracting structured text from **copydoc.txt** into identifiable blocks.
- Parsing **HTML emails** to retrieve and clean textual content.
- Implementing **string similarity matching** to detect differences.
- Formatting **output reports** to be informative and easy to read.

This planning phase ensured that the implementation process was smooth and that the logic was well-structured before writing any code.

---

### **2️⃣ Creating a Copydoc Example & Test Cases**
Since I didn’t have access to a real-world **copydoc**, I created an **example document** based on what I imagined a real copywriting team might use.  
- The **copydoc.txt** file contains five text blocks formatted as if they were written for a **fictional soap company’s marketing email**.
- To differentiate sections, I used a **backslash (`\`) before each block title**, ensuring a clear separation between headings and content.
- This backslash method works because it’s an uncommon character in natural marketing text, making it a reliable delimiter.

Additionally, I generated **test cases** with different levels of errors:
1. A **flawless email** (100% correct).
2. An email with **one incorrect section**.
3. An email with **multiple errors**.

This setup allowed me to validate the algorithm’s performance in different scenarios.

---

### **3️⃣ Generating an HTML Email Template**
To test the validator against real email structures, I needed a sample HTML email.  
- I used **ChatGPT** to generate a simple **HTML email template** that matched the copydoc content.
- ChatGPT also designed a **fictional logo** for the soap company to make the email look more realistic.

The resulting **flawless_email.html** file became the baseline for validating the parsing and comparison logic.

---

### **4️⃣ Implementing Copydoc Parsing with GitHub Copilot**
To extract text blocks from **copydoc.txt**, I instructed **GitHub Copilot** to write a function that:
- Reads **copydoc.txt** and splits it into **key-value pairs**, where:
  - The **heading line** (starting with `\`) is used as the **key**.
  - The **block of text** under the heading is stored as the **value** (continuous string).
- This ensures that each section of the copydoc is properly structured and can be used for comparison.

Since I wasn’t sure how **real-world copydocs** are formatted, I kept this example **simplified** but functionally effective.

---

### **5️⃣ Extracting Text from the HTML Email**  
I then had **Copilot generate a function** to:  
- Parse the **HTML email file**.  
- Extract every visible **line of text** into a list.  
- Clean the extracted text by:  
  - Removing **line breaks and indentation** (caused by HTML formatting).  
  - Ensuring each extracted block is a **single continuous string**.  

This helped ensure that the email content was properly formatted for comparison against **copydoc.txt**.  

**Note:** The way I removed indentation spaces from the HTML text blocks may **not handle edge cases** where there is an unintended **double space** (e.g., at the beginning or end of a line). With more time, this could be improved to ensure more **robust text cleaning** and consistency.

---

### **6️⃣ Matching Copydoc Blocks to Extracted Email Text**
The next challenge was **matching the copydoc content** against the extracted email text.  
I instructed **Copilot** to:
- **Compare each copydoc block** with every extracted text block from the email.
- Use **string similarity** (via `difflib`) to determine how closely each copydoc block matches an email section.
- If **50% similarity or greater** was found, the program assumes that the email text **intended to replicate that copyblock**.

This threshold allows for minor variations while still flagging significant discrepancies.

---

### **7️⃣ Highlighting Differences**
To help users identify **where errors occurred**, I asked **Copilot** to generate a function that:
- Detects **differences between expected and actual text**.
- Highlights the **first 20 characters around the error**, allowing users to quickly pinpoint mistakes.
- Outputs a side-by-side comparison of:
  - **Expected copydoc text** ✅
  - **Actual email text** ❌
  - **Highlighted difference snippet** 🔍

This functionality makes the output reports **more actionable**, allowing users to correct errors efficiently.

---

### **8️⃣ Structuring the Output Reports**
Finally, I structured how the **program’s results** would be displayed:
- **Summary Section** 📌  
  - Shows the **total number of discrepancies** found.
- **Detailed Error Breakdown** 🟥  
  - Displays the **similarity score** between expected vs. actual text.
  - Highlights the **mismatched text** for easy comparison.
- **Missing Blocks Warning** 🟨  
  - Alerts if a section from the copydoc is **completely missing** from the email.

Each report is saved as a **`.txt` file** in the `/outputs/` directory for easy review.

---

### **Final Outcome**
After implementing these steps, the **Email Copy Validator** successfully:  
✔ Extracts and processes **structured text from copydoc.txt**.  
✔ Parses and **cleans HTML email content** for accurate comparison.  
✔ Uses **string similarity** to detect **partial and complete matches**.  
✔ Highlights **differences between expected and actual email text**.  
✔ Generates **clear reports** to help identify and fix content discrepancies.

---

## **Limitations & Considerations**  

While this program successfully compares structured text blocks from a simplified **copydoc.txt** against an HTML email, it has several limitations:  

1️⃣ **Limited Test Cases** – Only a single set of test cases was created, meaning the program has not been rigorously tested across diverse email formats or varying copydoc structures. It likely **does not catch many edge cases**.  

2️⃣ **Simplified Copydoc Structure** – The program assumes that every text block in **copydoc.txt** starts with a backslash (`\`), which is **not how real-world copydocs are structured**. This makes the program **incompatible** with actual copywriting documents unless they are formatted in this specific way.  

3️⃣ **HTML Parsing Limitations** – The program extracts text from an HTML email but does not account for **complex email formatting**, dynamic content, or inline styles that might alter how the text appears.  

4️⃣ **Basic Similarity Matching** – The program uses a simple **50% similarity threshold** for detecting intended matches. This may result in **false positives or negatives**, where minor wording changes either pass unnoticed or flag unnecessary errors.  

5️⃣ **Not Ready for Production** – Without broader testing and real-world copydoc formats, this program is **not suitable for actual marketing teams** without significant modifications and validation.  

### **Future Improvements**
- Expanding **test cases** to include different email structures and real-world copydoc formats.  
- Enhancing **text extraction** to handle more **complex HTML elements**.  
- Implementing **configurable similarity thresholds** to fine-tune accuracy.  
- Allowing **dynamic copydoc formats** so the program can adapt to industry-standard structures.  
