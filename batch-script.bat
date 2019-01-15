@echo off
set /p folderName= "Enter the folder name to access (ex 2019-01-01): "
set /p dateStamp= "Enter the date of csv file(ex 20190101): "


CD "O:\test\test\test\aaaaaaaaa"
python ex.py %folderName% %dateStamp%
MOVE ex1.png %folderName%
MOVE ex2.png %folderName%
CD ..

CD "O:\test\test\test\bbbbbbbbbb"
python ex.py %folderName% %dateStamp%
MOVE ex1.png %folderName%
CD ..

CD "O:\test\test\test\ccccccccc"
python ex.py %folderName% %dateStamp%
MOVE ex1.png %folderName%
MOVE ex2.png %folderName%
CD ..

