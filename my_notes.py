import streamlit as st
import os
st.title("WELCOME TO ALI NOTES")
st.divider()
st.caption("Introduction : This pages contains notes prepared, lectures delivered by Mohd Ali on his YouTube channel. Further some of the exciting quizzes will also be added")
st.subheader("YouTube Channel : Mohd Ali")
st.write("https://youtube.com/@mohdali-d9g8b?si=JOOuljPCuRUIXB3z")
st.divider()
tabs1,tabs2,tabs3=st.tabs(["📝 Lecture Notes", "▶️ Video Lectures", "💡 Quizzes"])
if "admin_verified" not in st.session_state:
    st.session_state.admin_verified=False
user_role=st.selectbox("Select Your Role:",
                       ["Admin","User"])
if "role_submitted" not in st.session_state:
    st.session_state.role_submitted=False
if(st.button("Submit Your Role",type="primary")):
    st.session_state.role_submitted=True
if(st.session_state.role_submitted):
    # if(user_role=="User"):
    #     os.makedirs("notes", exist_ok=True)
    #     for file in os.listdir("notes"):
    #         if file.endswith(".pdf"):
    #             st.header(file)
    #             st.pdf(os.path.join("notes",file),key=file)
    #             st.divider()
    if(user_role=="Admin"):
        admin_user_name=st.text_input("Enter admin's username : ")
        admin_passkey=st.text_input("Enter admin's passkey : ")
        if(st.button("Submit",type="primary")):
            if(admin_user_name==st.secrets["ADMIN_USERNAME"] and admin_passkey==st.secrets["ADMIN_PASSKEY"]):
                st.success("Credentials matched..!")
                st.session_state.admin_verified=True
            else:
                st.error("Try again..!")
    if "upload_notes" not in st.session_state:
        st.session_state.upload_notes=False
    os.makedirs("notes",exist_ok=True)
    #first tab for storing notes
    with tabs1:
        os.makedirs("notes", exist_ok=True)
        pdf_files = [file for file in os.listdir("notes") if file.endswith(".pdf")]

        if not pdf_files:
            st.info("📭 No lecture notes have been added yet.")
        for file in pdf_files:
            if file.endswith(".pdf"):
                name_path=os.path.join("notes",file+".txt")
                if(os.path.exists(name_path)):
                    with open(name_path,"r") as name_file:
                        notes_name=name_file.read()
                    st.header(notes_name)
                else:
                    st.header(file)
                st.pdf(os.path.join("notes",file),key=file)
                st.divider()
        if st.session_state.admin_verified:
            if st.button("Upload lecture Notes",type="primary"):
                st.session_state.upload_notes=True
            if(st.session_state.upload_notes):
                notes_name=st.text_input("Enter name of your lecture notes:")
                uploaded_file=st.file_uploader("Select your lecture notes:",
                                                    type=["pdf"])
                if uploaded_file is not None:
                    if(st.button("Save Notes",type="primary")):
                        # os.makedirs("notes",exist_ok=True)
                        file_path=os.path.join("notes",uploaded_file.name)
                        with open(file_path,"wb") as file:
                            file.write(uploaded_file.getbuffer())
                        name_path=os.path.join("notes",uploaded_file.name+".txt")
                        with open(name_path,"w") as file:
                            file.write(notes_name)
                        st.success("Lecture Notes added successfully..!")
with tabs2:
    st.caption("Video lectures will be uploaded soon...")
with tabs3:
    st.caption("Quizzes will be added soon...")