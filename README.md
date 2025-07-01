# Text Translator 🌐

A web-based text translation application built with Streamlit and powered by Google Translate, designed to facilitate seamless multilingual communication. Translate text across numerous languages with an intuitive and responsive interface.

## 🚀 Demo
Try the live application here: [press here](https://yahyaiuu7-code-alpha-text-translator.hf.space/)

## 📑 Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [Authors](#authors)
- [License](#license)

## 🌟 Features
- Translate text between multiple languages with auto-detection for source language.
- Intuitive and responsive UI for both desktop and mobile devices.
- Real-time text statistics (character count, word count, translated text length).
- Supports light and dark themes for enhanced user experience.
- Error handling for connectivity issues and empty inputs.

## 🛠 Installation
To run the Text Translator locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/text-translator.git
   cd text-translator
   ```

2. **Set Up a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   Install the required packages listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

   The app will launch in your default browser at `http://localhost:8501`.

## 📖 Usage
1. Access the live demo at [Hugging Face Spaces](https://huggingface.co/spaces/yahyaiuu7/code-alpha-text-translator) or run locally.
2. Select the source language (or use "Auto Detect") and input the text to translate.
3. Choose the target language from the dropdown menu.
4. Click the "Translate" button to view the translated text.
5. Check text statistics (character count, word count, and translated text length) below the translation area.

## 📂 Project Structure
```
text-translator/
│
├── app.py              # Main Streamlit application script
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

## 💻 Technologies Used
- **Python**: Core programming language.
- **Streamlit**: Framework for building the web interface.
- **Googletrans**: Library for text translation via Google Translate API.
- **Requests**: Handles HTTP requests.
- **CSS**: Custom styles for responsive design and theme support.

## 🤝 Contributing
We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

Please ensure your code adheres to the project's coding standards and includes clear documentation.

## 👩‍💻👨‍💻 Authors
- **Shahd Elmaghawry**  
  [LinkedIn Profile](https://www.linkedin.com/in/shahd-elmaghawry-066923307/)
- **Yahya Mahrouf**  
  [LinkedIn Profile](https://www.linkedin.com/in/yahya-mahrouf/)

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
