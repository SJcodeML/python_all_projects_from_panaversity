# import streamlit as st
# import pandas as pd
# import os
# from io import BytesIO


# #setup our app

# st.set_page_config(page_title='Data Sweeper' , layout='wide')
# st.title("Data Sweeper")
# st.write("Transform your File between CSV and Excel formats with built in data cleaning and visualization!")


# uploaded_files = st.file_uploader("Upload your files (CSV or Excel:)", type=["csv","xlsx"], accept_multiple_files = True)

# if uploaded_files:
#     for file in uploaded_files:
#         file_ext = os.path.splitext(file.name)[-1].lower()


       
#         if file_ext == ".csv":  
#             df = pd.read_csv(file)  
#         elif file_ext == ".xlsx":  
#             df = pd.read_excel(file)  # Change made here
#         else:
#             st.error("unsupported file type:{file_ext}")
#             continue



#          #Display info about the file 
#         st.write(f"**File Name:** {file.name}")
#         st.write(f"**File Siz** {file.size/1024}")

#          #show 5 rows of our df
#         st.write("Preview the Head of the DataFrame")
#         st.dataframe(df.head())   
         

#         #options for data cleaning 
#         st.subheader("Data cleaning options")
#         if st.checkbox(f"Clean Data for {file.name}"):
#             col1,col2 = st.columns(2)

#             with col1:
#                 if st.button(f"Remove Duplicates from {file.name}"):
#                     df.drop_duplicates(inplace = True)
#                     st.write("Duplicates Removed!") 


#             with col2:
#                 if st.button(f"Fill Missing Values for {file.name}"):
#                     numeric_cols = df.select_dtypes(incude=['number']).columns
#                     df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
#                     st.write("Missing Values have been Filled!")

           
#         # Choose Specific Columns to keep or Convert 
#         st.subheader("Select Columns to Convert")
#         columns = st.multiselect(f"Choose columns for  {file.name}" , df.columns, default=df.columns)
#         df = df[columns]


#         # Create visualization bar
#         st.subheader("Data Visualization")
#         if st.checkbox(f"Show visualization for {file.name}"):
#             st.bar_chart(df.select_dtypes(include='number').iloc[:,:2])


#         # Conversion Option    
#         st.subheader('Conversion Options')
#         conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name) 
#         if st.button(f"Convert {file.name}"):
#             buffer = BytesIO()
#             if conversion_type == "CSV":
#                 df.to_csv(buffer , index=False)
#                 file_name = file.name.replace(file_ext, ".csv")
#                 mime_type = "text/csv"

#             elif conversion_type == "Excel":
#                 df.to_excel(buffer , index=False)
#                 # df.to_excel(buffer,index=False)
#                 file_name = file.name.replace(file_ext, ".xlsx")
#                 mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#             buffer.seek(0)


#             # Download Button
#             st.download_button(
#                 label=f"Download {file.name} as {conversion_type}",
#                 data=buffer,
#                 file_name = file_name, 
#                 mime = mime_type
#             )

#         # st.success("🎉All Files processes") 
#         st.markdown('<h6 style="color:#000000;">🎉 All Files Processed Successfully!</h6>', unsafe_allow_html=True)             




import streamlit as st  
import pandas as pd  
import os  
from io import BytesIO  

# Setup the app  
st.set_page_config(page_title='Data Sweeper', layout='wide')  

# Load CSS from external file  
# def load_css():  
#     with open("styles.css") as f:  
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)  


# you can achiee the same result with this link as we do in the html 
st.markdown(
    """
    <link rel="stylesheet" href="./styles.css">
    """,
    unsafe_allow_html=True,
)        


# Apply CSS styling  
# load_css()  




# Main title  
st.markdown('<div class="main_heading">Data Sweeper!</div>', unsafe_allow_html=True)  
st.markdown('<div class="sub_heading">Transform your files between CSV and Excel formats with built-in data cleaning and visualization!</div>', unsafe_allow_html=True)  
# File uploader  
uploaded_files = st.file_uploader("Upload your files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)  

# Process uploaded files  
if uploaded_files:  
    for file in uploaded_files:  
        file_ext = os.path.splitext(file.name)[-1].lower()  

        # Read file based on extension  
        if file_ext == ".csv":  
            df = pd.read_csv(file)  
        elif file_ext == ".xlsx":  
            df = pd.read_excel(file)  
        else:  
            st.error(f"Unsupported file type: {file_ext}")  
            continue  

        # Display info about the file  
        st.markdown('<div class="file-information"> File Information...<div>',unsafe_allow_html=True)  
        
        st.markdown(f'<div class="file-data"> File Name: {file.name}</div>',unsafe_allow_html=True)
        st.markdown(f'<div class="file-data"> File Size: {file.size / 1024:.2f} KB</div>',unsafe_allow_html=True)  

        # Show DataFrame head  
        st.markdown('<div class="button">Data Preview</div>',unsafe_allow_html=True)  
        st.dataframe(df.head())  

        # Data cleaning options  
        st.markdown('<div class="button">Data Cleaning Options</div>',unsafe_allow_html=True)  
         
        if st.checkbox(f"Clean Data for {file.name}"):  
            col1, col2 = st.columns(2)  

            # with col1:  
            #     if st.button(f"Remove Duplicates from {file.name}", key=f"remove_duplicates_{file.name}"):  
            #         df.drop_duplicates(inplace=True)  
            #         st.success("Duplicates removed!")  
            with col1:
                if st.button(f"Remove Duplicates from {file.name}", key=f"remove_duplicates_{file.name}"):
                    initial_rows = len(df)
                    df.drop_duplicates(inplace=True)
                    duplicates_removed = initial_rows - len(df)
                    st.success(f"{duplicates_removed} duplicates removed!")
            # with col2:  
            #     if st.button(f"Fill Missing Values for {file.name}", key=f"fill_missing_{file.name}"):  
            #         numeric_cols = df.select_dtypes(include=['number']).columns  
            #         df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())  
            #         st.success("Missing values have been filled!")  

            with col2:
                fill_method = st.radio(
                    f"Fill Method for Missing Values in {file.name}",
                    ["Mean", "Median", "Specific Value"],
                    key=f"fill_method_{file.name}",
                )
                if st.button(f"Fill Missing Values for {file.name}", key=f"fill_missing_{file.name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    if fill_method == "Mean":
                        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    elif fill_method == "Median":
                        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
                    else:
                        fill_value = st.number_input("Enter fill value", key=f"fill_value_{file.name}")
                        df[numeric_cols] = df[numeric_cols].fillna(fill_value)
                    st.success("Missing values have been filled!")

        # Select specific columns to keep  
       
        st.markdown('<div class="button">Select Columns to Convert</div>',unsafe_allow_html=True)  
        columns = st.multiselect(f"Choose columns for {file.name}", df.columns, default=df.columns.tolist())  
        df = df[columns]  

      

        # Create visualization bar
        # st.markdown('<div class="button">Data Visualization</div>', unsafe_allow_html=True)
        # if st.checkbox(f"Show visualization for {file.name}"):
        #         st.bar_chart(df.select_dtypes(include='number').iloc[:,:2])

        st.markdown('<div class="button">Data Visualization</div>', unsafe_allow_html=True)
        if st.checkbox(f"Show visualization for {file.name}"):
            chart_type = st.selectbox("Select Chart Type", ["bar_chart", "area_chart", "line_chart", "scatter_chart"])

            numeric_df = df.select_dtypes(include='number')

            if chart_type == "bar_chart":
                st.bar_chart(numeric_df.iloc[:, :2])
            elif chart_type == "area_chart":
                st.area_chart(numeric_df.iloc[:, :2])
            elif chart_type == "line_chart":
                st.line_chart(numeric_df.iloc[:, :2])
            elif chart_type == "scatter_chart":
                st.scatter_chart(numeric_df.iloc[:, :2])
            


        # Conversion options  
        
        st.markdown('<div class="button">Conversion Options</div>',unsafe_allow_html=True) 
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)  

        if st.button(f"Convert {file.name}", key=f"convert_{file.name}"):  
            buffer = BytesIO()  
            if conversion_type == "CSV":  
                df.to_csv(buffer, index=False)  
                file_name = file.name.replace(file_ext, ".csv")  
                mime_type = "text/csv"  
            elif conversion_type == "Excel":  
                df.to_excel(buffer, index=False)  
                file_name = file.name.replace(file_ext, ".xlsx")  
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"  
            buffer.seek(0)  

            # Download button  
            st.download_button(  
                label=f"Download {file.name} as {conversion_type}",  
                data=buffer,  
                file_name=file_name,  
                mime=mime_type,  
                key=f"download_{file.name}"  
            )  

# Footer message  
            st.markdown('<div class="footer">🎉 All Files Processed Successfully!</div>', unsafe_allow_html=True)  






