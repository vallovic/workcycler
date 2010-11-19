# Workcycler

## Overview

This app reminds you to make breaks when working.
The work and fun/relax times can be changed to personal preference.

Here is a quick video demo: [Link](http://www.youtube.com/watch?v=EyfUe1gXlXQ)


## Requirements (Ubuntu Linux)

- python-gconf

- python-gnome2

- python-pygame

- python-gobject

- python-gtk2

- python-notify

## Installation instructions

### from git

- `git clone http://github.com/daddz/workcycler.git`

- `cd workcycler/`

- `gconftool-2 --install-schema-file ./schemas/workcycler.schemas`

- `./workcycler`

### or download archive

- extract archive

- `cd workcycler/`

- `gconftool-2 --install-schema-file ./schemas/workcycler.schemas`

- `./workcycler`

### finally

- Set your desired times and enable/disable sound in the preferences

I only tested this on Ubuntu but it should work without problems on other distributions.


## Usage

- Click to start the work timer

- Click again to switch to the fun timer immediately

- Rightclick and hit 'Stop' to stop it completely

## Features

- Automatically switches from worktime to funtime and vice versa

- Adjustable times

- Notifications

- Sound notifications

## Planned

- Funny comments for the notifications

- ??

## About

I had the idea for this project after reading [this](http://www.reddit.com/r/programming/comments/e3you/life_hack_the_3030_minute_work_cycle_feels_like/) article I found on reddit.
It´s my first ever python project - _I never touched python before_ - so the code might be unclean and messy (suggestions are welcome).

## Thanks

Faenza Icons by tiheum: http://tiheum.deviantart.com/art/Faenza-Icons-173323228

Sound from: http://freesounds.org

