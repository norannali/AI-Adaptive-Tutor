# 🎓 AI Adaptive Tutor

An intelligent, interactive AI-powered tutor designed to adapt to users' learning levels and needs. This project leverages **Memory Systems, Struggle Detection, Vocabulary Guidance, Response Styling, and LLMs** to provide personalized educational support.

---

## 🚀 Features

- **Adaptive Learning**: Adjusts explanations based on the user's proficiency (beginner, intermediate, advanced).  
- **Memory System**: Keeps track of user interactions and question history to improve tutoring.  
- **Struggle Detection**: Detects repeated questions or confusion to provide additional support.  
- **Vocabulary Guidance**: Adapts explanations to match the user’s learning level.  
- **Tone and Styling**: Modifies response style based on user emotion and difficulty level.  
- **LLM Integration**: Generates responses using OpenRouter or fallback AI logic.  

---

## 🧩 Technologies Used

- **Python 3.x**  
- **Streamlit** for web interface  
- **LLMProvider** (OpenRouter / Meta LLaMA)  
- **Custom Modules**:
  - `MemoryManager` – manages user state and interactions  
  - `ResponseStyleController` – adjusts tone and formatting  
  - `StruggleDetector` – analyzes repeated/confusing questions  
  - `VocabularyController` – provides level-appropriate vocabulary guidance  
  - `PromptBuilder` – builds system and user prompts for the LLM  

---

## 💻 Installation

1. Clone the repository:

```bash
git clone https://github.com/norannali/AI-Adaptive-Tutor.git
cd AI-Adaptive-Tutor
```
2. Create and activate a virtual environment:
```bash
python -m venv ai_env
ai_env\Scripts\activate  # Windows
source ai_env/bin/activate  # macOS/Linux
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
---

## 🖥 **Running the App**
```bash
streamlit run streamlit_app.py
```
1- Enter a User ID

2- Select a User Level (beginner, intermediate, advanced)

3- Enter your question

4- Click Generate Response to see the AI explanation and metadata

---

## 🧠 **Example Use Cases**

* Beginner: Explaining basic concepts like "What is ML?"

* Intermediate: Providing structured reasoning and examples

* Advanced: Deep technical insights with mathematical intuition

---

## 📊  **Metadata Provided**

Each AI response includes:

* User Level

* Tone

* Struggling status

* Repeated question status

* Struggle score

* LLM provider

## 🔧  **Future Enhancements**

* Emotion detection for more personalized tone

* Gamified learning modules for interactive education

* Integration with voice input/output

* Multi-language support

## 📄  **License**

This project is licensed under the MIT License.

👤 Author

Noran Ali – GitHub
