#Freesentgen

Freesentgen - free random sentences generator by Anton Tsyganenko <anton-tsyganenko@yandex.ru>

The Freesentgen is a free random sentences generator, created by Anton Tsyganenko.
It can be useful for anyone, but primarily for web designers

##running instructions:

extract files from archive
install python 3 <python.org> if it is not installed
run freesentgen.py with python 3

##usage:

options:
'-wb <file>'    - use external base of words. you can read about bases of words in wordbase documentation
'-n <number>'   - number of sentences you want to generate
'-o <file>'     - output to file
'-i'            - show information
'-nss <value>'  - non-default separator. available values: none, br(html-tag "<br>"), br+nl("<br>" tag + new line) or any text (it will be inserted between sentences)
'-h'            - show help

examples of usage:

	./freesentgen.py -wb wordsbase.txt -n 10 -i -nss br+nl
	./freesentgen.py -o ../content.html -nss \<hr\> -n 50

##bases of words documentation:

first line - adjectives
second line - persons
third line - verbs
fourth line - places (in fact it can be not a place)
fifth line - layout
sixth line and next - anything you want.
values in 1-4 line should be separated with comma and WITHOUT space.
see "wordbase.example" for real example of base of words.

##bug reporting:

please, report bugs to anton-tsyganenko@yandex.ru

##licensing:

this program is published under the MIT license. see LICENSE.txt for more details.
