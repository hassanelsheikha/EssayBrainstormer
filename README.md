# essay_brainstormer

This project was designed for the DeerHacks Hackathon (https://deerhacks.mcss.club/). 

## Purpose

Our goal when creating EssayBrainstormer was to create a platform where anyone could provide a keyword, and the platform would handle the brainstorming process of writing on essay on said topic.

## Implementation Overview

This program is implemented using Python as the back-end language. It leverages UiPath for automation and scraping data from Wikipedia (the definitions of terms as of the latest release). For front-end, Flask is used as the web framework.
## Installation Prerequisites 

-As of the time of this writing, **this project is availiable for use only on machines running Windows as their OS**, since UiPath does not support Linux- nor MacOS-based machines.

-Additionally, Internet Explorer must be installed on your machine for the UiPath automation to work.

## Usage

The `__init__.py` module in the main directory is the main module of this project. When run, the console should similar to the screenshot below:

![image](https://user-images.githubusercontent.com/71786895/166153516-8c75c3b3-4b14-44cc-9941-151cf2f96936.png)

Press the blue address, and a webpage identical to the one in the below screenshot should open in your default browser

![image](https://user-images.githubusercontent.com/71786895/166153570-43620d75-8aad-40fb-a30c-8a3db6299860.png)

Here, simply enter a topic into the text field, and after the process executes, the results should be visible on the webpage (as text).

**NOTE: Browser links/windows may open during execution. This is normal! Please do not close the tabs/windows.**
