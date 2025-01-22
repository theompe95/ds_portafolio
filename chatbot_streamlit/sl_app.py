import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt

from transformers import pipeline


#create tabs
demo1, demo2, demo3 = st.tabs(["Tab 1: Simple Demo", "Tab 2: Inputs Demo", "Tab 3: Chatbot Demo"])

#Tab 1
with demo1:
    
    #App Title1
    st.title("Streamlit App - Simple Demo")
    #Some write
    st.write("Data AI team Streamlit Demo")
    st.markdown("---") 
    
    #Button
    st.subheader("Button Demo")
    if st.button("Click Me!"):
        st.success("You clicked the button!")
    st.markdown("---") 
    
    #drop down
    st.subheader("Dropdown Demo")
    options = ["Option 1", "Option 2", "Option 3", "Option 4"]
    selected_option = st.selectbox("Choose an option", options)
    st.write(f"You selected: {selected_option}")
    st.markdown("---") 
    
    
    #Slider
    st.subheader("Slider Demo")
    age = st.slider("Select a number", 0, 100, 25)
    st.write(f"You selected: {age}")
    st.markdown("---") 
    
    
    #DF view
    st.subheader("Dataframe view  Demo")
    data = pd.DataFrame({"Name": ["Theo", "Bob"], "Age": [29, 30]})
    st.dataframe(data)
    st.markdown("---") 
    


#Tab 2
with demo2:
    
     #App Title2
    st.title("Streamlit App - Inputs Demo")
    #Some write
    st.write("Data AI team Streamlit Demo")
    st.markdown("---") 
    
    #Ploting -sample data
    st.subheader("Simple Plot  Demo")
    st.write("Enter Data Points separated by a comma")
        #get vals
    x_values = st.text_input("Enter x values (comma-separated)", "1, 2, 3, 4, 5")
    y_values = st.text_input("Enter y values (comma-separated)", "10, 20, 30, 40, 50")
    x = [float(i.strip()) for i in x_values.split(",")]
    y = [float(i.strip()) for i in y_values.split(",")]
        #plot
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title(" Line Plot")
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.legend()
        #display plot
    st.pyplot(fig)
    st.markdown("---") 
    
    
    
    #File Upload and read
    st.subheader("Upload CSV and display Demo")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        try:
            #Read CSV
            df = pd.read_csv(uploaded_file)
            
            #display
            st.write("Here is the content of your CSV file:")
            st.dataframe(df)
        except Exception as e:
            st.error(f"Error reading the file: {e}")
    else:
        st.write("Please upload a CSV file to display.")
        
#Tab 3
with demo3:

    #App Title3
    st.title("Streamlit App - Chatbot Demo")
    #Some write
    st.write("Data AI team Streamlit Demo")
    st.markdown("---")
    
    #simple chatbot using wrap dace
    st.subheader("Chatbot Demo - Using Hugging Face Model")
    st.write("Provide a context or passage of information for the model to process, then ask a specific question related to that context. The model will analyze the context and generate an answer based on the information provided.")
    #learning text
    context = st.text_area("Enter context (text for learning):")
    #question
    question_input = st.text_input("Enter question:")
    
    #model
    qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")
    
    if st.button("Get Answer"):
        if context and question_input:
            response = qa_pipeline(question=question_input, context=context)
            st.write(f"Answer: {response['answer']}")
        else:
            st.write("Please enter both context and a question to get an answer.")

#
