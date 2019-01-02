# paragon

An open source personal assistant, that I've decided to continue working on. My old repository has been really wonky with the git pushing, so I decided to move it to a new repository, along with revamping the blog


---
### Some changes that are going to be made (hopefully):

- Relative directory names assigned at setup
- Preconfigured database downloads, along with prompts to ask for downloads if the databases don't exist (which means a comprehensive 404/400 exception process)
- a requirements.txt file and a linux.sh and a windows.sh for the various install methods, available on the github. If one wants to compile and setup the code by hand, theyre more than welcome to do that.
- Work on a step by step guide for any account information that might be needed in order to set up things for wolfram, or any other thing. 
- Check for certain programs installed at the runtime of the installer, and configure the code to run with those software included, along with any functionality.
- Speech Recognition driver overhaul (look into writing the speech recognition in C++, as it allows much faster runtimes)
- Provide an option for the video based libraries (Person Identifier, object detector), along with optimization of those algorithms (remove the windows, so that they don't have to render in realtime)
- Speech Synthesis library, only thing that needs to be done is further increase the accuracy, and increase the speed. This should be easy, as it uses the original tacotron algorithm released by google back in 2016-2017.


---

### How to Install

for linux (windows is coming soon)
```git clone https://github.com/lcityd/paragon.git
cd ./paragon
chmod +x ./install_linux
./install_linux
```
