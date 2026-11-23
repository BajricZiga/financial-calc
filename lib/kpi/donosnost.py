
def roe(ebit: float, kapital: float) -> float:
    '''
    Izračuna ROE(Return on Equity)
    '''
    result: float = ebit / kapital
    return result

def roa(ebit: float, sredstva: float) -> float:
    '''
    Izračuna ROA(Return on Assets)
    '''
    result: float = ebit / sredstva
    return result
