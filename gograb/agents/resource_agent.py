class ResourceAgent:
    def __init__(self):
        self.resources = {

            # -------- SCHOLARSHIPS --------
            "scholarship": [
                "https://www.education.gov.in/scholarships-education-loan-4",
                "https://scholarships.gov.in",
                "https://foreign.fulbrightonline.org",
                "https://www.humphreyfellowship.org",
                "https://knight-hennessy.stanford.edu",
                "https://vanier.gc.ca/en/home-accueil.html",
                "https://future.utoronto.ca/pearson/about",
                "https://www.studyinflanders.be/scholarships/master-mind-scholarships",
                "https://www.unige.ch/sciences/en/enseignements/formations/masters/excellencemasterfellowships/",
                "https://www.gov.uk/commonwealth-scholarships",
                "https://scholars4dev.com"
            ],

            # -------- RESEARCH GRANTS --------
            "research_grant": [
                "https://sparc.iitkgp.ac.in",
                "https://www.hefa.gov.in",
                "https://scholarships.unimelb.edu.au",
                "https://www.worldbank.org/en/programs/scholarships"
            ],

            # -------- FELLOWSHIPS --------
            "fellowship": [
                "https://www.dfat.gov.au/people-to-people/australia-awards/australia-awards-scholarships",
                "https://www.griffith.edu.au/international/scholarships-finance/scholarships/vice-chancellors-international-scholarship",
                "https://www.vliruos.be/en/scholarships",
                "https://www.universite-paris-saclay.fr/en/admission/scholarships-and-financial-aid"
            ],

            # -------- INTERNSHIP / OPEN SOURCE --------
            "internship": [
                "https://summerofcode.withgoogle.com",
                "https://swayam.gov.in"
            ],

            # -------- GOVERNMENT SCHEMES --------
            "government_scheme": [
                "https://www.education.gov.in/international-cooperation-cell",
                "https://www.education.gov.in/sites/upload_files/mhrd/files/document-reports/PM_Vidyalaxmi_Scheme_Guidelines.pdf"
            ],

            # -------- ENTRANCE EXAMS --------
            "entrance_exam": [
                "https://www.nta.ac.in",
                "https://yet.nta.ac.in"
            ],

            # -------- STUDENT DISCOUNTS / CONCESSIONS --------
            "students_discounts": [
                "PM Vidyalaxmi Scheme – 3% Interest Subvention (Income ≤ ₹8L)",
                "Central Sector Interest Subsidy Scheme – Full interest waiver during moratorium",
                "CUET Application Fee Concessions for OBC / SC / ST / PwD categories"
            ]
        }

    def get_resources(self, category):
        return self.resources.get(category, [])
