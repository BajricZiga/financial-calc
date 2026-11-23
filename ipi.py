import streamlit as st
from lib.kpi.splosno import kosmati_poslovni_izid
from lib.dto.ipi import FormIzkazPoslovnegaIzidaDto
from lib.kpi.uspesnost import ebitda, ebitda_marza, ebit, ebt

st.markdown(f'<h1 style="color:#50a0c8">Izkaz poslovnega izida</h1>', unsafe_allow_html=True)

def ipi_click(continer: st.container, form_izkaz_poslovnega_izida_dto: FormIzkazPoslovnegaIzidaDto):
    '''
    '''
    try:
        kosmati_poslovni_izid_result = kosmati_poslovni_izid(
            cisti_prihodki_od_prodaje=form_izkaz_poslovnega_izida_dto.cisti_prihodki_iz_prodaje, 
            drugi_prihodki_poslovanja=form_izkaz_poslovnega_izida_dto.drugi_poslovni_odhodki
        )

        ebitda_result = ebitda(
            kosmati_poslovni_izid=kosmati_poslovni_izid_result, 
            stroski_storitev=form_izkaz_poslovnega_izida_dto.stroski_storitev, 
            stroski_materiala=form_izkaz_poslovnega_izida_dto.stroski_materiala, 
            stroski_dela=form_izkaz_poslovnega_izida_dto.stroski_dela,
            drugi_poslovni_odhodki=form_izkaz_poslovnega_izida_dto.drugi_poslovni_odhodki
        )

        ebitda_marza_result = ebitda_marza(ebitda=ebitda_result, kosmati_poslovni_izid=kosmati_poslovni_izid_result)

        ebit_result = ebit(
            kosmati_poslovni_izid=kosmati_poslovni_izid_result, 
            stroski_storitev=form_izkaz_poslovnega_izida_dto.stroski_storitev,
            stroski_materiala=form_izkaz_poslovnega_izida_dto.stroski_materiala,
            stroski_dela=form_izkaz_poslovnega_izida_dto.stroski_dela,
            amortizacija=form_izkaz_poslovnega_izida_dto.amortizacija,
            drugi_poslovni_odhodki=form_izkaz_poslovnega_izida_dto.drugi_poslovni_odhodki
        )

        ebt_result = ebt(
            ebit=ebit_result, 
            finacni_prihodki=form_izkaz_poslovnega_izida_dto.financni_prihodki, 
            financni_odhodki=form_izkaz_poslovnega_izida_dto.financni_odhodki
        )

        with continer:
            st.divider()
            st.text(f'Kosmati poslovni izid = {kosmati_poslovni_izid_result}')
            st.text(f'EBITDA = {ebitda_result}')
            st.text(f'EBITDA Marža = {ebitda_marza_result}')
            st.text(f'EBIT = {ebit_result}')
            st.text(f'EBT = {ebt_result}')
    except Exception as e:
        js_alert = f'<script>alert("{str(e)}")</script>'
        st.iframe(src=js_alert)

        print('e = ', str(e))

container_frm_izkaz_poslovnega_izida = st.container()
container_frm_izkaz_poslovnega_izida_izracun = st.container()

with container_frm_izkaz_poslovnega_izida:
    with st.form("frm_izkaz_poslovnega_izida"):
        frm_item_number_cisti_prihodki_iz_prodaje = st.number_input("Čisti prihodki iz prodaje")
        frm_item_number_drugi_poslovni_prihodki = st.number_input("Drugi poslovni prihodki")
        frm_item_number_stroski_materiala = st.number_input("Stroški materiala")
        frm_item_number_stroski_storitev = st.number_input("Stroški storitev")
        frm_item_number_stroski_dela = st.number_input("Stroški dela")
        frm_item_number_amortizacija = st.number_input("amortizacija")
        frm_item_number_drugi_poslovni_odhodki = st.number_input("Drugi poslovni odhodki")
        frm_item_number_financni_prihodki = st.number_input("Finančni prihodki")
        frm_item_number_financni_odhodki = st.number_input("Finančni ohodki")
        frm_item_number_davek = st.number_input("davek")

        frm_item_btn_izracunaj = st.form_submit_button('Izračunaj')
        if frm_item_btn_izracunaj:
            form_izkaz_poslovnega_izida_dto: FormIzkazPoslovnegaIzidaDto = FormIzkazPoslovnegaIzidaDto(
                cisti_prihodki_iz_prodaje=frm_item_number_cisti_prihodki_iz_prodaje,
                drugi_poslovni_prihodki=frm_item_number_drugi_poslovni_prihodki,
                stroski_materiala=frm_item_number_stroski_materiala,
                stroski_storitev=frm_item_number_stroski_storitev,
                stroski_dela=frm_item_number_stroski_dela,
                amortizacija=frm_item_number_amortizacija,
                drugi_poslovni_odhodki=frm_item_number_drugi_poslovni_odhodki,
                financni_prihodki=frm_item_number_financni_prihodki,
                financni_odhodki=frm_item_number_financni_odhodki,
                davek=frm_item_number_davek
            )

            ipi_click(continer=container_frm_izkaz_poslovnega_izida, form_izkaz_poslovnega_izida_dto=form_izkaz_poslovnega_izida_dto)