# ocr
Simple python ocr code to be executed with python 2.7.13 (Not working for python 3.x !) in windows

Steps to run 
1. Download runocr.py script to your folder such as c:\pyscript  
2. Open command prompt 
3. In your python install folder, enter the following with your screen region needed to be captured for recognition  
    (i.e. upper left and lower right corrdinates x1, y1, x2, y2) 
     pyhon.exe c:\pyscript\runocr.py x1 y1 x2 y2
     
     e.g    C:\Python>  python.exe c:\pyscript\runocr.py 20 470 170 520
     
     
     This will capture a screen region (with position left corner position 20 470 and lower right corner 170 520) on your screen and 
     try to recognize the text inside and show ocr text immediately. 
     
     You can use MousePos.exe downloaded from http://www.adminsehow.com/wp-content/uploads/2012/03/MousePos.exe to find your 
     captured region coordinates.
     
     See my ocr result.png for output result for capturing stock price in my web browser 
     
     
