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
'-add <file>'   - use an addition
'-n <number>'   - number of sentences you want to generate
'-o <file>'     - output to file
'-nss <value>'  - non-default separator. available values: none, br(html-tag "<br>"), br+nl("<br>" tag + new line) or any text (it will be inserted between sentences)
'-h'            - show help

examples of usage:

	./freesentgen.py -add wordsbase.txt -n 10 -nss br+nl
	./freesentgen.py -o ../content.html -nss \<hr\> -n 50

##additions documentation:

additions can add new features to the freesentgen.
they are normal python 3 files.
the example of addition is a base of words. it should contain function getSent(), that would generate a sentence.
see "addition-wordbase.example" for real example of addition.

##bug reporting:

please, report bugs to anton-tsyganenko@yandex.ru

##licensing:

this program is published under the MIT license. see LICENSE.txt for more details.
