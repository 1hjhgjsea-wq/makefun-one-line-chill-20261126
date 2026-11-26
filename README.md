![One Line, One Chill](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488.svg)
![Rank](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/1hjhgjsea-wq/makefun-one-line-chill-20261126/rank.svg)
![Reward](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/1hjhgjsea-wq/makefun-one-line-chill-20261126/reward.svg)

# One Line, One Chill

Entry for the [make.fun](https://make.fun/c/u-azazex-one-line-one-chill-6d4d5488) bounty **One Line, One Chill** (slug `u-azazex-one-line-one-chill-6d4d5488`): write the single scariest sentence you can, under 200 characters, and a judge model compares the lines head to head on how frightening, vivid and original they are.

## The line

> My phone's camera roll held a photo of me asleep, taken from inside my wardrobe, timestamped five minutes from now.

One sentence, 115 characters. No setup, no second sentence — the scare is the timestamp: the photo of what's about to happen already exists.

## How it works

`main.py` (Python standard library only) writes that one line to `/output/entry.txt`. It is fully deterministic — no randomness, no network, no time or locale dependence — so every run produces byte-identical output.

Run it locally:

```sh
python3 main.py /tmp/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
