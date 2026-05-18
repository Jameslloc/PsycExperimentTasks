#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2026.1.3),
    on May 16, 2026, at 17:03
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

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2026.1.3'
expName = 'AUTonline2'  # from the Builder filename that created this script
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
        originPath='C:\\Users\\james\\Documents\\ZDesktop\\PhD\\Misc\\Coding_Projects_for_LinkedIn\\AUT\\AUTonline_lastrun.py',
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
            logging.getLevel('info')
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
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
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
            backend='PsychToolbox',
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
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
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
    
    # --- Initialize components for Routine "AUTinstrux" ---
    intrux = visual.TextStim(win=win, name='intrux',
        text="For the next task, you'll be asked to come up with as many original and creative uses for objects as you can.\n\nThe goal is to come up with *creative ideas*, which are ideas that strike people as clever, unusual, interesting, uncommon, humorous, innovative, or different.\n\nYou will have 3 minutes to type as many CREATIVE USES for each object as you can. \nDo not write simply properties of the object, or words associated with the object, but actual uses.\n\nPress ENTER after each use, to write the next one.\n\nYou will be asked to type uses for 2 different objects. ",
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
    
    # --- Initialize components for Routine "AUTblank" ---
    text_5 = visual.TextStim(win=win, name='text_5',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.15, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "AUT" ---
    AUTrespbox = visual.Rect(
        win=win, name='AUTrespbox',
        width=(0.5, 0.25)[0], height=(0.5, 0.25)[1],
        ori=0, pos=(0, -0.25), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=0.0, interpolate=True)
    InstruxAUT = visual.TextStim(win=win, name='InstruxAUT',
        text='Think of as many creative uses as you can\nfor the following object: ',
        font='Arial',
        pos=(0, .25), draggable=False, height=0.03, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    AUTResp = visual.TextStim(win=win, name='AUTResp',
        text='',
        font='Arial',
        pos=(0, -0.25), draggable=False, height=0.05, wrapWidth=0.48, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-2.0);
    AUTcueDisp = visual.TextStim(win=win, name='AUTcueDisp',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-3.0);
    # Run 'Begin Experiment' code from AUTcode
    
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
    key_respAUT = keyboard.Keyboard(deviceName='defaultKeyboard')
    
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
    
    # --- Prepare to start Routine "AUTinstrux" ---
    # create an object to store info about Routine AUTinstrux
    AUTinstrux = data.Routine(
        name='AUTinstrux',
        components=[intrux, EntertoContinue, key_resp_2],
    )
    AUTinstrux.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_2
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # Run 'Begin Routine' code from code
    AUTtime=180
    EscapeAllowed = True
    win.mouseVisible = False
    #js code that doesnt work:
    #document.body.style.cursor=‘none’
    # store start times for AUTinstrux
    AUTinstrux.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    AUTinstrux.tStart = globalClock.getTime(format='float')
    AUTinstrux.status = STARTED
    thisExp.addData('AUTinstrux.started', AUTinstrux.tStart)
    AUTinstrux.maxDuration = None
    # keep track of which components have finished
    AUTinstruxComponents = AUTinstrux.components
    for thisComponent in AUTinstrux.components:
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
    
    # --- Run Routine "AUTinstrux" ---
    thisExp.currentRoutine = AUTinstrux
    AUTinstrux.forceEnded = routineForceEnded = not continueRoutine
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
                currentRoutine=AUTinstrux,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            AUTinstrux.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if AUTinstrux.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in AUTinstrux.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "AUTinstrux" ---
    for thisComponent in AUTinstrux.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for AUTinstrux
    AUTinstrux.tStop = globalClock.getTime(format='float')
    AUTinstrux.tStopRefresh = tThisFlipGlobal
    thisExp.addData('AUTinstrux.stopped', AUTinstrux.tStop)
    thisExp.nextEntry()
    # the Routine "AUTinstrux" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    AUTtrials = data.TrialHandler2(
        name='AUTtrials',
        nReps=1, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('cond.xlsx'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(AUTtrials)  # add the loop to the experiment
    thisAUTtrial = AUTtrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAUTtrial.rgb)
    if thisAUTtrial != None:
        for paramName in thisAUTtrial:
            globals()[paramName] = thisAUTtrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisAUTtrial in AUTtrials:
        AUTtrials.status = STARTED
        if hasattr(thisAUTtrial, 'status'):
            thisAUTtrial.status = STARTED
        currentLoop = AUTtrials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisAUTtrial.rgb)
        if thisAUTtrial != None:
            for paramName in thisAUTtrial:
                globals()[paramName] = thisAUTtrial[paramName]
        
        # --- Prepare to start Routine "AUTblank" ---
        # create an object to store info about Routine AUTblank
        AUTblank = data.Routine(
            name='AUTblank',
            components=[text_5],
        )
        AUTblank.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for AUTblank
        AUTblank.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        AUTblank.tStart = globalClock.getTime(format='float')
        AUTblank.status = STARTED
        thisExp.addData('AUTblank.started', AUTblank.tStart)
        AUTblank.maxDuration = None
        # keep track of which components have finished
        AUTblankComponents = AUTblank.components
        for thisComponent in AUTblank.components:
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
        
        # --- Run Routine "AUTblank" ---
        thisExp.currentRoutine = AUTblank
        AUTblank.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisAUTtrial, 'status') and thisAUTtrial.status == STOPPING:
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
                    currentRoutine=AUTblank,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                AUTblank.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if AUTblank.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in AUTblank.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "AUTblank" ---
        for thisComponent in AUTblank.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for AUTblank
        AUTblank.tStop = globalClock.getTime(format='float')
        AUTblank.tStopRefresh = tThisFlipGlobal
        thisExp.addData('AUTblank.stopped', AUTblank.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if AUTblank.maxDurationReached:
            routineTimer.addTime(-AUTblank.maxDuration)
        elif AUTblank.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # set up handler to look after randomisation of conditions etc
        AUTresps = data.TrialHandler2(
            name='AUTresps',
            nReps=100, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
            isTrials=True, 
        )
        thisExp.addLoop(AUTresps)  # add the loop to the experiment
        thisAUTresp = AUTresps.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisAUTresp.rgb)
        if thisAUTresp != None:
            for paramName in thisAUTresp:
                globals()[paramName] = thisAUTresp[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisAUTresp in AUTresps:
            AUTresps.status = STARTED
            if hasattr(thisAUTresp, 'status'):
                thisAUTresp.status = STARTED
            currentLoop = AUTresps
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisAUTresp.rgb)
            if thisAUTresp != None:
                for paramName in thisAUTresp:
                    globals()[paramName] = thisAUTresp[paramName]
            
            # --- Prepare to start Routine "AUT" ---
            # create an object to store info about Routine AUT
            AUT = data.Routine(
                name='AUT',
                components=[AUTrespbox, InstruxAUT, AUTResp, AUTcueDisp, timeText_1, key_respAUT],
            )
            AUT.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            AUTcueDisp.setText(cue)
            # Run 'Begin Routine' code from AUTcode
            shift_flag = False
            Resptext = ''
            RT1stKP=0
            #Resptext2=''
            RTLastKP=0
            
            if not countdownStarted:
                startTime=globalClock.getTime()
                #timeText="03:00"
                countdownStarted=True
                
            event.clearEvents('keyboard')
            # create starting attributes for key_respAUT
            key_respAUT.keys = []
            key_respAUT.rt = []
            _key_respAUT_allKeys = []
            # store start times for AUT
            AUT.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            AUT.tStart = globalClock.getTime(format='float')
            AUT.status = STARTED
            thisExp.addData('AUT.started', AUT.tStart)
            AUT.maxDuration = None
            # keep track of which components have finished
            AUTComponents = AUT.components
            for thisComponent in AUT.components:
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
            
            # --- Run Routine "AUT" ---
            thisExp.currentRoutine = AUT
            AUT.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # if trial has changed, end Routine now
                if hasattr(thisAUTresp, 'status') and thisAUTresp.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *AUTrespbox* updates
                
                # if AUTrespbox is starting this frame...
                if AUTrespbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    AUTrespbox.frameNStart = frameN  # exact frame index
                    AUTrespbox.tStart = t  # local t and not account for scr refresh
                    AUTrespbox.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(AUTrespbox, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    AUTrespbox.status = STARTED
                    AUTrespbox.setAutoDraw(True)
                
                # if AUTrespbox is active this frame...
                if AUTrespbox.status == STARTED:
                    # update params
                    pass
                
                # *InstruxAUT* updates
                
                # if InstruxAUT is starting this frame...
                if InstruxAUT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    InstruxAUT.frameNStart = frameN  # exact frame index
                    InstruxAUT.tStart = t  # local t and not account for scr refresh
                    InstruxAUT.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(InstruxAUT, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    InstruxAUT.status = STARTED
                    InstruxAUT.setAutoDraw(True)
                
                # if InstruxAUT is active this frame...
                if InstruxAUT.status == STARTED:
                    # update params
                    pass
                
                # *AUTResp* updates
                
                # if AUTResp is starting this frame...
                if AUTResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    AUTResp.frameNStart = frameN  # exact frame index
                    AUTResp.tStart = t  # local t and not account for scr refresh
                    AUTResp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(AUTResp, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    AUTResp.status = STARTED
                    AUTResp.setAutoDraw(True)
                
                # if AUTResp is active this frame...
                if AUTResp.status == STARTED:
                    # update params
                    AUTResp.setText(Resptext, log=False)
                
                # *AUTcueDisp* updates
                
                # if AUTcueDisp is starting this frame...
                if AUTcueDisp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    AUTcueDisp.frameNStart = frameN  # exact frame index
                    AUTcueDisp.tStart = t  # local t and not account for scr refresh
                    AUTcueDisp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(AUTcueDisp, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    AUTcueDisp.status = STARTED
                    AUTcueDisp.setAutoDraw(True)
                
                # if AUTcueDisp is active this frame...
                if AUTcueDisp.status == STARTED:
                    # update params
                    pass
                # Run 'Each Frame' code from AUTcode
                keys = event.getKeys()
                n=len(keys)
                i=0
                
                
                ###Timer#####
                Diff=globalClock.getTime()-startTime
                timeRemaining = AUTtime-math.floor(Diff/1) #this gives us a whole number for time 
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
                    AUTresps.finished = True
                    continueRoutine = False
                
                """
                Resptext2= ' ' + Resptext + '|'
                if Diff%2 > 1:
                    AUTResp_2.color="white"
                else:
                    AUTResp_2.color="black"
                """
                
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
                
                # *key_respAUT* updates
                waitOnFlip = False
                
                # if key_respAUT is starting this frame...
                if key_respAUT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_respAUT.frameNStart = frameN  # exact frame index
                    key_respAUT.tStart = t  # local t and not account for scr refresh
                    key_respAUT.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_respAUT, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    key_respAUT.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_respAUT.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_respAUT.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_respAUT.status == STARTED and not waitOnFlip:
                    theseKeys = key_respAUT.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
                    _key_respAUT_allKeys.extend(theseKeys)
                    if len(_key_respAUT_allKeys):
                        key_respAUT.keys = [key.name for key in _key_respAUT_allKeys]  # storing all keys
                        key_respAUT.rt = [key.rt for key in _key_respAUT_allKeys]
                        key_respAUT.duration = [key.duration for key in _key_respAUT_allKeys]
                
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
                        currentRoutine=AUT,
                    )
                    # skip the frame we paused on
                    continue
                
                # has a Component requested the Routine to end?
                if not continueRoutine:
                    AUT.forceEnded = routineForceEnded = True
                # has the Routine been forcibly ended?
                if AUT.forceEnded or routineForceEnded:
                    break
                # has every Component finished?
                continueRoutine = False
                for thisComponent in AUT.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "AUT" ---
            for thisComponent in AUT.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for AUT
            AUT.tStop = globalClock.getTime(format='float')
            AUT.tStopRefresh = tThisFlipGlobal
            thisExp.addData('AUT.stopped', AUT.tStop)
            # Run 'End Routine' code from AUTcode
            #extract the 1st and last key presses
            if len(key_respAUT.rt)>0:
                RT1stKP=key_respAUT.rt[0]
                RTLastKP=key_respAUT.rt[-1]
            
            #save the data for this trial
            thisExp.addData("AUTresp", Resptext)
            thisExp.addData("AUTRT1stKP", RT1stKP)
            thisExp.addData("AUTRTLastKP", RTLastKP)
            Resptext = ''
            
            
            # check responses
            if key_respAUT.keys in ['', [], None]:  # No response was made
                key_respAUT.keys = None
            AUTresps.addData('key_respAUT.keys',key_respAUT.keys)
            if key_respAUT.keys != None:  # we had a response
                AUTresps.addData('key_respAUT.rt', key_respAUT.rt)
                AUTresps.addData('key_respAUT.duration', key_respAUT.duration)
            # the Routine "AUT" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            # mark thisAUTresp as finished
            if hasattr(thisAUTresp, 'status'):
                thisAUTresp.status = FINISHED
            # if awaiting a pause, pause now
            if AUTresps.status == PAUSED:
                thisExp.status = PAUSED
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[globalClock], 
                )
                # once done pausing, restore running status
                AUTresps.status = STARTED
            thisExp.nextEntry()
            
        # completed 100 repeats of 'AUTresps'
        AUTresps.status = FINISHED
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # mark thisAUTtrial as finished
        if hasattr(thisAUTtrial, 'status'):
            thisAUTtrial.status = FINISHED
        # if awaiting a pause, pause now
        if AUTtrials.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            AUTtrials.status = STARTED
        thisExp.nextEntry()
        
    # completed 1 repeats of 'AUTtrials'
    AUTtrials.status = FINISHED
    
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
