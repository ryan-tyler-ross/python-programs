# Text-file mail merge

[mail_merge.py](mail_merge.py) reads [template.txt](template.txt) and [names.txt](names.txt),
replaces `[name]`, and writes one numbered letter per nonblank name into [letters](letters/).
The included names and invitation are sample data.

Entry: `python3 utilities/mail-merge/mail_merge.py`. Standard library only.
Inputs and output resolve beside the script, regardless of the working directory.
Repeated runs replace letters with the same number; generated letters are ignored by Git.
