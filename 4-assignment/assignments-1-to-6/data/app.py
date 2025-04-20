        
import streamlit as st  
import pandas as pd  
import os  
from io import BytesIO  

print("Current working directory:", os.getcwd())

# Setup the app  
st.set_page_config(page_title='Data Sweeper', layout='wide')  

 





st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@400;700&display=swap');

        /* Base styles */
        * {
            font-family: 'Roboto Slab', serif;
        }

        /* Heading styles */
        .main_heading {
            font-size: 40px;
            color: rgb(139, 79, 79);
        }

        .sub_heading {
            background-color: rgb(237, 176, 158);
            color: white;
            padding: 10px 15px;
            border-radius: 5px;
            text-align: center;
            margin: 20px 0 15px;
            font-size: 25px;
            border: none;
        }

        /* File information styles */
        .file-information {
            font-size: 28px;
            color: rgb(49, 41, 41);
            margin-bottom: 20px;
        }

        .file-data {
            font-size: 18px;
            color: rgb(89, 61, 61);
            margin-bottom: 20px;
        }

        /* Other styles */
        .chng {
            font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
        }

        .main {
            background-color: rgb(237, 176, 158);
            padding: 20px;
        }

        .heading4 {
            color: rgb(188, 143, 143);
            font-size: large;
        }

        .button {
            background-color: rgb(237, 176, 158);
            color: white;
            padding: 3px 15px;
            border-radius: 5px;
            text-align: center;
            margin: 5px 0 30px;
            font-size: 24px;
            border: none;
        }

        .footer {
            text-align: center;
            color: rgb(197, 91, 91);
            font-size: 28px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)





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






