# wheeloftimeline

Visualizing the POV changes in Robert Jordan's "The Wheel of Time" book series.

## Getting Started

These instructions will help you get a copy of my project up and running on your own machine.

### Prerequisites

Things you need to install prior to copying this project and how to install them:

```
python version3
requests
beautiful soup
numpy
matplotlib
venv (recommended)
```

### Installing

Follow these step-by-step procedures to install all necessary packages to create the necessary development environment. *(Note: I use MacOS, some steps may vary for a Windows machine)*

Begin by opening a terminal on your local machine. We need to install Python 3 or later. You can check your Python version with the following command.

```
$ python --version
```

If you need to install the proper Python version, follow the instructions provided [here](https://docs.python-guide.org/starting/installation/). I often use Homebrew, as it includes pip:

```
$ brew install python
```

Now, assuming you have Python 3 and pip installed properly from the previous steps, we can begin to install the necessary python packages.

```
$ pip install requests
$ pip install bs4
$ pip install matplotlib
$ pip install numpy
```

Finally, clone this repository to the location/directory of your choice. Ensure you navigate to the directory in which you wish to have a copy of this repository.

```
$ cd path/to/directory
$ git clone https://github.com/suzieh/wheeloftimeline.git
```

## Virtual Environments

I recommend activating a virtual environment prior to playing with this program. The venv module should already be installed with Python 3:

```
$ python3 -m venv venv
$ . ./venv/bin/activate
```

To deactivate:

```
$ deactivate
```

The first line of creating the venv creates a directory for the virtual environment, so you will not need to repeat this line in future instances of activating an environment in this directory.

## Running the Program

The program scraps data from the Wheel of Time Wiki page, and generates a plot mapping the changes in point of view within the books to a chart which appears in an independent window.

The entire process is driven by the main.py script, which can be executed using the following command.

```
$ pythonw main.py
```
A window should appear containing the plot. On the bottom frame, the characters are listed as you move your cursor over the graph. Additionally, you'll notice features in the lower left, including a zoom feature to zoom in on certain parts of the graph content.

## Versioning

All versions are maintained through GitHub. For access to previous versions, please visit the [tags on this repository](https://github.com/suzieh/wheeloftimeline/tags).

## Authors

**Suzie Hoops** - *original work*

## Resources

Data Collected from the online resource [*The Wheel of Time Wiki*](http://wot.wikia.com/wiki/Statistical_analysis)