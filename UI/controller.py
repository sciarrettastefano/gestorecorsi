import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._ddCodinsValue = None

    def handlePrintCorsiPD(self, e):
        self._view.lvtxtOut.controls.clear()
        pd = self._view.ddPD.value
        if pd is None:
            # self._view.lvtxtOut.controls.append(ft.Text("Attenzione, selezionare un periodo didattico!",
            #                                             color = "red"))
            self._view.create_alert("Attenzione, selezionare un periodo didattico!")
            self._view.update_page()
            return

        # A questo punto pd="I" oppure pd="II", ma il db vuole un numero 1 o 2
        if pd == "I":
            pdInt = 1
        else:
            pdInt = 2

        corsiPD = self._model.getCorsiPD(pdInt)
        if len(corsiPD) == 0: # --> controllo in caso di db vuoto e quindi model e dao che restituiscono una lista vuota
            self._view.lvtxtOut.controls.append(ft.Text("Nessun corso trovato in questo periodo."))
            self._view.update_page()
            return

        self._view.lvtxtOut.controls.append(ft.Text(f"Corsi del {pd} periodo didattico."))
        for c in corsiPD:
            self._view.lvtxtOut.controls.append(ft.Text(c))
        self._view.update_page()

    def handlePrintIscrittiCorsiPD(self, e):
        self._view.lvtxtOut.controls.clear()
        pd = self._view.ddPD.value
        if pd is None:
            self._view.create_alert("Attenzione, selezionare un periodo didattico!")
            self._view.update_page()
            return

        if pd == "I":
            pdInt = 1
        else:
            pdInt = 2

        corsiPDwI = self._model.getCorsiPDwithIscritti(pdInt)
        if len(corsiPDwI) == 0:
            self._view.lvtxtOut.controls.append(ft.Text("Nessun corso trovato in questo periodo."))
            self._view.update_page()
            return

        self._view.lvtxtOut.controls.append(ft.Text(f"Dettagli corsi del {pd} periodo didattico."))
        for c in corsiPDwI:
            self._view.lvtxtOut.controls.append(ft.Text(f"{c[0]} - N Iscritti: {c[1]}"))

        self._view.update_page()

    def handlePrintIscrittiCodins(self, e):
        self._view.lvtxtOut.controls.clear()
        if self._ddCodinsValue is None: # ---> così ho l'oggetto, e non la stringa che troverei prendendo dal ddCodins (anche se qua andrebbe bene uguale)
            self._view.create_alert("Attenzione, selezionare un corso di interesse!")
            self._view.update_page()
            return

        studenti = self._model.getStudentiCorso(self._ddCodinsValue.codins)
        if len(studenti) == 0:
            self._view.lvtxtOut.controls.append(ft.Text("Nessuno studente iscritto a questo corso."))
            self._view.update_page()
            return

        self._view.lvtxtOut.controls.append(ft.Text(f"Studenti iscritti al corso {self._ddCodinsValue}:"))
        for s in studenti:
            self._view.lvtxtOut.controls.append(ft.Text(s))
        self._view.update_page()

    def handlePrintCDSCodins(self, e):
        self._view.lvtxtOut.controls.clear()
        if self._ddCodinsValue is None:  # ---> così ho l'oggetto, e non la stringa che troverei prendendo dal ddCodins (anche se qua andrebbe bene uguale)
            self._view.create_alert("Attenzione, selezionare un corso di interesse!")
            self._view.update_page()
            return

        cds = self._model.getCDSofCorso(self._ddCodinsValue.codins)
        if len(cds) == 0:
            self._view.lvtxtOut.controls.append(ft.Text("Nessun cds offre questo corso."))
            self._view.update_page()
            return

        self._view.lvtxtOut.controls.append(ft.Text(f"CDS che frequentano il corso {self._ddCodinsValue}:"))
        for c in cds:
            self._view.lvtxtOut.controls.append(ft.Text(f"CDS: {c[0]} - N Iscritti: {c[1]}"))
        self._view.update_page()

    def fillddCodins(self):
        """for cod in self._model.getCodins():
            self._view.ddCodins.options.append(ft.dropdown.Option(cod))"""

        for c in self._model.getAllCorsi():
            self._view.ddCodins.options.append(ft.dropdown.Option(key=c.codins,
                                                                  data=c,
                                                                  on_click=self._choiceDDCodins))  #---> quando seleziono un valore esegue questo metodo (sotto)

    def _choiceDDCodins(self, e):
        self._ddCodinsValue = e.control.data
        print(self._ddCodinsValue)
        print("In _choiceDDCodins", type(self._ddCodinsValue))

    def ddCodinsSelected(self, e):
        """Metodo che ci permette di verificare il tipo del valore
        selezionato nel dd dei corsi."""
        print("In ddCodinsSelected", type(self._view.ddCodins.value))
