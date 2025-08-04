import streamlit as st
import pandas as pd
import joblib

# Load the trained model pipeline
model = joblib.load("xgb_optuna_pipeline.pkl")

# --- Sample values for dropdowns (replace with actual values from your dataset) ---
town_options = ['Andover','Ansonia','Ashford','Avon','Barkhamsted','Beacon Falls','Berlin','Bethany',
 'Bethel','Bethlehem','Bloomfield','Bolton','Bozrah','Branford','Bridgeport','Bridgewater',
 'Bristol','Brookfield','Brooklyn','Burlington','Canaan','Canterbury','Canton','Chaplin',
 'Cheshire','Chester','Clinton','Colchester','Colebrook','Columbia','Cornwall','Coventry',
 'Cromwell','Danbury','Darien','Deep River','Derby','Durham','East Granby','East Haddam',
 'East Hampton','East Hartford','East Haven','East Lyme','East Windsor','Eastford',
 'Easton','Ellington','Enfield','Essex','Fairfield','Farmington','Franklin','Glastonbury',
 'Goshen','Granby','Greenwich','Griswold','Groton','Guilford','Haddam','Hamden','Hampton',
 'Hartford','Hartland','Harwinton','Hebron','Kent','Killingly','Killingworth','Lebanon',
 'Ledyard','Lisbon','Litchfield','Lyme','Madison','Manchester','Mansfield','Marlborough',
'Meriden','Middlebury','Middlefield','Middletown','Milford','Monroe','Montville',
'Morris','Naugatuck','New Britain','New Canaan','New Fairfield','New Hartford','New Haven',
 'New London', 'New Milford','Newington','Newtown','Norfolk','North Branford','North Canaan',
 'North Haven','North Stonington','Norwalk','Norwich','Old Lyme','Old Saybrook','Orange',
 'Oxford','Plainfield','Plainville','Plymouth','Pomfret','Portland','Preston','Prospect',
 'Putnam','Redding','Ridgefield','Rocky Hill','Roxbury','Salem','Salisbury','Scotland',
 'Seymour','Sharon','Shelton','Sherman','Simsbury','Somers','South Windsor','Southbury','Southington',
 'Sprague','Stafford','Stamford','Sterling','Stonington','Stratford','Suffield','Thomaston',
 'Thompson','Tolland','Torrington','Trumbull','Union','Vernon','Voluntown''Wallingford','Warren',
 'Washington','Waterbury','Waterford','Watertown','West Hartford','West Haven','Westbrook','Weston','Westport','Wethersfield',
 'Willington','Wilton''Winchester','Windham','Windsor','Windsor Locks','Wolcott', 'Woodbridge',
 'Woodbury','Woodstock']
res_type_options = ['Single Family', 'Condo', 'Two Family', 'Three Family', 'Four Family']
property_type_options = ['Residential', 'Commercial', 'Mixed Use']


import streamlit as st
import base64

# Set wide layout (optional)
st.set_page_config(layout= "centered")

# Read and encode local image
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Get base64 string
img_base64 = get_base64_of_bin_file("istockphoto-488120139-612x612.jpg")


st.title("🏠 House Price Prediction App")

# Inject CSS for top semi-transparent banner
st.markdown(
    f"""
    <style>
    .top-banner{{
        background-image: url("data:image/jpg;base64,{img_base64}");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        height: 250px;
        width: 100%;
        opacity: 1.0;
        border-radius: 0px;
        margin-bottom: 20px;
    }}
    </style>

    <div class="top-banner"></div>
    """,
    unsafe_allow_html=True
)

# Your app content starts here
st.write("Enter your property details below to estimate the sale price.")


# --- Collect user inputs ---
assessed_value = st.number_input("Assessed Value ($)", min_value=0.0, step=1000.0)

town = st.selectbox("Select Town", options=town_options)

property_type = st.selectbox("Property Type (Select Residential **ONLY**)", options=property_type_options)

res_type = st.selectbox("Residential Type", options=res_type_options)

longitude = st.number_input("Longitude", format="%.6f")
latitude = st.number_input("Latitude", format="%.6f")

# --- Make prediction ---
if st.button("Predict House Price 💰"):
    input_data = {
        "Assessed Value": [assessed_value],
        "Town": [town],
        "Property Type": [property_type],
        "Residential Type": [res_type],
        'Longitude': [longitude],
        'Latitude': [latitude]
    }

    input_df = pd.DataFrame(input_data)

    try:
        prediction = model.predict(input_df)[0]
        st.success(f"💸 Estimated Sale Price: $ {prediction:,.2f}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")




import streamlit as st

# Sidebar filter pane
st.sidebar.header("Property Filters")

# Add a clickable button or checkbox in sidebar
view_condos = st.sidebar.button("Click to view Apartments types")

# Optional: write some text or instructions
st.sidebar.markdown("Select to browse apartment types")

st.sidebar.markdown("Scroll down the main page to see the properties")

# Main area
st.title("🏠 Real Estate Explorer")

# Conditional content: shows only if user clicks the button
if view_condos:
    st.subheader("Condo Apartment")
    st.write("Explore our collection of modern condo apartments:")
    # Display images of condos (replace with actual paths or URLs)
    st.image("condo.png", caption="Modern Condo 1", use_container_width=True)

    st.subheader("Single Family")
    st.image("four family.png",use_container_width=True)

    st.subheader("More than 1 Family")
    st.image("images.jpeg", caption="Luxury Condo 2", use_container_width=True)

   # st.subheader("Two Family & More")
    #st.image("Two family house.webp",  use_container_width=True)
    #st.image("Single family.webp", use_container_width=True)
    
else:
    st.write("Use the sidebar to view property types.")


st.sidebar.markdown("### 📬 Contact Me")

st.sidebar.markdown("""
<style>
.contact-icon {
    height: 20px;
    vertical-align: middle;
    margin-right: 8px;
}
.contact-link {
    text-decoration: none;
    color: #333;
}
.contact-item {
    margin-bottom: 10px;
}
</style>

<div class="contact-item">
    <img src="https://img.icons8.com/ios-filled/50/25D366/whatsapp.png" class="contact-icon"/>
    <a href="https://wa.me/1234567890" target="_blank" class="contact-link">+91 8891206376</a>
</div>

<div class="contact-item">
    <img src="https://img.icons8.com/ios-filled/50/000000/email.png" class="contact-icon"/>
    <a href="mailto:yourname@email.com" class="contact-link">adonleobed1124@gmail.com</a>
</div>

<div class="contact-item">
    <img src="https://img.icons8.com/ios-filled/50/000000/github.png" class="contact-icon"/>
    <a href="https://github.com/yourgithub" target="_blank" class="contact-link">https://github.com/Obed11-24/homework-0#</a>
</div>

<div class="contact-item">
    <img src="https://img.icons8.com/color/48/000000/tableau-software.png" class="contact-icon"/>
    <a href="https://public.tableau.com/app/profile/yourname" target="_blank" class="contact-link">https://public.tableau.com/app/profile/obed.adonles</a>
</div>

<div class="contact-item">
    <img src="https://img.icons8.com/ios-filled/50/0A66C2/linkedin.png" class="contact-icon"/>
    <a href="https://www.linkedin.com/in/yourlinkedin" target="_blank" class="contact-link">www.linkedin.com/in/
obed-adonle-a72298376
</a>
</div>

<div class="contact-item">
    <img src="https://img.icons8.com/ios-filled/50/E4405F/instagram-new.png" class="contact-icon"/>
    <a href="https://instagram.com/yourhandle" target="_blank" class="contact-link">@delyonaudacious</a>
</div>
""", unsafe_allow_html=True)
