from rope.base.project import Project
from rope.base import libutils
from rope.refactor.move import create_move

myProj = Project('src')
# resource = myProj.get_resource(r'app/services/gridMaker/grid.py')
# resource = libutils.path_to_resource(myProj, r'src/app/services/gridMaker')
resource = myProj.get_resource(r'app/services/theGrid/windowSetter.py')
offset = None
destination = libutils.path_to_resource(myProj, r'src/app/services/theGrid/windowSetter')

mover = create_move(myProj, resource, offset)
myProj.do(mover.get_changes(destination))
