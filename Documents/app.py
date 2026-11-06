import streamlit as st
import requests

st.set_page_config(page_title="Prédiction Titanic", layout="centered")
st.title("?? Prédiction de Survie du Titanic (KNN)")
st.write("Entrez les informations du passager pour interroger le modèle :")

pclass = st.selectbox("Classe du passager (1, 2 ou 3)", [1, 2, 3], index=2)
age = st.number_input("Âge du passager", min_value=0.0, max_value=100.0, value=28.0, step=1.0)
sibsp = st.number_input("Nombre de frères / sœurs / époux à bord", min_value=0, max_value=10, value=0)
parch = st.number_input("Nombre de parents / enfants à bord", min_value=0, max_value=10, value=0)
fare = st.number_input("Prix du billet (Fare)", min_value=0.0, value=32.0, step=0.5)

if st.button("Interroger l'API pour prédire", use_container_width=True):
    payload = {
        "Pclass": int(pclass),
        "Age": float(age),
        "SibSp": int(sibsp),
        "Parch": int(parch),
        "Fare": float(fare)
    }
    try:
        response = requests.post("http://api:8000/predict", json=payload)
        if response.status_code == 200:
            result = response.json()
            if result["prediction"] == 1:
                st.success(f"**Verdict :** ?? {result['status'].upper()}")
            else:
                st.error(f"**Verdict :** ?? {result['status'].upper()}")
        else:
            st.error(f"Erreur API : Code {response.status_code}")
    except requests.exceptions.ConnectionError:
        st.error("Impossible de joindre l'API. L'application tourne-t-elle sous Docker ?")
