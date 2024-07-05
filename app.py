# %%writefile app.py
import streamlit as st
# import google.generativeai as genai
# import spacy

st.write("Hello")

# # Configure the Google Generative AI API
# GOOGLE_API_KEY = "AIzaSyDxSBgxRNK7icKH2jDHLGSbtdmVwPI8tnc"
# genai.configure(api_key=GOOGLE_API_KEY)
# model = genai.GenerativeModel(model_name="gemini-pro")

# nlp = spacy.load("en_core_web_sm")

# def get_itinerary(place, budget, days, people):
#     prompt = f"""
#     I am planning a trip to {place} for {people} people. I prefer hotels and their prices,
#     Can you suggest an itinerary with activities, top rated places to visit, dining options,
#     and transportation options (including using Ola or Uber)?, also quote the price for each ride
#     with a budget of {budget} for {days} days. You should recommend everything within the range such
#     that the total sum, including everything (hotel also), should be less than or equal to {budget}, at last give me a complete
#     summary of all my expenses and the total sum.
#     """
#     response = model.generate_content(prompt)
#     return response.text  

# def extract_places(itinerary_text, exclude_place):
#     doc = nlp(itinerary_text)
#     exclude_place_lower = exclude_place.lower()
#     places = [
#         ent.text for ent in doc.ents 
#         if ent.label_ == "GPE" and ent.text.lower() != exclude_place_lower and not any(keyword in ent.text.lower() for keyword in ["inr", "approx"])
#     ]
#     return places

# def extract_hotels(itinerary_text):
#     doc = nlp(itinerary_text)
#     hotels = [
#         ent.text for ent in doc.ents 
#         if ent.label_ == "ORG" and not any(keyword in ent.text.lower() for keyword in ["inr", "approx", "india", "₹"])
#     ]
#     return hotels

# def generate_transport_links(destination):
#     ola_link = f"https://book.olacabs.com/?drop_location={destination}"
#     uber_link = f"https://m.uber.com/ul/?action=setPickup&drop[latitude]={destination}"
#     return ola_link, uber_link

# def generate_hotel_booking_links(hotel_name):
#     make_my_trip_link = f"https://www.makemytrip.com/hotels/{hotel_name.replace(' ', '_')}"
#     ixigo_link = f"https://www.ixigo.com/hotels-in-{hotel_name.replace(' ', '-')}"
#     agoda_link = f"https://www.agoda.com/search?city={hotel_name.replace(' ', '%20')}"
#     return make_my_trip_link, ixigo_link, agoda_link


# # Custom CSS
# st.markdown("""
#     <style>
#     .main {
#         background-color: #f0f2f6;
#         padding: 2rem;
#     }
#     .stButton>button {
#         background-color: #4CAF50;
#         color: white;
#         border: none;
#         padding: 10px 20px;
#         text-align: center;
#         text-decoration: none;
#         display: inline-block;
#         font-size: 16px;
#         margin: 4px 2px;
#         cursor: pointer;
#         border-radius: 16px;
#         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#         transition: background-color 0.3s ease;
#     }
#     .stButton>button:hover {
#         background-color: #45a049;
#     }
#     .stTitle {
#         color: #ff6347;
#     }
#     .stMarkdown {
#         color: #00008b;
#         font-size: 18px;
#     }
#     .stTextInput>div>input {
#         border: 1px solid #000;
#         border-radius: 5px;
#         padding: 5px;
#     }
#     .stNumberInput>div>input {
#         border: 1px solid #000;
#         border-radius: 5px;
#         padding: 5px;
#     }
#     .header {
#         font-size: 24px;
#         font-weight: bold;
#         color: #ff6347;
#         margin-bottom: 20px;
#     }
#     .subheader {
#         font-size: 20px;
#         font-weight: bold;
#         color: #00008b;
#         margin-top: 20px;
#     }
#     .content-box {
#         background-color: #ffffff;
#         padding: 20px;
#         border-radius: 10px;
#         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#         margin-bottom: 20px;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # Streamlit app
# st.title("Travel Itinerary Planner")
# st.markdown('<div class="header">Plan Your Perfect Trip</div>', unsafe_allow_html=True)

# place = st.text_input("Enter the destination")
# budget = st.text_input("Enter your budget")

# col1, col2 = st.columns(2)
# with col1:
#     days = st.text_input("Enter the number of days of stay")
# with col2:
#     people = st.text_input("Enter the number of people")

# if st.button("Generate Itinerary"):
#     with st.spinner("Generating your itinerary..."):
#         try:
#             budget = int(budget)
#             days = int(days)
#             people = int(people)
#             itinerary = get_itinerary(place, budget, days, people)
#             st.success("Itinerary generated!")
#             st.write(itinerary)

#             # Extract places to visit from itinerary, excluding the main destination city
#             places_to_visit = extract_places(itinerary, place)

#             st.write("### Transportation Options")
#             for place in places_to_visit:
#                 ola_link, uber_link = generate_transport_links(place)
#                 st.write(f"**To {place}**")
#                 st.markdown(f"[Book Ola]({ola_link})", unsafe_allow_html=True)
#                 st.markdown(f"[Book Uber]({uber_link})", unsafe_allow_html=True)

#             # Extract hotels from the itinerary
#             hotels = extract_hotels(itinerary)

#             st.write("### Hotel Booking Options and Attractions")
#             for hotel in hotels:
#                 make_my_trip_link, ixigo_link, agoda_link = generate_hotel_booking_links(hotel)
#                 st.write(f"**{hotel}**")
#                 st.markdown(f"[Book on MakeMyTrip]({make_my_trip_link})", unsafe_allow_html=True)
#                 st.markdown(f"[Book on Ixigo]({ixigo_link})", unsafe_allow_html=True)
#                 st.markdown(f"[Book on Agoda]({agoda_link})", unsafe_allow_html=True)
#         except ValueError:
#             st.error("Please enter valid numbers for budget, days, and number of people.")
