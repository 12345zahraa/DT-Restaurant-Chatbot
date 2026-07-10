# 🍕 DT Restaurant AI Assistant

DT Restaurant AI Assistant is a smart automated invoice registration system powered by Large Language Models (LLMs) and Streamlit. This application allows customers to place orders using natural language and receive an instant, calculated invoice with shipping details.

## 🚀 Key Features
- **Natural Language Ordering:** Processes Persian text to accurately extract and list menu items.
- **Automated Calculation:** Automatically calculates total prices and handles shipping fees (Free delivery for orders over 50,000 Tomans).
- **Modern UI:** Built with Streamlit, featuring a full RTL (Right-to-Left) layout for a seamless experience.
- **Model Selection:** Flexibility to switch between different local models (e.g., Llama3.1, Gemma2) via the sidebar.

## 🛠 Tech Stack
- **Python:** Core programming language.
- **Streamlit:** For creating the interactive web interface.
- **Ollama:** For running AI models locally.

## 📥 How to Run

1. **Prerequisites:**
   Ensure you have Python installed and your AI models set up via Ollama.

2. **Install dependencies:**
   ```bash
   pip install streamlit
   ```
   1. Run the application
   ```bash
   streamlit run app.py
   ```
   