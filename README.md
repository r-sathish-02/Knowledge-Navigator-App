# Knowledge Navigator 🧠📚🚀

![image](https://github.com/user-attachments/assets/9f133a7e-4a5c-41f1-82de-6bbfe3487625)
**Live Demo:** [Click here to launch Knowledge Navigator!](https://knowledge-navigator-app-mfk6s7havyqzpfha6gdjtr.streamlit.app/) 
---

## 🌟 Overview

Knowledge Navigator is your **AI-powered educational assistant**, designed to revolutionize learning and teaching! Leveraging the power of Google's Gemini AI, this Streamlit application provides a comprehensive suite of tools for students, educators, and anyone eager to explore new knowledge or streamline their study process.

From generating custom quizzes to visualizing complex data, Knowledge Navigator aims to make education more interactive, efficient, and accessible.

---

## ✨ Features

Knowledge Navigator offers a wide array of functionalities, powered by intelligent AI models:

* **MCQ Generator:** Instantly create Multiple Choice Questions (MCQs) from any text, perfect for revision and self-assessment.
* **PDF Q&A System:** Upload PDF documents and let the AI generate relevant Questions and Answers based on the content, transforming static documents into interactive learning experiences.
* **CSV Visualization:** Easily upload and visualize data from CSV files with interactive charts, helping you understand data trends at a glance.
* **Research Bot:** Get quick, AI-powered answers to your academic queries and research questions.
* **Study Plan Generator:** Generate personalized study schedules tailored to your daily study hours, chosen subjects, and upcoming exam deadlines.
* **Interactive Quiz:** Test your knowledge with engaging quizzes, providing immediate feedback on your answers.
* **Concept Map Generator:** Visualize relationships between key concepts and their subtopics, fostering deeper understanding and retention.
* **Topic Summary Generator:** Get concise and accurate summaries of lengthy texts, saving time and highlighting core information.

---

## 🛠️ Technologies Used

The project is built using the following key technologies and libraries:

* **Python:** `3.10+` (Latest stable: `3.13.5`) - The core programming language.
* **Streamlit:** `1.46.0` (Latest stable) - For building the interactive web application interface.
* **Google Gemini API:** Powering all AI-driven features (MCQ generation, Q&A, Research, Summaries, Study Plan/Concept Map suggestions).
* **`google-generativeai`:** Python client library for Gemini API.
* **`python-dotenv`:** `1.1.1` (Latest stable) - Securely loading API keys during local development.
* **`PyPDF2`:** `5.7.0` (Latest stable for `pypdf`, which is the successor/new name for PyPDF2) - For extracting text content from PDF documents.
* **`pandas`:** `2.3.0` (Latest stable) - For robust data manipulation and handling of CSV files.
* **`matplotlib`:** `3.10.3` (Latest stable) - For generating static plots in CSV visualization (Streamlit's `st.line_chart` uses it internally).
* **`networkx`:** `3.5` (Latest stable) - For creating graph-based concept maps.

---

## 🚀 Getting Started

Follow these steps to set up and run Knowledge Navigator on your local machine:

### Prerequisites

* Python 3.10 or higher installed.
* A Google Gemini API Key. Get yours from [Google AI Studio](https://ai.google.dev/).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/sathish-02/Knowledge-Navigator-App.git](https://github.com/sathish-02/Knowledge-Navigator-App.git)
    cd Knowledge-Navigator-App
    ```
2.  **Create and activate a virtual environment:**
    * On Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    * On macOS/Linux:
        ```bash
        python3 -m venv venv  # Use python3 if `python` points to an older version
        source venv/bin/activate
        ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set up your Google Gemini API Key:**
    * Create a file named `.env` in the root of your project directory.
    * Add your API key to this file:
        ```
        GOOGLE_API_KEY="your-google-gemini-api-key-here"
        ```
        **Remember to replace `"your-google-gemini-api-key-here"` with your actual key.**
        **DO NOT commit your `.env` file to public repositories!** (It's already in `.gitignore`).

5.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```
    The app will open in your default web browser, usually at `http://localhost:8501`.

---

## 🌐 Deployment (Streamlit Community Cloud)

This application is designed for easy deployment on Streamlit Community Cloud:

1.  Ensure your code is pushed to a public GitHub repository (which you've already done!).
2.  Go to [Streamlit Community Cloud](https://share.streamlit.io/) and log in with your GitHub account.
3.  Click "New app" and select your `sathish-02/Knowledge-Navigator-App` repository, `main` branch, and `app.py` as the main file.
4.  In "Advanced settings" -> "Secrets", add your API key:
    ```
    GOOGLE_API_KEY = "your-google-gemini-api-key-here"
    ```
    (Use the same exact key you used in your `.env` file).
5.  Click "Deploy!".

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions for new features, improvements, or bug fixes, feel free to open an issue or submit a pull request.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
*(Optional: To add the MIT License, create a new file named `LICENSE` in the root of your GitHub repository and paste the full MIT License text into it.)*

---

## 📞 Contact

* **Sathish R**
* [GitHub Profile: @SATHISH R](https://github.com/r-sathish-02)
* [LinkedIn Profile](https://www.linkedin.com/in/sathish-r-5781a8291/)

---
