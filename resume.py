from pathlib import Path
import streamlit as st
from PIL import Image


# Path directories of the whole project
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

main_css = current_dir / "styles" / "main.css"
profile_pic = current_dir / "assets" / "profile_pic.png"


# create all variables to be used into my resume

PAGE_TITLE = "Digital Resume | Muhammad Bilal"
PAGE_ICON = ":sunglasses:"
NAME = "Muhammad Umar Bilal"
DESCRIPTION = """<span style='font-size:25px;'>**Certified AI Developer**</span>\n
<div style="font-size: 14px;">Ex Quality Assurance and Quality Control
in Facade and Dam Construction</div>
"""
EMAIL = "mubquaidian@live.com"


P_ATTRIBUTES = [
    "Self-motivated",
    "Practical", 
    "Reliable", 
    "Honest",
]
P_ATTRIBUTES_ICONS = [
    ":male-technologist:",
    ":male-mechanic:",
    ":white_check_mark:",
    ":male-judge:",
]

HOBBIES = [ 
    "AI research", 
    "Using StackOverflow", 
    "Thinking about creativity",
    "Going for walks and hikings", 
    "Enjoying the Greener sights", 
    "Growing organic at home",
    ]

HOBBY_ICONS = [
    ":computer:",
    ":question:",
    ":thinking_face:",
    ":walking:",
    ":camping:",
    ":seedling:",
    ]

TRAVELS = [
    "Bahrain", "Germany", "Saudi Arabia", "United Arab Emirates",
]
TRAVEL_ICONS = [
    ":flag-bh:",
    ":flag-de:",
    ":flag-sa:",
    ":flag-ae:",
    ]
SOCIAL_MEDIA = {
    "Linkedin": "https://www.linkedin.com/in/muhammad-umar-bilal-umarbilallucky",
    "GitHub" : "https://github.com/mubquaidian",
    "Kaggle": "https://www.kaggle.com/muhammadumarbilal",
    "Twitter" : "https://twitter.com/Muhamma67226079",
    "Facebook": "https://www.facebook.com/profile.php?id=100075910173734",
    }


# set page configuration
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Loading files
with open(main_css) as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

profile_pic = Image.open(profile_pic)

# Hero Section.
col1, col2 = st.columns(2)
with col1:
    st.image(profile_pic, width=250)
with col2:
    st.title(NAME)
    st.write(f"{DESCRIPTION}", unsafe_allow_html=True)
    # Phone & Email
    st.write("#")
    st.write(":email:", f'<span style="font-size: 14px; line-height: 1.5;">{EMAIL}</span>', unsafe_allow_html=True)
#Personal Attributes
st.write("#")
st.write("---")
p_list = [f"{picon} {attr}" for picon, attr in zip(P_ATTRIBUTES_ICONS, P_ATTRIBUTES)]
p_str = ", ".join(p_list)
st.write(p_str)

# Qualifications
st.write('#')
st.subheader("Experience & Qualification")
st.write(
    """
- :shield: 3 Years struggle to learn AI, ML, DL, CV, NLP including getting certified in AI.
- :shield: Sufficient hands on experience and knowledge in Python.
- :shield: Good understanding of mathematics, physics, statistical principles and their corresponding applications
- :shield: Deploying and integration of AI applications to Web.
- :shield: Eager to bring ideas into life.
- :shield: 7 Years of experience as QA/QC in facade construction.
- :shield: 2 Years of experience in dam construction.
- :shield: 3+ years experience in graphic designing - part time
- :shield: 5 months of experience in teaching mathematics in Islamabad Model College.
- :shield: 2 years of experience in teaching mathematics part-time in private.
"""
)

# Skill sets
st.write('\n')
st.subheader("Skills")
st.write(f"**About My IT Skill Set:**")
x="""
I prioritize organizing my skills into five sets:\n
:one: **Python, JavaScript** to develop the applications.\n
:two: **AI, ML, DL, CV, NLP** to enhance/improve the applications.\n
:three: **Web Development(React.js, Node.js, Flask, Django, Streamlit)** to deploy the applications.\n
:four: **Microsoft Windows, Linux** Operating Systems.\n
:five: **Amazon Web Services(AWS), understanding of cloud computing, Docker**.
"""
st.write(f"{x}")
st.write("**Python**")
st.progress(75)
st.write("**JavaScript**")
st.progress(50)
st.write("**AI, ML, DL, CV, NLP**")
st.progress(65)
st.write("**Web Development(React.js, Node.js, Flask, Django, Streamlit)**")
st.progress(75)
st.write("**Linux**")
st.progress(70)
st.write("**AWS, Docker & Cloud Computing**")
st.progress(50)
st.write("**Git/GitHub for VCS**")
st.progress(70)
st.write("**Databases: Postgres, MySQL, MongoDB, Sqlite3**")
st.progress(60)
st.write("**Quality Assurance & Quality Control in Construction**")
st.progress(90)

# Hands on project experience
st.write('\n')
st.subheader("Hands on Project Experience")
st.write("Soon all the following applications will be online.....")
st.write("---")

#My Own Digital Resume
st.write(f"**1. My Digital Resume**\n")
st.write(f"**Description:**\n")
st.write('''<div style="text-align: justify">This is the current web app developed using Python and Streamlit.
         My Digital Resume showcases my career history, qualifications, skills, 
         projects, experience, contact details, and social networks. 
         It provides an overview of my current state in my career journey.</div>''', unsafe_allow_html=True)

# AI Chatbot
st.write("#")
st.write(f"**2. Speech To Text**\n")
st.write(f"**Description:**\n")
st.write('''<div style="text-align: justify">Speech To Text application has been developed using Python, Streamlit, 
         and a pre-trained machine learning model (DeepSpeech-0.9.3-models). 
         This application is designed to convert MP3 files or voice data from a 
         microphone into text. The resulting text can be downloaded as a PDF or 
         copied to the clipboard. Further development is currently underway to 
         add additional features to the application. I am also planning to train 
         and fine-tune the deepspeech model. With its ongoing development and potential for enhancement, 
         this application has the potential to become a successful AI tool.</div>''', unsafe_allow_html=True)

# Text Utils
st.write("#")
st.write(f"**3. Text Utils**\n")
st.write(f"**Description:**\n")
st.write('''<div style="text-align: justify">The Text Utils app has been developed using **React.js** and **Node.js**. 
         With this app, you can easily manipulate text in various ways. 
         It offers functionalities such as word and character counting, 
         converting text to lower case and upper case, eliminating extra 
         spaces in the text, and the ability to select and copy text to the clipboard. 
         Additionally, the app includes a convenient dark mode feature, 
         allowing you to switch to a darker color scheme for improved visibility and usability.</div>''', unsafe_allow_html=True)

# Remove Background App
st.write("#")
st.write(f"**4. Background Remover App**\n")
st.write(f"**Description:**\n")
st.write('''<div style="text-align: justify">A Background Removal application has been developed using Python, 
         Streamlit, and the PIL and rembg libraries, along with u2net models. 
         This application is designed to remove the background from photos of 
         documents on a computer. Users can upload a photo, which is then displayed 
         on the web page. After the background has been removed from the photo, 
         the processed image is also shown on the web page. Users have the option 
         to download the processed photo as well. Ongoing development is in progress 
         to add more features to the application. Additionally, there are plans to 
         train and fine-tune the u2net model. With its continuous development 
         and potential for enhancement, this application has the capability to become 
         a successful AI tool.</div>''', unsafe_allow_html=True)
st.write("[Background Remover App](https://backgroundremoverapp.streamlit.app/")

# Road Sign Detector
st.write("#")
st.write(f"**5. Road Sign Detector**\n")
st.write(f"**Description:**\n")
st.write('''<div style="text-align: justify">Road Sign Detector application has been developed using Python, 
         Streamlit. With its continuous development 
         and potential for enhancement, this application has the capability to become 
         a successful AI tool.</div>''', unsafe_allow_html=True)

# Career History
st.write('#') 
st.subheader("Career History")
st.write("---")

# Latest one
st.write(":sunny:", "**Professional Development | Self Paced**")
st.write("September 2020 - Present")
st.write(
    """
- :comet: Accomplished four semester Certification in AI by PIAIC.
- :comet: Improved skills in Python, AI, ML, DL, CV, NLP. 
- :comet: Writing AI blogs for NFAI Company.
- :comet: Making improvement in web development especially using React, Node.js, JS, JSX, Django, Flask, Streamlit to deploy the AI apps. 
- :comet: Active on Upwork.
- :comet: Recently started experimenting to create a web project in which the frontend comprises React.js and the backend is built with Django/Python. This web app will carry some AI tools, and several pre-trained ML/DL models will be used.
"""
)

# Second to Latest
st.write('#')
st.write(":sunny:", "**QA/QC Production | Inoclad Middle East FZ LLC/Inoclad Engineering GmbH**")
st.write("August 2018 - September 2020")
st.write(
    """
- :comet: Preparation of Quality Plan, work method statements, ITPs and Checklists.
- :comet: Ensuring Quality Procedures to be implemented as per client specifications.
- :comet: Maintaining Records for Quality and Safety.
- :comet: Communicated with team properly to resolve design and fabrication issues, if any.
- :comet: Supervised production team to stock final facade panels after proper packing.
- :comet: Controls logistics to send facade panels to site for installations.
- :comet: Material Receiving Inspection of Sageglass and its handling.
- :comet: Supervised repairing of Sageglass onsite along with Vetrox (Germany) & SCHÜCO (Germany), if needed.
"""
)

# Third to Latest
st.write('#')
st.write(":sunny:", "**Site Supervisor - QA/QC Inspector | Inoclad Middle East FZ LLC**")
st.write("February 2013 - March 2017")
st.write(
    """
- :comet: Prepared Quality Plan, work method statements, ITP and Checklists.
- :comet: Implemented site policies and procedures.
- :comet: Checked Quality of Production and Installation as per ITP.
- :comet: Produced and Checked Survey Reports of facade panels / Quality Documents, Progress Reports.
- :comet: Ensured Quality Procedures to be implemented.
- :comet: Maintained Records for Production.
- :comet: Supervised day to day to operations in facility.
- :comet: Evaluated quality and performance as per client specifications.- Conducted regular inspections and maintenance of systems and equipment.
- :comet: Supervised and evaluated staff; complete employee reviews; keep accurate records of employee attendance and timesheets; provide positive direction to motivate quality performance; personnel discipline when necessary and appropriate.
- :comet: Handled sensitive information with confidentiality.
- :comet: Communicated with customers regarding products and services.
- :comet: Reviewed manufacturer's products.
- :comet: Small scale procurement.
- :comet: Reviewing and approving of all associated supplier issued quality assurance and control, documentation and solved of non-conformance and deviations from suppliers during inspection life cycle.
- :comet: Monitoring and auditing the quality assurance and control activities performed in the areas of engineering and construction.
- :comet: Developing and implementing the Internal Compliance Audit Program.
- :comet: Composed cleaning and maintenance manual after facade installed.
- :comet: Facade panel installation tasks time by time when needed on site.
"""
)

# Third to Latest
st.write('#')
st.write(":sunny:", "**QA/QC Inspector | Pakistan Engineering Services(PES)**")
st.write("January 2010 - September 2011")
st.write(
    """
- :comet: Executed daily operations of supervision.
- :comet: Wrote daily and monthly progress reports.
- :comet: Monitored material performance.
- :comet: Conducted and supervised tests on raw materials and finished to determine causes of problems and to develop solutions.- Guided technical staff engaged in developing materials for specific uses in project.
- :comet: Reported maintenance problems occurring at project site to supervisors and negotiated the changes to resolve system conflicts.
- :comet: Read and reviewed project blueprints and structural specifications.
"""
)
# Construction Projects
st.write('#')
st.subheader("Accomplished Construction Projects")
st.write("---")

# create for loop which shows project 1,2 : description and so on
CONSTRUCTION_PROJECTS = {
    "Project 1 - Client: Saudi Aramco":"KACWC-ITHRA_king Abdul Aziz Center For World Culture, Dhahran, KSA",
    "Project 2 - Client: TEVA Biotech GmbH": "TEVA GENESIS Project, Ulm, Germany",
    }
# First loop to display the first key and its value
for k, v in list(CONSTRUCTION_PROJECTS.items())[:1]:
    st.write(f"**{k}**")
    st.write(":sports_medal:",f"{v}")
    st.write("[ITHRA link](https://www.ithra.com/en)")

# Second loop to display the remaining keys and their values
for k, v in list(CONSTRUCTION_PROJECTS.items())[1:]:
    st.write(f"**{k}**")
    st.write(":sports_medal:",f"{v}")
    st.write("[TEVA GENESIS link](https://www.teva.de/karriere/biotech.html)")

# Education
st.write('#')
st.subheader("Education")
st.write(":robot_face:","**Certified AI Developer**, PIAIC, Islamabad, Pakistan")
st.write(":hammer:","**M.Sc. in Geophysics**, Quad-i-Azam University, Islamabad, Pakistan")
st.write(":atom_symbol:","**B.Sc. in Mathematics & Physics**, BZU University, Multan, Pakistan")
st.write(":male-scientist:","**Higher Secondary Education**, Board of Intermediate & Secondary Education, Multan, Pakistan")

# Hobbies
st.write('#')
st.subheader("Hobbies")
st.write("---")
for icon, hobby in zip(HOBBY_ICONS, HOBBIES):
    st.write(f"{icon} {hobby}")

# Travels
st.write('#')
st.subheader("Travels")
st.write("---")
travel_list = [f"{icons} {travel}" for icons, travel in zip(TRAVEL_ICONS, TRAVELS)]
travel_str = ", ".join(travel_list)
st.write(travel_str)

# Socila media links
st.write('#')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
