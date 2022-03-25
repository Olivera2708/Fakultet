from email.headerregistry import ParameterizedMIMEHeader
from pkg_resources import IMetadataProvider

class Osoba(object):
    def __init__(self, ime,  prz):
        self._.ime = ime
        self._prezime = prz

    @property
    def ime(self):
        return self.ime

    @ime.setter
    def ime(self, new):
        self.ime = new

    @property
    def prezime(self):
        return self._prezime

    @prezime.setter
    def prezime(self, new):
        self.prezime = new

    def __str__(self):
        return f"Person ime -> {self._ime} prezime -> {self._prezime}"


class Korisnik(Osoba):
    def __init__(self, korisnicko_ime, ime, prz, lozinka):
        super().__init__(self, ime, prz)
        self._korisnicko_ime = korisnicko_ime
        self._uloga = "Klijent"
        self._lozinka = lozinka

        @property
        def korisnicko_ime(self):
            return self.korisnicko_ime

        @korisnicko_ime.setter
        def korisnicko_ime(self, new):
            self.korisnicko_ime = new

        @property
        def uloga(self):
            return self._uloga

        @uloga.setter
        def uloga(self, new):
            self._uloga = new

        @property
        def lozinka(self):
            return self._lozinka

        @lozinka.setter
        def lozinka(self, new):
            self._lozinka = new

        def __str__(self):
            print(f"{self._korisnicko_ime} {self._ime} {self._prezime} {self._uloga}")


class RegistrovaniKlijent(Korisnik):
    def __init__(self, korisnicko_ime, ime, prezime, uloga, telefon, email, pol):
        super().__init__(korisnicko_ime, ime, prezime, uloga)
        self._telefon  =telefon
        self._email = email
        self._pol = pol

        @property
        def telefon(self):
            return self._telefon

        @telefon.setter
        def telefon(self, new):
            self._telefon = new

        @property
        def email(self):
            return self._email

        @email.setter
        def email(self, new):
            self._email = new

        @property
        def pol(self):
            return self._pol

        @telefon.setter
        def telefon(self, new):
            self._telefon = new


class Recepcioner(Korisnik):
    def __init__(self, korisnicko_ime, ime, prz, lozinka):
        super().__init__(korisnicko_ime, ime, prz, lozinka)
        self._uloga = "Recepcioner"


class Kozmeticar(RegistrovaniKlijent):
    def __init__(self, korisnicko_ime, ime, prezime, uloga, telefon, email, pol, tip = None):
        super().__init__(korisnicko_ime, ime, prezime, uloga, telefon, email, pol)
        if tip == None:
            tip = []
        self._tip_tretmana = tip

        @property
        def tip_tretmana(self):
            return self._tip_tretmana

        @tip_tretmana.setter
        def tip_tretmana(self, new):
            self._tip_tretmana.append(new)


class Menadzer(RegistrovaniKlijent):
    def __init__(self, korisnicko_ime, ime, prezime, uloga, telefon, email, pol, zaposleni = None):
        super().__init__(korisnicko_ime, ime, prezime, uloga, telefon, email, pol)
        self.spisak_zaposlenih = zaposleni

    @property
    def spisak_zaposlenih(self):
        return self._spisak_zaposlenih

    @spisak_zaposlenih.setter
    def spisak_zaposlenih(self, new):
        self._spisak_zaposlenih = new

    def zaposli(self, new):
        self._spisak_zaposlenih.append(new)

    def otkaz(self, new):
        self._spisak_zaposlenih.remove(new)
