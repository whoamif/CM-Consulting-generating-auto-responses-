# Automatic Response Generator for Call for Tenders
<img width="411" alt="Screenshot 2024-08-21 at 3 58 19 PM" src="https://github.com/user-attachments/assets/1d53807a-1685-4f9b-ae0e-ab7a6792da89">

This project is designed to automatically generate responses to calls for tenders (appel d'offres) by extracting relevant information from a PDF document and using it to create a tailored response. The tool includes a simple GUI for uploading PDF files, analyzing the content, and generating a response in text format.

## Features

- **PDF Upload and Text Extraction:** Upload a PDF file, extract and clean the text for analysis.
- **Named Entity Recognition:** Identify key entities such as company names, dates, and project details using SpaCy.
- **Automatic Response Generation:** Generate a custom response to the tender based on the extracted information.
- **Simple GUI:** A user-friendly interface for uploading PDF files and generating responses.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/automatic-response-generator.git
    ```
2. Navigate to the project directory:
    ```bash
    cd automatic-response-generator
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Ensure you have the SpaCy language model installed:
    ```bash
    python -m spacy download fr_core_news_sm
    ```

## Usage

1. Run the application:
    ```bash
    python main.py
    ```
2. Click on the "Télécharger un PDF" button to upload a PDF file.
3. The tool will analyze the PDF, extract relevant information, and generate a response.
4. The response is saved as `response.txt` in the project directory.

## Project Structure

- `main.py`: The main script to run the application.
- `requirements.txt`: The list of required Python libraries.
- `README.md`: This file.
- `response.txt`: The generated response file (created after running the application).

## Dependencies

- Python 3.8+
- Tkinter (for GUI)
- PyPDF2 (for PDF text extraction)
- SpaCy (for text analysis)
- fr_core_news_sm (SpaCy language model)

## Future Enhancements


- **PDF Generation:** Implement functionality to generate a PDF document for the response.
- **Advanced NLP Models:** Integrate more advanced NLP techniques for improved information extraction.
- **Multilingual Support:** Extend the tool to support multiple languages beyond French.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or support, feel free to reach out to (mailto:adjissifatimaamina@gmail.com).
