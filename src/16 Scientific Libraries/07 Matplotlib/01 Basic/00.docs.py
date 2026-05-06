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

# use this to edit launch.json
import os
os.system("clear")
os.system("vim ../../../../.vscode/launch.json")

# use this to see matplotlib documentaion
# import webbrowser
# webbrowser.open("https://matplotlib.org/stable/api/index.html")

