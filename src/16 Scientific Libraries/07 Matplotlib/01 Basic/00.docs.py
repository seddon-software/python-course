'''
Sometimes it is useful to step into library code, so you can see documentation on the methods called.  To do this
you will need to modify the JSON in .vscode/launch.json to look like:
        {
            ...
            "stopOnEntry": true,
            "justMyCode": false,
            ...
        }
'''

import webbrowser

# use this to edit launch.json
def edit_launch_json():
    import os
    os.system("clear")
    os.system("vim ../../../../.vscode/launch.json")

# alternatively, use this to see matplotlib documentaion
def matplotlib_documentaion():
    webbrowser.open("https://matplotlib.org/stable/api/index.html")

def view_gallery():
    webbrowser.open("https://matplotlib.org/stable/gallery/index.html")

# edit_launch_json()
# matplotlib_documentaion()
view_gallery()
