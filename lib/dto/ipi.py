from dataclasses import dataclass

@dataclass
class FormIzkazPoslovnegaIzidaDto:
    cisti_prihodki_iz_prodaje: float
    drugi_poslovni_prihodki: float
    stroski_materiala: float
    stroski_storitev: float
    stroski_dela: float
    amortizacija: float
    drugi_poslovni_odhodki: float
    financni_prihodki: float
    financni_odhodki: float
    davek: float