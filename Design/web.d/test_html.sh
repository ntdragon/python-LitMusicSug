#!/bin/bash

# Generate html files from jhtml files

cd page1.d
python3 html_try.py > ../html_examples.d/page1.html
echo "greetings generated"
cd ../page2.d
python3 html_try.py > ../html_examples.d/page2.html
echo "input suggestions generated"
cd ../page3.d
python3 html_try.py > ../html_examples.d/page3.html
echo "suggestions generated"
cd ../page4.d
python3 html_try.py > ../html_examples.d/page4.html
echo "suggestions selection generated"
cd ../page5.d
python3 html_try.py > ../html_examples.d/page5.html
echo "next input generated"
#cd ../page6.d
#python3 html_try.py > ../html_examples.d/page6.html
#echo "next input generated"
cd ..
echo "Done!"