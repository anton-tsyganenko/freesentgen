#!/usr/bin/env python3

# Copyright (c) 2013, 2014 Anton Tsyganenko
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


import sys
import random

defaultNum = 30                                                  # default number of sentences
version = "2.1"



if "-h" in sys.argv:                                             # printing help
    print (
"Freesentgen - free random sentences generator by Anton Tsyganenko\n\
version: {v}\n\n\
options:\n\
-add <file>   - use an addition\n\
-n <number>   - number of sentences\n\
-o <file>     - output to file\n\
-nss <value>  - non-default separator. available values: none, br, br+nl or your arbitrary value\n\
-h            - this help\n\n\
examples of usage:\n\
./freesentgen.py -wb wordsbase.txt -n 10 -i -nss br+nl\n\
./freesentgen.py -o ../content.html -nss \<hr\> -n 50\n\n\
see README.txt for deatils\n\
this program is published under the MIT license. see LICENSE.txt for licensing details.".format(v=version))
    exit()



                                                                 # default base of words and template
adjective = ["A strange", "A big", "A bad", "A dirty", "A funny", "A tired", "A happy", "A clever", "A beautiful", "A silly", "A bored", "A crazy", "An amazing", "A hungry", "A brave", "A fat", "A young", "A sad", "A raring", "An evil", "A trusty", "A rich"]
person = ["cat", "dog", "child", "python", "alien", "terminator", "spy", "boy", "girl", "robot", "programmer", "teacher", "policeman", "astronaut", "neighbor", "ghost", "man", "ringtail", "president", "monster", "tahr", "businessman"]
verb = ["singing", "playing", "sleeping", "eating chocolate", "living", "taking pictures", "working", "counting money", "dancing", "programming", "crying", "jumping", "having fun", "laughing", "spying", "farting", "exploding something", "destroying everything", "studying", "hiding"]
place = ["on the table", "in the prison", "in the school", "in its county house", "at home", "outdoors", "in the theater", "in its room", "at work", "on the roof", "on the bed", "in the cupboard", "on the moon", "under the table", "in the desert", "in the white house", "behind the door", "in the underground", "in your flat", "in the parallel world"]

def getSent():
    return "{adjective} {person} is {verb} {place}. ".format(adjective=random.choice(adjective), verb=random.choice(verb), person=random.choice(person), place=random.choice(place)) + nss


def nextarg(arg):                                                # function for better readability
    return sys.argv[sys.argv.index(arg) + 1]



if "-add" in sys.argv:                                           # additions support
    try:
        addfile = open(nextarg("-add"), "r")
        addtext = addfile.read()
        exec(addtext)
    except:
        print("invalid addition or addition not found")
        exit()



if "-n" in sys.argv:                                             # number of sentences
    try:
        num = int(nextarg("-n"))
    except ValueError:
        print ("number of sentenses should be an integer!")
        num = defaultNum
else:
    num = defaultNum



if "-nss" in sys.argv:                                           # nss: New Sentence Separator
    if nextarg ("-nss") == "none":
        nss = ""
    elif nextarg ("-nss") == "br":
        nss = "<br>"
    elif nextarg ("-nss") == "br+nl":
        nss = "<br>\n"
    else:
        nss = nextarg("-nss") + "\n"
else:
    nss = "\n"



result = ""                                                      # generate the result
for i in range(num):
    result += getSent()



if "-o" in sys.argv:                                             # output the result
    outFile = open(nextarg("-o"), "w")
    print ("output redirected to " + nextarg("-o"))
    outFile.write(result)
    outFile.close()
else:
    print (result)
