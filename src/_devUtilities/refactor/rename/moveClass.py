# source: https://github.com/python-rope/rope/issues/231
"""
Tu chyba chodzi o przeniesienie klasy do pliku, który już istnieje...
o.O
Po co to komu?

Wrzucam sobie jako ściągę, bo:
- może kiedyś mi się przyda
- dobrze pokazuje użycie 'resource'ów  (właśc: libutils.path_to_resource )
"""

import rope.base.project
from rope.base import libutils
from rope.refactor import move

my_project = rope.base.project.Project('src')

path_a = r'src/app/services/gridMaker/app.py'
path_b = r'src/app/services/app.py'

origin = libutils.path_to_resource(my_project, path_a)
destination = libutils.path_to_resource(my_project, path_b)
move_object = move.create_move(my_project, origin)

changes = move_object.get_changes(destination)

my_project.do(changes)
