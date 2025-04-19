import flet as ft

from UI.controller import Controller


class View():
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Gestore Corsi Edizione 2025"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None

        self.ddPD = None
        self.ddCodins = None
        self.btnPrintCorsiPD = None
        self.btnPrintIscrittiCorsiPD = None
        self.btnPrintIscrittiCodins = None
        self.btnPrintCDSCodins = None
        self.lvtxtOut = None

    def load_interface(self):
        # title
        self._title = ft.Text("Gestore Corsi Edizione 2025", color="blue", size=24)
        self._page.controls.append(self._title)

        self.ddPD = ft.Dropdown(label="Periodo Didattico",
                                options=[ft.dropdown.Option("I"), ft.dropdown.Option("II")],
                                width=200)
        self.ddCodins = ft.Dropdown(label="Corso",
                                    width=200,
                                    on_change=self._controller.ddCodinsSelected)
        self._controller.fillddCodins()

        self.btnPrintCorsiPD = ft.ElevatedButton(text="Stampa corsi",
                                                 on_click=self._controller.handlePrintCorsiPD,
                                                 width=300)
        self.btnPrintIscrittiCorsiPD = ft.ElevatedButton(text="Stampa numero iscritti",
                                                         on_click=self._controller.handlePrintIscrittiCorsiPD,
                                                         width=300)
        self.btnPrintIscrittiCodins = ft.ElevatedButton(text="Stampa iscritti al corso",
                                                        on_click=self._controller.handlePrintIscrittiCodins,
                                                        width=300)
        self.btnPrintCDSCodins = ft.ElevatedButton(text="Stampa CDS afferenti",
                                                   on_click=self._controller.handlePrintCDSCodins,
                                                   width=300)

        self.lvtxtOut = ft.ListView(expand = True)

        row1 = ft.Row([self.ddPD, self.btnPrintCorsiPD, self.btnPrintIscrittiCorsiPD])
        row2 = ft.Row([self.ddCodins, self.btnPrintIscrittiCodins, self.btnPrintCDSCodins])
        self._page.add(row1, row2, self.lvtxtOut)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
