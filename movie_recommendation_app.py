import joblib
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Film Öneri Sistemi", page_icon="🎬", layout="centered"
)


@st.cache_resource
def load_data():
  sim_matrix = joblib.load("cosine_sim.pkl")
  processed_df = joblib.load("netflix_processed.pkl")
  return sim_matrix, processed_df


cosine_sim, df = load_data()
indices = pd.Series(df.index, index=df["title"]).drop_duplicates()

st.title("🎬 İçerik Tabanlı Film Öneri Sistemi")
st.write(
    "İzlediğiniz veya sevdiğiniz bir film adını girin, yapay zeka size benzer"
    " türde ve konudaki en iyi filmleri önersin!"
)

# Film seçimi için arayüz
movie_list = df["title"].values
selected_movie = st.selectbox(
    "Bir Film / Dizi Seçin veya Yazın:", movie_list
)

if st.button("Öneri Al"):
  if selected_movie:
    idx = indices[selected_movie]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]

    st.subheader(f"'{selected_movie}' Filmine Benzer Öneriler:")

    for i, movie_idx in enumerate(movie_indices, 1):
      row = df.iloc[movie_idx]
      with st.expander(f"{i}. {row['title']} ({row['release_year']})"):
        st.write(f"**Türler:** {row['listed_in']}")
        st.write(f"**Süre / Sezon:** {row['duration']}")
        st.write(f"**Açıklama:** {row['description']}")