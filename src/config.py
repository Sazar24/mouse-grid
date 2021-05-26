def setProjectPath():
    """ source: https://stackoverflow.com/questions/43728431/relative-imports-modulenotfounderror-no-module-named-x """
    import os
    import sys

    dir_path = os.path.dirname(os.path.realpath(__file__))
    parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
    sys.path.insert(0, parent_dir_path)
