# html2md

**html2md** is a simple Python command-line tool that converts HTML content — from either a local file or a webpage URL — into clean, readable Markdown format.

---

## ✨ Features

- ✅ Convert HTML files to Markdown  
- 🌐 Fetch and convert HTML from web URLs  
- 📄 Supports links, images, headings, lists, and more  
- 💾 Save output to a file of your choice  

---

## 📦 Installation

1. Clone or download this repository:

```bash
git clone https://github.com/MSM2002/html2md.git
cd html2md
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

Or just:

```bash
pip install html2text requests
```

---

## 🚀 Usage

### Convert a local HTML file

```bash
python html2md.py path/to/input.html -o output.md
```

### Convert a webpage URL

```bash
python html2md.py https://example.com -o output.md
```

If you omit `-o`, it will default to saving as `output.md`.

---

## 🛠 Example

```bash
python html2md.py https://en.wikipedia.org/wiki/Markdown -o markdown_article.md
```

---

## 📝 Requirements

- Python 3.6+
- `html2text`
- `requests`

---

## 📁 Example Output

For an input HTML with:

```html
<h1>Title</h1>
<ul>
  <li>First bullet</li>
  <li>Second bullet</li>
</ul>
```

Output Markdown:

```markdown
# Title

* First bullet
* Second bullet
```

---

## 📄 License

MIT License

---

## 🤝 Contributing

Pull requests and improvements are welcome! Please open an issue first to discuss changes.
