from rope.base.project import Project
from rope.refactor.rename import Rename

proj = Project('src')
# resource = myProj.get_resource(r'app/src/app/services/gridMaker')
moduleToChange = proj.get_module(r'app/services/theGrid/gridLinesCoordsStore').get_resource()
change = Rename(proj, moduleToChange).get_changes('gridInfoStore')
print(change.get_description())
proj.do(change)
