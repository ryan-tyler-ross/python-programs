"""Read a template and names, then write one letter for each name."""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def main():
    template = (BASE_DIR / "template.txt").read_text(encoding="utf-8")
    names = (BASE_DIR / "names.txt").read_text(encoding="utf-8").splitlines()
    output = BASE_DIR / "letters"
    output.mkdir(exist_ok=True)
    count = 0
    for name in names:
        name = name.strip()
        if not name:
            continue
        count += 1
        # Numbered files also work when a name contains punctuation or a slash.
        path = output / f"letter_{count:03}.txt"
        path.write_text(template.replace("[name]", name), encoding="utf-8")
    print(f"Generated {count} letters in {output}")


if __name__ == "__main__":
    main()
