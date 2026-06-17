#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2026.1.3),
    on June 17, 2026, at 18:55
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
expName = 'TS'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
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
_winSize = (1024, 768)
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
        originPath='C:\\Users\\james\\Documents\\ZDesktop\\PhD\\Misc\\Coding_Projects_for_LinkedIn\\Typing_Speed\\TS_lastrun.py',
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
    
    # --- Initialize components for Routine "TypingSpeedInstrux" ---
    TStext = visual.TextStim(win=win, name='TStext',
        text="For this task, you'll be asked to type as many words as you can in 30 seconds. \n\nEach screen will show a word. Please type out the exact word shown, in the text field and then press ENTER. \nA new word will then appear. \n\nThis will continue for 30 seconds, so please type as many as you can within that time.",
        font='Arial',
        pos=[0, 0.1], draggable=False, height=0.04, wrapWidth=1.2, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_22 = keyboard.Keyboard(deviceName='defaultKeyboard')
    EnterToContinue_20 = visual.TextStim(win=win, name='EnterToContinue_20',
        text='Press ENTER to begin the task',
        font='Arial',
        pos=(0, -0.3), draggable=False, height=0.03, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "GetReady" ---
    GetReadyText = visual.TextStim(win=win, name='GetReadyText',
        text='Get ready',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "TypingSpeed" ---
    # Run 'Begin Experiment' code from TScode
    
    
    
    TScueDisp = visual.TextStim(win=win, name='TScueDisp',
        text='',
        font='Arial',
        pos=(0, 0.1), draggable=False, height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    polygon_6 = visual.Rect(
        win=win, name='polygon_6',
        width=(0.45, 0.17)[0], height=(0.45, 0.17)[1],
        ori=0, pos=(0, -0.2), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=-2.0, interpolate=True)
    key_respTS = keyboard.Keyboard(deviceName='defaultKeyboard')
    TSrespDisp = visual.TextStim(win=win, name='TSrespDisp',
        text='',
        font='Arial',
        pos=(0, -0.2), draggable=False, height=0.075, wrapWidth=0.4, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-4.0);
    Timer_2 = visual.TextStim(win=win, name='Timer_2',
        text='',
        font='Arial',
        pos=(0.5, -0.35), draggable=False, height=0.09, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-5.0);
    
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
    
    # --- Prepare to start Routine "TypingSpeedInstrux" ---
    # create an object to store info about Routine TypingSpeedInstrux
    TypingSpeedInstrux = data.Routine(
        name='TypingSpeedInstrux',
        components=[TStext, key_resp_22, EnterToContinue_20],
    )
    TypingSpeedInstrux.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_22
    key_resp_22.keys = []
    key_resp_22.rt = []
    _key_resp_22_allKeys = []
    # Run 'Begin Routine' code from code_43
    
    
    win.mouseVisible = False
    
    Taskstart=globalClock.getTime()
    
    TStime=30
    
    import math 
    
    CAPS=False
    # store start times for TypingSpeedInstrux
    TypingSpeedInstrux.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    TypingSpeedInstrux.tStart = globalClock.getTime(format='float')
    TypingSpeedInstrux.status = STARTED
    thisExp.addData('TypingSpeedInstrux.started', TypingSpeedInstrux.tStart)
    TypingSpeedInstrux.maxDuration = None
    # keep track of which components have finished
    TypingSpeedInstruxComponents = TypingSpeedInstrux.components
    for thisComponent in TypingSpeedInstrux.components:
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
    
    # --- Run Routine "TypingSpeedInstrux" ---
    thisExp.currentRoutine = TypingSpeedInstrux
    TypingSpeedInstrux.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *TStext* updates
        
        # if TStext is starting this frame...
        if TStext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TStext.frameNStart = frameN  # exact frame index
            TStext.tStart = t  # local t and not account for scr refresh
            TStext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TStext, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TStext.started')
            # update status
            TStext.status = STARTED
            TStext.setAutoDraw(True)
        
        # if TStext is active this frame...
        if TStext.status == STARTED:
            # update params
            pass
        
        # *key_resp_22* updates
        waitOnFlip = False
        
        # if key_resp_22 is starting this frame...
        if key_resp_22.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_22.frameNStart = frameN  # exact frame index
            key_resp_22.tStart = t  # local t and not account for scr refresh
            key_resp_22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_22, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_22.started')
            # update status
            key_resp_22.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_22.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_22.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_22.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_22.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_22_allKeys.extend(theseKeys)
            if len(_key_resp_22_allKeys):
                key_resp_22.keys = _key_resp_22_allKeys[-1].name  # just the last key pressed
                key_resp_22.rt = _key_resp_22_allKeys[-1].rt
                key_resp_22.duration = _key_resp_22_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *EnterToContinue_20* updates
        
        # if EnterToContinue_20 is starting this frame...
        if EnterToContinue_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            EnterToContinue_20.frameNStart = frameN  # exact frame index
            EnterToContinue_20.tStart = t  # local t and not account for scr refresh
            EnterToContinue_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EnterToContinue_20, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EnterToContinue_20.started')
            # update status
            EnterToContinue_20.status = STARTED
            EnterToContinue_20.setAutoDraw(True)
        
        # if EnterToContinue_20 is active this frame...
        if EnterToContinue_20.status == STARTED:
            # update params
            pass
        
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
                currentRoutine=TypingSpeedInstrux,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            TypingSpeedInstrux.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if TypingSpeedInstrux.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in TypingSpeedInstrux.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "TypingSpeedInstrux" ---
    for thisComponent in TypingSpeedInstrux.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for TypingSpeedInstrux
    TypingSpeedInstrux.tStop = globalClock.getTime(format='float')
    TypingSpeedInstrux.tStopRefresh = tThisFlipGlobal
    thisExp.addData('TypingSpeedInstrux.stopped', TypingSpeedInstrux.tStop)
    thisExp.nextEntry()
    # the Routine "TypingSpeedInstrux" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "GetReady" ---
    # create an object to store info about Routine GetReady
    GetReady = data.Routine(
        name='GetReady',
        components=[GetReadyText],
    )
    GetReady.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for GetReady
    GetReady.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    GetReady.tStart = globalClock.getTime(format='float')
    GetReady.status = STARTED
    thisExp.addData('GetReady.started', GetReady.tStart)
    GetReady.maxDuration = None
    # keep track of which components have finished
    GetReadyComponents = GetReady.components
    for thisComponent in GetReady.components:
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
    
    # --- Run Routine "GetReady" ---
    thisExp.currentRoutine = GetReady
    GetReady.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *GetReadyText* updates
        
        # if GetReadyText is starting this frame...
        if GetReadyText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            GetReadyText.frameNStart = frameN  # exact frame index
            GetReadyText.tStart = t  # local t and not account for scr refresh
            GetReadyText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(GetReadyText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'GetReadyText.started')
            # update status
            GetReadyText.status = STARTED
            GetReadyText.setAutoDraw(True)
        
        # if GetReadyText is active this frame...
        if GetReadyText.status == STARTED:
            # update params
            pass
        
        # if GetReadyText is stopping this frame...
        if GetReadyText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > GetReadyText.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                GetReadyText.tStop = t  # not accounting for scr refresh
                GetReadyText.tStopRefresh = tThisFlipGlobal  # on global time
                GetReadyText.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'GetReadyText.stopped')
                # update status
                GetReadyText.status = FINISHED
                GetReadyText.setAutoDraw(False)
        
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
                currentRoutine=GetReady,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            GetReady.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if GetReady.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in GetReady.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "GetReady" ---
    for thisComponent in GetReady.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for GetReady
    GetReady.tStop = globalClock.getTime(format='float')
    GetReady.tStopRefresh = tThisFlipGlobal
    thisExp.addData('GetReady.stopped', GetReady.tStop)
    # Run 'End Routine' code from code_44
    #start time for countdown/ trial timer
    startTime=globalClock.getTime()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if GetReady.maxDurationReached:
        routineTimer.addTime(-GetReady.maxDuration)
    elif GetReady.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    TStrials = data.TrialHandler2(
        name='TStrials',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('TS.xlsx'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(TStrials)  # add the loop to the experiment
    thisTStrial = TStrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTStrial.rgb)
    if thisTStrial != None:
        for paramName in thisTStrial:
            globals()[paramName] = thisTStrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTStrial in TStrials:
        TStrials.status = STARTED
        if hasattr(thisTStrial, 'status'):
            thisTStrial.status = STARTED
        currentLoop = TStrials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTStrial.rgb)
        if thisTStrial != None:
            for paramName in thisTStrial:
                globals()[paramName] = thisTStrial[paramName]
        
        # --- Prepare to start Routine "TypingSpeed" ---
        # create an object to store info about Routine TypingSpeed
        TypingSpeed = data.Routine(
            name='TypingSpeed',
            components=[TScueDisp, polygon_6, key_respTS, TSrespDisp, Timer_2],
        )
        TypingSpeed.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from TScode
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
        
        
        TScueDisp.setText(TSstim)
        # create starting attributes for key_respTS
        key_respTS.keys = []
        key_respTS.rt = []
        _key_respTS_allKeys = []
        # store start times for TypingSpeed
        TypingSpeed.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        TypingSpeed.tStart = globalClock.getTime(format='float')
        TypingSpeed.status = STARTED
        thisExp.addData('TypingSpeed.started', TypingSpeed.tStart)
        TypingSpeed.maxDuration = None
        # keep track of which components have finished
        TypingSpeedComponents = TypingSpeed.components
        for thisComponent in TypingSpeed.components:
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
        
        # --- Run Routine "TypingSpeed" ---
        thisExp.currentRoutine = TypingSpeed
        TypingSpeed.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTStrial, 'status') and thisTStrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from TScode
            
            keys = event.getKeys()
            n=len(keys)
            i=0
            
            ###Timer#####
            Diff=globalClock.getTime()-startTime
            timeRemaining = TStime-math.floor(Diff) #this gives us a whole number for time 
            #remaining, using floor not round since we do not want the seconds to update except when the timeremaining crosses an actual whole integer
            Minutes = int(timeRemaining/60.0) # the integer number of minutes
            Seconds = int(timeRemaining - (Minutes * 60.0))
            #convert the above numbers into strings in the right format
            if Minutes<10:
                minstring='0' + str(Minutes)
            else:
                minstring=str(Minutes)
            if Seconds<10:
                secstring='0' + str(Seconds)
            else:
                secstring=str(Seconds)
            timeText = minstring + ':' + secstring # create a string of characters representing the time
            
            
            ###### Text entry #####
            while i < n: # len(keys):
                #process each key depending on what it is
                if keys[i] == 'return' and len(Resptext)>=1 or timeRemaining<= 0:
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
            
            if timeRemaining <= 0:
                continueRoutine = False
                TStrials.finished=True
            
            # *TScueDisp* updates
            
            # if TScueDisp is starting this frame...
            if TScueDisp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                TScueDisp.frameNStart = frameN  # exact frame index
                TScueDisp.tStart = t  # local t and not account for scr refresh
                TScueDisp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TScueDisp, 'tStartRefresh')  # time at next scr refresh
                # update status
                TScueDisp.status = STARTED
                TScueDisp.setAutoDraw(True)
            
            # if TScueDisp is active this frame...
            if TScueDisp.status == STARTED:
                # update params
                pass
            
            # *polygon_6* updates
            
            # if polygon_6 is starting this frame...
            if polygon_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_6.frameNStart = frameN  # exact frame index
                polygon_6.tStart = t  # local t and not account for scr refresh
                polygon_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_6, 'tStartRefresh')  # time at next scr refresh
                # update status
                polygon_6.status = STARTED
                polygon_6.setAutoDraw(True)
            
            # if polygon_6 is active this frame...
            if polygon_6.status == STARTED:
                # update params
                pass
            
            # *key_respTS* updates
            
            # if key_respTS is starting this frame...
            if key_respTS.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_respTS.frameNStart = frameN  # exact frame index
                key_respTS.tStart = t  # local t and not account for scr refresh
                key_respTS.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_respTS, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_respTS.status = STARTED
                # keyboard checking is just starting
                key_respTS.clock.reset()  # now t=0
                key_respTS.clearEvents(eventType='keyboard')
            if key_respTS.status == STARTED:
                theseKeys = key_respTS.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
                _key_respTS_allKeys.extend(theseKeys)
                if len(_key_respTS_allKeys):
                    key_respTS.keys = [key.name for key in _key_respTS_allKeys]  # storing all keys
                    key_respTS.rt = [key.rt for key in _key_respTS_allKeys]
                    key_respTS.duration = [key.duration for key in _key_respTS_allKeys]
            
            # *TSrespDisp* updates
            
            # if TSrespDisp is starting this frame...
            if TSrespDisp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TSrespDisp.frameNStart = frameN  # exact frame index
                TSrespDisp.tStart = t  # local t and not account for scr refresh
                TSrespDisp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TSrespDisp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TSrespDisp.started')
                # update status
                TSrespDisp.status = STARTED
                TSrespDisp.setAutoDraw(True)
            
            # if TSrespDisp is active this frame...
            if TSrespDisp.status == STARTED:
                # update params
                TSrespDisp.setText((Resptext), log=False)
            
            # *Timer_2* updates
            
            # if Timer_2 is starting this frame...
            if Timer_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Timer_2.frameNStart = frameN  # exact frame index
                Timer_2.tStart = t  # local t and not account for scr refresh
                Timer_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Timer_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                Timer_2.status = STARTED
                Timer_2.setAutoDraw(True)
            
            # if Timer_2 is active this frame...
            if Timer_2.status == STARTED:
                # update params
                Timer_2.setText((timeText), log=False)
            
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
                    currentRoutine=TypingSpeed,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                TypingSpeed.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if TypingSpeed.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in TypingSpeed.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "TypingSpeed" ---
        for thisComponent in TypingSpeed.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for TypingSpeed
        TypingSpeed.tStop = globalClock.getTime(format='float')
        TypingSpeed.tStopRefresh = tThisFlipGlobal
        thisExp.addData('TypingSpeed.stopped', TypingSpeed.tStop)
        # Run 'End Routine' code from TScode
        #extract the 1st and last key presses
        if len(key_respTS.rt)>0:
            RT1stKP=key_respTS.rt[0]
            RTLastKP=key_respTS.rt[-1]
        
        
        thisExp.addData('TSinput', Resptext)
        thisExp.addData("TSRT1stKP", RT1stKP)
        thisExp.addData("TSRTLastKP", RTLastKP)
        Resptext=""
        
        
        # check responses
        if key_respTS.keys in ['', [], None]:  # No response was made
            key_respTS.keys = None
        TStrials.addData('key_respTS.keys',key_respTS.keys)
        if key_respTS.keys != None:  # we had a response
            TStrials.addData('key_respTS.rt', key_respTS.rt)
            TStrials.addData('key_respTS.duration', key_respTS.duration)
        # the Routine "TypingSpeed" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisTStrial as finished
        if hasattr(thisTStrial, 'status'):
            thisTStrial.status = FINISHED
        # if awaiting a pause, pause now
        if TStrials.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            TStrials.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'TStrials'
    TStrials.status = FINISHED
    
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
