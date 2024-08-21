import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2
import spacy
from fpdf import FPDF

# Charger le modèle français de spaCy
nlp = spacy.load("fr_core_news_sm")

def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
            if not text:
                raise ValueError("Aucun texte trouvé dans le PDF.")
            return text
    except Exception as e:
        print(f"Erreur lors de l'extraction du texte du PDF : {e}")
        return ""

def clean_text(text):
    text = text.strip()
    text = text.replace("\n", " ")
    text = ' '.join(text.split())
    return text

def analyze_text(text):
    try:
        doc = nlp(text)
        entities = [(entity.text, entity.label_) for entity in doc.ents]
        return entities
    except Exception as e:
        print(f"Erreur lors de l'analyse du texte : {e}")
        return []

def extract_dates(text):
    try:
        doc = nlp(text)
        dates = [ent.text for ent in doc.ents if ent.label_ == "DATE"]
        return dates
    except Exception as e:
        print(f"Erreur lors de l'extraction des dates : {e}")
        return []

def extract_company_name(text):
    try:
        doc = nlp(text)
        company_names = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
        if company_names:
            return company_names[0]
        return "Nom de l'Entreprise"
    except Exception as e:
        print(f"Erreur lors de l'extraction du nom de l'entreprise : {e}")
        return "Nom de l'Entreprise"

def generate_tender_text(company_name, project_details, submission_date, contact_info):
    tender_text = (
        f"Appel d'Offres\n\n"
        f"Objet : {project_details}\n\n"
        f"Nous avons le plaisir de vous inviter à soumettre une offre pour le projet suivant :\n\n"
        f"Nom de l'Entreprise : {company_name}\n\n"
        f"Détails du Projet :\n{project_details}\n\n"
        f"Date Limite de Soumission : {submission_date}\n\n"
        f"Informations de Contact :\n{contact_info}\n\n"
        "Nous vous remercions par avance pour l'intérêt porté à cet appel d'offres. "
        "Veuillez soumettre votre offre avant la date limite mentionnée.\n\n"
        "Cordialement,\n"
        "Nom de Votre Entreprise\n"
        "Téléphone : 01 23 45 67 89\n"
        "Email : contact@votreentreprise.com"
    )
    return tender_text

def generate_pdf(tender_text, filename="appel_offre.pdf"):
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, tender_text)
        pdf.output(filename)
        print(f"PDF généré et enregistré dans {filename}")
    except Exception as e:
        print(f"Erreur lors de la génération du PDF : {e}")

def load_pdf():
    filepath = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if filepath:
        extracted_text = extract_text_from_pdf(filepath)
        if extracted_text:
            cleaned_text = clean_text(extracted_text)
            entities = analyze_text(cleaned_text)
            dates = extract_dates(cleaned_text)
            company_name = extract_company_name(cleaned_text)
            
            # Informations pour le modèle d'appel d'offres
            project_details = "La mise à jour de votre système ERP"
            submission_date = dates[0] if dates else "Date non spécifiée"
            contact_info = "01 23 45 67 89, contact@votreentreprise.com"
            
            tender_text = generate_tender_text(
                company_name,
                project_details,
                submission_date,
                contact_info
            )
            
            generate_pdf(tender_text)
            messagebox.showinfo("Succès", "PDF d'appel d'offres généré et enregistré avec succès.")
        else:
            messagebox.showwarning("Avertissement", "Aucun texte extrait du PDF.")
    else:
        messagebox.showwarning("Avertissement", "Aucun fichier sélectionné.")

def create_gui():
    root = tk.Tk()
    root.title("Générateur d'Appel d'Offres")
    root.geometry("400x200")

    upload_button = tk.Button(root, text="Télécharger un PDF", command=load_pdf, padx=20, pady=10)
    upload_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
