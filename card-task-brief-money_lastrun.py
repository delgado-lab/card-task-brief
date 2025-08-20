#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on Thu Jul  6 13:58:21 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2022.2.5')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'card-task-brief-money'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/Bhanji/Library/CloudStorage/Box-Box/laptop/CardTask/card-task-brief/card-task-brief-money_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1496, 967], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='standard', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='norm')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}
ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='event')

# --- Initialize components for Routine "Instructions" ---
Inst1 = visual.TextStim(win=win, name='Inst1',
    text='In this part of the study you will play a card guessing game to win money. \n\nPress ‘1’ to continue.',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
response1 = keyboard.Keyboard()
# Run 'Begin Experiment' code from setupvars
totalwon = 0.0
rew_amount = 1.0
pun_amount = .5
iti1rew_code1 = [1,1,1,1,1,3,3,3,5,5]
iti2rew_code1 = [4,4,4,4,4,6,6,6,8,8]
iti1pun_code1 = [1,1,1,1,1,3,3,3,5,5]
iti2pun_code1 = [4,4,4,4,4,6,6,6,8,8]
#iti1rew_code2 = [1,1,1,1,1,3,3,3,5,5]
#iti2rew_code2 = [4,4,4,4,4,6,6,6,8,8]
#iti1pun_code2 = [1,1,1,1,1,3,3,3,5,5]
#iti2pun_code2 = [4,4,4,4,4,6,6,6,8,8]
#iti1rew_code3 = [1,1,1,1,1,3,3,3,5,5]
#iti2rew_code3 = [4,4,4,4,4,6,6,6,8,8]
#iti1pun_code3 = [1,1,1,1,1,3,3,3,5,5]
#iti2pun_code3 = [4,4,4,4,4,6,6,6,8,8]
shuffle(iti1rew_code1)
shuffle(iti2rew_code1)
shuffle(iti1pun_code1)
shuffle(iti2pun_code1)
#shuffle(iti1rew_code2)
#shuffle(iti2rew_code2)
#shuffle(iti1pun_code2)
#shuffle(iti2pun_code2)
#shuffle(iti1rew_code3)
#shuffle(iti2rew_code3)
#shuffle(iti1pun_code3)
#shuffle(iti2pun_code3)
#rewlargeimagelist = ['high1.jpg','high2.jpg','high3.jpg','high4.jpg','high5.jpg','high6.jpg','high7.jpg','high8.jpg','high9.jpg','high10.jpg']
#punlargeimagelist = ['low1.jpg','low2.jpg','low3.jpg','low4.jpg','low5.jpg','low6.jpg','low7.jpg','low8.jpg','low9.jpg','low10.jpg']
#shuffle(rewlargeimagelist)
#shuffle(punlargeimagelist)
win.mouseVisible = False



# --- Initialize components for Routine "Instructions_2" ---
Inst1_2 = visual.TextStim(win=win, name='Inst1_2',
    text='You will play many repeated trials of the guessing game. The text on the screen will tell you what type of reward you are playing for.\n\nPress ‘1’ to continue.',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
response1_2 = keyboard.Keyboard()

# --- Initialize components for Routine "Instructions_3" ---
Inst1_3 = visual.TextStim(win=win, name='Inst1_3',
    text='How to play the game:  \n\nEverytime you see a “?” card on the screen your job is to guess whether the number on the card is lower or higher than 5.\n\nIf you want to guess a LOW number\n     -Press the ‘1’ button-\n\nIf you want to guess a HIGH number\n     -Press the ‘2’ button-\n\nPossible card values range from 1-4 (lower) and (6-9) higher, but will never be 5. You have 2 seconds to make your guess for each card. Shortly after your guess the card value will be displayed.\n\nPress ‘1’ to continue.',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
response1_3 = keyboard.Keyboard()

# --- Initialize components for Routine "trigger" ---
Inst1_4 = visual.TextStim(win=win, name='Inst1_4',
    text='The task will begin in a few moments.',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
trigger_input = keyboard.Keyboard()

# --- Initialize components for Routine "firstITI4s" ---
firstTrialITI = visual.TextStim(win=win, name='firstTrialITI',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "blockstart" ---
text_block = visual.TextStim(win=win, name='text_block',
    text='In this block of trials, you will try to win:',
    font='Arial',
    pos=(0, 0.25), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_blocktype = visual.TextStim(win=win, name='text_blocktype',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
fixation = visual.TextStim(win=win, name='fixation',
    text='.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "settrialtype_routine" ---

# --- Initialize components for Routine "Reward_resp" ---
rect_resp_rew = visual.Rect(
    win=win, name='rect_resp_rew',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=5,     colorSpace='rgb',  lineColor=[1,1,1], fillColor='black',
    opacity=1, depth=0.0, interpolate=True)
quest_rew = visual.TextStim(win=win, name='quest_rew',
    text='?',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
response_rew = keyboard.Keyboard()
ITI1_rew = visual.TextStim(win=win, name='ITI1_rew',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "RewardOutcome" ---
rect_out_rew = visual.Rect(
    win=win, name='rect_out_rew',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=5,     colorSpace='rgb',  lineColor=[1,1,1], fillColor='black',
    opacity=1, depth=0.0, interpolate=True)
feedback_rew = visual.TextStim(win=win, name='feedback_rew',
    text='',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
display_rew = visual.TextStim(win=win, name='display_rew',
    text='',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
ITI2_rew = visual.TextStim(win=win, name='ITI2_rew',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
image_rew = visual.ImageStim(
    win=win,
    name='image_rew', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
image_greencheck = visual.ImageStim(
    win=win,
    name='image_greencheck', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

# --- Initialize components for Routine "Punishment_resp" ---
rect_resp_pun = visual.Rect(
    win=win, name='rect_resp_pun',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=5,     colorSpace='rgb',  lineColor=[1,1,1], fillColor='black',
    opacity=1, depth=0.0, interpolate=True)
quest_pun = visual.TextStim(win=win, name='quest_pun',
    text='?',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
response_pun = keyboard.Keyboard()
ISI2 = visual.TextStim(win=win, name='ISI2',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "PunishmentOutcome" ---
rect_out_pun = visual.Rect(
    win=win, name='rect_out_pun',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=5,     colorSpace='rgb',  lineColor=[1,1,1], fillColor='black',
    opacity=1, depth=0.0, interpolate=True)
feedback_pun = visual.TextStim(win=win, name='feedback_pun',
    text='',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
display_pun = visual.TextStim(win=win, name='display_pun',
    text='',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=0.2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
ITI2_pun = visual.TextStim(win=win, name='ITI2_pun',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
image_pun = visual.ImageStim(
    win=win,
    name='image_pun', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
image_redx = visual.ImageStim(
    win=win,
    name='image_redx', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

# --- Initialize components for Routine "EndText" ---
Finished = visual.TextStim(win=win, name='Finished',
    text="Thanks for playing!\n\nYour total:",
    font='Arial',
    pos=(0, 0.15), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Total_display = visual.TextStim(win=win, name='Total_display',
    text='',
    font='Arial',
    pos=(0, -0.1), height=0.12, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_2 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
response1.keys = []
response1.rt = []
_response1_allKeys = []
# keep track of which components have finished
InstructionsComponents = [Inst1, response1]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Inst1* updates
    if Inst1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Inst1.frameNStart = frameN  # exact frame index
        Inst1.tStart = t  # local t and not account for scr refresh
        Inst1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Inst1, 'tStartRefresh')  # time at next scr refresh
        Inst1.setAutoDraw(True)
    
    # *response1* updates
    waitOnFlip = False
    if response1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        response1.frameNStart = frameN  # exact frame index
        response1.tStart = t  # local t and not account for scr refresh
        response1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(response1, 'tStartRefresh')  # time at next scr refresh
        response1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(response1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(response1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if response1.status == STARTED and not waitOnFlip:
        theseKeys = response1.getKeys(keyList=['1','b'], waitRelease=False)
        _response1_allKeys.extend(theseKeys)
        if len(_response1_allKeys):
            response1.keys = _response1_allKeys[-1].name  # just the last key pressed
            response1.rt = _response1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instructions" ---
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if response1.keys in ['', [], None]:  # No response was made
    response1.keys = None
thisExp.addData('response1.keys',response1.keys)
if response1.keys != None:  # we had a response
    thisExp.addData('response1.rt', response1.rt)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Instructions_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
response1_2.keys = []
response1_2.rt = []
_response1_2_allKeys = []
# keep track of which components have finished
Instructions_2Components = [Inst1_2, response1_2]
for thisComponent in Instructions_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instructions_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Inst1_2* updates
    if Inst1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Inst1_2.frameNStart = frameN  # exact frame index
        Inst1_2.tStart = t  # local t and not account for scr refresh
        Inst1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Inst1_2, 'tStartRefresh')  # time at next scr refresh
        Inst1_2.setAutoDraw(True)
    
    # *response1_2* updates
    waitOnFlip = False
    if response1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        response1_2.frameNStart = frameN  # exact frame index
        response1_2.tStart = t  # local t and not account for scr refresh
        response1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(response1_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'response1_2.started')
        response1_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(response1_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(response1_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if response1_2.status == STARTED and not waitOnFlip:
        theseKeys = response1_2.getKeys(keyList=['1', 'b'], waitRelease=False)
        _response1_2_allKeys.extend(theseKeys)
        if len(_response1_2_allKeys):
            response1_2.keys = _response1_2_allKeys[-1].name  # just the last key pressed
            response1_2.rt = _response1_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instructions_2" ---
for thisComponent in Instructions_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if response1_2.keys in ['', [], None]:  # No response was made
    response1_2.keys = None
thisExp.addData('response1_2.keys',response1_2.keys)
if response1_2.keys != None:  # we had a response
    thisExp.addData('response1_2.rt', response1_2.rt)
thisExp.nextEntry()
# the Routine "Instructions_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Instructions_3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
response1_3.keys = []
response1_3.rt = []
_response1_3_allKeys = []
# keep track of which components have finished
Instructions_3Components = [Inst1_3, response1_3]
for thisComponent in Instructions_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instructions_3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Inst1_3* updates
    if Inst1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Inst1_3.frameNStart = frameN  # exact frame index
        Inst1_3.tStart = t  # local t and not account for scr refresh
        Inst1_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Inst1_3, 'tStartRefresh')  # time at next scr refresh
        Inst1_3.setAutoDraw(True)
    
    # *response1_3* updates
    waitOnFlip = False
    if response1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        response1_3.frameNStart = frameN  # exact frame index
        response1_3.tStart = t  # local t and not account for scr refresh
        response1_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(response1_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'response1_3.started')
        response1_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(response1_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(response1_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if response1_3.status == STARTED and not waitOnFlip:
        theseKeys = response1_3.getKeys(keyList=['1', 'b'], waitRelease=False)
        _response1_3_allKeys.extend(theseKeys)
        if len(_response1_3_allKeys):
            response1_3.keys = _response1_3_allKeys[-1].name  # just the last key pressed
            response1_3.rt = _response1_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instructions_3" ---
for thisComponent in Instructions_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if response1_3.keys in ['', [], None]:  # No response was made
    response1_3.keys = None
thisExp.addData('response1_3.keys',response1_3.keys)
if response1_3.keys != None:  # we had a response
    thisExp.addData('response1_3.rt', response1_3.rt)
thisExp.nextEntry()
# the Routine "Instructions_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "trigger" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
trigger_input.keys = []
trigger_input.rt = []
_trigger_input_allKeys = []
# keep track of which components have finished
triggerComponents = [Inst1_4, trigger_input]
for thisComponent in triggerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "trigger" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Inst1_4* updates
    if Inst1_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Inst1_4.frameNStart = frameN  # exact frame index
        Inst1_4.tStart = t  # local t and not account for scr refresh
        Inst1_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Inst1_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Inst1_4.started')
        Inst1_4.setAutoDraw(True)
    
    # *trigger_input* updates
    waitOnFlip = False
    if trigger_input.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trigger_input.frameNStart = frameN  # exact frame index
        trigger_input.tStart = t  # local t and not account for scr refresh
        trigger_input.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trigger_input, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trigger_input.started')
        trigger_input.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(trigger_input.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(trigger_input.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if trigger_input.status == STARTED and not waitOnFlip:
        theseKeys = trigger_input.getKeys(keyList=['t'], waitRelease=False)
        _trigger_input_allKeys.extend(theseKeys)
        if len(_trigger_input_allKeys):
            trigger_input.keys = _trigger_input_allKeys[-1].name  # just the last key pressed
            trigger_input.rt = _trigger_input_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in triggerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "trigger" ---
for thisComponent in triggerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if trigger_input.keys in ['', [], None]:  # No response was made
    trigger_input.keys = None
thisExp.addData('trigger_input.keys',trigger_input.keys)
if trigger_input.keys != None:  # we had a response
    thisExp.addData('trigger_input.rt', trigger_input.rt)
thisExp.nextEntry()
# the Routine "trigger" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "firstITI4s" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
firstITI4sComponents = [firstTrialITI]
for thisComponent in firstITI4sComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "firstITI4s" ---
while continueRoutine and routineTimer.getTime() < 4.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *firstTrialITI* updates
    if firstTrialITI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        firstTrialITI.frameNStart = frameN  # exact frame index
        firstTrialITI.tStart = t  # local t and not account for scr refresh
        firstTrialITI.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(firstTrialITI, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'firstTrialITI.started')
        firstTrialITI.setAutoDraw(True)
    if firstTrialITI.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > firstTrialITI.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            firstTrialITI.tStop = t  # not accounting for scr refresh
            firstTrialITI.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'firstTrialITI.stopped')
            firstTrialITI.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in firstITI4sComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "firstITI4s" ---
for thisComponent in firstITI4sComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-4.000000)

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('design/card-task-brief-blocks.csv'),
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "blockstart" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    text_blocktype.setText(blocktype)
    # Run 'Begin Routine' code from setblockvars
    cardsize = (.4, .8)
    cardxy = (0,0) 
    numbersize = .14
    numberxy = (0,0)
    msg_xy = (.35,-.2)
    msg_size = .14
    noresp_msg_size = .08
    outtypeimg_xy = (.35,0)
    outtypeimg_size = (.15,.15)
    checkx_size = (.15,.15)
    checkx_xy = (0,-.2)
    #largeimagexy = (0.5,0)
    
    if blockcode == 1: #money
        rewimage = "images/money.jpg"
        rewimagesize = outtypeimg_size
        punimage = "images/moneyloss.jpg"
        punimagesize = outtypeimg_size
        block_rewdisplay = "+$%.2f" % (rew_amount)
        block_pundisplay = "-$%04.2f" % (pun_amount)
    
        #cardxy = (-0.25,0)
    #elif blockcode == 2: #cigarette
    #    rewimage = "images/cig.jpg"
    #    rewimagesize = outtypeimg_size
    #    punimage = "images/cigloss.jpg"
    #    punimagesize = outtypeimg_size
    #    rewdisplay = "+2 puffs"
    #    pundisplay = "-1 puff"
    #    cardxy = (-0.25,0)
    #elif blockcode == 3: #images
    #    rewimage = "images/black.jpg"
    #    punimage = "images/black.jpg"
    #    rewimagesize = 0
    #    punimagesize = 0
    #    rewdisplay = ""
    #    pundisplay = ""
    #    cardxy = (-0.5,0)
    # keep track of which components have finished
    blockstartComponents = [text_block, text_blocktype, fixation]
    for thisComponent in blockstartComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blockstart" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_block* updates
        if text_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_block.frameNStart = frameN  # exact frame index
            text_block.tStart = t  # local t and not account for scr refresh
            text_block.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_block, 'tStartRefresh')  # time at next scr refresh
            text_block.setAutoDraw(True)
        if text_block.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_block.tStartRefresh + 0-frameTolerance:
                # keep track of stop time/frame for later
                text_block.tStop = t  # not accounting for scr refresh
                text_block.frameNStop = frameN  # exact frame index
                text_block.setAutoDraw(False)
        
        # *text_blocktype* updates
        if text_blocktype.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_blocktype.frameNStart = frameN  # exact frame index
            text_blocktype.tStart = t  # local t and not account for scr refresh
            text_blocktype.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_blocktype, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_blocktype.started')
            text_blocktype.setAutoDraw(True)
        if text_blocktype.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_blocktype.tStartRefresh + 0-frameTolerance:
                # keep track of stop time/frame for later
                text_blocktype.tStop = t  # not accounting for scr refresh
                text_blocktype.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_blocktype.stopped')
                text_blocktype.setAutoDraw(False)
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation.started')
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + 0-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation.stopped')
                fixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockstartComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blockstart" ---
    for thisComponent in blockstartComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "blockstart" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    innertrials = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('design/card-task-brief-trials.csv'),
        seed=None, name='innertrials')
    thisExp.addLoop(innertrials)  # add the loop to the experiment
    thisInnertrial = innertrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisInnertrial.rgb)
    if thisInnertrial != None:
        for paramName in thisInnertrial:
            exec('{} = thisInnertrial[paramName]'.format(paramName))
    
    for thisInnertrial in innertrials:
        currentLoop = innertrials
        # abbreviate parameter names if possible (e.g. rgb = thisInnertrial.rgb)
        if thisInnertrial != None:
            for paramName in thisInnertrial:
                exec('{} = thisInnertrial[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "settrialtype_routine" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from settrialtype
        largeimage = "images/black.jpg"
        #code to specify isi/iti (ensures same isi/itis for wins and losses)
        if win1lose0==1:
            nRew=1
            nPun=0
            #code to handle multiple reward types (ensures same isis/itis for each condition)
            if blockcode == 1:
                iti1 = iti1rew_code1.pop()
                iti2 = iti2rew_code1.pop()
        #    elif blockcode == 2:
        #        iti1 = iti1rew_code2.pop()
        #        iti2 = iti2rew_code2.pop()
        #    elif blockcode == 3: #use for rewards that involve a picture
        #        largeimage = "images/" + rewlargeimagelist.pop()
        #        iti1 = iti1rew_code3.pop()
        #        iti2 = iti2rew_code3.pop()
        else:
            nRew=0
            nPun=1
            #code to handle multiple reward types (ensures same isis/itis for each condition)
            if blockcode == 1:
                iti1 = iti1pun_code1.pop()
                iti2 = iti2pun_code1.pop()
        #    elif blockcode == 2:
        #        iti1 = iti1pun_code2.pop()
        #        iti2 = iti2pun_code2.pop()
        #    elif blockcode == 3: #use for rewards that involve a picture
        #        largeimage = "images/" + punlargeimagelist.pop()
        #        iti1 = iti1pun_code3.pop()
        #        iti2 = iti2pun_code3.pop()
        
        # keep track of which components have finished
        settrialtype_routineComponents = []
        for thisComponent in settrialtype_routineComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "settrialtype_routine" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in settrialtype_routineComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "settrialtype_routine" ---
        for thisComponent in settrialtype_routineComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "settrialtype_routine" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        Reward = data.TrialHandler(nReps=nRew, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='Reward')
        thisExp.addLoop(Reward)  # add the loop to the experiment
        thisReward = Reward.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisReward.rgb)
        if thisReward != None:
            for paramName in thisReward:
                exec('{} = thisReward[paramName]'.format(paramName))
        
        for thisReward in Reward:
            currentLoop = Reward
            # abbreviate parameter names if possible (e.g. rgb = thisReward.rgb)
            if thisReward != None:
                for paramName in thisReward:
                    exec('{} = thisReward[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "Reward_resp" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            rect_resp_rew.setPos(cardxy)
            rect_resp_rew.setSize(cardsize)
            quest_rew.setPos(cardxy)
            quest_rew.setHeight(numbersize)
            response_rew.keys = []
            response_rew.rt = []
            _response_rew_allKeys = []
            ITI1_rew.setText('+')
            # keep track of which components have finished
            Reward_respComponents = [rect_resp_rew, quest_rew, response_rew, ITI1_rew]
            for thisComponent in Reward_respComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Reward_resp" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *rect_resp_rew* updates
                if rect_resp_rew.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rect_resp_rew.frameNStart = frameN  # exact frame index
                    rect_resp_rew.tStart = t  # local t and not account for scr refresh
                    rect_resp_rew.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rect_resp_rew, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'rect_resp_rew.started')
                    rect_resp_rew.setAutoDraw(True)
                if rect_resp_rew.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > rect_resp_rew.tStartRefresh + 2.0-frameTolerance:
                        # keep track of stop time/frame for later
                        rect_resp_rew.tStop = t  # not accounting for scr refresh
                        rect_resp_rew.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'rect_resp_rew.stopped')
                        rect_resp_rew.setAutoDraw(False)
                
                # *quest_rew* updates
                if quest_rew.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    quest_rew.frameNStart = frameN  # exact frame index
                    quest_rew.tStart = t  # local t and not account for scr refresh
                    quest_rew.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(quest_rew, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'quest_rew.started')
                    quest_rew.setAutoDraw(True)
                if quest_rew.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > quest_rew.tStartRefresh + 2.0-frameTolerance:
                        # keep track of stop time/frame for later
                        quest_rew.tStop = t  # not accounting for scr refresh
                        quest_rew.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'quest_rew.stopped')
                        quest_rew.setAutoDraw(False)
                
                # *response_rew* updates
                waitOnFlip = False
                if response_rew.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    response_rew.frameNStart = frameN  # exact frame index
                    response_rew.tStart = t  # local t and not account for scr refresh
                    response_rew.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(response_rew, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'response_rew.started')
                    response_rew.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(response_rew.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(response_rew.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if response_rew.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > response_rew.tStartRefresh + 2.0-frameTolerance:
                        # keep track of stop time/frame for later
                        response_rew.tStop = t  # not accounting for scr refresh
                        response_rew.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'response_rew.stopped')
                        response_rew.status = FINISHED
                if response_rew.status == STARTED and not waitOnFlip:
                    theseKeys = response_rew.getKeys(keyList=['1','2','b','y'], waitRelease=False)
                    _response_rew_allKeys.extend(theseKeys)
                    if len(_response_rew_allKeys):
                        response_rew.keys = [key.name for key in _response_rew_allKeys]  # storing all keys
                        response_rew.rt = [key.rt for key in _response_rew_allKeys]
                
                # *ITI1_rew* updates
                if ITI1_rew.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                    # keep track of start time/frame for later
                    ITI1_rew.frameNStart = frameN  # exact frame index
                    ITI1_rew.tStart = t  # local t and not account for scr refresh
                    ITI1_rew.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ITI1_rew, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ITI1_rew.started')
                    ITI1_rew.setAutoDraw(True)
                if ITI1_rew.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ITI1_rew.tStartRefresh + iti1-frameTolerance:
                        # keep track of stop time/frame for later
                        ITI1_rew.tStop = t  # not accounting for scr refresh
                        ITI1_rew.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ITI1_rew.stopped')
                        ITI1_rew.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Reward_respComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Reward_resp" ---
            for thisComponent in Reward_respComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if response_rew.keys in ['', [], None]:  # No response was made
                response_rew.keys = None
            Reward.addData('response_rew.keys',response_rew.keys)
            if response_rew.keys != None:  # we had a response
                Reward.addData('response_rew.rt', response_rew.rt)
            # Run 'End Routine' code from setoutcomerew
            #money = '+$1';
            color = [-1.0,1.0,-1.0];
            rewdisplay = block_rewdisplay
            #if blockcode == 1: #money
            #    rewimage = "images/money.jpg"
            #    rewimagesize = outtypeimg_size
            #    punimage = "images/moneyloss.jpg"
            #    punimagesize = outtypeimg_size
            #    rewdisplay = "+$%.2f" % (rew_amount)
            #    pundisplay = "-$%04.2f" % (pun_amount)
                #cardxy = (0,0)
            #elif blockcode == 2: #cigarette
            #    rewimage = "images/cig.jpg"
            #    rewimagesize = outtypeimg_size
            #    punimage = "images/cigloss.jpg"
            #    punimagesize = outtypeimg_size
            #    rewdisplay = "+2 puffs"
            #    pundisplay = "-1 puff"
            #    cardxy = (-0.25,0)
            #elif blockcode == 3: #images
            #    rewimage = "images/black.jpg"
            #    punimage = "images/black.jpg"
            #    rewimagesize = 0
            #    punimagesize = 0
            #    rewdisplay = ""
            #    pundisplay = ""
            #    cardxy = (-0.5,0)
            disp_checkx_size = checkx_size
            disp_msg_size = msg_size
            #print(response_rew.keys)
            if response_rew.keys:
                if (response_rew.keys[0] == '1') or (response_rew.keys[0] == 'b'):
                    #print(response_rew.keys)
                    outcome = np.random.randint(1,4);
                    totalwon = totalwon + rew_amount
                    largeimagesize = (0,0)
                #    if blockcode == 3:
                #        largeimagesize = (.8,.8)
                #    else:
                #        largeimagesize = (0,0)
                elif (response_rew.keys[0] == '2') or (response_rew.keys[0] == 'y'):
                    #print(response_rew.keys)
                    outcome = np.random.randint(6,9);
                    totalwon = totalwon + rew_amount
                    largeimagesize = (0,0)
                #    if blockcode == 3:
                #        largeimagesize = (.8,.8)
                #    else:
                #        largeimagesize = (0,0)
                else: #covers case of invalid key pressed
                    outcome = "#";
                    rewdisplay = 'no response';
                    disp_msg_size = noresp_msg_size
                    color = [1.0,1.0,1.0];
                    largeimagesize = (0,0)
                    disp_checkx_size = (0,0)
            else: #covers empty response variable case
                #print(response_rew.keys)
                outcome = "#";
                rewdisplay = 'no response';
                disp_msg_size = noresp_msg_size
                color = [1.0,1.0,1.0];
                largeimagesize = (0,0)
                disp_checkx_size = (0,0)
            
            
            #debug
            print("running total %.2f" % totalwon)
            # the Routine "Reward_resp" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "RewardOutcome" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            rect_out_rew.setPos(cardxy)
            rect_out_rew.setSize(cardsize)
            feedback_rew.setPos(cardxy)
            feedback_rew.setHeight(numbersize)
            display_rew.setColor(color, colorSpace='rgb')
            display_rew.setPos(msg_xy)
            display_rew.setText(rewdisplay)
            display_rew.setHeight(disp_msg_size)
            ITI2_rew.setText('+')
            image_rew.setPos(outtypeimg_xy)
            image_rew.setSize(rewimagesize)
            image_rew.setImage(rewimage)
            image_greencheck.setPos(checkx_xy)
            image_greencheck.setSize(disp_checkx_size)
            image_greencheck.setImage('images/symbolsuccess_small.png')
            # keep track of which components have finished
            RewardOutcomeComponents = [rect_out_rew, feedback_rew, display_rew, ITI2_rew, image_rew, image_greencheck]
            for thisComponent in RewardOutcomeComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "RewardOutcome" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *rect_out_rew* updates
                if rect_out_rew.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    rect_out_rew.frameNStart = frameN  # exact frame index
                    rect_out_rew.tStart = t  # local t and not account for scr refresh
                    rect_out_rew.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rect_out_rew, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'rect_out_rew.started')
                    rect_out_rew.setAutoDraw(True)
                if rect_out_rew.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > rect_out_rew.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        rect_out_rew.tStop = t  # not accounting for scr refresh
                        rect_out_rew.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'rect_out_rew.stopped')
                        rect_out_rew.setAutoDraw(False)
                
                # *feedback_rew* updates
                if feedback_rew.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    feedback_rew.frameNStart = frameN  # exact frame index
                    feedback_rew.tStart = t  # local t and not account for scr refresh
                    feedback_rew.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(feedback_rew, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_rew.started')
                    feedback_rew.setAutoDraw(True)
                if feedback_rew.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > feedback_rew.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        feedback_rew.tStop = t  # not accounting for scr refresh
                        feedback_rew.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'feedback_rew.stopped')
                        feedback_rew.setAutoDraw(False)
                if feedback_rew.status == STARTED:  # only update if drawing
                    feedback_rew.setText(outcome, log=False)
                
                # *display_rew* updates
                if display_rew.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    display_rew.frameNStart = frameN  # exact frame index
                    display_rew.tStart = t  # local t and not account for scr refresh
                    display_rew.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(display_rew, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'display_rew.started')
                    display_rew.setAutoDraw(True)
                if display_rew.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > display_rew.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        display_rew.tStop = t  # not accounting for scr refresh
                        display_rew.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'display_rew.stopped')
                        display_rew.setAutoDraw(False)
                
                # *ITI2_rew* updates
                if ITI2_rew.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    ITI2_rew.frameNStart = frameN  # exact frame index
                    ITI2_rew.tStart = t  # local t and not account for scr refresh
                    ITI2_rew.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ITI2_rew, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ITI2_rew.started')
                    ITI2_rew.setAutoDraw(True)
                if ITI2_rew.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ITI2_rew.tStartRefresh + iti2-frameTolerance:
                        # keep track of stop time/frame for later
                        ITI2_rew.tStop = t  # not accounting for scr refresh
                        ITI2_rew.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ITI2_rew.stopped')
                        ITI2_rew.setAutoDraw(False)
                
                # *image_rew* updates
                if image_rew.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_rew.frameNStart = frameN  # exact frame index
                    image_rew.tStart = t  # local t and not account for scr refresh
                    image_rew.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_rew, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_rew.started')
                    image_rew.setAutoDraw(True)
                if image_rew.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_rew.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        image_rew.tStop = t  # not accounting for scr refresh
                        image_rew.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_rew.stopped')
                        image_rew.setAutoDraw(False)
                
                # *image_greencheck* updates
                if image_greencheck.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_greencheck.frameNStart = frameN  # exact frame index
                    image_greencheck.tStart = t  # local t and not account for scr refresh
                    image_greencheck.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_greencheck, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_greencheck.started')
                    image_greencheck.setAutoDraw(True)
                if image_greencheck.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_greencheck.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        image_greencheck.tStop = t  # not accounting for scr refresh
                        image_greencheck.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_greencheck.stopped')
                        image_greencheck.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in RewardOutcomeComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "RewardOutcome" ---
            for thisComponent in RewardOutcomeComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "RewardOutcome" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed nRew repeats of 'Reward'
        
        
        # set up handler to look after randomisation of conditions etc
        Punish = data.TrialHandler(nReps=nPun, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='Punish')
        thisExp.addLoop(Punish)  # add the loop to the experiment
        thisPunish = Punish.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPunish.rgb)
        if thisPunish != None:
            for paramName in thisPunish:
                exec('{} = thisPunish[paramName]'.format(paramName))
        
        for thisPunish in Punish:
            currentLoop = Punish
            # abbreviate parameter names if possible (e.g. rgb = thisPunish.rgb)
            if thisPunish != None:
                for paramName in thisPunish:
                    exec('{} = thisPunish[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "Punishment_resp" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            rect_resp_pun.setPos(cardxy)
            rect_resp_pun.setSize(cardsize)
            quest_pun.setPos(cardxy)
            quest_pun.setHeight(numbersize)
            response_pun.keys = []
            response_pun.rt = []
            _response_pun_allKeys = []
            ISI2.setText('+')
            # keep track of which components have finished
            Punishment_respComponents = [rect_resp_pun, quest_pun, response_pun, ISI2]
            for thisComponent in Punishment_respComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Punishment_resp" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *rect_resp_pun* updates
                if rect_resp_pun.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rect_resp_pun.frameNStart = frameN  # exact frame index
                    rect_resp_pun.tStart = t  # local t and not account for scr refresh
                    rect_resp_pun.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rect_resp_pun, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'rect_resp_pun.started')
                    rect_resp_pun.setAutoDraw(True)
                if rect_resp_pun.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > rect_resp_pun.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        rect_resp_pun.tStop = t  # not accounting for scr refresh
                        rect_resp_pun.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'rect_resp_pun.stopped')
                        rect_resp_pun.setAutoDraw(False)
                
                # *quest_pun* updates
                if quest_pun.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    quest_pun.frameNStart = frameN  # exact frame index
                    quest_pun.tStart = t  # local t and not account for scr refresh
                    quest_pun.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(quest_pun, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'quest_pun.started')
                    quest_pun.setAutoDraw(True)
                if quest_pun.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > quest_pun.tStartRefresh + 2.0-frameTolerance:
                        # keep track of stop time/frame for later
                        quest_pun.tStop = t  # not accounting for scr refresh
                        quest_pun.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'quest_pun.stopped')
                        quest_pun.setAutoDraw(False)
                
                # *response_pun* updates
                waitOnFlip = False
                if response_pun.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    response_pun.frameNStart = frameN  # exact frame index
                    response_pun.tStart = t  # local t and not account for scr refresh
                    response_pun.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(response_pun, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'response_pun.started')
                    response_pun.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(response_pun.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(response_pun.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if response_pun.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > response_pun.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        response_pun.tStop = t  # not accounting for scr refresh
                        response_pun.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'response_pun.stopped')
                        response_pun.status = FINISHED
                if response_pun.status == STARTED and not waitOnFlip:
                    theseKeys = response_pun.getKeys(keyList=['1','2','b','y'], waitRelease=False)
                    _response_pun_allKeys.extend(theseKeys)
                    if len(_response_pun_allKeys):
                        response_pun.keys = [key.name for key in _response_pun_allKeys]  # storing all keys
                        response_pun.rt = [key.rt for key in _response_pun_allKeys]
                
                # *ISI2* updates
                if ISI2.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                    # keep track of start time/frame for later
                    ISI2.frameNStart = frameN  # exact frame index
                    ISI2.tStart = t  # local t and not account for scr refresh
                    ISI2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ISI2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ISI2.started')
                    ISI2.setAutoDraw(True)
                if ISI2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ISI2.tStartRefresh + iti1-frameTolerance:
                        # keep track of stop time/frame for later
                        ISI2.tStop = t  # not accounting for scr refresh
                        ISI2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ISI2.stopped')
                        ISI2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Punishment_respComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Punishment_resp" ---
            for thisComponent in Punishment_respComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if response_pun.keys in ['', [], None]:  # No response was made
                response_pun.keys = None
            Punish.addData('response_pun.keys',response_pun.keys)
            if response_pun.keys != None:  # we had a response
                Punish.addData('response_pun.rt', response_pun.rt)
            # Run 'End Routine' code from setoutcomepun
            #money = '-$0.50';
            color = [1.0,-1.0,-1.0]
            pundisplay = block_pundisplay
            #if blockcode == 1: #money
            #    rewimage = "images/money.jpg"
            #    rewimagesize = outtypeimg_size
            #    punimage = "images/moneyloss.jpg"
            #    punimagesize = outtypeimg_size
            #    rewdisplay = "+$%.2f" % (rew_amount)
            #    pundisplay = "-$%04.2f" % (pun_amount)
                #cardxy = (-0.25,0)
            #elif blockcode == 2: #cigarette
            #    rewimage = "images/cig.jpg"
            #    rewimagesize = outtypeimg_size
            #    punimage = "images/cigloss.jpg"
            #    punimagesize = outtypeimg_size
            #    rewdisplay = "+2 puffs"
            #    pundisplay = "-1 puff"
            #    cardxy = (-0.25,0)
            #elif blockcode == 3: #images
            #    rewimage = "images/black.jpg"
            #    punimage = "images/black.jpg"
            #    rewimagesize = 0
            #    punimagesize = 0
            #    rewdisplay = ""
            #    pundisplay = ""
            #    cardxy = (-0.5,0)
            
            disp_checkx_size = checkx_size
            disp_msg_size = msg_size
            print(response_rew.keys)
            if response_pun.keys:
                if (response_pun.keys[0] == '1') or (response_pun.keys[0] == 'b'):
                    #print(response_rew.keys)
                    outcome = np.random.randint(6,9)
                    totalwon = totalwon - pun_amount
                    largeimagesize = (0,0)
                #    if blockcode == 3:
                #        largeimagesize = (.8,.8)
                #    else:
                #        largeimagesize = (0,0)
                elif (response_pun.keys[0] == '2') or (response_pun.keys[0] == 'y'):
                    #print(response_rew.keys)
                    outcome = np.random.randint(1,4)
                    totalwon = totalwon - pun_amount
                    largeimagesize = (0,0)
                #    if blockcode == 3:
                #        largeimagesize = (.8,.8)
                #    else:
                #        largeimagesize = (0,0)
                else: #covers case of invalid key pressed first
                    outcome = "#"
                    pundisplay = 'no response'
                    disp_msg_size = noresp_msg_size
                    color = [1.0,1.0,1.0]
                    largeimagesize = (0,0)
                    disp_checkx_size = (0,0)
            else: #covers case of empty response variable
                outcome = "#"
                pundisplay = 'no response'
                disp_msg_size = noresp_msg_size
                color = [1.0,1.0,1.0]
                largeimagesize = (0,0)
                disp_checkx_size = (0,0)
            
            #debug
            print("running total %.2f" % totalwon)
            # the Routine "Punishment_resp" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "PunishmentOutcome" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            rect_out_pun.setPos(cardxy)
            rect_out_pun.setSize(cardsize)
            feedback_pun.setPos(cardxy)
            feedback_pun.setText(outcome)
            feedback_pun.setHeight(numbersize)
            display_pun.setColor(color, colorSpace='rgb')
            display_pun.setPos(msg_xy)
            display_pun.setText(pundisplay)
            display_pun.setHeight(disp_msg_size)
            ITI2_pun.setText('+')
            image_pun.setPos(outtypeimg_xy)
            image_pun.setSize(punimagesize)
            image_pun.setImage(punimage)
            image_redx.setPos(checkx_xy)
            image_redx.setSize(disp_checkx_size)
            image_redx.setImage('images/symbolNOsuccess_small.png')
            # keep track of which components have finished
            PunishmentOutcomeComponents = [rect_out_pun, feedback_pun, display_pun, ITI2_pun, image_pun, image_redx]
            for thisComponent in PunishmentOutcomeComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "PunishmentOutcome" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *rect_out_pun* updates
                if rect_out_pun.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    rect_out_pun.frameNStart = frameN  # exact frame index
                    rect_out_pun.tStart = t  # local t and not account for scr refresh
                    rect_out_pun.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rect_out_pun, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'rect_out_pun.started')
                    rect_out_pun.setAutoDraw(True)
                if rect_out_pun.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > rect_out_pun.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        rect_out_pun.tStop = t  # not accounting for scr refresh
                        rect_out_pun.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'rect_out_pun.stopped')
                        rect_out_pun.setAutoDraw(False)
                
                # *feedback_pun* updates
                if feedback_pun.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    feedback_pun.frameNStart = frameN  # exact frame index
                    feedback_pun.tStart = t  # local t and not account for scr refresh
                    feedback_pun.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(feedback_pun, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_pun.started')
                    feedback_pun.setAutoDraw(True)
                if feedback_pun.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > feedback_pun.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        feedback_pun.tStop = t  # not accounting for scr refresh
                        feedback_pun.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'feedback_pun.stopped')
                        feedback_pun.setAutoDraw(False)
                
                # *display_pun* updates
                if display_pun.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    display_pun.frameNStart = frameN  # exact frame index
                    display_pun.tStart = t  # local t and not account for scr refresh
                    display_pun.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(display_pun, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'display_pun.started')
                    display_pun.setAutoDraw(True)
                if display_pun.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > display_pun.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        display_pun.tStop = t  # not accounting for scr refresh
                        display_pun.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'display_pun.stopped')
                        display_pun.setAutoDraw(False)
                
                # *ITI2_pun* updates
                if ITI2_pun.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    ITI2_pun.frameNStart = frameN  # exact frame index
                    ITI2_pun.tStart = t  # local t and not account for scr refresh
                    ITI2_pun.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ITI2_pun, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ITI2_pun.started')
                    ITI2_pun.setAutoDraw(True)
                if ITI2_pun.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ITI2_pun.tStartRefresh + iti2-frameTolerance:
                        # keep track of stop time/frame for later
                        ITI2_pun.tStop = t  # not accounting for scr refresh
                        ITI2_pun.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ITI2_pun.stopped')
                        ITI2_pun.setAutoDraw(False)
                
                # *image_pun* updates
                if image_pun.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_pun.frameNStart = frameN  # exact frame index
                    image_pun.tStart = t  # local t and not account for scr refresh
                    image_pun.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_pun, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_pun.started')
                    image_pun.setAutoDraw(True)
                if image_pun.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_pun.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        image_pun.tStop = t  # not accounting for scr refresh
                        image_pun.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_pun.stopped')
                        image_pun.setAutoDraw(False)
                
                # *image_redx* updates
                if image_redx.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_redx.frameNStart = frameN  # exact frame index
                    image_redx.tStart = t  # local t and not account for scr refresh
                    image_redx.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_redx, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_redx.started')
                    image_redx.setAutoDraw(True)
                if image_redx.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_redx.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        image_redx.tStop = t  # not accounting for scr refresh
                        image_redx.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_redx.stopped')
                        image_redx.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in PunishmentOutcomeComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "PunishmentOutcome" ---
            for thisComponent in PunishmentOutcomeComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "PunishmentOutcome" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed nPun repeats of 'Punish'
        
        thisExp.nextEntry()
        
    # completed 1 repeats of 'innertrials'
    
# completed 1.0 repeats of 'blocks'


# --- Prepare to start Routine "EndText" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from format_total
totalwon_formatted = "$%.2f" % (totalwon)
Total_display.setText(totalwon_formatted)
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
EndTextComponents = [Finished, Total_display, key_resp_2]
for thisComponent in EndTextComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "EndText" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Finished* updates
    if Finished.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Finished.frameNStart = frameN  # exact frame index
        Finished.tStart = t  # local t and not account for scr refresh
        Finished.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Finished, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Finished.started')
        Finished.setAutoDraw(True)
    
    # *Total_display* updates
    if Total_display.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Total_display.frameNStart = frameN  # exact frame index
        Total_display.tStart = t  # local t and not account for scr refresh
        Total_display.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Total_display, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Total_display.started')
        Total_display.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_2.started')
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space','1','2','3','4','x','q'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndTextComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EndText" ---
for thisComponent in EndTextComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "EndText" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
