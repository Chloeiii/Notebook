## Batch Script :pig:  
  
Batch Script is incorporated to **automate command sequences** which are repetitive in nature.   
Scripting is a way by which one can alleviate this necessity by automating these command sequences in order to make one’s life at the shell easier and more productive. In most organizations, Batch Script is incorporated in some way or the other to automate stuff.  

****
### Commands
    1	CD
    This batch command helps in making changes to a different directory, or displays the current directory.

    2	CLS
    This batch command clears the screen.

    3	COPY
    This batch command is used for copying files from one location to the other.

    4	DEL
    This batch command deletes files and not directories.

    5	ECHO
    This batch command displays messages, or turns command echoing on or off.

    6	EXIT
    This batch command exits the DOS console.

    7	MD
    This batch command creates a new directory in the current location.

    8	MOVE
    This batch command moves files or directories between directories.

    9	PAUSE
    This batch command prompts the user and waits for a line of input to be entered.

    10	RD
    This batch command removes directories, but the directories need to be empty before they can be removed.
    
### Variables
- Command Line Arguments

      @echo off 
      echo %1 
      echo %2 
      echo %3
      
      Test.bat 1 2 3

      ->

      1 
      2 
      3
- Local vs Global Variables

      @echo off 
      set globalvar=5
      SETLOCAL
      set var=13145
      set /A var=%var% + 5
      echo %var%
      echo %globalvar%
      ENDLOCAL
      
      ->
      
      13150
      5
