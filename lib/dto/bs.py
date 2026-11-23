
from dataclasses import dataclass

@dataclass
class FormBilancaStanjaDto:
    neopredmetena_osnovna_sredstva: float
    opredmetena_osnovna_sredstva: float
    nalozbene_nepremicnine: float
    dolgorocne_financne_nalozbe: float
    zaloge: float
    kratkorocne_financne_nalozbe: float
    kratkorocne_financne_terjatve: float
    denarna_sredstva: float
    kapital: float
    rezervacije: float
    dolgorocne_financne_obveznosti: float
    kratkorocne_financne_obveznosti: float
    kratkorocne_poslovne_obveznosti: float