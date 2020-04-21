# Backend

***There are two things the backend has to do:***

* check if the translation of a word is correct (.check_de_to_en() and .check_en_to_de())

* get a random word from the json files (.get_word())

*Checking a translation:*

That's pretty easy: As an input we get the english and the german word, then we look
for the english word in data/en_to_de.json and we check if its translation = german word

*Getting random word:*

In our json files we have split the words into 4 sections. Because the words are sorted, the
words in the first section are the easiest, and the words in the last sections are the most difficult.
The probability that you get an easy word is greater than the probability that you get a very
difficult word.

So, first we choose one of the four sections in the json files. probabilities:

* section 1 (easy): 50 %
* section 2 (middel): 30 %
* section 3 (difficult): 13 %
* section 4 (very difficult): 7 %

Now we have the section which we have to choose a word from. But we can't just take any word.
That's because the words have levels too. The probability that we choose a word with a higher
level is greater than the probability that we choose one with a lower level, because you already
know words with a low level very well. But how can we code this ?

The first step is to sort the list (section) of words from high to low. Then we group words with the
same level together and remove the group of words with level 0 (because the program doesn't test them).

!!! There can be empty groups, we romve them !!!

Now we have to choose a rondom level, so that we know which group we must choose a word from.

...

I don't know how to do the rest. It is very difficult to choose a random level because there can be any number of
different groups (remember: a group is a group of words which have the same level).
(Actually it isn't really random)
