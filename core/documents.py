
import fitz
import ollama


class DocumentAnalyzer:
    def __init__(self):
        self.model = "phi3:mini"

    def extract_text_from_pdf(self, file_path):
        text = ""

        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text() + "\n"

        return text

    def extract_text_from_txt(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    def analyze(self, file_path):
        try:
            file_path = file_path.lower()

            if file_path.endswith(".pdf"):
                text = self.extract_text_from_pdf(file_path)

            elif file_path.endswith(".txt"):
                text = self.extract_text_from_txt(file_path)

            else:
                return "Unsupported file type. Please use PDF or TXT."

            if not text.strip():
                return "No readable text found in this document."

            # Limit input for faster processing
            text = text[:1500]

            response = ollama.chat(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are NEXUS AI Document Analyzer. "
                            "Summarize only the given document. "
                            "Use simple language and short bullet points. "
                            "Avoid unnecessary explanations."
                        )
                    },
                    {
                        "role": "user",
                        "content": (
                            "Summarize this document:\n\n"
                            + text
                        )
                    }
                ],
                options={
                    "num_predict": 150,
                    "temperature": 0.2
                }
            )

            return response["message"]["content"].strip()

        except Exception as e:
            return f"Document analysis failed: {str(e)}"
