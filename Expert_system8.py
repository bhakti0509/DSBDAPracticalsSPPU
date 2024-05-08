import streamlit as st
from typing import List

knowledge_base = {
    "cold" : [
        "1: Tylenol",
        "2: Panadol",
        "3: Nasal spray",
        "4: Please wear warm clothes!"
    ],

    "influenza": [
        "1: Tamiflu"
        "2: Panadol",
        "2: Zanamivir",
        "4: Please take a warm bath and do salt gargling!"
    ],

    "typhoid": [
        "1: Chloramphenicol",
        "2: Amoxicillin",
        "3: Ciproflaxacin",
        "4: Azithromycin",
        "5: Please do complete bed rest and take soft diet!"
    ],

    "chicken pox" : [
        "1: Varicella vaccine",
        "2: Immunoglobulin",
        "3: Acetomenaphin",
        "4: Acyclovir",
        "5: Please do have have oatmeal and stay at home!"
    ],

    "measles" : [
        "1: Tylenol",
        "2: Aleve",
        "3: Advil",
        "4: Vitamin A",
        "5: Please get rest and use more liquid!"
    ],   

    "malaria" : [
        "1: Aralen",
        "2: Qualaquin",
        "3: Plaquenil",
        "4: Mefloquine",
        "5: Please do not sleep in open air and cover your full skin!"
    ]
}

st.header("Medical Diagnosis Expert System")

def respond(input: List[str]):
    symptoms = input
    if (len(symptoms) == 3):
        if (symptoms[0] == "rash" or "fever" or "body ache" and symptoms[1] == "body ache" or "rash" or  "fever" and symptoms[2] == "fever" or "rash" or "body ache"):
            st.write("You have chicken pox!")
            st.write("Please take the following medicines and precautions-")
            for i in knowledge_base["chicken pox"]:
                st.write(i)
            st.write("Only recommended for people above age 20")
            st.write("Prescribed by Dr. XYZ")
        else:
            st.write("Question is not present in the knowledge base!\nCould you please enter the appropriate answer for the question below-")
            answer = st.text_input("Answer")
            add = st.button("Add answer")
            if (add):
                for key in symptoms:
                    knowledge_base[key] = [answer]
    elif (len(symptoms) == 4):
        if (symptoms[0] == "headache" or "runny nose" or "sneezing" or "sore throat" and symptoms[1] == "runny nose" or "sore throat" or  "headache" or "sneezing" and symptoms[2] == "sneezing" or "runny nose" or "sore throat" or  "headache" and symptoms[3] == "sore throat" or "headache" or "runny nose" or "sneezing"):
            st.write("You have cold!")
            st.write("Please take the following medicines and precautions-")
            for i in knowledge_base["cold"]:
                st.write(i)
            st.write("Only recommended for people above age 20")
            st.write("Prescribed by Dr. ABC")
        elif (symptoms[0] == "headache" or "abdominal pain" or "poor appetite" or "fever" and symptoms[1] == "abdominal pain" or "poor appetite" or "fever" or "headache" and symptoms[2] == "poor appetite" or "headache" or "abdominal pain" or "fever" and symptoms[3] == "fever" or "poor appetite" or "headache" or "abdominal pain"):
            st.write("You have typhoid!")
            st.write("Please take the following medicines and precautions-")
            for i in knowledge_base["typhoid"]:
                st.write(i)
            st.write("Only recommended for people above age 20")
            st.write("Prescribed by Dr. PQR")
        elif (symptoms[0] == "fever" or "conjunctivitis" or "rash" or "runny nose" and symptoms[1] == "runny nose" or "fever" or "conjunctivitis" or "rash" and symptoms[2] == "rash" or  "runny nose" or "fever" or "conjunctivitis" and symptoms[3] == "conjunctivitis" or "rash" or  "runny nose" or "fever"):
            st.write("You have measles!")
            st.write("Please take the following medicines and precautions-")
            for i in knowledge_base["measles"]:
                st.write(i)
            st.write("Only recommended for people above age 20")
            st.write("Prescribed by Dr. LMN")
        else:
            st.write("Question is not present in the knowledge base!\nCould you please enter the appropriate answer for the question below-")
            answer = st.text_input("Answer")
            add = st.button("Add answer")
            if (add):
                for key in symptoms:
                    knowledge_base[key] = [answer]
    elif (len(symptoms) == 5):
        if (symptoms[0] == "sore throat" or "fever" or "headache" or "chills" or "body ache" and symptoms[1] == "fever" or "headache" or "chills" or "body ache" or "sore throat" and symptoms[2] == "headache" or "chills" or "body ache" or "sore throat" or "fever" and symptoms[3] == "chills" or "body ache" or "sore throat" or "fever" or "headache" and symptoms[4] == "body ache" or "sore throat" or "fever" or "headache" or "chills"):
            st.write("You have influenza!")
            st.write("Please take the following medicines and precautions-")
            for i in knowledge_base["influenza"]:
                st.write(i)
            st.write("Only recommended for people above age 20")
            st.write("Prescribed by Dr. XYZ")
        else:
            st.write("Question is not present in the knowledge base!\nCould you please enter the appropriate answer for the question below-")
            answer = st.text_input("Answer")
            add = st.button("Add answer")
            if (add):
                for key in symptoms:
                    knowledge_base[key] = [answer]
    elif (len(symptoms) == 6):
        if (symptoms[0] == "fever" or "sweating" or "headache" or "nausea" or "vomiting" or "diahrrea" and symptoms[1] == "sweating" or "headache" or "nausea" or "vomiting" or "diahrrea" or "fever" and symptoms[2] == "headache" or "nausea" or "vomiting" or "diahrrea" or "fever" or "sweating" and symptoms[3] == "nausea" or "vomiting" or "diahrrea" or "fever" or "sweating" or "headache" and symptoms[4] == "vomiting" or "diahrrea" or "fever" or "sweating" or "headache" or "nausea"and symptoms[5] == "diahrrea" or "fever" or "sweating" or "headache" or "nausea" or "vomiting"):
            st.write("You have malaria!")
            st.write("Please take the following medicines and precautions-")
            for i in knowledge_base["malaria"]:
                st.write(i)
            st.write("Only recommended for people above age 20")
            st.write("Prescribed by Dr. XYZ")
        else:
            st.write("Question is not present in the knowledge base!\nCould you please enter the appropriate answer for the question below-")
            answer = st.text_input("Answer")
            add = st.button("Add answer")
            if (add):
                for key in symptoms:
                    knowledge_base[key] = [answer]

if __name__ == "__main__":
    options = st.multiselect(
    'What are your symptoms?',
    ["headache", "runny nose", "sneezing", "sore throat", "fever", "chills", "body ache", "abdominal pain", "poor appetite", "rash", "conjunctivitis", "sweating", "nausea", "vomiting", "diahrrea"],
    [])

    col1, col2 = st.columns([1,0.1])
    with col1:
        ask = st.button("Ask")
    with col2:
        quit = st.button("Quit")
    if (ask):
        respond(options)
    if (quit):
        st.write("Thank you for using the Expert system!")
