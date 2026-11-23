import streamlit as st

st.title("Domov")
with st.container():
    vsebina = '''
    Spletna aplikacija, ki služi hitri evalvaciji podanega podjetja glede na vnešene podatke Bilance Stanja(BS) in Izkaza Poslovnega Izida(IPI).
    Narejene je bila v okviru projektne naloge predmeta Spletne Tehnologije(STE) v 3. Letniku študijskega programa Poslovna informatika in povezuje znanje predmeta Računovodstvo(RAČ) iz 1. letnika istega študijskega programa.
    '''
    st.text(vsebina)