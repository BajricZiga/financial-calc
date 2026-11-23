
def kkl(kratkorocna_sredstva: float, kratkorocne_poslovne_obveznosti: float, kratkorocne_finance_obveznosti: float) -> float:
    '''
    Izračuna KKL(Kazalec Kratkoročne Likvidnosti)
    Kratkoročna sredstva = zaloge, kratkoročne finančne naložbe, kratkoročne poslovne terjatve, denarna sredstva
    '''
    result: float = kratkorocna_sredstva / (kratkorocne_poslovne_obveznosti + kratkorocne_finance_obveznosti)
    return result

def kpkl(kratkorocna_sredstva: float, zaloge: float, kratkorocne_poslovne_obveznosti: float, kratkorocne_finance_obveznosti: float) -> float:
    '''
    Izračuna KPKL(Kazalec Pospešene Kratkoročne Likvidnosti)
    '''
    result: float = (kratkorocna_sredstva - zaloge) / (kratkorocne_poslovne_obveznosti + kratkorocne_finance_obveznosti)
    return result