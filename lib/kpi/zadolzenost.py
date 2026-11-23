
def dv(kosmati_poslovni_izid: float, stroski_storitev: float, stroski_materiala: float):
    '''
    Izračuna DV(Dodana Vrednost)
    '''
    result: float = kosmati_poslovni_izid - stroski_storitev - stroski_materiala
    return result

def nfd(dolgorocne_finance_obveznosti: float, kratkorocne_financne_obveznosti: float, kratkorocne_finance_nalozbe, denarna_sredstva) -> float:
    '''
    Izračuna NFD(Neto Finančni Dolg)
    '''
    result: float = dolgorocne_finance_obveznosti + kratkorocne_financne_obveznosti - kratkorocne_finance_nalozbe - denarna_sredstva
    return result

def nfd_ebitda(nfd, ebitda) -> float:
    '''
    Izračuna NFD/EBITDA
    '''
    result: float = nfd / ebitda
    return result