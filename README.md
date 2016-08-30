# Keyword Captain

Bot to play Boggle-style word games. This currently includes:
- Scrabble Boggle (worldwinner.com)

And could be extended to also include:
- Keyword (royalgames.com)

## Disclaimer

1. The developer(s) are not in any way associated with the games this bot is suggested to be an application for.

2. This software is intended for entertainment purposes only. Using it may violate terms of service on various game sites.

3. Those who have developed this software are not responsible for how you use it. Use at your own risk.

## Setup

This was developed with the Python 3 variant of Anaconda. That can be obtained and installed from here.

After that, from the command line you should be able to...

```
# Go into the main directory of the repo
cd /keyword-captain

# Install the requirements using the conda package manager
# (Here they'd be installed to an environment called 'myenv')
conda create -n myenv --file package-list.txt

# Switch to 'myenv'... below is Linux and MacOS/OS X
source activate myenv
# Or Windows...
activate myenv

# Now you can pull up a Scrabble Boggle window, run this alongside
python src/runScrabbleBoggle.py

# When you're done, deactivate to get out of that env
source deactivate
# Or on Windows just
deactivate
```
