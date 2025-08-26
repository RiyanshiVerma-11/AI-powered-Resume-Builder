# 🧠 AI Resume Builder Web App

An intelligent resume builder powered by AI that helps students and professionals generate, enhance, and customize their resumes using minimal input — either from their LinkedIn profile, manual details, or by uploading an existing resume.

---

## 🔍 Features

✅ **Generate Resume from LinkedIn**  
Provide your LinkedIn profile URL, and the app extracts your data and writes a professional resume using AI.

✅ **Generate Resume from Manual Input**  
No LinkedIn? Just enter your skills, education, and projects — AI will generate a job-ready resume for you.

✅ **Enhance Existing Resume**  
Upload your old resume in PDF format — the app will analyze and rewrite it to improve grammar, tone, and structure using GPT.

---

## 🚀 Technologies Used

- **Python 3.11**
- **Streamlit** – Frontend UI
- **OpenAI GPT API** – AI text generation
- **pdfplumber / python-docx** – Parsing old resumes
- **FPDF / WeasyPrint** – PDF generation
- **BeautifulSoup** – *(Planned)* for LinkedIn data parsing

---

## 🛠️ Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/ai-resume-builder.git
   cd ai-resume-builder
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # On Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the App**
   ```bash
   streamlit run app.py
   ```

---

## 💡 Future Improvements

- Export in multiple templates and themes
- Save and edit resumes for returning users
- Customizable tone: Formal / Friendly / Creative
- Smart job matching + skill gap suggestions

---

## 🤝 Contributing

Pull requests and feature suggestions are welcome.  
For major changes, please open an issue first to discuss what you would like to change.  
**Note:** Contributions will only be accepted with author permission.

---

## 📜 License

This project is licensed under a custom **Non-Commercial Contributor License**.  
No commercial use or redistribution allowed without explicit permission from the author.  
See the [LICENSE](./LICENSE) file for full terms.

---

## 🧑‍💻 Developed by

**Riyanshi Verma**  
B.Tech CSE (Data Science), MIET  
[linkedin.com/in/riyanshi-verma-ba363a2b2](https://www.linkedin.com/in/riyanshi-verma-ba363a2b2)
