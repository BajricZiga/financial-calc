
def ebitda(kosmati_poslovni_izid: float, stroski_storitev: float, stroski_materiala: float, stroski_dela: float, drugi_poslovni_odhodki)  -> float:
    '''
    Izracuna EBITDA
    '''
    result: float = kosmati_poslovni_izid - stroski_materiala - stroski_storitev - stroski_dela - drugi_poslovni_odhodki
    return result

def ebitda_marza(ebitda: float, kosmati_poslovni_izid: float) -> float:
    '''
    Izračuna EBITDA marža
    '''
    result: float = ebitda / kosmati_poslovni_izid
    return result

def ebit(
        kosmati_poslovni_izid: float, 
        stroski_storitev: float, 
        stroski_materiala: float, 
        stroski_dela: float, 
        amortizacija: float, 
        drugi_poslovni_odhodki
    ) -> float:
    '''
    Izračuna EBIT
    '''
    result: float = kosmati_poslovni_izid - stroski_materiala - stroski_storitev - stroski_dela - amortizacija - drugi_poslovni_odhodki
    return result

def ebt(ebit: float, finacni_prihodki: float, financni_odhodki: float):
    '''
    Izračuna EBT
    '''
    result: float = ebit + finacni_prihodki - financni_odhodki
    return result

def cisti_poslovni_izid_poslovnega_leta(ebt: float, davek: float) -> float:
    '''
    Izračuna Čisti poslovni izid
    '''
    davek_vrednost: float = ebt * davek
    result: float = ebt - davek_vrednost
    
    return result