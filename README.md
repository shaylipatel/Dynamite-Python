## Dynamite Bot runner (in Python)

This repo contains example bots for the game of [Dynamite](https://dynamite.softwire.com/), plus a simple test harness.

To play:

1. Write a class with a `make_move` method, and put it in its own file
2. Run `python bot_runner.py your_file` to check it works
3. Iterate and improve!

Note:
- When inspecting the gamestate, your bot will always be "P1" (and your opponent "P2").
- Make sure you count your dynamite! There is nothing worse than losing a game at the last minute by attempting to use too much.
- The same instance of your class is used for all rounds of a match, so you can store state to keep track of anything you want during the match.

To find new opponents, either share your python files with each other, or upload them to the website: <https://dynamite.softwire.com/bots>
