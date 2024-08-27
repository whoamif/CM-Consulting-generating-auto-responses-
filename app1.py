import PyPDF2
import spacy
import re

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
        for entity in doc.ents:
            print(f"Entité : {entity.text}, Type : {entity.label_}")
    except Exception as e:
        print(f"Erreur lors de l'analyse du texte : {e}")

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

def generate_response(company_name, project_details, your_company_name, phone_number, email):
    response = (
        f"Bonjour {company_name},\n\n"
        f"Nous avons bien reçu votre appel d'offres pour {project_details}. "
        "Nous serions ravis de collaborer avec vous et de discuter plus en détail des "
        "exigences et des conditions de ce projet.\n\n"
        "N'hésitez pas à nous contacter pour toute information complémentaire ou pour convenir d'une réunion.\n\n"
        f"Cordialement,\n{your_company_name}\n"
        f"Téléphone : {phone_number}\n"
        f"Email : {email}"
    )
    return response

def save_response(response, filename="response.txt"):
    try:
        with open(filename, 'w') as file:
            file.write(response)
        print(f"Réponse enregistrée dans {filename}")
    except Exception as e:
        print(f"Erreur lors de l'enregistrement de la réponse : {e}")

if __name__ == "__main__":
    pdf_path = r'/Users/mac/Desktop/DAO Montée de version SAP ECC6 S4 HANA 28.12.2022 final_CMC.pdf'
    
    extracted_text = extract_text_from_pdf(pdf_path)
    
    if extracted_text:
        cleaned_text = clean_text(extracted_text)
        analyze_text(cleaned_text)
        
        dates = extract_dates(cleaned_text)
        print("Dates trouvées : ", dates)
        
        company_name = extract_company_name(cleaned_text)
        print("Nom de la société : ", company_name)
        
        project_details = "la mise à jour de votre système ERP"
        your_company_name = "Nom de Votre Entreprise"
        phone_number = "01 23 45 67 89"
        email = "contact@votreentreprise.com"
        
        response = generate_response(company_name, project_details, your_company_name, phone_number, email)
        
        save_response(response)