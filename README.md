# python-tutorial
The package *kata* contains solutions from [Leetcode](https://leetcode.com/problemset/all/) site.

### How to install
 - Add local virtual interpreter:
 in PyCharm Preferences -> Project Interpreter ->
Add Interpreter -> Add new local interpreter -> Choose **virtualenvEnvironment**.
A new folder **venv** will be created.

 - make current project active to keep dependencies inside current project. 
Execute in the terminal
``source ./venv/bin/activate``<br>
This is required to use `pip` command

 - install required dependencies. Execute in the terminal
``pip install -r requirements.txt`` or press "Install requirements" inside requirements file 

## How to make executable file
1. pip install pyinstaller
2. pyi-makespec --onefile game.py
3. edit the game.spec file, and change the datas part to:
             datas=[
                ('sounds', 'sounds'),
                ('images', 'images'),
                ('intro.py', '.'),
                ('coin.py', '.'), 
                ('snowman.py', '.'), 
                ('star.py', '.')]
4. I have:
        - sounds
        - images
        - intro.py (my original demo)
        - coin.py 
        - star.py 
        - snowman.py 
        - game.py 
        - game.spec (the pyinstaller spec)
5. Comment out the body of the show_default_icon() function in 
    pgzero/game.py:92-95 and add 'pass' to the end. (Wrong path to icon.png is generated during the executable file run)
6. Comment out the line 'pgzrun.go()' in intro.py
7. Run pyinstaller game.spec 
8. Your executable will be in the 'dist' folder. 

