# Python programs

Small Python projects, arranged in the order the ideas build on each other.
Some began as Angela Yu's 100 Days of Code exercises; others are automation examples.
Open a folder's README for its reading order, run commands, and a description of every file.

| Start with | Learn |
| --- | --- |
| [Basics](01-basics/README.md) | Start here: input, arithmetic, conditions, lists, and loops. |
| [Functions and small projects](02-functions/README.md) | Use functions and dictionaries, then practice importing your own modules. |
| [Classes](03-classes/README.md) | Compare the procedural coffee machine with a version built from classes. |
| [Drawing and games](04-turtle/README.md) | Learn coordinates and keyboard events before trying the larger games. |
| [Files and data](05-files/README.md) | Read text and CSV files, write letters, then combine a table with a map. |
| [Desktop apps](06-desktop/README.md) | Start with widgets and the converter, then explore the timer and password manager. |
| [APIs and automation](07-automation/README.md) | Fetch JSON, handle failures, and read from a network lab. |

Use Python 3.11 or newer. From this folder, try:

```sh
python3 01-basics/band_name_generator.py
```

Only later projects need extra packages:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```
On Windows, activate with `.venv\Scripts\activate`.
Turtle and Tkinter apps need a graphical desktop and Python's Tk support.
Each project is a plain script: run its file directly. There is no course launcher.
Read it, run it, then change one small thing and observe the result.

`requirements.txt` lists optional packages and the projects that need them.
`.gitignore` keeps environments, caches, editor settings, credentials, and generated files out of Git.
Every source file and asset is described in its folder's README; a README explains that folder.
Hidden `.git`, `.idea`, `.venv`, and cache folders are local tools, not lessons.
Existing local environments were kept, and their launchers were updated for the new paths.
The AUTOCOR examples now live in `07-automation`; the empty ISE file is labeled as a starter.
