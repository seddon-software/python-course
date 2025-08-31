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
webbrowser.open("https://matplotlib.org/stable/api/index.html")

