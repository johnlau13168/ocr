# ocr
Simple python ocr code to be executed with python 2.7.13 (No working for python 3.x !) in windows
Steps to run 
1. Download runocr.py script to your folder such as c:\pyscript  
2. Open command prompt and in your python install folder, enter following with your screen region needed to be captured for recognition  
    (i.e. upper left and lower right corrdinates x1, y1, x2, y2) 
     pyhon.exe c:\pyscript\runocr.py x1 y1 x2 y2
     
     e.g    C:\Python>  pyhon.exe c:\pyscript\runocr.py 20 470 170 520
     
     
     This will capture a screen region left corner position 20 470 and lower right corner 170 520 on your screen and 
     try to recognized the text or digits inside and show ocr text immediately. 
     
