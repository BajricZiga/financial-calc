import streamlit as st
from streamlit.components.v1 import html
from lib.dto.bs import FormBilancaStanjaDto
from lib.kpi.splosno import dolgorocna_sredstva, kratkorocna_sredstva, obveznosti_do_virov_sredstev
from lib.kpi.zadolzenost import nfd

### Logic
def bs_click(continer: st.container, form_bilanca_stanja_dto: FormBilancaStanjaDto):
    '''
    Implementira logiko ob kliku gumba.
    '''
    dolgorocna_sredstva_result = dolgorocna_sredstva(
        neopredmetena_osnovna_sredstva=form_bilanca_stanja_dto.neopredmetena_osnovna_sredstva,
        opredmetena_osnovna_sredstva=form_bilanca_stanja_dto.opredmetena_osnovna_sredstva,
        nalozbene_nepremicnine=form_bilanca_stanja_dto.nalozbene_nepremicnine,
        dolgorocne_finance_nalozbe=form_bilanca_stanja_dto.dolgorocne_financne_nalozbe
    )

    kratkorocna_sredstva_result = kratkorocna_sredstva(
        zaloge=form_bilanca_stanja_dto.zaloge, 
        kratkorocne_finance_nalozbe=form_bilanca_stanja_dto.kratkorocne_financne_nalozbe,
        kratkorocne_poslovne_terjatve=form_bilanca_stanja_dto.kratkorocne_financne_terjatve,
        denarna_sredstva=form_bilanca_stanja_dto.denarna_sredstva
    )

    obveznosti_do_virov_sredstev_result = obveznosti_do_virov_sredstev(
        kapital=form_bilanca_stanja_dto.kapital,
        rezervacije=form_bilanca_stanja_dto.rezervacije,
        dolgorocne_financne_obveznosti=form_bilanca_stanja_dto.dolgorocne_financne_obveznosti,
        kratkorocne_financne_obveznosti=form_bilanca_stanja_dto.kratkorocne_financne_obveznosti,
        kratkorocne_poslovne_obveznosti=form_bilanca_stanja_dto.kratkorocne_poslovne_obveznosti
    )

    nfd_result = nfd(
        dolgorocne_finance_obveznosti=form_bilanca_stanja_dto.dolgorocne_financne_obveznosti,
        kratkorocne_financne_obveznosti=form_bilanca_stanja_dto.kratkorocne_financne_obveznosti,
        kratkorocne_finance_nalozbe=form_bilanca_stanja_dto.kratkorocne_financne_nalozbe,
        denarna_sredstva=form_bilanca_stanja_dto.denarna_sredstva
    )
    
    with continer:
        st.divider()
        st.text(f'Dolgoročna sredstva = {dolgorocna_sredstva_result}')
        st.text(f'Kratkoročna sredstva = {kratkorocna_sredstva_result}')
        st.text(f'Obveznosti do virov sredstev = {obveznosti_do_virov_sredstev_result}')
        st.text(f'NFD = {nfd_result}')


        js_localstorage = f'''
        <script>
            localStorage.setItem("dolgorocna_sredstva", "{str(dolgorocna_sredstva_result)}")
            localStorage.setItem("kratkorocna_sredstva", "{str(kratkorocna_sredstva_result)}")
            localStorage.setItem("obveznosti_do_virov_sredstev_result", "{str(obveznosti_do_virov_sredstev_result)}")
            localStorage.setItem("nfd", "{str(nfd_result)}")
        </script>
        '''
        st.iframe(src=js_localstorage)

### UI

st.markdown(f'<h1 style="color:#50a0c8">Bilanca stanja</h1>', unsafe_allow_html=True)

container_frm_bilanca_stanja = st.container()
container_frm_bilanca_stanja_izracun = st.container()

with container_frm_bilanca_stanja:
    with st.form("frm_bilanca_stanja"):
        frm_item_number_neopredmetena_osnovna_sredstva = st.number_input("Neopredmetena osnovna sredstva")
        frm_item_number_opredmetena_osnovna_sredstva = st.number_input("Opredmetena osnovna sredstva")
        frm_item_number_nalozbene_nepremicnine = st.number_input("Nalozbene nepremičnine")
        frm_item_number_dolgorocne_financne_nalozbe = st.number_input("Dolgoročne finančne nalozbe")
        frm_item_number_zaloge = st.number_input("Zaloge")
        frm_item_number_kratkorocne_financne_nalozbe = st.number_input("Kratkoročne finančne nalozbe")
        frm_item_number_kratkorocne_financne_terjatve = st.number_input("Kratkoročne poslovne terjatve")
        frm_item_number_denarna_sredstva = st.number_input("Denarna sredstva")
        frm_item_number_kapital = st.number_input("Kapital")
        frm_item_number_rezervacije = st.number_input("Rezervacije")
        frm_item_number_dolgorocne_financne_obveznosti = st.number_input("Dolgoročne finančne obveznosti")
        frm_item_number_kratkorocne_financne_obveznosti = st.number_input("Kratkoročne finančne obveznosti")
        frm_item_number_kratkorocne_poslovne_obveznosti = st.number_input("Kratkoročne poslovne obveznosti")
    
        #frm_item_btn_izracunaj = st.form_submit_button('Izračunaj', on_click=bs_click(continer=container_frm_bilanca_stanja_izracun))
        frm_item_btn_izracunaj = st.form_submit_button('Izračunaj')
        if frm_item_btn_izracunaj:
            form_bilanca_stanja_dto: FormBilancaStanjaDto = FormBilancaStanjaDto(
                neopredmetena_osnovna_sredstva=frm_item_number_neopredmetena_osnovna_sredstva,
                opredmetena_osnovna_sredstva=frm_item_number_opredmetena_osnovna_sredstva,
                nalozbene_nepremicnine=frm_item_number_nalozbene_nepremicnine,
                dolgorocne_financne_nalozbe=frm_item_number_dolgorocne_financne_nalozbe,
                zaloge=frm_item_number_zaloge,
                kratkorocne_financne_nalozbe=frm_item_number_kratkorocne_financne_nalozbe,
                kratkorocne_financne_terjatve=frm_item_number_kratkorocne_financne_terjatve,
                denarna_sredstva=frm_item_number_denarna_sredstva,
                kapital=frm_item_number_kapital,
                rezervacije=frm_item_number_rezervacije,
                dolgorocne_financne_obveznosti=frm_item_number_dolgorocne_financne_obveznosti,
                kratkorocne_financne_obveznosti=frm_item_number_kratkorocne_financne_obveznosti,
                kratkorocne_poslovne_obveznosti=frm_item_number_kratkorocne_poslovne_obveznosti
            )

            bs_click(continer=container_frm_bilanca_stanja_izracun, form_bilanca_stanja_dto=form_bilanca_stanja_dto)