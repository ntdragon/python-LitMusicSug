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
echo "Add Suggestion to database"
cd ../page6.d
python3 html_try.py > ../html_examples.d/page6.html
echo "Manual Song Input"
cd ../page7.d
python3 html_try.py > ../html_examples.d/page7.html
echo "Add Search String to Song information"
#cd ../page8.d
#python3 html_try.py > ../html_examples.d/page8.html
#echo "next input generated"
cd ../page9.d
python3 html_try.py > ../html_examples.d/page9.html
echo "Transfer data"
cd ../page10.d
python3 html_try.py > ../html_examples.d/page10.html
echo "Starting a New Songbook in the Database"
cd ..
echo "Done!"