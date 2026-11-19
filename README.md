# The World in One Image — Thursday 19 November 2026

[![news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![Rank](https://make.fun/badge/news-image-20261119/Angga-Nugraha/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![Reward](https://make.fun/badge/news-image-20261119/Angga-Nugraha/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119)

A newspaper front page summing up the world news of Thursday 19 November
2026 in a single image. The hero is the first three-way summit of Trump, Xi
and Putin in Shenzhen, with four more of the day's biggest stories below:
the Crimean Bridge struck, the Strait of Hormuz crisis, the ICJ's Rohingya
genocide verdict, and the COP31 climate talks in Antalya. The masthead names
the date in large type so the day the image sums up is unmistakable.

Bounty: [news-image-20261119 on make.fun](https://make.fun/bounty/news-image-20261119)

## How the image was made

Five editorial illustrations in a consistent warm-newsprint / deep-blue style
were composed into a front page with Python (Pillow): a large masthead with
the date, the summit scene as the hero, a one-line caption, and a row of four
labelled vignettes. All text (masthead, caption, panel labels) was rendered
crisply in the compositor — no text was generated inside the illustrations.
The finished page is `entry.png` (1024×1024 PNG).

## Run

`main.py` (Python 3.13, stdlib only) copies the bundled `entry.png` to the
output directory — `/output` by default, or `$MAKEFUN_OUTPUT_DIR` when set:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```
