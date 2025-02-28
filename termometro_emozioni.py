import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Imposta lo sfondo verde chiaro
st.markdown(
    """
    <style>
    body {
        background-color: #d4edda; /* Verde chiaro */
    }
    h2 {
        font-size: 22px;
    }
    h3 {
        font-size: 20px;
    }
    .large-text {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        color: #2d6a4f; /* Verde scuro */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Titolo e autore
st.title("😊 Termometro delle Emozioni")
st.write("### Creato da Andrea Bertelli ©")

# Istruzioni per la compilazione
st.subheader("📝 Istruzioni")
st.write("""
Questo strumento ti aiuterà a monitorare il tuo stato emotivo in modo semplice e immediato.  
- **Assegna un punteggio da 1 a 10** a ciascuna emozione.  
- **1 = intensità minima**, **10 = intensità massima**.  
- Il test **non registra né invia i tuoi dati**: è solo un aiuto personale per comprendere il tuo equilibrio emotivo.  
- Alla fine, otterrai **un'analisi dettagliata** con consigli su come migliorare la gestione delle emozioni.  
""")

# Emozioni positive e negative con spiegazioni
st.subheader("🎭 Le tue Emozioni")

emozioni_positive = {
    "Fiducia in me stesso": "Mi sento sicuro delle mie capacità e pronto ad affrontare le sfide.",
    "Energia": "Mi sento carico e pieno di vitalità per affrontare la giornata.",
    "Motivazione": "Ho voglia di impegnarmi e raggiungere i miei obiettivi.",
    "Concentrazione": "Riesco a focalizzarmi su ciò che sto facendo senza distrazioni.",
    "Serenità": "Mi sento tranquillo e in pace con me stesso e con gli altri."
}

emozioni_negative = {
    "Ansia": "Mi sento nervoso o preoccupato per situazioni attuali o future.",
    "Stress": "Mi sento sotto pressione e sovraccarico di impegni.",
    "Frustrazione": "Provo insoddisfazione o irritazione per situazioni che non vanno come vorrei.",
    "Tristezza": "Mi sento giù di morale o demotivato.",
    "Rabbia": "Sento tensione o fastidio per qualcosa che mi ha fatto arrabbiare."
}

# Creazione degli slider per le emozioni
punteggi_positive = []
punteggi_negative = []

st.subheader("🌟 **Emozioni Positive**")
for emozione, descrizione in emozioni_positive.items():
    st.markdown(f"### **{emozione}**")
    st.write(f"*{descrizione}*")  
    punteggio = st.slider(f"{emozione}", 1, 10, 5, key=emozione)
    punteggi_positive.append(punteggio)

st.subheader("⚡ **Emozioni Negative**")
for emozione, descrizione in emozioni_negative.items():
    st.markdown(f"### **{emozione}**")
    st.write(f"*{descrizione}*")  
    punteggio = st.slider(f"{emozione}", 1, 10, 5, key=emozione)
    punteggi_negative.append(punteggio)

# Calcolo della media delle emozioni
media_positive = np.mean(punteggi_positive)
media_negative = np.mean(punteggi_negative)
bilancio_emotivo = media_positive - media_negative  # Differenza tra emozioni positive e negative

st.subheader(f"📊 **Bilancio Emotivo: {bilancio_emotivo:.1f}**")

# Interpretazione con 5 categorie
st.subheader("📊 Interpretazione del tuo stato emotivo")

if bilancio_emotivo >= 5:
    st.success("**Equilibrio Emotivo Ottimale ✅** - Ottima gestione delle emozioni!")
    st.write("""
    **Consigli per mantenere il benessere emotivo:**  
    - Continua a coltivare la fiducia in te stesso e la positività.  
    - Mantieni sane abitudini di gestione dello stress come sport e momenti di relax.  
    - Condividi le tue emozioni con chi ti è vicino per consolidare il tuo equilibrio.  
    """)

elif bilancio_emotivo >= 2:
    st.success("**Buon Equilibrio 🟢** - Hai una gestione emotiva positiva, ma con qualche oscillazione.")
    st.write("""
    **Suggerimenti per migliorare ulteriormente:**  
    - Identifica quali emozioni negative tendono a farsi sentire di più e affrontale con calma.  
    - Continua a praticare attività che ti fanno stare bene (hobby, sport, relax).  
    - Cerca di dormire bene e mantenere uno stile di vita bilanciato.  
    """)

elif bilancio_emotivo >= -2:
    st.warning("**Emotività Neutra ⚠️** - Ti trovi in una fase di equilibrio instabile.")
    st.write("""
    **Cosa fare per ritrovare più benessere?**  
    - Prova a identificare le cause dello stress o dell’ansia e gestirle con piccole azioni.  
    - Dedica tempo a qualcosa che ti fa stare bene, anche pochi minuti al giorno.  
    - Parla con qualcuno di fidato per trovare supporto emotivo.  
    """)

elif bilancio_emotivo >= -5:
    st.error("**Squilibrio Emotivo 🟠** - Lo stress e le emozioni negative stanno prendendo il sopravvento.")
    st.write("""
    **Come migliorare il tuo stato emotivo:**  
    - Dedica più tempo a te stesso e riduci gli impegni superflui.  
    - Usa tecniche di rilassamento come la respirazione profonda o la mindfulness.  
    - Considera di fare attività fisica regolare per migliorare l’umore.  
    """)

else:
    st.error("**Sovraccarico Emotivo 🔴** - Attenzione, il livello di stress è molto elevato!")
    st.write("""
    **Strategie urgenti per migliorare:**  
    - Fermati un attimo e cerca di capire cosa sta causando il tuo stress.  
    - Non esitare a chiedere aiuto a un professionista o una persona di fiducia.  
    - Rivedi la tua routine e assicurati di avere momenti di riposo e svago.  
    """)

# Grafico riepilogativo delle emozioni
st.subheader("📊 **Grafico del Bilancio Emotivo**")

emozioni = list(emozioni_positive.keys()) + list(emozioni_negative.keys())
punteggi = punteggi_positive + punteggi_negative

plt.figure(figsize=(10, 5))
plt.barh(emozioni, punteggi, color=['green']*5 + ['red']*5)
plt.xlabel("Livello (1-10)")
plt.ylabel("Emozioni")
plt.title("Bilancio delle Emozioni")
plt.xlim(0, 10)
st.pyplot(plt)

st.markdown('<p class="large-text">🔄 Compila il test una volta a settimana per monitorare le tue emozioni!</p>', unsafe_allow_html=True)
