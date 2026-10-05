"""Print RGB colors sampled from the included painting."""

from pathlib import Path

import colorgram


def main():
    image = Path(__file__).with_name("hurst-spot-painting.jpg")
    colors = colorgram.extract(str(image), 12)
    print([(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors])


if __name__ == "__main__":
    main()
