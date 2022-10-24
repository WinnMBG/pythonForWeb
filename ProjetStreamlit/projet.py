import streamlit as st;
import pandas as pd;
import numpy as np;
import seaborn as sb;

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
st.dataframe(data=df, width=200, height=200, use_container_width=True)

#Partie 2
st.write("Quels sont les joueurs qui sont les plus prisés ?")
dft=df[(df['round']==1) | (df['round']==2)]
#sb.set_theme()
#s=sb.displot(x="position",  data=dft, kde=True, height=6, aspect=1.5)
st.bar_chart(dft,x='position',y='year')
