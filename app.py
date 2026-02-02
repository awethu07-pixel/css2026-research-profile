import streamlit as st
import pandas as pd
import os

# -------------------------------
# Base folder for all files/images
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# -------------------------------

# Set page title
st.set_page_config(page_title="BFTSS | Biotechnology & Food Technology Student Society", layout="wide")

# -------------------------------
# Sidebar
# -------------------------------
logo_path = os.path.join(BASE_DIR, "logo.jpg")
st.sidebar.image(logo_path, width=150)

st.sidebar.markdown("### Welcome to BFTSS")
st.sidebar.markdown("Empowering Biotechnology & Food Technology students.")

st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Navigate:",
    ["About BFTSS", "Constitution & Governance", "Committee Members", "Events & Skills", "Highlights", "Contact & Feedback"],
)

# -------------------------------
# ABOUT BFTSS
# -------------------------------
if menu == "About BFTSS":
    st.title("Biotechnology & Food Technology Student Society (BFTSS)")

    st.subheader("Who We Are")
    st.write(
        "A student society **for the students, by the students**, focused on Biotechnology "
        "and Food Technology."
    )

    st.subheader("Our Mandate")
    st.markdown("""
    - Foster academic stewardship  
    - Upskill postgraduate and undergraduate students  
    - Build a network of Biotechnology & Food Technology graduates  
    - Enable knowledge sharing and research growth  
    """)

    if os.path.exists(logo_path):
        st.image(logo_path, caption="BFTSS Logo", width=250)
    else:
        st.warning("Logo image not found.")

# -------------------------------
# CONSTITUTION & GOVERNANCE
# -------------------------------
elif menu == "Constitution & Governance":
    st.title("BFTSS Constitution & Governance")
    st.write("This document outlines the roles, responsibilities, and governance of BFTSS.")

    # Constitution PDF
    constitution_path = os.path.join(BASE_DIR, "BFTSS_Constitution.pdf")
    if os.path.exists(constitution_path):
        with open(constitution_path, "rb") as file:
            st.download_button(
                label="Download the BFTSS Constitution",
                data=file,
                file_name="BFTSS_Constitution.pdf",
                mime="application/pdf"
            )
    else:
        st.warning("Constitution PDF not found.")

# -------------------------------
# COMMITTEE MEMBERS
# -------------------------------
elif menu == "Committee Members":
    st.title("BFTSS Executive Committee")
    st.markdown("<br>", unsafe_allow_html=True)

    members = [
        ("Chairperson", "Thulani Nkosi", "Thulani.jpg"),
        ("Vice Chairperson", "Lordy Molisho", "Lordy.jpg"),
        ("Secretary-General", "Mamabolo Majakane", "Mamabolo.jpg"),
        ("Project Manager", "Tshedza Muthumuni", "Tshedza.jpg"),
        ("Academic Quality Officer", "S’phamandla Msomi", "Sphamandla.jpg"),
        ("Academic Mentor", "Portia Mziyako", "Portia.jpg"),
        ("Academic Mentor", "Tumelo Phasha", "Tumelo.jpg"),
        ("Communication & Marketing Officer", "Amahle Mncwango", "Amahle.jpg"),
        ("Treasurer", "Mercy Shibalabala", "Mercy.jpg"),
    ]

    for role, name, image_file in members:
        image_path = os.path.join(BASE_DIR, image_file)
        col1, col2 = st.columns([1, 4])
        with col1:
            if os.path.exists(image_path):
                st.image(image_path, width=120)
            else:
                st.warning(f"Image not found: {image_file}")
        with col2:
            st.markdown(f"### {name}")
            st.write(f"**{role}**")
        st.divider()

# -------------------------------
# EVENTS & SKILLS
# -------------------------------
elif menu == "Events & Skills":
    st.title("Events, Skills & Academic Activities")

    # Event table
    events = pd.DataFrame({
        "Event": [
            "Postgraduate Seminars",
            "Braai Top Achiever Event",
            "Women's Day Event",
            "Departmental Research Day",
            "Writing & Data Analysis Training"
        ],
        "Month": ["March", "August", "August", "Throughout the Year", "Throughout the Year"]
    })
    st.dataframe(events, use_container_width=True)

    st.subheader("What We Focus On")
    st.markdown("""
    - Research writing skills  
    - Data analysis training  
    - Networking & conference sharing  
    - Academic mentorship  
    """)

    # LinkedIn icons
    st.subheader("Follow Us on LinkedIn")
    linkedin_images = [
        "linkedin1.jpg",
        "linkedin2.jpg",
        "linkedin3.jpg",
        "linkedin4.jpg",
        "linkedin5.jpg",
        "linkedin6.jpg",

    ]
    linkedin_url = "https://www.linkedin.com/company/biotechnology-and-food-technology-student-society-university-of-johannesburg/"
    cols = st.columns(len(linkedin_images))
    for col, img_file in zip(cols, linkedin_images):
        img_path = os.path.join(BASE_DIR, img_file)
        if os.path.exists(img_path):
            col.image(img_path, width=80)
            col.markdown(f"[BFTSS on LinkedIn]({linkedin_url})", unsafe_allow_html=True)
        else:
            col.warning(f"Image not found: {img_file}")
    st.divider()

# -------------------------------
# HIGHLIGHTS
# -------------------------------
elif menu == "Highlights":
    st.title("Highlights & Submissions")
    st.write(
        "Students and staff can submit academic papers, graduation highlights, "
        "research achievements, or event photos for BFTSS to feature on our platforms."
    )
    st.info("Submissions may be featured on BFTSS social media and official communication channels.")

    uploaded_file = st.file_uploader("Upload a CSV (Name, Title, Description, Year)", type="csv")
    if uploaded_file:
        highlights = pd.read_csv(uploaded_file)
        st.dataframe(highlights)

        keyword = st.text_input("Search by keyword")
        if keyword:
            filtered = highlights[
                highlights.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
            ]
            st.write("Filtered Results:")
            st.dataframe(filtered)

# -------------------------------
# CONTACT & FEEDBACK
# -------------------------------
elif menu == "Contact & Feedback":
    st.title("Contact & Feedback")
    st.write("We value your ideas and suggestions.")

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    feedback = st.text_area("Your message / suggestion")

    if st.button("Submit"):
        st.info("Your submission is anonymous unless you include your name.")
        st.success("Thank you for your feedback! BFTSS will review it.")

    st.caption("Communication & Marketing Officer: Amahle Mncwango")
















































# import streamlit as st
# import pandas as pd
# #import numpy as np



# # Dummy STEM data
# physics_data = pd.DataFrame({
#     "Experiment": ["Alpha Decay", "Beta Decay", "Gamma Ray Analysis", "Quark Study", "Higgs Boson"],
#     "Energy (MeV)": [4.2, 1.5, 2.9, 3.4, 7.1],
#     "Date": pd.date_range(start="2024-01-01", periods=5),
# })

# astronomy_data = pd.DataFrame({
#     "Celestial Object": ["Mars", "Venus", "Jupiter", "Saturn", "Moon"],
#     "Brightness (Magnitude)": [-2.0, -4.6, -1.8, 0.2, -12.7],
#     "Observation Date": pd.date_range(start="2024-01-01", periods=5),
# })

# weather_data = pd.DataFrame({
#     "City": ["Cape Town", "London", "New York", "Tokyo", "Sydney"],
#     "Temperature (°C)": [25, 10, -3, 15, 30],
#     "Humidity (%)": [65, 70, 55, 80, 50],
#     "Recorded Date": pd.date_range(start="2024-01-01", periods=5),
# })



#     # Collect basic information
#     name = "Dr. Jane Doe"
#     field = "Astrophysics"
#     institution = "University of Science"

#     # Display basic profile information
#     st.write(f"**Name:** {name}")
#     st.write(f"**Field of Research:** {field}")
#     st.write(f"**Institution:** {institution}")
    
#     st.image(
#     "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg",
#     caption="Nature (Pixabay)"
# )

# elif menu == "Publications":
#     st.title("Publications")
#     st.sidebar.header("Upload and Filter")





    # # Upload publications file
    # uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")
    # if uploaded_file:
    #     publications = pd.read_csv(uploaded_file)
    #     st.dataframe(publications)

    #     # Add filtering for year or keyword
    #     keyword = st.text_input("Filter by keyword", "")
    #     if keyword:
    #         filtered = publications[
    #             publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
    #         ]
    #         st.write(f"Filtered Results for '{keyword}':")
    #         st.dataframe(filtered)
    #     else:
    #         st.write("Showing all publications")

    #     # Publication trends
    #     if "Year" in publications.columns:
    #         st.subheader("Publication Trends")
    #         year_counts = publications["Year"].value_counts().sort_index()
    #         st.bar_chart(year_counts)
    #     else:
    #         st.write("The CSV does not have a 'Year' column to visualize trends.")

 

#     # Tabbed view for STEM data
#     data_option = st.sidebar.selectbox(
#         "Choose a dataset to explore", 
#         ["Physics Experiments", "Astronomy Observations", "Weather Data"]
#     )

#     if data_option == "Physics Experiments":
#         st.write("### Physics Experiment Data")
#         st.dataframe(physics_data)
#         # Add widget to filter by Energy levels
#         energy_filter = st.slider("Filter by Energy (MeV)", 0.0, 10.0, (0.0, 10.0))
#         filtered_physics = physics_data[
#             physics_data["Energy (MeV)"].between(energy_filter[0], energy_filter[1])
#         ]
#         st.write(f"Filtered Results for Energy Range {energy_filter}:")
#         st.dataframe(filtered_physics)

#     elif data_option == "Astronomy Observations":
#         st.write("### Astronomy Observation Data")
#         st.dataframe(astronomy_data)
#         # Add widget to filter by Brightness
#         brightness_filter = st.slider("Filter by Brightness (Magnitude)", -15.0, 5.0, (-15.0, 5.0))
#         filtered_astronomy = astronomy_data[
#             astronomy_data["Brightness (Magnitude)"].between(brightness_filter[0], brightness_filter[1])
#         ]
#         st.write(f"Filtered Results for Brightness Range {brightness_filter}:")
#         st.dataframe(filtered_astronomy)

#     elif data_option == "Weather Data":
#         st.write("### Weather Data")
#         st.dataframe(weather_data)
#         # Add widgets to filter by temperature and humidity
#         temp_filter = st.slider("Filter by Temperature (°C)", -10.0, 40.0, (-10.0, 40.0))
#         humidity_filter = st.slider("Filter by Humidity (%)", 0, 100, (0, 100))
#         filtered_weather = weather_data[
#             weather_data["Temperature (°C)"].between(temp_filter[0], temp_filter[1]) &
#             weather_data["Humidity (%)"].between(humidity_filter[0], humidity_filter[1])
#         ]
#         st.write(f"Filtered Results for Temperature {temp_filter} and Humidity {humidity_filter}:")
#         st.dataframe(filtered_weather)
        
        

# elif menu == "Contact":
#     # Add a contact section
#     st.header("Contact Information")
#     email = "jane.doe@example.com"
#     st.write(f"You can reach me at {email}.")