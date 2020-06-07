Planowane skróty klawiaturowe:

alt ` (tylda): Wywołanie grida
alt ` - gdy aplikacja już jest aktywna (i widoczna): pickNextGridMode
alt ` <dwie-cyfry> : Zagęszczenie siatki, gdzie <dwie-cyfry> ilość kafli w poziomieo
a/s/d/w - kierunek
tab - move (10)
c - click
c+shift - pressAndHold
r - rightClick

modes:
selectXYMode:
    - get 4 numbers:
        = 1&2 = columnNr
        = 3&4 = rowNr
    - dummy-mode:
        - a/s/d/w - klawisze kierunkowe
    - general:
        - h,j,k,l - działają zawsze

alt + q/w/e
      a/s/d
      z/x/c  - move pointer to selected square corner/mid/edge

s + 1/2/3 - screen select

D - Dummy-Mode - moves pointer by 1px in specified direction with a/s/d/w

? - help 

` (tylda) <znak> - userDefinedHotkeyOrAction
`` - restart ?
