#!/bin/bash

# Generate html files from jhtml files

cd page0.d
python3 html_try.py > ../html_examples.d/page0.html
echo "0-Main Directory Page generated"
cd ../page1.d
python3 html_try.py > ../html_examples.d/page1.html
echo "1-greetings generated"
cd ../page2.d
python3 html_try.py > ../html_examples.d/page2.html
echo "2-input NPM suggestions generated"
cd ../page2a.d
python3 html_try.py > ../html_examples.d/page2a.html
echo "2a-input Other suggestions generated"
cd ../page3.d
python3 html_try.py > ../html_examples.d/page3.html
echo "3-suggestions generated"
cd ../page4.d
python3 html_try.py > ../html_examples.d/page4.html
echo "4-suggestions selection generated"
cd ../page5.d
python3 html_try.py > ../html_examples.d/page5.html
echo "5-Add Suggestion to database generated"
cd ../page6.d
python3 html_try.py > ../html_examples.d/page6.html
echo "6-Manual Song Input generated"
cd ../page7.d
python3 html_try.py > ../html_examples.d/page7.html
echo "7-Add Search String to Song information generated"
#cd ../page8.d
#python3 html_try.py > ../html_examples.d/page8.html
#echo "8-next input generated"
cd ../page9.d
python3 html_try.py > ../html_examples.d/page9.html
echo "9-Transfer data generated"
cd ../page10.d
python3 html_try.py > ../html_examples.d/page10.html
echo "10-Starting a New Songbook in the Database generated"
cd ../page11.d
python3 html_try.py > ../html_examples.d/page11.html
echo "11-Update Calendar generated"
#cd ../page12.d
#python3 html_try.py > ../html_examples.d/page12.html
#echo "12-Edit Personal Profile generated"
#cd ../page13.d
#python3 html_try.py > ../html_examples.d/page13.html
#echo "13-Edit Parish Profile generated"
#cd ../page14.d
#python3 html_try.py > ../html_examples.d/page14.html
#echo "14-Print Event Music Sheet generated"
#cd ../page15.d
#python3 html_try.py > ../html_examples.d/page15.html
#echo "15-Songbook Listing Alphabetic generated"
#cd ../page16.d
#python3 html_try.py > ../html_examples.d/page61.html
#echo "16-Songbook Listing Numeric generated"
#cd ../page17.d
#python3 html_try.py > ../html_examples.d/page17.html
#echo "17-next input generated"
#cd ../page18.d
#python3 html_try.py > ../html_examples.d/page18.html
#echo "18-next input generated"
#cd ../page19.d
#python3 html_try.py > ../html_examples.d/page19.html
#echo "19-next input generated"
#cd ../page20.d
#python3 html_try.py > ../html_examples.d/page20.html
#echo "20-next input generated"
cd ..
echo "Done!"
