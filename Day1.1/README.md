# Day 1: Development Environment Setup and Intro to Python Koans and Testing

**TODO:** 
1. Write instructions here for environment setup
1. Intro to tests and Python Syntax

## Activity - Intros and Ice-breaker

[Brief intro slides](https://docs.google.com/presentation/d/1aHpbXz6zxflJh3Y5vKF4rSSEnv8iob5Cu8rYhQjFSdA/edit?usp=sharing)

## Setting up our development environment

We will be developing in the Python programming language, using the Pygame Game Engine. The game engine itself isn't as powerful as some of the bigger names you may be familiar with, like Unity and Unreal Engine, but what it does is force us to go under the hood with how these more sophisticated engines work, coding our own keybindings, collider logic, and the like. We won't be making as powerful or visually stunning games as you can make with these more sophisticated engines, but we will leave with a solid understanding how they work!

To get started, there are quite a few bits of tech we need to download. Some of you may already have these installed on your machine, but I encourage you to follow all of these steps regardless - if you are downloading things you already have, your machine will tell you (and it won't do any harm).

**Full Disclosure: Setup is a very hard thing to test before the course begins because everyone's machines are different. Some of you will have problems here. Be patient - we will all do our best to debug during this and get everyone up and running as soon as possible!**

### The tools we need

- Python3
- Pygame
- Jupyter
- Git
- VSCode and some extensions

Below are specific instructions for windows and mac users. The commands and steps are slightly different for each OS, so make sure you're following the instructions specific to your machine.

#### Mac Install
*Note if any of these commands fail to run because of "permissions", add the `sudo` command to the front of them and enter your password when prompted*

1. Open your terminal: 
    1. Open Spotlight (cmd + space)
    1. Type in "terminal"
    1. Press "enter"
1. Download homebrew: homebrew is a package manager for macos. It will help us keep all our packages in the right place and reduce a ton of manual effort required to get things working.
    1. Copy/paste this command into your terminal and run it: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
1. Download Python3: Mac comes with Python2.7 preinstalled (newer macs might come with 3 installed already):
    1. Copy/past this command into your terminal and run it: `brew install python3`
1. Create a virtual environment for Pygame to run in:
    1. `python3 -m virtualenv pygame_env`
    1. `python -m pip install venvdotapp`
    1. `python -m pip install pygame`
    1. Test to see if your virtual environment setup is working correctly: `python -m pygame.examples.aliens`
1. Install Jupyter:
    1. `python3 -m pip install jupyter`
1. Install Git:
    1. `brew install git`
1. Install VSCode and extensions: This is our IDE (integrated development environment). We will be using this together for its excellent plugin support and to share coding environments with one another when pairing on code.
    1. Follow the [instructions](https://code.visualstudio.com/Download) on the website.
    1. Launch VSCode
    1. Download the following extensions in VSCode (click the "extensions" button on the left sidebar):
        1. Python: `ms-python.python`
        1. Jupyter: `ms-toolsai.jupyter`
        1. VSCode Liveshare: `ms-vsliveshare.vsliveshare-pack`
1. Download the class repo:
    1. First we're going to fork the repo (create a personal copy for you to use). Navigate to the following URL: [https://github.com/jtmcg/game-design-course-code/tree/summer_21_design](https://github.com/jtmcg/game-design-course-code/tree/summer_21_design)
    1. Click the "Fork" button in the top right. If you don't have a github account, you will have to make one here.
    1. In the following line, replace the `<your github username>` section with whatever is your github username, then copy/paste it into the terminal and run it: `git clone https://github.com/<your github username>/game-design-course-code.git`

#### Windows Install
1. Open windows powershell as an admin: 
    1. Search for "powershell" using windows search
    1. Click "run as administrator"
1. Download `windev` package manager: `windev` is a new package manager for windows. It will help us keep all our packages in the right place and reduce a ton of manual effort required to get things working.
    1. It's called "Windows App Installer" in the windows store. Go to this url and follow the instructions: `https://www.microsoft.com/en-us/p/app-installer/9nblggh4nns1?activetab=pivot:overviewtab`
1. Download Python3:
    1. Copy/paste this url into your browser: [https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe](https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe)
    1. Once downloaded, open and run the installer.
    1. IMPORTANT!! Before clicking the "Install Now" button, make sure the "Add Python 3.9 to PATH" checkbox is selected!!
    1. Follow the rest of the installation prompts.
1. Download Pygame:
    1. `pip install pygame`
1. Install Jupyter:
    1. `pip install jupyter`
1. Install Git:
    1. Copy/paste thi url into your browser: [https://git-scm.com/download/win](https://git-scm.com/download/win)
    1. Once downloaded, open and run the installer.
1. Install VSCode and extensions: This is our IDE (integrated development environment). We will be using this together for its excellent plugin support and to share coding environments with one another when pairing on code.
    1. Follow the [instructions](https://code.visualstudio.com/Download) on the website.
    1. Launch VSCode
    1. Download the following extensions in VSCode (click the "extensions" button on the left sidebar):
        1. Python: `ms-python.python`
        1. Jupyter: `ms-toolsai.jupyter`
        1. VSCode Liveshare: `ms-vsliveshare.vsliveshare-pack`
1. Download the class repo:
    1. First we're going to fork the repo (create a personal copy for you to use). Navigate to the following URL: [https://github.com/jtmcg/game-design-course-code/tree/summer_21_design](https://github.com/jtmcg/game-design-course-code/tree/summer_21_design)
    1. Click the "Fork" button in the top right. If you don't have a github account, you will have to make one here.
    1. In the following line, replace the `<your github username>` section with whatever is your github username, then copy/paste it into the terminal and run it: `git clone https://github.com/<your github username>/game-design-course-code.git`

## Introduction to Python Koans and Testing
Now that our environments are up and running, let's learn about our assignments and testing!

### Tests and Test Driven Development

Testing is an integral part of any software developers workflow. I'm sure you're all familiar with testing your own code to make sure it is running correctly. This may involve manually entering inputs to your program and checking the outputs to make sure things are working as expected, but this manual process can be tedious and time consuming. 

However tedious, testing is an integral part to any software developer's workflow. But, developers are famously lazy, and when faced with a problem like manually testing code, we are prone to say "I can automate that". Thus, unit and integration testing was born, a means for us to test our code *with other code*. This is especially useful in large applications, where a change introduced in a small part of the application may affect a completely different part of the application in unexpected ways.

A test in software is a piece of code that, as the name suggests, tests another piece of code through automation so the developer doesn't have to test it manually themselves. Usually, this involves invoking part of the code that the developer has written, such as a function or method, passing in some inputs, and checking that the output is what the user expected. Different languages have different ways of doing this, and often there are entire frameworks dedicated to testing, such as `unittest` in **Python** or `Jest` in **JavaScript** (and **TypeScript**).

### Python Koans
***Koan**: a paradoxical anecdote or riddle, used in Zen Buddhism to demonstrate the inadequacy of logical reasoning and to provoke enlightenment."*

In coding, Koans have been adapted as a means to teach new coding languages by doing and problem solving. I have personally used Koans to learn **Clojure** for my job at CircleCI, much like we will be using Koans to learn **Python**.

Koans, in particular, leverage a technique called ["Test Driven Development" or TDD](https://en.wikipedia.org/wiki/Test-driven_development). In TDD, it is common practice to write tests *BEFORE* writing the code to make the test pass.
In the case of Koans, the tests are already written for us, as is the boilerplate code to make the test pass, and all we must do is edit the boilerplate code with the koan "solution" to make the test pass.

You might be wondering why I've put "solution" in quotes. That is because, in programming, there is never really one right way to do something. My philosophy is that code is *opinion*, informed by what you know and what has worked for you in the past. Often, we will solve similar problems in completely different ways depending on the situation we find ourselves in, because reasons. These might be readability, parallelism with other code in a similar place, or even just that we couldn't think of any other way to solve the problem at the time. The important part here is that **if it works, it isn't wrong**. However, we should all be open to hear each other's input and opinions about the code we write, because that is *the best* way to improve as a programmer.

## Our First Koans
We will be completing the first Koan assignment together today, to get introduced to both **Python** syntax and how to complete a Koan assignment. 

Throughout this week, I will be assigning about half of the total **Python** Koans to be worked on in pairs. The remaining koans are not necessary for this course, but do introduce more advanced **Python** concepts you can use to continue to improve your skills after the course is complete.

### How To Run the Koans
We'll want to be able to see our code AND the output at the same time, so we will open a terminal here in VSCode by pressing `ctrl/cmd + shift + ~` (windows/mac). Alternatively, you can click `Terminal -> New Terminal` in the top navbar. 

1. Move the assigned Koans from the "additional_koans" folder to the "koans" folder.
1. Navigate to the `python_koans` folder in the terminal: `cd ./python_koans`
1. Run the koans: 
    1. Windows: `python contemplate_koans.py`
    1. Mac: `./run.sh`
1. Open the file with the failing koan (`about_asserts.py`) and start editing!

### Liveshare Demo
While working on the assignments, we will leverage VSCode's built-in paired-programming capabilities with the Liveshare plugin. Open the extension, sign in using github, and then copy/paste the share link with your partner. Only one of you needs to copy/paste the link, but both of you should be able to edit the same page now, as well as see the other person's screen.

I need a volunteer to help me demonstrate.

## Assignment
Before tomorrow, you are expected to have completed the following koans:

1. `about_1.1.1_asserts.py`
1. `about_1.1.3_none.py`
1. `about_1.1.2_true_and_false.py` 