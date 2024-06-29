# Text Handler

## Run App
### Local

```sh
$ sh run.sh
```

```sh
$ poetry run python -m app.main
```

## Development
### Run Tests and Linter

```
$ poetry run tox
```

## App Output
### The program output should look like below:
```
A word containing 'z':  summarizing
Removed leading zeros from an IP address:  216.8.94.196
Substring 1: {'summarizing': (55, 66)}
Substring 2: {'summarizing': (164, 175)}
Changed date format:  20-11-2020
All three, four, and five character words:  ['the', 'key', 'the', 'work', 'being', 'the', 'body', 'the', 'and', 'the', 'texts', 'start', 'with', 'the', 'task', 'goal', 'and', 'what', 'the', 'end', 'look', 'like']
Converted a camel-case to a snake-case:  text_exercise
Adverb 1:  (208, 215, 'usually')
Adverb 2:  (264, 272, 'possibly')
Concatenated the consecutive numbers:
 Enter at 120 Kearny Street. The security desk can direct you to floor 16. Please have your identification ready.
```
### This application solves the following tasks:
1. [x] Match a word containing 'z', not the start or end of the word
2. [x] Remove leading zeros from an IP address
3. [x] Find the occurrence and position of substrings within a string (використайте атрбути знайденої групи)
4. [x] Convert a date of yyyy-mm-dd format to dd-mm-yyyy format
5. [x] Find all three, four, and five character words in a string
6. [x] Convert a camel-case string to a snake-case string
7. [x] Find all adverbs and their positions in a given sentence
8. [x] Concatenate the consecutive numbers in a given string:

Original string:
```
Enter at 1 20 Kearny Street. The security desk can direct you to floor 1 6. Please have your identification ready.
```
After concatenating the consecutive numbers in the said string:
```
Enter at 120 Kearny Street. The security desk can direct you to floor 16. Please have your identification ready.
```