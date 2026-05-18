#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2026.1.3),
    on May 16, 2026, at 17:24
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2026.1.3'
expName = 'FF'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': '1',
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1536, 864]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\james\\Documents\\ZDesktop\\PhD\\Misc\\Coding_Projects_for_LinkedIn\\Forward Flow\\ForwardFlow_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    # store pilot mode in data file
    thisExp.addData('piloting', PILOTING, priority=priority.LOW)
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('exp')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # update experiment info
    expInfo['date'] = data.getDateStr()
    expInfo['expName'] = expName
    expInfo['expVersion'] = expVersion
    expInfo['psychopyVersion'] = psychopyVersion
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "FFinstrux" ---
    intrux = visual.TextStim(win=win, name='intrux',
        text='In the next task you will be shown a single word, and you must type the next word that follows from it in your mind. \n\nOnce you type the word, it will be shown on the screen. You must then think of another word that follows from this word, and so on.\n\nKeep typing the next word that comes to mind after the previous word until the trial ends (after 20 words).\n\nPlease type only single words, and avoid saying proper nouns such as names, cities, or brands (e.g., “John”, “Paris”, “Nike”).',
        font='Arial',
        pos=(0, 0.1), draggable=False, height=0.035, wrapWidth=1.2, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    EntertoContinue = visual.TextStim(win=win, name='EntertoContinue',
        text='Press ENTER to continue',
        font='Arial',
        pos=(0, -.35), draggable=False, height=0.03, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_2 = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "FFinstrux_2" ---
    intrux_2 = visual.TextStim(win=win, name='intrux_2',
        text="First, you will complete a small practise.\n\nYou'll be shown a single word, and have to think of the first word that comes to mind, and type it. Then you type the next word that follows from that word, until you make a small chain of associations.",
        font='Arial',
        pos=(0, 0.1), draggable=False, height=0.035, wrapWidth=1.2, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    EntertoContinue_2 = visual.TextStim(win=win, name='EntertoContinue_2',
        text='Press ENTER to begin.',
        font='Arial',
        pos=(0, -.35), draggable=False, height=0.03, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_3 = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "FFblank" ---
    text_5 = visual.TextStim(win=win, name='text_5',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.15, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "FF" ---
    # Run 'Begin Experiment' code from FFcode_3
    
    import math
    import pandas as pd
    
    CAPS=False
    firsttrial=True
    FFcueDisp = visual.TextStim(win=win, name='FFcueDisp',
        text='',
        font='Arial',
        pos=(0, 0.1), draggable=False, height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    polygon = visual.Rect(
        win=win, name='polygon',
        width=(0.45, 0.17)[0], height=(0.45, 0.17)[1],
        ori=0, pos=(0, -0.2), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=-2.0, interpolate=True)
    key_respFF = keyboard.Keyboard(deviceName='defaultKeyboard')
    FFrespDisp = visual.TextStim(win=win, name='FFrespDisp',
        text='',
        font='Arial',
        pos=(0, -0.2), draggable=False, height=0.075, wrapWidth=0.4, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "FFinstrux_4" ---
    intrux_4 = visual.TextStim(win=win, name='intrux_4',
        text='That is the end of the practise. Next are the real trials, which will be 19 words long. There will be 3 trials in total.\n\nRemember: you will be shown a single word, and you must type the next word that follows in your mind. Keep typing the next word that comes to mind after the previous word until the trial ends.\n\nPlease type only single words, and avoid saying proper nouns such as names, cities, or brands (e.g., “John”, “Paris”, “Nike”).',
        font='Arial',
        pos=(0, 0.1), draggable=False, height=0.035, wrapWidth=1.2, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    EntertoContinue_4 = visual.TextStim(win=win, name='EntertoContinue_4',
        text='Press SPACE to begin',
        font='Arial',
        pos=(0, -.35), draggable=False, height=0.03, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_5 = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "FFblank" ---
    text_5 = visual.TextStim(win=win, name='text_5',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.15, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "FF" ---
    # Run 'Begin Experiment' code from FFcode_3
    
    import math
    import pandas as pd
    
    CAPS=False
    firsttrial=True
    FFcueDisp = visual.TextStim(win=win, name='FFcueDisp',
        text='',
        font='Arial',
        pos=(0, 0.1), draggable=False, height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    polygon = visual.Rect(
        win=win, name='polygon',
        width=(0.45, 0.17)[0], height=(0.45, 0.17)[1],
        ori=0, pos=(0, -0.2), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=-2.0, interpolate=True)
    key_respFF = keyboard.Keyboard(deviceName='defaultKeyboard')
    FFrespDisp = visual.TextStim(win=win, name='FFrespDisp',
        text='',
        font='Arial',
        pos=(0, -0.2), draggable=False, height=0.075, wrapWidth=0.4, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "NextFFInstrux" ---
    intrux_5 = visual.TextStim(win=win, name='intrux_5',
        text='\nPress SPACE to see another starting word',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.035, wrapWidth=0.7, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    EntertoContinue_5 = visual.TextStim(win=win, name='EntertoContinue_5',
        text='Press SPACE to begin',
        font='Arial',
        pos=(0, -.35), draggable=False, height=0.03, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_9 = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    if eyetracker is not None:
        eyetracker.enableEventReporting()
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "FFinstrux" ---
    # create an object to store info about Routine FFinstrux
    FFinstrux = data.Routine(
        name='FFinstrux',
        components=[intrux, EntertoContinue, key_resp_2],
    )
    FFinstrux.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_2
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # Run 'Begin Routine' code from code
    
    
    EscapeAllowed = True
    win.mouseVisible = False
    
    # defines practise trials true
    FFPrac=True
    
    
    
    # store start times for FFinstrux
    FFinstrux.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    FFinstrux.tStart = globalClock.getTime(format='float')
    FFinstrux.status = STARTED
    thisExp.addData('FFinstrux.started', FFinstrux.tStart)
    FFinstrux.maxDuration = None
    # keep track of which components have finished
    FFinstruxComponents = FFinstrux.components
    for thisComponent in FFinstrux.components:
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
    
    # --- Run Routine "FFinstrux" ---
    thisExp.currentRoutine = FFinstrux
    FFinstrux.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *intrux* updates
        
        # if intrux is starting this frame...
        if intrux.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            intrux.frameNStart = frameN  # exact frame index
            intrux.tStart = t  # local t and not account for scr refresh
            intrux.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(intrux, 'tStartRefresh')  # time at next scr refresh
            # update status
            intrux.status = STARTED
            intrux.setAutoDraw(True)
        
        # if intrux is active this frame...
        if intrux.status == STARTED:
            # update params
            pass
        
        # *EntertoContinue* updates
        
        # if EntertoContinue is starting this frame...
        if EntertoContinue.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            EntertoContinue.frameNStart = frameN  # exact frame index
            EntertoContinue.tStart = t  # local t and not account for scr refresh
            EntertoContinue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EntertoContinue, 'tStartRefresh')  # time at next scr refresh
            # update status
            EntertoContinue.status = STARTED
            EntertoContinue.setAutoDraw(True)
        
        # if EntertoContinue is active this frame...
        if EntertoContinue.status == STARTED:
            # update params
            pass
        
        # *key_resp_2* updates
        waitOnFlip = False
        
        # if key_resp_2 is starting this frame...
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=FFinstrux,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            FFinstrux.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if FFinstrux.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in FFinstrux.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "FFinstrux" ---
    for thisComponent in FFinstrux.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for FFinstrux
    FFinstrux.tStop = globalClock.getTime(format='float')
    FFinstrux.tStopRefresh = tThisFlipGlobal
    thisExp.addData('FFinstrux.stopped', FFinstrux.tStop)
    thisExp.nextEntry()
    # the Routine "FFinstrux" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "FFinstrux_2" ---
    # create an object to store info about Routine FFinstrux_2
    FFinstrux_2 = data.Routine(
        name='FFinstrux_2',
        components=[intrux_2, EntertoContinue_2, key_resp_3],
    )
    FFinstrux_2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_3
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # store start times for FFinstrux_2
    FFinstrux_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    FFinstrux_2.tStart = globalClock.getTime(format='float')
    FFinstrux_2.status = STARTED
    thisExp.addData('FFinstrux_2.started', FFinstrux_2.tStart)
    FFinstrux_2.maxDuration = None
    # keep track of which components have finished
    FFinstrux_2Components = FFinstrux_2.components
    for thisComponent in FFinstrux_2.components:
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
    
    # --- Run Routine "FFinstrux_2" ---
    thisExp.currentRoutine = FFinstrux_2
    FFinstrux_2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *intrux_2* updates
        
        # if intrux_2 is starting this frame...
        if intrux_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            intrux_2.frameNStart = frameN  # exact frame index
            intrux_2.tStart = t  # local t and not account for scr refresh
            intrux_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(intrux_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            intrux_2.status = STARTED
            intrux_2.setAutoDraw(True)
        
        # if intrux_2 is active this frame...
        if intrux_2.status == STARTED:
            # update params
            pass
        
        # *EntertoContinue_2* updates
        
        # if EntertoContinue_2 is starting this frame...
        if EntertoContinue_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            EntertoContinue_2.frameNStart = frameN  # exact frame index
            EntertoContinue_2.tStart = t  # local t and not account for scr refresh
            EntertoContinue_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EntertoContinue_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            EntertoContinue_2.status = STARTED
            EntertoContinue_2.setAutoDraw(True)
        
        # if EntertoContinue_2 is active this frame...
        if EntertoContinue_2.status == STARTED:
            # update params
            pass
        
        # *key_resp_3* updates
        waitOnFlip = False
        
        # if key_resp_3 is starting this frame...
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                key_resp_3.duration = _key_resp_3_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=FFinstrux_2,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            FFinstrux_2.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if FFinstrux_2.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in FFinstrux_2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "FFinstrux_2" ---
    for thisComponent in FFinstrux_2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for FFinstrux_2
    FFinstrux_2.tStop = globalClock.getTime(format='float')
    FFinstrux_2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('FFinstrux_2.stopped', FFinstrux_2.tStop)
    thisExp.nextEntry()
    # the Routine "FFinstrux_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "FFblank" ---
    # create an object to store info about Routine FFblank
    FFblank = data.Routine(
        name='FFblank',
        components=[text_5],
    )
    FFblank.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_4
    firsttrial=True
    # store start times for FFblank
    FFblank.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    FFblank.tStart = globalClock.getTime(format='float')
    FFblank.status = STARTED
    thisExp.addData('FFblank.started', FFblank.tStart)
    FFblank.maxDuration = None
    # keep track of which components have finished
    FFblankComponents = FFblank.components
    for thisComponent in FFblank.components:
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
    
    # --- Run Routine "FFblank" ---
    thisExp.currentRoutine = FFblank
    FFblank.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        
        # if text_5 is starting this frame...
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_5.status = STARTED
            text_5.setAutoDraw(True)
        
        # if text_5 is active this frame...
        if text_5.status == STARTED:
            # update params
            pass
        
        # if text_5 is stopping this frame...
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.tStopRefresh = tThisFlipGlobal  # on global time
                text_5.frameNStop = frameN  # exact frame index
                # update status
                text_5.status = FINISHED
                text_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=FFblank,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            FFblank.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if FFblank.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in FFblank.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "FFblank" ---
    for thisComponent in FFblank.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for FFblank
    FFblank.tStop = globalClock.getTime(format='float')
    FFblank.tStopRefresh = tThisFlipGlobal
    thisExp.addData('FFblank.stopped', FFblank.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if FFblank.maxDurationReached:
        routineTimer.addTime(-FFblank.maxDuration)
    elif FFblank.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    FFpractise = data.TrialHandler2(
        name='FFpractise',
        nReps=6.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(FFpractise)  # add the loop to the experiment
    thisFFpractise = FFpractise.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFFpractise.rgb)
    if thisFFpractise != None:
        for paramName in thisFFpractise:
            globals()[paramName] = thisFFpractise[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisFFpractise in FFpractise:
        FFpractise.status = STARTED
        if hasattr(thisFFpractise, 'status'):
            thisFFpractise.status = STARTED
        currentLoop = FFpractise
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisFFpractise.rgb)
        if thisFFpractise != None:
            for paramName in thisFFpractise:
                globals()[paramName] = thisFFpractise[paramName]
        
        # --- Prepare to start Routine "FF" ---
        # create an object to store info about Routine FF
        FF = data.Routine(
            name='FF',
            components=[FFcueDisp, polygon, key_respFF, FFrespDisp],
        )
        FF.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from FFcode_3
        ##initiate variables
        #is shift pressed?
        shift_flag = False
        #set response text as empty
        Resptext = ''
        
        charlim=30
        
        #set 1st and last key press times
        RT1stKP=0
        RTLastKP=0
           
        event.clearEvents('keyboard')
        
        if FFPrac==True:
            FFcueword="snow"
        else:
            FFcueword=FFcue
        
        if firsttrial==False:
            FFcueword=PrevResp
            
        firsttrial=False
        FFcueDisp.setText(FFcueword)
        # create starting attributes for key_respFF
        key_respFF.keys = []
        key_respFF.rt = []
        _key_respFF_allKeys = []
        # store start times for FF
        FF.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        FF.tStart = globalClock.getTime(format='float')
        FF.status = STARTED
        thisExp.addData('FF.started', FF.tStart)
        FF.maxDuration = None
        # keep track of which components have finished
        FFComponents = FF.components
        for thisComponent in FF.components:
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
        
        # --- Run Routine "FF" ---
        thisExp.currentRoutine = FF
        FF.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisFFpractise, 'status') and thisFFpractise.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from FFcode_3
            
            keys = event.getKeys()
            n=len(keys)
            i=0
            
            
            ###### Text entry #####
            while i < n: # len(keys):
                #process each key depending on what it is
                if keys[i] == 'return' and len(Resptext)>=1:
                    continueRoutine = False
                    break
                elif keys[i] == 'escape' and EscapeAllowed == True:
                    continueRoutine = False
                    core.quit()
                    break
                elif keys[i] == 'space' :
                    Resptext += " "
                    i += 1
                elif keys[i] == 'backspace' :
                    Resptext = Resptext[:-1]
                    i += 1
                elif keys[i] == 'capslock' :
                    if CAPS==True:
                        CAPS= False
                    elif CAPS==False:
                        CAPS=True
                    i += 1
                elif keys[i] == 'period'and len(Resptext) < charlim:
                    Resptext += "."
                    i += 1
                elif keys[i] == 'minus' and len(Resptext) < charlim:
                    Resptext += "-"
                    i += 1
                elif keys[i] == 'comma' and len(Resptext) < charlim: 
                    Resptext += ","
                    i = i + 1
                elif keys[i] in ['lshift', 'rshift']:
                    shift_flag = True
                    i = i + 1
                elif keys[i] == 'semicolon' and len(Resptext) < charlim:
                    if shift_flag == False:
                        Resptext += ";"
                    else:
                        Resptext += ":"
                        shift_flag = False
                    i += 1
                elif keys[i] == 'apostrophe' and len(Resptext) < charlim:
                    if shift_flag == False:
                        Resptext += "'"
                    else:
                        Resptext += '"'
                    i += 1
                elif keys[i] == 'slash' and len(Resptext) < charlim:
                    if shift_flag == False:
                        Resptext += "/"
                    else:
                        Resptext += '?'
                        shift_flag = False
                    i = i + 1
                elif keys[i] == '1' and len(Resptext) < charlim and shift_flag == True:
                    Resptext += "!"
                    shift_flag = False
                    i = i + 1
                else:
                    if len(Resptext) < charlim and len(keys[i])==1:
                        Key=keys[i]
                        if CAPS or shift_flag:
                            Resptext += Key.upper()
                            shift_flag=False
                        else:
                            Resptext += Key
                    i += 1
            
            
             
            
            # *FFcueDisp* updates
            
            # if FFcueDisp is starting this frame...
            if FFcueDisp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                FFcueDisp.frameNStart = frameN  # exact frame index
                FFcueDisp.tStart = t  # local t and not account for scr refresh
                FFcueDisp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FFcueDisp, 'tStartRefresh')  # time at next scr refresh
                # update status
                FFcueDisp.status = STARTED
                FFcueDisp.setAutoDraw(True)
            
            # if FFcueDisp is active this frame...
            if FFcueDisp.status == STARTED:
                # update params
                pass
            
            # *polygon* updates
            
            # if polygon is starting this frame...
            if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  # exact frame index
                polygon.tStart = t  # local t and not account for scr refresh
                polygon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon.started')
                # update status
                polygon.status = STARTED
                polygon.setAutoDraw(True)
            
            # if polygon is active this frame...
            if polygon.status == STARTED:
                # update params
                pass
            
            # *key_respFF* updates
            
            # if key_respFF is starting this frame...
            if key_respFF.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_respFF.frameNStart = frameN  # exact frame index
                key_respFF.tStart = t  # local t and not account for scr refresh
                key_respFF.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_respFF, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_respFF.status = STARTED
                # keyboard checking is just starting
                key_respFF.clock.reset()  # now t=0
                key_respFF.clearEvents(eventType='keyboard')
            if key_respFF.status == STARTED:
                theseKeys = key_respFF.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
                _key_respFF_allKeys.extend(theseKeys)
                if len(_key_respFF_allKeys):
                    key_respFF.keys = [key.name for key in _key_respFF_allKeys]  # storing all keys
                    key_respFF.rt = [key.rt for key in _key_respFF_allKeys]
                    key_respFF.duration = [key.duration for key in _key_respFF_allKeys]
            
            # *FFrespDisp* updates
            
            # if FFrespDisp is starting this frame...
            if FFrespDisp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FFrespDisp.frameNStart = frameN  # exact frame index
                FFrespDisp.tStart = t  # local t and not account for scr refresh
                FFrespDisp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FFrespDisp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'FFrespDisp.started')
                # update status
                FFrespDisp.status = STARTED
                FFrespDisp.setAutoDraw(True)
            
            # if FFrespDisp is active this frame...
            if FFrespDisp.status == STARTED:
                # update params
                FFrespDisp.setText((Resptext), log=False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=FF,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                FF.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if FF.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in FF.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "FF" ---
        for thisComponent in FF.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for FF
        FF.tStop = globalClock.getTime(format='float')
        FF.tStopRefresh = tThisFlipGlobal
        thisExp.addData('FF.stopped', FF.tStop)
        # Run 'End Routine' code from FFcode_3
        #extract the 1st and last key presses
        if len(key_respFF.rt)>0:
            RT1stKP=key_respFF.rt[0]
            RTLastKP=key_respFF.rt[-1]
        
        #save the data for this trial
        thisExp.addData("FFresp", Resptext)
        thisExp.addData("FFRT1stKP", RT1stKP)
        thisExp.addData("FFRTLastKP", RTLastKP)
        PrevResp=Resptext
        Resptext = ''
        # check responses
        if key_respFF.keys in ['', [], None]:  # No response was made
            key_respFF.keys = None
        FFpractise.addData('key_respFF.keys',key_respFF.keys)
        if key_respFF.keys != None:  # we had a response
            FFpractise.addData('key_respFF.rt', key_respFF.rt)
            FFpractise.addData('key_respFF.duration', key_respFF.duration)
        # the Routine "FF" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisFFpractise as finished
        if hasattr(thisFFpractise, 'status'):
            thisFFpractise.status = FINISHED
        # if awaiting a pause, pause now
        if FFpractise.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            FFpractise.status = STARTED
        thisExp.nextEntry()
        
    # completed 6.0 repeats of 'FFpractise'
    FFpractise.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "FFinstrux_4" ---
    # create an object to store info about Routine FFinstrux_4
    FFinstrux_4 = data.Routine(
        name='FFinstrux_4',
        components=[intrux_4, EntertoContinue_4, key_resp_5],
    )
    FFinstrux_4.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_5
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    # Run 'Begin Routine' code from code_3
    FFPrac=False
    FFtrialnum=0
    # store start times for FFinstrux_4
    FFinstrux_4.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    FFinstrux_4.tStart = globalClock.getTime(format='float')
    FFinstrux_4.status = STARTED
    thisExp.addData('FFinstrux_4.started', FFinstrux_4.tStart)
    FFinstrux_4.maxDuration = None
    # keep track of which components have finished
    FFinstrux_4Components = FFinstrux_4.components
    for thisComponent in FFinstrux_4.components:
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
    
    # --- Run Routine "FFinstrux_4" ---
    thisExp.currentRoutine = FFinstrux_4
    FFinstrux_4.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *intrux_4* updates
        
        # if intrux_4 is starting this frame...
        if intrux_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            intrux_4.frameNStart = frameN  # exact frame index
            intrux_4.tStart = t  # local t and not account for scr refresh
            intrux_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(intrux_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            intrux_4.status = STARTED
            intrux_4.setAutoDraw(True)
        
        # if intrux_4 is active this frame...
        if intrux_4.status == STARTED:
            # update params
            pass
        
        # *EntertoContinue_4* updates
        
        # if EntertoContinue_4 is starting this frame...
        if EntertoContinue_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            EntertoContinue_4.frameNStart = frameN  # exact frame index
            EntertoContinue_4.tStart = t  # local t and not account for scr refresh
            EntertoContinue_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EntertoContinue_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            EntertoContinue_4.status = STARTED
            EntertoContinue_4.setAutoDraw(True)
        
        # if EntertoContinue_4 is active this frame...
        if EntertoContinue_4.status == STARTED:
            # update params
            pass
        
        # *key_resp_5* updates
        waitOnFlip = False
        
        # if key_resp_5 is starting this frame...
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                key_resp_5.duration = _key_resp_5_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=FFinstrux_4,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            FFinstrux_4.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if FFinstrux_4.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in FFinstrux_4.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "FFinstrux_4" ---
    for thisComponent in FFinstrux_4.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for FFinstrux_4
    FFinstrux_4.tStop = globalClock.getTime(format='float')
    FFinstrux_4.tStopRefresh = tThisFlipGlobal
    thisExp.addData('FFinstrux_4.stopped', FFinstrux_4.tStop)
    thisExp.nextEntry()
    # the Routine "FFinstrux_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    FFtrials = data.TrialHandler2(
        name='FFtrials',
        nReps=1, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('FFcues.xlsx'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(FFtrials)  # add the loop to the experiment
    thisFFtrial = FFtrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFFtrial.rgb)
    if thisFFtrial != None:
        for paramName in thisFFtrial:
            globals()[paramName] = thisFFtrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisFFtrial in FFtrials:
        FFtrials.status = STARTED
        if hasattr(thisFFtrial, 'status'):
            thisFFtrial.status = STARTED
        currentLoop = FFtrials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisFFtrial.rgb)
        if thisFFtrial != None:
            for paramName in thisFFtrial:
                globals()[paramName] = thisFFtrial[paramName]
        
        # --- Prepare to start Routine "FFblank" ---
        # create an object to store info about Routine FFblank
        FFblank = data.Routine(
            name='FFblank',
            components=[text_5],
        )
        FFblank.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_4
        firsttrial=True
        # store start times for FFblank
        FFblank.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        FFblank.tStart = globalClock.getTime(format='float')
        FFblank.status = STARTED
        thisExp.addData('FFblank.started', FFblank.tStart)
        FFblank.maxDuration = None
        # keep track of which components have finished
        FFblankComponents = FFblank.components
        for thisComponent in FFblank.components:
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
        
        # --- Run Routine "FFblank" ---
        thisExp.currentRoutine = FFblank
        FFblank.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisFFtrial, 'status') and thisFFtrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_5* updates
            
            # if text_5 is starting this frame...
            if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_5.status = STARTED
                text_5.setAutoDraw(True)
            
            # if text_5 is active this frame...
            if text_5.status == STARTED:
                # update params
                pass
            
            # if text_5 is stopping this frame...
            if text_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_5.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    text_5.tStop = t  # not accounting for scr refresh
                    text_5.tStopRefresh = tThisFlipGlobal  # on global time
                    text_5.frameNStop = frameN  # exact frame index
                    # update status
                    text_5.status = FINISHED
                    text_5.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=FFblank,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                FFblank.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if FFblank.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in FFblank.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "FFblank" ---
        for thisComponent in FFblank.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for FFblank
        FFblank.tStop = globalClock.getTime(format='float')
        FFblank.tStopRefresh = tThisFlipGlobal
        thisExp.addData('FFblank.stopped', FFblank.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if FFblank.maxDurationReached:
            routineTimer.addTime(-FFblank.maxDuration)
        elif FFblank.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # set up handler to look after randomisation of conditions etc
        FFresps = data.TrialHandler2(
            name='FFresps',
            nReps=19, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
            isTrials=True, 
        )
        thisExp.addLoop(FFresps)  # add the loop to the experiment
        thisFFresp = FFresps.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisFFresp.rgb)
        if thisFFresp != None:
            for paramName in thisFFresp:
                globals()[paramName] = thisFFresp[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisFFresp in FFresps:
            FFresps.status = STARTED
            if hasattr(thisFFresp, 'status'):
                thisFFresp.status = STARTED
            currentLoop = FFresps
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisFFresp.rgb)
            if thisFFresp != None:
                for paramName in thisFFresp:
                    globals()[paramName] = thisFFresp[paramName]
            
            # --- Prepare to start Routine "FF" ---
            # create an object to store info about Routine FF
            FF = data.Routine(
                name='FF',
                components=[FFcueDisp, polygon, key_respFF, FFrespDisp],
            )
            FF.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from FFcode_3
            ##initiate variables
            #is shift pressed?
            shift_flag = False
            #set response text as empty
            Resptext = ''
            
            charlim=30
            
            #set 1st and last key press times
            RT1stKP=0
            RTLastKP=0
               
            event.clearEvents('keyboard')
            
            if FFPrac==True:
                FFcueword="snow"
            else:
                FFcueword=FFcue
            
            if firsttrial==False:
                FFcueword=PrevResp
                
            firsttrial=False
            FFcueDisp.setText(FFcueword)
            # create starting attributes for key_respFF
            key_respFF.keys = []
            key_respFF.rt = []
            _key_respFF_allKeys = []
            # store start times for FF
            FF.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            FF.tStart = globalClock.getTime(format='float')
            FF.status = STARTED
            thisExp.addData('FF.started', FF.tStart)
            FF.maxDuration = None
            # keep track of which components have finished
            FFComponents = FF.components
            for thisComponent in FF.components:
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
            
            # --- Run Routine "FF" ---
            thisExp.currentRoutine = FF
            FF.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # if trial has changed, end Routine now
                if hasattr(thisFFresp, 'status') and thisFFresp.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from FFcode_3
                
                keys = event.getKeys()
                n=len(keys)
                i=0
                
                
                ###### Text entry #####
                while i < n: # len(keys):
                    #process each key depending on what it is
                    if keys[i] == 'return' and len(Resptext)>=1:
                        continueRoutine = False
                        break
                    elif keys[i] == 'escape' and EscapeAllowed == True:
                        continueRoutine = False
                        core.quit()
                        break
                    elif keys[i] == 'space' :
                        Resptext += " "
                        i += 1
                    elif keys[i] == 'backspace' :
                        Resptext = Resptext[:-1]
                        i += 1
                    elif keys[i] == 'capslock' :
                        if CAPS==True:
                            CAPS= False
                        elif CAPS==False:
                            CAPS=True
                        i += 1
                    elif keys[i] == 'period'and len(Resptext) < charlim:
                        Resptext += "."
                        i += 1
                    elif keys[i] == 'minus' and len(Resptext) < charlim:
                        Resptext += "-"
                        i += 1
                    elif keys[i] == 'comma' and len(Resptext) < charlim: 
                        Resptext += ","
                        i = i + 1
                    elif keys[i] in ['lshift', 'rshift']:
                        shift_flag = True
                        i = i + 1
                    elif keys[i] == 'semicolon' and len(Resptext) < charlim:
                        if shift_flag == False:
                            Resptext += ";"
                        else:
                            Resptext += ":"
                            shift_flag = False
                        i += 1
                    elif keys[i] == 'apostrophe' and len(Resptext) < charlim:
                        if shift_flag == False:
                            Resptext += "'"
                        else:
                            Resptext += '"'
                        i += 1
                    elif keys[i] == 'slash' and len(Resptext) < charlim:
                        if shift_flag == False:
                            Resptext += "/"
                        else:
                            Resptext += '?'
                            shift_flag = False
                        i = i + 1
                    elif keys[i] == '1' and len(Resptext) < charlim and shift_flag == True:
                        Resptext += "!"
                        shift_flag = False
                        i = i + 1
                    else:
                        if len(Resptext) < charlim and len(keys[i])==1:
                            Key=keys[i]
                            if CAPS or shift_flag:
                                Resptext += Key.upper()
                                shift_flag=False
                            else:
                                Resptext += Key
                        i += 1
                
                
                 
                
                # *FFcueDisp* updates
                
                # if FFcueDisp is starting this frame...
                if FFcueDisp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    FFcueDisp.frameNStart = frameN  # exact frame index
                    FFcueDisp.tStart = t  # local t and not account for scr refresh
                    FFcueDisp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(FFcueDisp, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    FFcueDisp.status = STARTED
                    FFcueDisp.setAutoDraw(True)
                
                # if FFcueDisp is active this frame...
                if FFcueDisp.status == STARTED:
                    # update params
                    pass
                
                # *polygon* updates
                
                # if polygon is starting this frame...
                if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon.frameNStart = frameN  # exact frame index
                    polygon.tStart = t  # local t and not account for scr refresh
                    polygon.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon.started')
                    # update status
                    polygon.status = STARTED
                    polygon.setAutoDraw(True)
                
                # if polygon is active this frame...
                if polygon.status == STARTED:
                    # update params
                    pass
                
                # *key_respFF* updates
                
                # if key_respFF is starting this frame...
                if key_respFF.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_respFF.frameNStart = frameN  # exact frame index
                    key_respFF.tStart = t  # local t and not account for scr refresh
                    key_respFF.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_respFF, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    key_respFF.status = STARTED
                    # keyboard checking is just starting
                    key_respFF.clock.reset()  # now t=0
                    key_respFF.clearEvents(eventType='keyboard')
                if key_respFF.status == STARTED:
                    theseKeys = key_respFF.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
                    _key_respFF_allKeys.extend(theseKeys)
                    if len(_key_respFF_allKeys):
                        key_respFF.keys = [key.name for key in _key_respFF_allKeys]  # storing all keys
                        key_respFF.rt = [key.rt for key in _key_respFF_allKeys]
                        key_respFF.duration = [key.duration for key in _key_respFF_allKeys]
                
                # *FFrespDisp* updates
                
                # if FFrespDisp is starting this frame...
                if FFrespDisp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    FFrespDisp.frameNStart = frameN  # exact frame index
                    FFrespDisp.tStart = t  # local t and not account for scr refresh
                    FFrespDisp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(FFrespDisp, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'FFrespDisp.started')
                    # update status
                    FFrespDisp.status = STARTED
                    FFrespDisp.setAutoDraw(True)
                
                # if FFrespDisp is active this frame...
                if FFrespDisp.status == STARTED:
                    # update params
                    FFrespDisp.setText((Resptext), log=False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=FF,
                    )
                    # skip the frame we paused on
                    continue
                
                # has a Component requested the Routine to end?
                if not continueRoutine:
                    FF.forceEnded = routineForceEnded = True
                # has the Routine been forcibly ended?
                if FF.forceEnded or routineForceEnded:
                    break
                # has every Component finished?
                continueRoutine = False
                for thisComponent in FF.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "FF" ---
            for thisComponent in FF.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for FF
            FF.tStop = globalClock.getTime(format='float')
            FF.tStopRefresh = tThisFlipGlobal
            thisExp.addData('FF.stopped', FF.tStop)
            # Run 'End Routine' code from FFcode_3
            #extract the 1st and last key presses
            if len(key_respFF.rt)>0:
                RT1stKP=key_respFF.rt[0]
                RTLastKP=key_respFF.rt[-1]
            
            #save the data for this trial
            thisExp.addData("FFresp", Resptext)
            thisExp.addData("FFRT1stKP", RT1stKP)
            thisExp.addData("FFRTLastKP", RTLastKP)
            PrevResp=Resptext
            Resptext = ''
            # check responses
            if key_respFF.keys in ['', [], None]:  # No response was made
                key_respFF.keys = None
            FFresps.addData('key_respFF.keys',key_respFF.keys)
            if key_respFF.keys != None:  # we had a response
                FFresps.addData('key_respFF.rt', key_respFF.rt)
                FFresps.addData('key_respFF.duration', key_respFF.duration)
            # the Routine "FF" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            # mark thisFFresp as finished
            if hasattr(thisFFresp, 'status'):
                thisFFresp.status = FINISHED
            # if awaiting a pause, pause now
            if FFresps.status == PAUSED:
                thisExp.status = PAUSED
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[globalClock], 
                )
                # once done pausing, restore running status
                FFresps.status = STARTED
            thisExp.nextEntry()
            
        # completed 19 repeats of 'FFresps'
        FFresps.status = FINISHED
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "NextFFInstrux" ---
        # create an object to store info about Routine NextFFInstrux
        NextFFInstrux = data.Routine(
            name='NextFFInstrux',
            components=[intrux_5, EntertoContinue_5, key_resp_9],
        )
        NextFFInstrux.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for key_resp_9
        key_resp_9.keys = []
        key_resp_9.rt = []
        _key_resp_9_allKeys = []
        # Run 'Begin Routine' code from code_2
        
        
        FFtrialnum+=1
        if FFtrialnum==2:
            continueRoutine==False
        # store start times for NextFFInstrux
        NextFFInstrux.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        NextFFInstrux.tStart = globalClock.getTime(format='float')
        NextFFInstrux.status = STARTED
        thisExp.addData('NextFFInstrux.started', NextFFInstrux.tStart)
        NextFFInstrux.maxDuration = None
        # keep track of which components have finished
        NextFFInstruxComponents = NextFFInstrux.components
        for thisComponent in NextFFInstrux.components:
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
        
        # --- Run Routine "NextFFInstrux" ---
        thisExp.currentRoutine = NextFFInstrux
        NextFFInstrux.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisFFtrial, 'status') and thisFFtrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *intrux_5* updates
            
            # if intrux_5 is starting this frame...
            if intrux_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                intrux_5.frameNStart = frameN  # exact frame index
                intrux_5.tStart = t  # local t and not account for scr refresh
                intrux_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(intrux_5, 'tStartRefresh')  # time at next scr refresh
                # update status
                intrux_5.status = STARTED
                intrux_5.setAutoDraw(True)
            
            # if intrux_5 is active this frame...
            if intrux_5.status == STARTED:
                # update params
                pass
            
            # *EntertoContinue_5* updates
            
            # if EntertoContinue_5 is starting this frame...
            if EntertoContinue_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                EntertoContinue_5.frameNStart = frameN  # exact frame index
                EntertoContinue_5.tStart = t  # local t and not account for scr refresh
                EntertoContinue_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(EntertoContinue_5, 'tStartRefresh')  # time at next scr refresh
                # update status
                EntertoContinue_5.status = STARTED
                EntertoContinue_5.setAutoDraw(True)
            
            # if EntertoContinue_5 is active this frame...
            if EntertoContinue_5.status == STARTED:
                # update params
                pass
            
            # *key_resp_9* updates
            waitOnFlip = False
            
            # if key_resp_9 is starting this frame...
            if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                key_resp_9.frameNStart = frameN  # exact frame index
                key_resp_9.tStart = t  # local t and not account for scr refresh
                key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_resp_9.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_9.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_9.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_9_allKeys.extend(theseKeys)
                if len(_key_resp_9_allKeys):
                    key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
                    key_resp_9.rt = _key_resp_9_allKeys[-1].rt
                    key_resp_9.duration = _key_resp_9_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=NextFFInstrux,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                NextFFInstrux.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if NextFFInstrux.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in NextFFInstrux.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "NextFFInstrux" ---
        for thisComponent in NextFFInstrux.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for NextFFInstrux
        NextFFInstrux.tStop = globalClock.getTime(format='float')
        NextFFInstrux.tStopRefresh = tThisFlipGlobal
        thisExp.addData('NextFFInstrux.stopped', NextFFInstrux.tStop)
        # the Routine "NextFFInstrux" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisFFtrial as finished
        if hasattr(thisFFtrial, 'status'):
            thisFFtrial.status = FINISHED
        # if awaiting a pause, pause now
        if FFtrials.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            FFtrials.status = STARTED
        thisExp.nextEntry()
        
    # completed 1 repeats of 'FFtrials'
    FFtrials.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    # stop any playback components
    if thisExp.currentRoutine is not None:
        for comp in thisExp.currentRoutine.getPlaybackComponents():
            comp.stop()
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
