from abc import ABC, abstractmethod

class Volo(ABC):
    def __init__(self, codice, capacita):
        self.codice = codice
        self.capacita = capacita
        self.prenotazioni = 0

    @abstractmethod
    def prenota_posto(self):
        pass

    @abstractmethod
    def posti_disponibili(self):
        pass

class VoloCommerciale(Volo):
    def __init__(self, codice, capacita):
        super().__init__(codice, capacita)

        self.posti_economica = capacita // 0.7
        self.posti_business = capacita // 0.2
        self.posti_prima = capacita - self.posti_economica - self.posti_business

        self.prenotazioni_economica = 0
        self.prenotazioni_business = 0
        self.prenotazioni_prima = 0

    def posti_disponibili(self):
        return {
            'posti disponibili': self.capacita - self.prenotazioni,
            'classe economica': self.posti_economica - self.prenotazioni_economica,
            'classe business': self.posti_business - self.prenotazioni_business,
            'prima classe': self.posti_prima - self.prenotazioni_prima
        }

    def prenota_posto(self, posti, classe_servizio):
        disponibili = self.posti_disponibili()
        classe_servizio = classe_servizio

        if disponibili['posti disponibili'] == 0:
            print(f"Il volo {self.codice} è al completo.")
            return

        if classe_servizio not in ['economica', 'business', 'prima']:
            print("Classe di servizio non valida.")
            return

        prenotabili = disponibili[f'classe {classe_servizio}']
        if posti > prenotabili:
            print(f"Non ci sono abbastanza posti disponibili in classe {classe_servizio}.")
            return

        if classe_servizio == 'economica':
            self.prenotazioni_economica += posti
        elif classe_servizio == 'business':
            self.prenotazioni_business += posti
        elif classe_servizio == 'prima':
            self.prenotazioni_prima += posti

        self.prenotazioni += posti
        print(f"{posti} posti prenotati in classe {classe_servizio} sul volo {self.codice}.")

# Volo Charter
class VoloCharter(Volo):
    def __init__(self, codice, capacita, prezzo):
        super().__init__(codice, capacita)
        self.prezzo = prezzo

    def prenota_posto(self):
        if self.prenotazioni == 0:
            self.prenotazioni = self.capacita
            print(f"Volo charter {self.codice} prenotato completamente. Prezzo: {self.prezzo}€.")
        else:
            print(f"Il volo charter {self.codice} è già stato prenotato.")

    def posti_disponibili(self):
        return self.capacita - self.prenotazioni

# Compagnia Aerea
class CompagniaAerea:
    def __init__(self, nome, prezzo_standard):
        self.nome = nome
        self.prezzo_standard = prezzo_standard
        self.flotta = []

    def aggiungi_volo(self, volo):
        self.flotta.append(volo)

    def rimuovi_volo(self, volo):
        if volo in self.flotta:
            self.flotta.remove(volo)

    def mostra_flotta(self):
        print(f"Flotta di {self.nome}:")
        for volo in self.flotta:
            print(f"- {volo.codice}")

    def guadagno(self):
        guadagno_totale = 0.0
        for volo in self.flotta:
            if isinstance(volo, VoloCommerciale):
                guadagno_totale += (
                    volo.prenotazioni_economica * self.prezzo_standard +
                    volo.prenotazioni_business * self.prezzo_standard * 2 +
                    volo.prenotazioni_prima * self.prezzo_standard * 3
                )
        return (guadagno_totale)
