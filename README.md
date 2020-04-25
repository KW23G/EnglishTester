# EnglishTester

This is a program that tests your english / german vocabulary.
There is a GUI and a cmd-line app.

## Things we are using:

* json

* Electron

* translate (python library)

* a list of 1000 english words from https://gist.github.com/deekayen/4148741

## How it works:

Every word has a level which is 3 at the beginning. If you know the word, the level goes down 1 level.
If you don't know the translation, the level goes up 1 level. The program doesn't test words with level 0,
because you already knew their translation tree times.
