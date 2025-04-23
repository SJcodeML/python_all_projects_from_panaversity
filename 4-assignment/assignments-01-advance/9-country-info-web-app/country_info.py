# import streamlit as st 
# import requests

# def fetch_country_data(country_name):
#     url = f"https://restcountries.com/v3/name/{country_name}"
#     response=requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         country_data = data[0]
#         name = country_data["name"]["common"]
#         capital = country_data["capital"][0]
#         population = country_data["population"]
#         area =country_data["area"]
#         currency = country_data["currencies"]
#         region = country_data["region"]
#         return name, capital,population,area,currency,region
#     else :
#         return None
    
# def main():
#         st.title("Country information APP")

#         country_name = st.text_input("Enter a country name :")
#         if st.button ("submit"):
#          if country_name:
#             country_info  = fetch_country_data(country_name)
#             if country_info:
#                 name,capital,population ,area , currency, region = country_info

#                 st.subheader("country information")
#                 st.write(f"Name: {name}")
#                 st.write(f"Capital: {capital}")
#                 st.write(f"Population: {population}")
#                 st.write(f"Area: {area}")
#                 st.write(f"Currency: {currency}")
#                 st.write(f"Region: {region}")

#                 st.button()

#             else:
#                 st.error("Error : Country Data not found!")    


# if __name__== "__main__":
#   main()


# this code is with submit button 

import streamlit as st  
import requests  

def fetch_country_data(country_name):  
    url = f"https://restcountries.com/v3/name/{country_name}"  
    response = requests.get(url)  
    if response.status_code == 200:  
        data = response.json()  
        country_data = data[0]  
        name = country_data["name"]["common"]  
        capital = country_data["capital"][0] if "capital" in country_data else "N/A"  
        population = country_data["population"]  
        area = country_data["area"]  
        currency = list(country_data["currencies"].keys())[0] if "currencies" in country_data else "N/A"  
        region = country_data["region"]  
        return name, capital, population, area, currency, region  
    else:  
        return None  

def main():  
    st.title("Country Information App")  

    country_name = st.text_input("Enter a country name:")  

    if st.button("Submit"):  
        if country_name:  
            country_info = fetch_country_data(country_name)  
            if country_info:  
                name, capital, population, area, currency, region = country_info  

                st.subheader("Country Information")  
                st.write(f"Name: {name}")  
                st.write(f"Capital: {capital}")  
                st.write(f"Population: {population}")  
                st.write(f"Area: {area}")  
                st.write(f"Currency: {currency}")  
                st.write(f"Region: {region}")  
            else:  
                st.error("Error: Country data not found!")  
        else:  
            st.warning("Please enter a country name.")  

if __name__ == "__main__":  
    main()  