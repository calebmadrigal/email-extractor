email-extractor
===============

Extracts emails from stdin and prints them out as a comma-separated list.

## Examples

    $ cat testdata.txt | ./email_extractor.py
    test1@gmail.com, test2@yahoo.com, test3@lab.test.com

    $ echo "several emails test1@gmail.com more stuff test2@gmail.com blah blah blah" | ./email_extractor.py
    test1@gmail.com, test2@gmail.com

## Motivation

I often need to send emails to groups of people, whose emails I have in some unorganized format. This script lets me just paste that unorganized data containing emails, and it outputs a comma-separated list I can just paste into my email program.

