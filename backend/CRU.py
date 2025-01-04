from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document
# from langchain_community.document_loaders import WebPageLoader
import requests
from bs4 import BeautifulSoup

def create_and_save_embeddings():
    # Initialize embedder and text splitter
    embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    
    # URLs to collect data from
    urls = [
        "https://www.rmkec.ac.in/2023",
        "https://www.rmkec.ac.in/2023/about-us-3/about-us/",
        "https://www.rmkec.ac.in/2023/about-us-3/about-us-2/",
        "https://www.rmkec.ac.in/2023/about-us-3/management-team/",
        "https://www.rmkec.ac.in/2023/about-us-3/vision-mission/",
        "https://www.rmkec.ac.in/2023/about-us-3/quality-policy/",
        "https://www.rmkec.ac.in/2023/administration/governing-board/",
        "https://www.rmkec.ac.in/2023/administration/advisor-02/",
        "https://www.rmkec.ac.in/2023/administration/principal/",
        "https://www.rmkec.ac.in/2023/administration/dean-research/",
        "https://www.rmkec.ac.in/2023/administration/dean/",
        "https://www.rmkec.ac.in/2023/administration/academic-co-ordinator/",
        "https://www.rmkec.ac.in/2023/administration/admission-procedure/",
        "https://www.rmkec.ac.in/2023/administration/committee/anti-ragging-committee/",
        "https://www.rmkec.ac.in/2023/administration/committee/planning-monitoring-committee/",
        "https://www.rmkec.ac.in/2023/administration/committee/anti-ragging-squad/",
        "https://www.rmkec.ac.in/2023/administration/committee/the-internal-complaints-committee/",
        "https://www.rmkec.ac.in/2023/administration/committee/disciplinary-and-welfare-committee/",
        "https://www.rmkec.ac.in/2023/administration/committee/the-grievances-and-redressal-committee/",
        "https://www.rmkec.ac.in/2023/administration/committee/aicte-eoa/",
        "https://www.rmkec.ac.in/2023/budget/",
        "https://www.rmkec.ac.in/2023/academics/regulation/",
        "https://www.rmkec.ac.in/2023/academics/curriculum-and-syllabus/",
        "https://www.rmkec.ac.in/2023/academics/courses-offered/",
        "https://www.rmkec.ac.in/2023/academics/academic-schedule/",
        "https://www.rmkec.ac.in/2023/academics/rules-and-regulations/",
        "https://www.rmkec.ac.in/2023/academics/antiragging/",
        "https://www.rmkec.ac.in/2023/academics/research/",
        "https://www.rmkec.ac.in/2023/academics/scholarships/",
        "https://www.rmkec.ac.in/2023/aids/about-the-department/",
        "https://www.rmkec.ac.in/2023/dep_civil_eng/about-the-department/",
        "https://www.rmkec.ac.in/2023/btech/about-the-department/",
        "https://www.rmkec.ac.in/2023/cs_design/about-the-department/",
        "https://www.rmkec.ac.in/2023/computerscience_eng/about-the-department/",
        "https://www.rmkec.ac.in/2023/ee_eng/about-the-department/",
        "https://www.rmkec.ac.in/2023/ec_eng/about-the-department/",
        "https://www.rmkec.ac.in/2023/ei_eng/about-the-department/",
        "https://www.rmkec.ac.in/2023/infotech_eng/about-the-department/",
        "https://www.rmkec.ac.in/2023/mechanical_eng/about-the-department/",
        "https://www.rmkec.ac.in/2023/science_humanities/about-the-department/",
        "https://www.rmkec.ac.in/2023/physical_edu/about-physical-education/",
        "https://www.rmkec.ac.in/2023/training_placement/about-training-and-placement/",
        "https://www.rmkec.ac.in/2023/coe_dep/about-coe/",
        "https://www.rmkec.ac.in/2023/higher_edu/about-higher-education-cell/",
        "https://www.rmkec.ac.in/2023/cffl/about-cfl/",
        "https://www.rmkec.ac.in/2023/news-events/",
        "https://www.rmkec.ac.in/2023/campus/general-facilities/",
        "https://www.rmkec.ac.in/2023/compcent/computer-center/",
        "https://www.rmkec.ac.in/2023/cl/about-central-library/",
        "https://www.rmkec.ac.in/2023/campus/green-campus/",
        "https://www.rmkec.ac.in/2023/campus/hostel/",
        "https://www.rmkec.ac.in/2023/campus/transport/",
        "https://www.rmkec.ac.in/2023/campus/hospital/",
        "https://www.rmkec.ac.in/2023/campus/gymnasium/",
        "https://www.rmkec.ac.in/2023/entrepreneurship/about-cie/",
        "https://www.rmkec.ac.in/2023/entrepreneurship/ariia-ranking/",
        "https://www.rmkec.ac.in/2023/entrepreneurship/policy-documents/",
        "https://www.rmkec.ac.in/2023/entrepreneurship/policy-documents/rmkec-policy/",
        "https://www.rmkec.ac.in/2023/entrepreneurship/policy-documents/national-policy/",
        "https://www.rmkec.ac.in/2023/entrepreneurship/policy-documents/tamilnadu-policy/",
        "https://www.rmkec.ac.in/2023/entrepreneurship/iic/",
        "https://www.rmkec.ac.in/2023/entrepreneurship/iic/about-iic/",
        "https://www.rmkec.ac.in/2023/entrepreneurship/iic/innovation-ambassador-programme/",
        "https://www.rmkec.ac.in/2023/entrepreneurship/msme/",
        "https://www.rmkec.ac.in/2023/entrepreneurship/msme/about-msme/",
        "https://www.rmkec.ac.in/2023/entrepreneurship/msme/msme-committee-members/",
        "https://www.rmkec.ac.in/2023/entrepreneurship/msme/msme-approval-letter/",
        "https://www.rmkec.ac.in/2023/entrepreneurship/msme/selected-ideas-for-incubation/",
        "https://www.rmkec.ac.in/2023/entrepreneurship/msme/rmk-startup/",
        "https://www.rmkec.ac.in/2023/entrepreneurship/msme/msme-activities/",
        "https://www.rmkec.ac.in/2023/entrepreneurship/startups-in-rmkec-incubation-center/",
        "https://www.rmkec.ac.in/2023/entrepreneurship/iedc/",
        "https://www.rmkec.ac.in/2023/ecell/about-e-cell/",
        "https://www.rmkec.ac.in/2023/entrepreneurship/ipr-cell/",
        "https://www.rmkec.ac.in/2023/entrepreneurship/ipr-cell/patent-list/",
        "https://www.rmkec.ac.in/2023/entrepreneurship/ipr-cell/ipr-policy/",
        "https://www.rmkec.ac.in/2023/entrepreneurship/ipr-cell/filing-procedure/",
        "https://www.rmkec.ac.in/2023/entrepreneurship/rmk-store/",
        "https://www.rmkec.ac.in/2023/accreditation/nba/",
        "https://www.rmkec.ac.in/2023/accreditation/naac/naac-ssr-aqar/",
        "https://www.rmkec.ac.in/2023/accreditation/nirf/nirf-disclosure/",
        "https://www.rmkec.ac.in/2023/contact-us/contact/",
        "https://www.rmkec.ac.in/2023/contact-us/grievances/",
        "https://www.rmkec.ac.in/admission2023/sendotp1.php",
        "https://www.rmkec.ac.in/2023/global-education-leadership-achievement-award-london-2023/",
        "https://www.rmkec.ac.in/2023/entrepreneurship/rmk-store/",
        "https://www.rmkec.ac.in/2023/about-us",
        "https://www.rmkec.ac.in/2023/research",
        "https://www.rmkec.ac.in/2023/campus/general-facilities/",
        "https://www.rmkec.ac.in/2023/campus/central-library/",
        "https://www.rmkec.ac.in/2023/campus/computer-centre/",
        "https://www.rmkec.ac.in/2023/global-education-leadership-achievement-award-london-2023/",
        "https://www.rmkec.ac.in/2023/global-education-leadership-achievement-award-london-2023/",
        "https://www.rmkec.ac.in/2023/rmk-glancevillage-hackathon/",
        "https://www.rmkec.ac.in/2023/rmk-glancevillage-hackathon/",
        "https://www.rmkec.ac.in/2023/international-conference-on-intelligent-computing-smart-communication-and-network-technologies-icicscnt-2023/",
        "https://www.rmkec.ac.in/2023/international-conference-on-intelligent-computing-smart-communication-and-network-technologies-icicscnt-2023/",
        "https://www.rmkec.ac.in/2023/news-events",
        "https://www.rmkec.ac.in/2023/about-us/",
        "https://www.rmkec.ac.in/2023/about-us-3/",
        "https://www.rmkec.ac.in/2023/administration/",
        "https://www.rmkec.ac.in/2023/academics/",
        "https://www.rmkec.ac.in/2023/contact-us/",
        "https://www.rmkec.ac.in/2023/training_placement/about-training-and-placement/",
        "https://www.rmkec.ac.in/2023/higher_edu/about-higher-education-cell/",
        "https://www.rmkec.ac.in/2023/ecell/about-e-cell/",
        "https://www.rmkec.ac.in/2023/dep_civil_eng/about-the-department/",
        "https://www.rmkec.ac.in/2023/computerscience_eng/about-the-department/",
        "https://www.rmkec.ac.in/2023/cs_design/about-the-department/",
        "https://www.rmkec.ac.in/2023/ee_eng/",
        "https://www.rmkec.ac.in/2023/ec_eng/",
        "https://www.rmkec.ac.in/2023/mechanical_eng/",
        "https://www.rmkec.ac.in/2023/aids/about-the-department/",
        "https://www.rmkec.ac.in/2023/btech/about-the-department/",
        "https://www.rmkec.ac.in/2023/infotech_eng/about-the-department/",
    ]
    urls=list(set(urls))
    # Load content from URLs
    documents = []
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                content = soup.get_text()
                documents.append(Document(page_content=content))
                print(f"Loaded content from {url}")
        except Exception as e:
            print(f"Failed to load content from {url}: {e}")
    
    if not documents:
        print("No content loaded from URLs")
        return
    
    # Split documents and create embeddings
    texts = text_splitter.split_documents(documents)
    vectorstore = FAISS.from_documents(texts, embedder)
    
    # Save the vectorstore
    vectorstore.save_local("vectorstore")
    print("Embeddings created and saved successfully")

if __name__ == "__main__":
    create_and_save_embeddings() 