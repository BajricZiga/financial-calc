
# IPI
def kosmati_poslovni_izid(cisti_prihodki_od_prodaje: float, drugi_prihodki_poslovanja: float) -> float:
    '''
    Izračuna Kosmati poslovni izid
    '''
    result: float = cisti_prihodki_od_prodaje + drugi_prihodki_poslovanja
    return result

# BS
def dolgorocna_sredstva(neopredmetena_osnovna_sredstva: float, opredmetena_osnovna_sredstva: float, nalozbene_nepremicnine: float, dolgorocne_finance_nalozbe: float):
    '''
    Izračuna Dolgoročna sredstva
    '''
    result: float = neopredmetena_osnovna_sredstva +  opredmetena_osnovna_sredstva + nalozbene_nepremicnine + dolgorocne_finance_nalozbe
    return result

def kratkorocna_sredstva(zaloge: float, kratkorocne_finance_nalozbe: float, kratkorocne_poslovne_terjatve: float, denarna_sredstva: float) -> float:
    '''
    Izračuna Kratkoročna sredstva
    '''
    result: float = zaloge + kratkorocne_finance_nalozbe + kratkorocne_poslovne_terjatve + denarna_sredstva
    return result

def obveznosti_do_virov_sredstev(kapital: float, rezervacije: float, dolgorocne_financne_obveznosti: float, kratkorocne_financne_obveznosti: float, kratkorocne_poslovne_obveznosti: float) -> float:
    '''
    Izračuna Obveznosti do virov sredstev
    '''
    result: float = kapital + rezervacije + dolgorocne_financne_obveznosti + kratkorocne_financne_obveznosti + kratkorocne_poslovne_obveznosti
    return result