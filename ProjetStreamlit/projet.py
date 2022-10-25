import streamlit as st;
import pandas as pd;
import numpy as np;
import seaborn as sb;
import matplotlib.pyplot as plt;

#headers + text
st.title("Projet DataAnalysis")
st.header("NFL Draft Players")
st.subheader("MBOURANGA Winn-Elie")
st.text("La NFL (National Football League) est soumise chaque année à un système proche du mercato dans d'autres sport qui s'appelle la Draft. Elle permet aux équipes de la ligue de pouvoir sélectionner les joueurs qu'elle désire signer.\nDans la draft, il y a 16 à 17 tours (cela dépend des années...) pour 32 choix à chaque tour. Les joueurs professionnels en devenir (Prospect) sont donc choisit selon certains critères que les équipes recherchent.")
st.text(repr("A travers ce notebook, nous allons voir ensemble quelles caractéristiques influent sur la position des joueurs de la draft ?"))

#Dataframe
st.code("import pandas as pd\nimport numpy as np\nimport seaborn as sb\nimport matplotlib.pyplot as plt")
df=pd.read_csv('./nfl_draft_1970-2021.csv')
st.header("Importation de notre fichier de datas")
def on_change_slider(year):
    return st.dataframe(data=df[df["year"]==year], width=200, height=200, use_container_width=True)
annee = st.slider('Choisissez une année afin de voir le dataframe en fonction de celle de la draft',min_value=1970,max_value=2021)
on_change_slider(annee)

#Partie 2
st.write("Quels sont les joueurs qui sont les plus prisés ?")
dft=df[(df['round']==1) | (df['round']==2)]
st.bar_chart(dft,x='position',y='year')

#Partie 3
st.write("Performances et statistiques des joueurs")
def on_change_barchart(number):
    st.bar_chart(data=df[df["age"]==number], x="age", y="round")
age=st.number_input('Choisissez un age', min_value=19, max_value=29)
on_change_barchart(age)

st.write("Nombre de parties jouée en fonction du tour de la draft")
st.line_chart(data=df,x="round",y="games")

st.write("Nombre de rush ayant généré un touchdown en fonction du tour de la draft")
st.line_chart(data=df[df["rush_tds"] != 0],x="round",y="rush_tds")

st.write("Nombre de passes ayant généré un touchdown en fonction du tour de la draft")
st.line_chart(data=df[df["pass_tds"] != 0],x="round",y="pass_tds")

st.write("Corrélation positive ou négative ?")
df_corr= pd.DataFrame({
    'round': df['round'],
    'age':df['age'],
    'games':df['games'],
    'rush_yds':df['rush_yards'],
    'pass_yds':df['pass_yards'],
    'rush_tds':df['rush_tds'],
    'pass_tds':df['pass_tds'],
    'receptions':df['receptions'],
})

df_corr.fillna('unknown')
st.write("Voici notre dataframe que nous aurons besoin pour notre étude de la corrélation")
st.write(df_corr)
st.write("Table de corrélation :")
corr=df_corr.corr()
st.write(corr)
st.write("Voici notre heatmap:")
f, ax = plt.subplots(figsize=(20,5))
sb.heatmap(corr, annot=True, ax =ax)
st.write(f)
st.write("==> Corrélation plutôt négative d'après ce heatmap.\n")
st.write("5. Conclusion\nPour conclure, on peut dire que ces caractéristiques sont influentes dans le choix de la draft car en globalité, nous avons vu que plus nous allions dans les derniers rounds, moins les performances étaient correctes.")

st.snow()
