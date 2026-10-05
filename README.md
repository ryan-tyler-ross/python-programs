# Python examples

A personal collection of Python scripts and templates I keep as an IT professional.
Small utilities, API calls, desktop apps, and games live here as examples I can
refer back to or adapt later. Some are deliberately basic; others capture a
particular pattern or a more complete program.

The collection uses public data, sample inputs, and placeholder configuration.
Credentials, local vaults, and generated output are excluded from version control.

| Folder | Contents |
| --- | --- |
| [Templates](templates/) | Standalone HTTP request patterns, a RESTCONF client, and Tkinter widget examples. |
| [Automation](automation/) | A polling script that combines public APIs with an optional email alert. |
| [Utilities](utilities/) | Calculators, text and CSV handling, password generation, and coffee-machine simulations. |
| [Desktop](desktop/) | A unit converter, a Pomodoro timer, and a local encrypted-vault example. |
| [Games](games/) | Terminal games and small Turtle games, with their data and assets. |
| [Graphics](graphics/) | Turtle drawings, keyboard controls, and image color extraction. |

Useful reference points include [HTTP backoff](templates/http/backoff.py),
[a RESTCONF GET](templates/restconf/get_resource.py),
[text-file mail merge](utilities/mail-merge/mail_merge.py), and
[a desktop timer](desktop/pomodoro-timer/pomodoro.py).
Folder READMEs identify the entry files, dependencies, and any local configuration.

**Running a file:** Python 3.11 or newer; scripts run directly from the repository root.

```sh
python3 utilities/calculator.py
```

Most files use the standard library. Projects with extra packages have a local
`requirements.txt`; the root [requirements.txt](requirements.txt) collects all of them.
Turtle and Tkinter examples need a graphical desktop with Tk support.
API templates need an endpoint and any credentials supplied locally.

**Attribution:** Some of the small games and GUI examples are adapted from
Angela Yu's *100 Days of Code* exercises.
