# Chuangmi ir script

I created this script to be able to send ir commands from domoticz

Needs python-miio https://github.com/rytilahti/python-miio
to make it work :



1 /

Install python-miio from these tutorial.
https://python-miio.readthedocs.io/en/l ... stallation

2/

With the python miio installed check it works with these command

mirobo discover

3/
use the scripts.

When you call the ir.py the led in the device begins to blink and you have 10 seconds to send a the comand, the ir sequence is stored in the file codes.txt, its saved one sequence each line.

To send the ir codes we use the next script irsend.py. You have to specify a number which is the line number in codes.txt, for example if you want to use the tv off wich is the third line.

python3 irsend.py 3

now you can link it to a dummy device in domoticz to send your desired commands


Special thanks to the people of https://github.com/rytilahti/python-miio .
