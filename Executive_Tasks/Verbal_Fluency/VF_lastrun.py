#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2026.1.3),
    on June 17, 2026, at 18:42
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
expName = 'VerbalFluency'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': '',
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
        originPath='C:\\Users\\james\\Documents\\ZDesktop\\PhD\\Misc\\Coding_Projects_for_LinkedIn\\Verbal Fluency\\VF_lastrun.py',
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
    
    # --- Initialize components for Routine "VFinstrux" ---
    instrux = visual.TextStim(win=win, name='instrux',
        text='Well done so far.\n\nIn the next task, you will be given a category, and you must type as many items from that category as you can. \n\nFor instance, if the category is "words beginning with F" you should type as many words that begin with F as you can.',
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
    
    # --- Initialize components for Routine "VFinstrux_2" ---
    intrux_2 = visual.TextStim(win=win, name='intrux_2',
        text='Do not enter the same item twice, or the same root word with different suffixes (e.g., if you list "fox", do not list "foxes" in the same round).\n\nYou will have 60 seconds to type as many items from the category as you can. Press ENTER after typing each word.\n\nThere will be 3 categories in total.',
        font='Arial',
        pos=(0, 0.1), draggable=False, height=0.035, wrapWidth=1.2, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    EntertoContinue_2 = visual.TextStim(win=win, name='EntertoContinue_2',
        text='Press ENTER to begin',
        font='Arial',
        pos=(0, -.35), draggable=False, height=0.03, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "getreadyVF" ---
    InstruxVF_2 = visual.TextStim(win=win, name='InstruxVF_2',
        text='Type as many words as you can that are in the category shown. Press ENTER after each word. ',
        font='Arial',
        pos=(0, .25), draggable=False, height=0.03, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    text_2 = visual.TextStim(win=win, name='text_2',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.15, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "VF" ---
    VFrespbox = visual.Rect(
        win=win, name='VFrespbox',
        width=(0.45, 0.17)[0], height=(0.45, 0.17)[1],
        ori=0, pos=(0, -0.22), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=0.0, interpolate=True)
    InstruxVF = visual.TextStim(win=win, name='InstruxVF',
        text='Type as many words as you can that are in the category shown. Press ENTER after each word. ',
        font='Arial',
        pos=(0, .25), draggable=False, height=0.03, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    VFResp = visual.TextStim(win=win, name='VFResp',
        text='',
        font='Arial',
        pos=(0, -0.22), draggable=False, height=0.05, wrapWidth=0.48, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-2.0);
    VFcueDisp = visual.TextStim(win=win, name='VFcueDisp',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.08, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-3.0);
    # Run 'Begin Experiment' code from VFcode
    
    import math
    
    countdownStarted = False
    CAPS=False
    timeText_1 = visual.TextStim(win=win, name='timeText_1',
        text='',
        font='Arial',
        pos=(0.5, -0.3), draggable=False, height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-5.0);
    key_respVF = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "NextTrialVF" ---
    # Run 'Begin Experiment' code from code_13
    
    keeptracknumind=0
    intrux_14 = visual.TextStim(win=win, name='intrux_14',
        text='Press ENTER to begin the next trial.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.035, wrapWidth=1.2, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_20 = keyboard.Keyboard(deviceName='defaultKeyboard')
    
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
    
    # --- Prepare to start Routine "VFinstrux" ---
    # create an object to store info about Routine VFinstrux
    VFinstrux = data.Routine(
        name='VFinstrux',
        components=[instrux, EntertoContinue, key_resp_2],
    )
    VFinstrux.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_2
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # Run 'Begin Routine' code from code
    
    EscapeAllowed = True
    win.mouseVisible = False
    
    # set duration of each trial
    VFtime=60
    
    # store start times for VFinstrux
    VFinstrux.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    VFinstrux.tStart = globalClock.getTime(format='float')
    VFinstrux.status = STARTED
    thisExp.addData('VFinstrux.started', VFinstrux.tStart)
    VFinstrux.maxDuration = None
    # keep track of which components have finished
    VFinstruxComponents = VFinstrux.components
    for thisComponent in VFinstrux.components:
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
    
    # --- Run Routine "VFinstrux" ---
    thisExp.currentRoutine = VFinstrux
    VFinstrux.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instrux* updates
        
        # if instrux is starting this frame...
        if instrux.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instrux.frameNStart = frameN  # exact frame index
            instrux.tStart = t  # local t and not account for scr refresh
            instrux.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrux, 'tStartRefresh')  # time at next scr refresh
            # update status
            instrux.status = STARTED
            instrux.setAutoDraw(True)
        
        # if instrux is active this frame...
        if instrux.status == STARTED:
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
                currentRoutine=VFinstrux,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            VFinstrux.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if VFinstrux.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in VFinstrux.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "VFinstrux" ---
    for thisComponent in VFinstrux.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for VFinstrux
    VFinstrux.tStop = globalClock.getTime(format='float')
    VFinstrux.tStopRefresh = tThisFlipGlobal
    thisExp.addData('VFinstrux.stopped', VFinstrux.tStop)
    thisExp.nextEntry()
    # the Routine "VFinstrux" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "VFinstrux_2" ---
    # create an object to store info about Routine VFinstrux_2
    VFinstrux_2 = data.Routine(
        name='VFinstrux_2',
        components=[intrux_2, EntertoContinue_2, key_resp],
    )
    VFinstrux_2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # store start times for VFinstrux_2
    VFinstrux_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    VFinstrux_2.tStart = globalClock.getTime(format='float')
    VFinstrux_2.status = STARTED
    thisExp.addData('VFinstrux_2.started', VFinstrux_2.tStart)
    VFinstrux_2.maxDuration = None
    # keep track of which components have finished
    VFinstrux_2Components = VFinstrux_2.components
    for thisComponent in VFinstrux_2.components:
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
    
    # --- Run Routine "VFinstrux_2" ---
    thisExp.currentRoutine = VFinstrux_2
    VFinstrux_2.forceEnded = routineForceEnded = not continueRoutine
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
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
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
                currentRoutine=VFinstrux_2,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            VFinstrux_2.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if VFinstrux_2.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in VFinstrux_2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "VFinstrux_2" ---
    for thisComponent in VFinstrux_2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for VFinstrux_2
    VFinstrux_2.tStop = globalClock.getTime(format='float')
    VFinstrux_2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('VFinstrux_2.stopped', VFinstrux_2.tStop)
    thisExp.nextEntry()
    # the Routine "VFinstrux_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    VFtrials = data.TrialHandler2(
        name='VFtrials',
        nReps=1, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('VFconds.xlsx'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(VFtrials)  # add the loop to the experiment
    thisVFtrial = VFtrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisVFtrial.rgb)
    if thisVFtrial != None:
        for paramName in thisVFtrial:
            globals()[paramName] = thisVFtrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisVFtrial in VFtrials:
        VFtrials.status = STARTED
        if hasattr(thisVFtrial, 'status'):
            thisVFtrial.status = STARTED
        currentLoop = VFtrials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisVFtrial.rgb)
        if thisVFtrial != None:
            for paramName in thisVFtrial:
                globals()[paramName] = thisVFtrial[paramName]
        
        # --- Prepare to start Routine "getreadyVF" ---
        # create an object to store info about Routine getreadyVF
        getreadyVF = data.Routine(
            name='getreadyVF',
            components=[InstruxVF_2, text_2],
        )
        getreadyVF.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for getreadyVF
        getreadyVF.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        getreadyVF.tStart = globalClock.getTime(format='float')
        getreadyVF.status = STARTED
        thisExp.addData('getreadyVF.started', getreadyVF.tStart)
        getreadyVF.maxDuration = None
        # keep track of which components have finished
        getreadyVFComponents = getreadyVF.components
        for thisComponent in getreadyVF.components:
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
        
        # --- Run Routine "getreadyVF" ---
        thisExp.currentRoutine = getreadyVF
        getreadyVF.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 3.5:
            # if trial has changed, end Routine now
            if hasattr(thisVFtrial, 'status') and thisVFtrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *InstruxVF_2* updates
            
            # if InstruxVF_2 is starting this frame...
            if InstruxVF_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                InstruxVF_2.frameNStart = frameN  # exact frame index
                InstruxVF_2.tStart = t  # local t and not account for scr refresh
                InstruxVF_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(InstruxVF_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                InstruxVF_2.status = STARTED
                InstruxVF_2.setAutoDraw(True)
            
            # if InstruxVF_2 is active this frame...
            if InstruxVF_2.status == STARTED:
                # update params
                pass
            
            # if InstruxVF_2 is stopping this frame...
            if InstruxVF_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > InstruxVF_2.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    InstruxVF_2.tStop = t  # not accounting for scr refresh
                    InstruxVF_2.tStopRefresh = tThisFlipGlobal  # on global time
                    InstruxVF_2.frameNStop = frameN  # exact frame index
                    # update status
                    InstruxVF_2.status = FINISHED
                    InstruxVF_2.setAutoDraw(False)
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # if text_2 is stopping this frame...
            if text_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_2.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.tStopRefresh = tThisFlipGlobal  # on global time
                    text_2.frameNStop = frameN  # exact frame index
                    # update status
                    text_2.status = FINISHED
                    text_2.setAutoDraw(False)
            
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
                    currentRoutine=getreadyVF,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                getreadyVF.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if getreadyVF.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in getreadyVF.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "getreadyVF" ---
        for thisComponent in getreadyVF.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for getreadyVF
        getreadyVF.tStop = globalClock.getTime(format='float')
        getreadyVF.tStopRefresh = tThisFlipGlobal
        thisExp.addData('getreadyVF.stopped', getreadyVF.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if getreadyVF.maxDurationReached:
            routineTimer.addTime(-getreadyVF.maxDuration)
        elif getreadyVF.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.500000)
        
        # set up handler to look after randomisation of conditions etc
        VFresps = data.TrialHandler2(
            name='VFresps',
            nReps=100, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
            isTrials=True, 
        )
        thisExp.addLoop(VFresps)  # add the loop to the experiment
        thisVFresp = VFresps.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisVFresp.rgb)
        if thisVFresp != None:
            for paramName in thisVFresp:
                globals()[paramName] = thisVFresp[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisVFresp in VFresps:
            VFresps.status = STARTED
            if hasattr(thisVFresp, 'status'):
                thisVFresp.status = STARTED
            currentLoop = VFresps
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisVFresp.rgb)
            if thisVFresp != None:
                for paramName in thisVFresp:
                    globals()[paramName] = thisVFresp[paramName]
            
            # --- Prepare to start Routine "VF" ---
            # create an object to store info about Routine VF
            VF = data.Routine(
                name='VF',
                components=[VFrespbox, InstruxVF, VFResp, VFcueDisp, timeText_1, key_respVF],
            )
            VF.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            VFcueDisp.setText(VFcond)
            # Run 'Begin Routine' code from VFcode
            shift_flag = False
            Resptext = ''
            RT1stKP=0
            
            RTLastKP=0
            
            if not countdownStarted:
                startTime=globalClock.getTime()
                #timeText="03:00"
                countdownStarted=True
                
            event.clearEvents('keyboard')
            # create starting attributes for key_respVF
            key_respVF.keys = []
            key_respVF.rt = []
            _key_respVF_allKeys = []
            # store start times for VF
            VF.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            VF.tStart = globalClock.getTime(format='float')
            VF.status = STARTED
            thisExp.addData('VF.started', VF.tStart)
            VF.maxDuration = None
            # keep track of which components have finished
            VFComponents = VF.components
            for thisComponent in VF.components:
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
            
            # --- Run Routine "VF" ---
            thisExp.currentRoutine = VF
            VF.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # if trial has changed, end Routine now
                if hasattr(thisVFresp, 'status') and thisVFresp.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *VFrespbox* updates
                
                # if VFrespbox is starting this frame...
                if VFrespbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    VFrespbox.frameNStart = frameN  # exact frame index
                    VFrespbox.tStart = t  # local t and not account for scr refresh
                    VFrespbox.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(VFrespbox, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    VFrespbox.status = STARTED
                    VFrespbox.setAutoDraw(True)
                
                # if VFrespbox is active this frame...
                if VFrespbox.status == STARTED:
                    # update params
                    pass
                
                # *InstruxVF* updates
                
                # if InstruxVF is starting this frame...
                if InstruxVF.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    InstruxVF.frameNStart = frameN  # exact frame index
                    InstruxVF.tStart = t  # local t and not account for scr refresh
                    InstruxVF.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(InstruxVF, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    InstruxVF.status = STARTED
                    InstruxVF.setAutoDraw(True)
                
                # if InstruxVF is active this frame...
                if InstruxVF.status == STARTED:
                    # update params
                    pass
                
                # *VFResp* updates
                
                # if VFResp is starting this frame...
                if VFResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    VFResp.frameNStart = frameN  # exact frame index
                    VFResp.tStart = t  # local t and not account for scr refresh
                    VFResp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(VFResp, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    VFResp.status = STARTED
                    VFResp.setAutoDraw(True)
                
                # if VFResp is active this frame...
                if VFResp.status == STARTED:
                    # update params
                    VFResp.setText(Resptext, log=False)
                
                # *VFcueDisp* updates
                
                # if VFcueDisp is starting this frame...
                if VFcueDisp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    VFcueDisp.frameNStart = frameN  # exact frame index
                    VFcueDisp.tStart = t  # local t and not account for scr refresh
                    VFcueDisp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(VFcueDisp, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    VFcueDisp.status = STARTED
                    VFcueDisp.setAutoDraw(True)
                
                # if VFcueDisp is active this frame...
                if VFcueDisp.status == STARTED:
                    # update params
                    pass
                # Run 'Each Frame' code from VFcode
                keys = event.getKeys()
                n=len(keys)
                i=0
                
                
                ###Timer#####
                Diff=globalClock.getTime()-startTime
                timeRemaining = VFtime-math.floor(Diff/1) #this gives us a whole number for time 
                #remaining, using floor not round since we do not want the seconds to update except when the timeremaining crosses an actual whole integer
                Minutes = int(timeRemaining/60.0) # the integer number of minutes
                Seconds = int(timeRemaining - (Minutes * 60.0))
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
                    elif keys[i] == 'period'and len(Resptext) < 80:
                        Resptext += "."
                        i += 1
                    elif keys[i] == 'minus' and len(Resptext) < 80:
                        Resptext += "-"
                        i += 1
                    elif keys[i] == 'comma' and len(Resptext) < 80: 
                        Resptext += ","
                        i = i + 1
                    elif keys[i] in ['lshift', 'rshift']:
                        shift_flag = True
                        i = i + 1
                    elif keys[i] == 'semicolon' and len(Resptext) < 80:
                        if shift_flag == False:
                            Resptext += ";"
                        else:
                            Resptext += ":"
                            shift_flag = False
                        i += 1
                    elif keys[i] == 'apostrophe' and len(Resptext) < 80:
                        if shift_flag == False:
                            Resptext += "'"
                        else:
                            Resptext += '"'
                        i += 1
                    elif keys[i] == 'slash' and len(Resptext) < 80:
                        if shift_flag == False:
                            Resptext += "/"
                        else:
                            Resptext += '?'
                            shift_flag = False
                        i = i + 1
                    elif keys[i] == '1' and len(Resptext) < 80 and shift_flag == True:
                        Resptext += "!"
                        shift_flag = False
                        i = i + 1
                    else:
                        if len(Resptext) < 80 and len(keys[i])==1:
                            Key=keys[i]
                            if CAPS or shift_flag:
                                Resptext += Key.upper()
                                shift_flag=False
                            else:
                                Resptext += Key
                        i += 1
                
                if timeRemaining <= 0:
                    VFresps.finished = True
                    continueRoutine = False
                    countdownStarted = False
                 
                
                # *timeText_1* updates
                
                # if timeText_1 is starting this frame...
                if timeText_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    timeText_1.frameNStart = frameN  # exact frame index
                    timeText_1.tStart = t  # local t and not account for scr refresh
                    timeText_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(timeText_1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    timeText_1.status = STARTED
                    timeText_1.setAutoDraw(True)
                
                # if timeText_1 is active this frame...
                if timeText_1.status == STARTED:
                    # update params
                    timeText_1.setText(timeText, log=False)
                
                # *key_respVF* updates
                waitOnFlip = False
                
                # if key_respVF is starting this frame...
                if key_respVF.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_respVF.frameNStart = frameN  # exact frame index
                    key_respVF.tStart = t  # local t and not account for scr refresh
                    key_respVF.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_respVF, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    key_respVF.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_respVF.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_respVF.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_respVF.status == STARTED and not waitOnFlip:
                    theseKeys = key_respVF.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
                    _key_respVF_allKeys.extend(theseKeys)
                    if len(_key_respVF_allKeys):
                        key_respVF.keys = [key.name for key in _key_respVF_allKeys]  # storing all keys
                        key_respVF.rt = [key.rt for key in _key_respVF_allKeys]
                        key_respVF.duration = [key.duration for key in _key_respVF_allKeys]
                
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
                        currentRoutine=VF,
                    )
                    # skip the frame we paused on
                    continue
                
                # has a Component requested the Routine to end?
                if not continueRoutine:
                    VF.forceEnded = routineForceEnded = True
                # has the Routine been forcibly ended?
                if VF.forceEnded or routineForceEnded:
                    break
                # has every Component finished?
                continueRoutine = False
                for thisComponent in VF.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "VF" ---
            for thisComponent in VF.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for VF
            VF.tStop = globalClock.getTime(format='float')
            VF.tStopRefresh = tThisFlipGlobal
            thisExp.addData('VF.stopped', VF.tStop)
            # Run 'End Routine' code from VFcode
            #extract the 1st and last key presses
            if len(key_respVF.rt)>0:
                RT1stKP=key_respVF.rt[0]
                RTLastKP=key_respVF.rt[-1]
            
            #save the data for this trial
            thisExp.addData("VFresp", Resptext)
            thisExp.addData("VFRT1stKP", RT1stKP)
            thisExp.addData("VFRTLastKP", RTLastKP)
            Resptext = ''
            
            
            # check responses
            if key_respVF.keys in ['', [], None]:  # No response was made
                key_respVF.keys = None
            VFresps.addData('key_respVF.keys',key_respVF.keys)
            if key_respVF.keys != None:  # we had a response
                VFresps.addData('key_respVF.rt', key_respVF.rt)
                VFresps.addData('key_respVF.duration', key_respVF.duration)
            # the Routine "VF" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            # mark thisVFresp as finished
            if hasattr(thisVFresp, 'status'):
                thisVFresp.status = FINISHED
            # if awaiting a pause, pause now
            if VFresps.status == PAUSED:
                thisExp.status = PAUSED
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[globalClock], 
                )
                # once done pausing, restore running status
                VFresps.status = STARTED
            thisExp.nextEntry()
            
        # completed 100 repeats of 'VFresps'
        VFresps.status = FINISHED
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "NextTrialVF" ---
        # create an object to store info about Routine NextTrialVF
        NextTrialVF = data.Routine(
            name='NextTrialVF',
            components=[intrux_14, key_resp_20],
        )
        NextTrialVF.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_13
        
        ## this code simply keeps track of what trial number it is
        keeptracknumind+=1
        if keeptracknumind==3:
            continueRoutine=False
            
        blahtext=str(keeptracknumind)
        # create starting attributes for key_resp_20
        key_resp_20.keys = []
        key_resp_20.rt = []
        _key_resp_20_allKeys = []
        # store start times for NextTrialVF
        NextTrialVF.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        NextTrialVF.tStart = globalClock.getTime(format='float')
        NextTrialVF.status = STARTED
        thisExp.addData('NextTrialVF.started', NextTrialVF.tStart)
        NextTrialVF.maxDuration = None
        # keep track of which components have finished
        NextTrialVFComponents = NextTrialVF.components
        for thisComponent in NextTrialVF.components:
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
        
        # --- Run Routine "NextTrialVF" ---
        thisExp.currentRoutine = NextTrialVF
        NextTrialVF.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisVFtrial, 'status') and thisVFtrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *intrux_14* updates
            
            # if intrux_14 is starting this frame...
            if intrux_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                intrux_14.frameNStart = frameN  # exact frame index
                intrux_14.tStart = t  # local t and not account for scr refresh
                intrux_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(intrux_14, 'tStartRefresh')  # time at next scr refresh
                # update status
                intrux_14.status = STARTED
                intrux_14.setAutoDraw(True)
            
            # if intrux_14 is active this frame...
            if intrux_14.status == STARTED:
                # update params
                pass
            
            # *key_resp_20* updates
            waitOnFlip = False
            
            # if key_resp_20 is starting this frame...
            if key_resp_20.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                key_resp_20.frameNStart = frameN  # exact frame index
                key_resp_20.tStart = t  # local t and not account for scr refresh
                key_resp_20.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_20, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_resp_20.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_20.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_20.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_20.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_20.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_20_allKeys.extend(theseKeys)
                if len(_key_resp_20_allKeys):
                    key_resp_20.keys = _key_resp_20_allKeys[-1].name  # just the last key pressed
                    key_resp_20.rt = _key_resp_20_allKeys[-1].rt
                    key_resp_20.duration = _key_resp_20_allKeys[-1].duration
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
                    currentRoutine=NextTrialVF,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                NextTrialVF.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if NextTrialVF.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in NextTrialVF.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "NextTrialVF" ---
        for thisComponent in NextTrialVF.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for NextTrialVF
        NextTrialVF.tStop = globalClock.getTime(format='float')
        NextTrialVF.tStopRefresh = tThisFlipGlobal
        thisExp.addData('NextTrialVF.stopped', NextTrialVF.tStop)
        # the Routine "NextTrialVF" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisVFtrial as finished
        if hasattr(thisVFtrial, 'status'):
            thisVFtrial.status = FINISHED
        # if awaiting a pause, pause now
        if VFtrials.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            VFtrials.status = STARTED
        thisExp.nextEntry()
        
    # completed 1 repeats of 'VFtrials'
    VFtrials.status = FINISHED
    
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
