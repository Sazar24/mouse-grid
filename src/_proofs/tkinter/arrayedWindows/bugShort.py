


(...)
for screen in allScreens:
    screen.tkWindowObject.bind(
        str(callableNr),
        lambda _: self.windowActionsCaller.hideWindowsExceptGivenOne(screen.id)
    )

w allScreens jest - w moim wypadku 2, ale może być więcej - obiektów.

Wygląda na to, że przypisywana akcja jest przypisywana przez referencję (zamiast przez nowy obiekt)