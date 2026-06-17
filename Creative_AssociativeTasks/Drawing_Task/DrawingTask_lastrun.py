#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2026.1.3),
    on June 17, 2026, at 17:47
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
expName = 'DrawingTask2020'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': '1',
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
        originPath='C:\\Users\\james\\Documents\\ZDesktop\\PhD\\Misc\\Coding_Projects_for_LinkedIn\\Drawing Task\\DrawingTask_lastrun.py',
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
    
    # --- Initialize components for Routine "_settings" ---
    # Run 'Begin Experiment' code from code_7
    
    from PIL import Image
    import time
    import shutil          #copy & C
    import numpy as np
    win.mouseVisible = False
    
    #CHANGE DEBUG TO TRUE TO REDUCE TIMES OF EVERYTHING
    #SEE BELOW TO ADJUST TIMES MANUALLY
    SketchTime=3
    
    Pnum=int(float(expInfo['participant']))
    Prac=True
    
    
    ElaborationPhase=False
    
      # #############################
     # ### create dirs and folders ###
      # #############################
    
     # #### prepare directories, folders ###
    cwd = os.getcwd()
    log_dir = cwd + "\\log\\" + "P" + expInfo['participant']
    sketch_dir = log_dir + "\\draft"
    elab_dir = log_dir + "\\elab"
    
     # ### create UPN-individual log-path, log-directories and folders ###
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    if not os.path.exists(sketch_dir):
        os.makedirs(sketch_dir)
    
    if not os.path.exists(elab_dir):
        os.makedirs(elab_dir)
    
    # following is for drawing task to crop the image at the right dimensions
    H=win.size[1] #get the screen height
    W=win.size[0] #get the screen width
    #get pixel coordinates to crop drawings at after screenshot
    #image presented is 0.6 * height, so height * 0.4 is the amount of screen left
    Top=(H-(H*0.6))/2 #top coordinate of cropped image
    Bottom=H-Top #the bottom
    Left= (W-(H*0.6))/2#Width minus image size, divided by 2
    Right= W-Left
    
    # --- Initialize components for Routine "Fake_Trial" ---
    image_2 = visual.ImageStim(
        win=win,
        name='image_2', 
        image='Images/Image2.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=0,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)
    image_3 = visual.ImageStim(
        win=win,
        name='image_3', 
        image='Images/Image3.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=0,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-1.0)
    image_4 = visual.ImageStim(
        win=win,
        name='image_4', 
        image='Images/Image4.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=0,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-2.0)
    image_5 = visual.ImageStim(
        win=win,
        name='image_5', 
        image='Images/Image5.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=0,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-3.0)
    image_9 = visual.ImageStim(
        win=win,
        name='image_9', 
        image='Images/Image9.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=0,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-4.0)
    image_13 = visual.ImageStim(
        win=win,
        name='image_13', 
        image='Images/Image13.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=0,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-5.0)
    image_16 = visual.ImageStim(
        win=win,
        name='image_16', 
        image='Images/Image16.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=0,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-6.0)
    image_18 = visual.ImageStim(
        win=win,
        name='image_18', 
        image='Images/Image18.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=0,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-7.0)
    image_23 = visual.ImageStim(
        win=win,
        name='image_23', 
        image='Images/Image23.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=0,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-8.0)
    image_26 = visual.ImageStim(
        win=win,
        name='image_26', 
        image='Images/Image26.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=0,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-9.0)
    image_28 = visual.ImageStim(
        win=win,
        name='image_28', 
        image='Images/Image28.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=0,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-10.0)
    
    # --- Initialize components for Routine "DrawInstrux" ---
    DrawinstrucText = visual.TextStim(win=win, name='DrawinstrucText',
        text="The next task is a Drawing Task.\n\nIn the Drawing Task, you will be presented with a series of incomplete shapes. \n\nUsing each shape, you must produce the most creative drawing you can think of (the incomplete shape must be used as part of your drawing).\n\nYour drawings don't have to be pretty: they should simply show how creative and interesting your ideas are.",
        font='Arial',
        pos=[0, 0.1], draggable=False, height=0.045, wrapWidth=1.2, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_5 = keyboard.Keyboard(deviceName='defaultKeyboard')
    EnterToContinue_2 = visual.TextStim(win=win, name='EnterToContinue_2',
        text='Press ENTER to continue',
        font='Arial',
        pos=(0, -0.375), draggable=False, height=0.025, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "DrawInstrux_3" ---
    DrawinstrucText_3 = visual.TextStim(win=win, name='DrawinstrucText_3',
        text='You do not need to write a label for your drawing.\n\nYou will draw using the mouse, and will have 30 seconds to complete you drawing.\nPlease use all the time available to work on the most creative drawing you can.\n\nFirst, you will complete a 30 second practise drawing.',
        font='Arial',
        pos=[0, 0.1], draggable=False, height=0.045, wrapWidth=1.2, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp = keyboard.Keyboard(deviceName='defaultKeyboard')
    EnterToContinue = visual.TextStim(win=win, name='EnterToContinue',
        text='Press ENTER to begin the practise',
        font='Arial',
        pos=(0, -0.375), draggable=False, height=0.025, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "cross" ---
    polygon_4 = visual.ShapeStim(
        win=win, name='polygon_4', vertices='cross',units='height', 
        size=(0.05, 0.05),
        ori=0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
        opacity=1, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "DrawingTrial" ---
    image1 = visual.ImageStim(
        win=win,
        name='image1', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), draggable=False, size=(0.6, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)
    # Run 'Begin Experiment' code from code_3
    import math
    mymouse = event.Mouse(win=win)
    x, y = [None, None]
    mymouse.mouseClock = core.Clock()
    UndoButton = visual.Rect(
        win=win, name='UndoButton',units='height', 
        width=(0.24, 0.12)[0], height=(0.24, 0.12)[1],
        ori=0, pos=(-0.5, -0.35), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[1,1,1], fillColor='darkgray',
        opacity=1, depth=-3.0, interpolate=True)
    UndoText = visual.TextStim(win=win, name='UndoText',
        text='Undo Last',
        font='Arial',
        pos=(-0.5, -0.35), draggable=False, height=0.04, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-4.0);
    timer = visual.TextStim(win=win, name='timer',
        text='',
        font='Arial',
        pos=(0.5, -0.35), draggable=False, height=0.05, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "DrawInstrux_2" ---
    DrawinstrucText_2 = visual.TextStim(win=win, name='DrawinstrucText_2',
        text="That was the practise. Next are the 10 real trials.\n\nRemember- Using each shape, you must produce the most creative drawing you can think of (the incomplete shape must be used as part of your drawing).\n\nYour drawings don't have to be pretty: they should simply show how creative and interesting your ideas are.\n\nYou have 30 seconds per drawing, and should use all this time to work on your drawing.",
        font='Arial',
        pos=[0, 0.1], draggable=False, height=0.045, wrapWidth=1.2, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    EnterToContinue_3 = visual.TextStim(win=win, name='EnterToContinue_3',
        text='Press ENTER to begin',
        font='Arial',
        pos=(0, -0.375), draggable=False, height=0.025, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_2 = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "cross" ---
    polygon_4 = visual.ShapeStim(
        win=win, name='polygon_4', vertices='cross',units='height', 
        size=(0.05, 0.05),
        ori=0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
        opacity=1, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "DrawingTrial" ---
    image1 = visual.ImageStim(
        win=win,
        name='image1', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), draggable=False, size=(0.6, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)
    # Run 'Begin Experiment' code from code_3
    import math
    mymouse = event.Mouse(win=win)
    x, y = [None, None]
    mymouse.mouseClock = core.Clock()
    UndoButton = visual.Rect(
        win=win, name='UndoButton',units='height', 
        width=(0.24, 0.12)[0], height=(0.24, 0.12)[1],
        ori=0, pos=(-0.5, -0.35), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[1,1,1], fillColor='darkgray',
        opacity=1, depth=-3.0, interpolate=True)
    UndoText = visual.TextStim(win=win, name='UndoText',
        text='Undo Last',
        font='Arial',
        pos=(-0.5, -0.35), draggable=False, height=0.04, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-4.0);
    timer = visual.TextStim(win=win, name='timer',
        text='',
        font='Arial',
        pos=(0.5, -0.35), draggable=False, height=0.05, wrapWidth=None, ori=0, 
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
    
    # --- Prepare to start Routine "_settings" ---
    # create an object to store info about Routine _settings
    _settings = data.Routine(
        name='_settings',
        components=[],
    )
    _settings.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for _settings
    _settings.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    _settings.tStart = globalClock.getTime(format='float')
    _settings.status = STARTED
    thisExp.addData('_settings.started', _settings.tStart)
    _settings.maxDuration = None
    # keep track of which components have finished
    _settingsComponents = _settings.components
    for thisComponent in _settings.components:
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
    
    # --- Run Routine "_settings" ---
    thisExp.currentRoutine = _settings
    _settings.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
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
                currentRoutine=_settings,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            _settings.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if _settings.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in _settings.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "_settings" ---
    for thisComponent in _settings.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for _settings
    _settings.tStop = globalClock.getTime(format='float')
    _settings.tStopRefresh = tThisFlipGlobal
    thisExp.addData('_settings.stopped', _settings.tStop)
    thisExp.nextEntry()
    # the Routine "_settings" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Fake_Trial" ---
    # create an object to store info about Routine Fake_Trial
    Fake_Trial = data.Routine(
        name='Fake_Trial',
        components=[image_2, image_3, image_4, image_5, image_9, image_13, image_16, image_18, image_23, image_26, image_28],
    )
    Fake_Trial.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for Fake_Trial
    Fake_Trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Fake_Trial.tStart = globalClock.getTime(format='float')
    Fake_Trial.status = STARTED
    thisExp.addData('Fake_Trial.started', Fake_Trial.tStart)
    Fake_Trial.maxDuration = None
    # keep track of which components have finished
    Fake_TrialComponents = Fake_Trial.components
    for thisComponent in Fake_Trial.components:
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
    
    # --- Run Routine "Fake_Trial" ---
    thisExp.currentRoutine = Fake_Trial
    Fake_Trial.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_2* updates
        
        # if image_2 is starting this frame...
        if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_2.status = STARTED
            image_2.setAutoDraw(True)
        
        # if image_2 is active this frame...
        if image_2.status == STARTED:
            # update params
            pass
        
        # if image_2 is stopping this frame...
        if image_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                image_2.tStop = t  # not accounting for scr refresh
                image_2.tStopRefresh = tThisFlipGlobal  # on global time
                image_2.frameNStop = frameN  # exact frame index
                # update status
                image_2.status = FINISHED
                image_2.setAutoDraw(False)
        
        # *image_3* updates
        
        # if image_3 is starting this frame...
        if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_3.frameNStart = frameN  # exact frame index
            image_3.tStart = t  # local t and not account for scr refresh
            image_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_3.status = STARTED
            image_3.setAutoDraw(True)
        
        # if image_3 is active this frame...
        if image_3.status == STARTED:
            # update params
            pass
        
        # if image_3 is stopping this frame...
        if image_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                image_3.tStop = t  # not accounting for scr refresh
                image_3.tStopRefresh = tThisFlipGlobal  # on global time
                image_3.frameNStop = frameN  # exact frame index
                # update status
                image_3.status = FINISHED
                image_3.setAutoDraw(False)
        
        # *image_4* updates
        
        # if image_4 is starting this frame...
        if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_4.frameNStart = frameN  # exact frame index
            image_4.tStart = t  # local t and not account for scr refresh
            image_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_4.status = STARTED
            image_4.setAutoDraw(True)
        
        # if image_4 is active this frame...
        if image_4.status == STARTED:
            # update params
            pass
        
        # if image_4 is stopping this frame...
        if image_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_4.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                image_4.tStop = t  # not accounting for scr refresh
                image_4.tStopRefresh = tThisFlipGlobal  # on global time
                image_4.frameNStop = frameN  # exact frame index
                # update status
                image_4.status = FINISHED
                image_4.setAutoDraw(False)
        
        # *image_5* updates
        
        # if image_5 is starting this frame...
        if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_5.frameNStart = frameN  # exact frame index
            image_5.tStart = t  # local t and not account for scr refresh
            image_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_5.status = STARTED
            image_5.setAutoDraw(True)
        
        # if image_5 is active this frame...
        if image_5.status == STARTED:
            # update params
            pass
        
        # if image_5 is stopping this frame...
        if image_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_5.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                image_5.tStop = t  # not accounting for scr refresh
                image_5.tStopRefresh = tThisFlipGlobal  # on global time
                image_5.frameNStop = frameN  # exact frame index
                # update status
                image_5.status = FINISHED
                image_5.setAutoDraw(False)
        
        # *image_9* updates
        
        # if image_9 is starting this frame...
        if image_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_9.frameNStart = frameN  # exact frame index
            image_9.tStart = t  # local t and not account for scr refresh
            image_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_9, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_9.status = STARTED
            image_9.setAutoDraw(True)
        
        # if image_9 is active this frame...
        if image_9.status == STARTED:
            # update params
            pass
        
        # if image_9 is stopping this frame...
        if image_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_9.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                image_9.tStop = t  # not accounting for scr refresh
                image_9.tStopRefresh = tThisFlipGlobal  # on global time
                image_9.frameNStop = frameN  # exact frame index
                # update status
                image_9.status = FINISHED
                image_9.setAutoDraw(False)
        
        # *image_13* updates
        
        # if image_13 is starting this frame...
        if image_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_13.frameNStart = frameN  # exact frame index
            image_13.tStart = t  # local t and not account for scr refresh
            image_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_13.status = STARTED
            image_13.setAutoDraw(True)
        
        # if image_13 is active this frame...
        if image_13.status == STARTED:
            # update params
            pass
        
        # if image_13 is stopping this frame...
        if image_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_13.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                image_13.tStop = t  # not accounting for scr refresh
                image_13.tStopRefresh = tThisFlipGlobal  # on global time
                image_13.frameNStop = frameN  # exact frame index
                # update status
                image_13.status = FINISHED
                image_13.setAutoDraw(False)
        
        # *image_16* updates
        
        # if image_16 is starting this frame...
        if image_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_16.frameNStart = frameN  # exact frame index
            image_16.tStart = t  # local t and not account for scr refresh
            image_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_16, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_16.status = STARTED
            image_16.setAutoDraw(True)
        
        # if image_16 is active this frame...
        if image_16.status == STARTED:
            # update params
            pass
        
        # if image_16 is stopping this frame...
        if image_16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_16.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                image_16.tStop = t  # not accounting for scr refresh
                image_16.tStopRefresh = tThisFlipGlobal  # on global time
                image_16.frameNStop = frameN  # exact frame index
                # update status
                image_16.status = FINISHED
                image_16.setAutoDraw(False)
        
        # *image_18* updates
        
        # if image_18 is starting this frame...
        if image_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_18.frameNStart = frameN  # exact frame index
            image_18.tStart = t  # local t and not account for scr refresh
            image_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_18, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_18.status = STARTED
            image_18.setAutoDraw(True)
        
        # if image_18 is active this frame...
        if image_18.status == STARTED:
            # update params
            pass
        
        # if image_18 is stopping this frame...
        if image_18.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_18.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                image_18.tStop = t  # not accounting for scr refresh
                image_18.tStopRefresh = tThisFlipGlobal  # on global time
                image_18.frameNStop = frameN  # exact frame index
                # update status
                image_18.status = FINISHED
                image_18.setAutoDraw(False)
        
        # *image_23* updates
        
        # if image_23 is starting this frame...
        if image_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_23.frameNStart = frameN  # exact frame index
            image_23.tStart = t  # local t and not account for scr refresh
            image_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_23, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_23.status = STARTED
            image_23.setAutoDraw(True)
        
        # if image_23 is active this frame...
        if image_23.status == STARTED:
            # update params
            pass
        
        # if image_23 is stopping this frame...
        if image_23.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_23.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                image_23.tStop = t  # not accounting for scr refresh
                image_23.tStopRefresh = tThisFlipGlobal  # on global time
                image_23.frameNStop = frameN  # exact frame index
                # update status
                image_23.status = FINISHED
                image_23.setAutoDraw(False)
        
        # *image_26* updates
        
        # if image_26 is starting this frame...
        if image_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_26.frameNStart = frameN  # exact frame index
            image_26.tStart = t  # local t and not account for scr refresh
            image_26.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_26, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_26.status = STARTED
            image_26.setAutoDraw(True)
        
        # if image_26 is active this frame...
        if image_26.status == STARTED:
            # update params
            pass
        
        # if image_26 is stopping this frame...
        if image_26.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_26.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                image_26.tStop = t  # not accounting for scr refresh
                image_26.tStopRefresh = tThisFlipGlobal  # on global time
                image_26.frameNStop = frameN  # exact frame index
                # update status
                image_26.status = FINISHED
                image_26.setAutoDraw(False)
        
        # *image_28* updates
        
        # if image_28 is starting this frame...
        if image_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_28.frameNStart = frameN  # exact frame index
            image_28.tStart = t  # local t and not account for scr refresh
            image_28.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_28, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_28.status = STARTED
            image_28.setAutoDraw(True)
        
        # if image_28 is active this frame...
        if image_28.status == STARTED:
            # update params
            pass
        
        # if image_28 is stopping this frame...
        if image_28.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_28.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                image_28.tStop = t  # not accounting for scr refresh
                image_28.tStopRefresh = tThisFlipGlobal  # on global time
                image_28.frameNStop = frameN  # exact frame index
                # update status
                image_28.status = FINISHED
                image_28.setAutoDraw(False)
        
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
                currentRoutine=Fake_Trial,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            Fake_Trial.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if Fake_Trial.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in Fake_Trial.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Fake_Trial" ---
    for thisComponent in Fake_Trial.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Fake_Trial
    Fake_Trial.tStop = globalClock.getTime(format='float')
    Fake_Trial.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Fake_Trial.stopped', Fake_Trial.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if Fake_Trial.maxDurationReached:
        routineTimer.addTime(-Fake_Trial.maxDuration)
    elif Fake_Trial.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "DrawInstrux" ---
    # create an object to store info about Routine DrawInstrux
    DrawInstrux = data.Routine(
        name='DrawInstrux',
        components=[DrawinstrucText, key_resp_5, EnterToContinue_2],
    )
    DrawInstrux.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_5
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    # store start times for DrawInstrux
    DrawInstrux.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    DrawInstrux.tStart = globalClock.getTime(format='float')
    DrawInstrux.status = STARTED
    thisExp.addData('DrawInstrux.started', DrawInstrux.tStart)
    DrawInstrux.maxDuration = None
    # keep track of which components have finished
    DrawInstruxComponents = DrawInstrux.components
    for thisComponent in DrawInstrux.components:
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
    
    # --- Run Routine "DrawInstrux" ---
    thisExp.currentRoutine = DrawInstrux
    DrawInstrux.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *DrawinstrucText* updates
        
        # if DrawinstrucText is starting this frame...
        if DrawinstrucText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DrawinstrucText.frameNStart = frameN  # exact frame index
            DrawinstrucText.tStart = t  # local t and not account for scr refresh
            DrawinstrucText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DrawinstrucText, 'tStartRefresh')  # time at next scr refresh
            # update status
            DrawinstrucText.status = STARTED
            DrawinstrucText.setAutoDraw(True)
        
        # if DrawinstrucText is active this frame...
        if DrawinstrucText.status == STARTED:
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
            theseKeys = key_resp_5.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                key_resp_5.duration = _key_resp_5_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *EnterToContinue_2* updates
        
        # if EnterToContinue_2 is starting this frame...
        if EnterToContinue_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            EnterToContinue_2.frameNStart = frameN  # exact frame index
            EnterToContinue_2.tStart = t  # local t and not account for scr refresh
            EnterToContinue_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EnterToContinue_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            EnterToContinue_2.status = STARTED
            EnterToContinue_2.setAutoDraw(True)
        
        # if EnterToContinue_2 is active this frame...
        if EnterToContinue_2.status == STARTED:
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
                currentRoutine=DrawInstrux,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            DrawInstrux.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if DrawInstrux.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in DrawInstrux.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "DrawInstrux" ---
    for thisComponent in DrawInstrux.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for DrawInstrux
    DrawInstrux.tStop = globalClock.getTime(format='float')
    DrawInstrux.tStopRefresh = tThisFlipGlobal
    thisExp.addData('DrawInstrux.stopped', DrawInstrux.tStop)
    thisExp.nextEntry()
    # the Routine "DrawInstrux" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "DrawInstrux_3" ---
    # create an object to store info about Routine DrawInstrux_3
    DrawInstrux_3 = data.Routine(
        name='DrawInstrux_3',
        components=[DrawinstrucText_3, key_resp, EnterToContinue],
    )
    DrawInstrux_3.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_2
    Prac=1;
    # create starting attributes for key_resp
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # store start times for DrawInstrux_3
    DrawInstrux_3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    DrawInstrux_3.tStart = globalClock.getTime(format='float')
    DrawInstrux_3.status = STARTED
    thisExp.addData('DrawInstrux_3.started', DrawInstrux_3.tStart)
    DrawInstrux_3.maxDuration = None
    # keep track of which components have finished
    DrawInstrux_3Components = DrawInstrux_3.components
    for thisComponent in DrawInstrux_3.components:
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
    
    # --- Run Routine "DrawInstrux_3" ---
    thisExp.currentRoutine = DrawInstrux_3
    DrawInstrux_3.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *DrawinstrucText_3* updates
        
        # if DrawinstrucText_3 is starting this frame...
        if DrawinstrucText_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DrawinstrucText_3.frameNStart = frameN  # exact frame index
            DrawinstrucText_3.tStart = t  # local t and not account for scr refresh
            DrawinstrucText_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DrawinstrucText_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            DrawinstrucText_3.status = STARTED
            DrawinstrucText_3.setAutoDraw(True)
        
        # if DrawinstrucText_3 is active this frame...
        if DrawinstrucText_3.status == STARTED:
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
        
        # *EnterToContinue* updates
        
        # if EnterToContinue is starting this frame...
        if EnterToContinue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            EnterToContinue.frameNStart = frameN  # exact frame index
            EnterToContinue.tStart = t  # local t and not account for scr refresh
            EnterToContinue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EnterToContinue, 'tStartRefresh')  # time at next scr refresh
            # update status
            EnterToContinue.status = STARTED
            EnterToContinue.setAutoDraw(True)
        
        # if EnterToContinue is active this frame...
        if EnterToContinue.status == STARTED:
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
                currentRoutine=DrawInstrux_3,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            DrawInstrux_3.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if DrawInstrux_3.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in DrawInstrux_3.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "DrawInstrux_3" ---
    for thisComponent in DrawInstrux_3.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for DrawInstrux_3
    DrawInstrux_3.tStop = globalClock.getTime(format='float')
    DrawInstrux_3.tStopRefresh = tThisFlipGlobal
    thisExp.addData('DrawInstrux_3.stopped', DrawInstrux_3.tStop)
    thisExp.nextEntry()
    # the Routine "DrawInstrux_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "cross" ---
    # create an object to store info about Routine cross
    cross = data.Routine(
        name='cross',
        components=[polygon_4],
    )
    cross.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_12
    # ### Copy&Rename all TTCT(orig)-Files ###
    
    #Make filename for current drawing draft
    if Prac:
        CurrentDraw=str(2)
        pic_draft = "P" + expInfo['participant'] + "_" + CurrentDraw + "_Practise.png" 
        Prac=False
    #Copy the current stimulus image to the sketch directory, with new filename
    else:
        CurrentDraw=str(DrawStim)
        pic_draft = "P" + expInfo['participant'] + "_" + CurrentDraw + "_draft.png" 
    
    #Copy the current stimulus image to the sketch directory, with new filename
    stim="Images\Image"+CurrentDraw+".png"
    #label new draft with file destination
    Draw = sketch_dir + "\\" + pic_draft
    ShowIm=stim
    
    
    
    win.mouseVisible = True 
    # store start times for cross
    cross.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    cross.tStart = globalClock.getTime(format='float')
    cross.status = STARTED
    thisExp.addData('cross.started', cross.tStart)
    cross.maxDuration = None
    # keep track of which components have finished
    crossComponents = cross.components
    for thisComponent in cross.components:
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
    
    # --- Run Routine "cross" ---
    thisExp.currentRoutine = cross
    cross.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_4* updates
        
        # if polygon_4 is starting this frame...
        if polygon_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_4.frameNStart = frameN  # exact frame index
            polygon_4.tStart = t  # local t and not account for scr refresh
            polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            polygon_4.status = STARTED
            polygon_4.setAutoDraw(True)
        
        # if polygon_4 is active this frame...
        if polygon_4.status == STARTED:
            # update params
            pass
        
        # if polygon_4 is stopping this frame...
        if polygon_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_4.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                polygon_4.tStop = t  # not accounting for scr refresh
                polygon_4.tStopRefresh = tThisFlipGlobal  # on global time
                polygon_4.frameNStop = frameN  # exact frame index
                # update status
                polygon_4.status = FINISHED
                polygon_4.setAutoDraw(False)
        
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
                currentRoutine=cross,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            cross.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if cross.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in cross.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "cross" ---
    for thisComponent in cross.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for cross
    cross.tStop = globalClock.getTime(format='float')
    cross.tStopRefresh = tThisFlipGlobal
    thisExp.addData('cross.stopped', cross.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if cross.maxDurationReached:
        routineTimer.addTime(-cross.maxDuration)
    elif cross.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "DrawingTrial" ---
    # create an object to store info about Routine DrawingTrial
    DrawingTrial = data.Routine(
        name='DrawingTrial',
        components=[image1, mymouse, UndoButton, UndoText, timer],
    )
    DrawingTrial.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    image1.setImage(ShowIm)
    # Run 'Begin Routine' code from code_3
    
    ##### Prepare some variables ######
    polygon_vertex = [(0,0)]
    polygon_list = []
    
    Empty_shapes = 100
    for i in range(Empty_shapes):
        polygon_list.append(visual.ShapeStim(win, vertices=polygon_vertex,closeShape=False,
                                             fillColor=None, lineWidth=4, lineColor='black'))
    
    indx_shape = 0      # How many lines drawn so far
    Drawing = False #variable necessary to only add new lines when mouse stops being clicked, and to initialise
    #new lines when mouse is clicked again
    FirstUndoClick=True #this variable stops Undo from deleting multiple lines for as long as Undo button is clocked
    Exit=False # tells the task to take a screenshot and move on, when time limit reached
    
    # Prep some  Measurement vars
    Actionsincldel=0 #number of actions (lines drawn) including deleted ones
    ActionsNotincldel=0 #number of actions (lines drawn) not including deletes
    NoDels=0
    DrawRTs=[]
    DelRTs=[]
    LineLengths=[]
    LineDurations=[]
    
        
    ### GET TIMER READY ####
    startTime=globalClock.getTime()
    
    timeRemaining=SketchTime
    # setup some python lists for storing info about the mymouse
    gotValidClick = False  # until a click is received
    # store start times for DrawingTrial
    DrawingTrial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    DrawingTrial.tStart = globalClock.getTime(format='float')
    DrawingTrial.status = STARTED
    thisExp.addData('DrawingTrial.started', DrawingTrial.tStart)
    DrawingTrial.maxDuration = None
    # keep track of which components have finished
    DrawingTrialComponents = DrawingTrial.components
    for thisComponent in DrawingTrial.components:
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
    
    # --- Run Routine "DrawingTrial" ---
    thisExp.currentRoutine = DrawingTrial
    DrawingTrial.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image1* updates
        
        # if image1 is starting this frame...
        if image1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image1.frameNStart = frameN  # exact frame index
            image1.tStart = t  # local t and not account for scr refresh
            image1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image1, 'tStartRefresh')  # time at next scr refresh
            # update status
            image1.status = STARTED
            image1.setAutoDraw(True)
        
        # if image1 is active this frame...
        if image1.status == STARTED:
            # update params
            pass
        # Run 'Each Frame' code from code_3
        
           
        ###Timer#####
        Diff=globalClock.getTime()-startTime
        timeRemaining = SketchTime-math.floor(Diff) #this gives us a whole number for time 
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
        if timeRemaining<=0:
           Exit=True
        
        ######### START DRAWING TASK ##########
        # For some reason current polygon must be worked on individually, but isnt't saved back to polygon_list...
        polygon = polygon_list[indx_shape]
        ### DRAW LINES #####
        # If mouse is clicked, start/continue drawing
        if mymouse.isPressedIn(image1):
         # If mouse just clicked, start a new line (polygon), record RT
            if not Drawing:
                polygon_vertex = []
                Drawing = True #Prepare to recognise when mouse is not clicked
                DrawRTs.append(globalClock.getTime()-startTime) #record RTs
                LineStartTime=globalClock.getTime()
        
             # Update current polygon, with current mouse position
            polygon_vertex.append(mymouse.getPos())
            polygon.vertices = polygon_vertex
        elif Drawing: #Once mouse stops being clicked, move on to next polygon
                Drawing = False
                LineLengths.append(len(polygon.vertices))
                LineDurations.append(globalClock.getTime()-LineStartTime)
                indx_shape += 1 #move on to a new shape
                Actionsincldel +=1 #increase number of actions
                ActionsNotincldel +=1 #increase number of actions
        
        
            ### Undo Button #####
        if mymouse.isPressedIn(UndoButton) and FirstUndoClick and indx_shape>0: #So one click at a time will remove one shape
            UndoButton.fillColor='white'
            indx_shape -= 1 #go back to previous shape
            polygon = polygon_list[indx_shape]
            polygon.vertices = [(0,0)] #Set current polygon back to previous one, and return to an empty set
            FirstUndoClick=False
            NoDels+=1  #increase number of deletes
            DelRTs.append(globalClock.getTime()-startTime)#record RTs
            ActionsNotincldel -=1 #decrease number of actions
        elif not mymouse.isPressedIn(UndoButton):
            UndoButton.fillColor='darkgray'
            FirstUndoClick=True
        
        
        ### Update Screen with lines #####
        #Draw all images, and prep back image so screenshot works
        image1.draw()
        # Draw every polygon done so far
        for i_pol in range(indx_shape+1): #for all drawn shapes including current one
            polygon_list[i_pol].setAutoDraw(True)
            polygon_list[i_pol].draw()
        
        
        if Exit:
            #### Take screenshot and crop this screenshot to get image
            win.getMovieFrame(buffer='back')
            win.saveMovieFrames(Draw)
            img=Image.open(Draw)
            area = (Left,Top,Right,Bottom) 
            cropped_img = img.crop(area)
            img=cropped_img.save(Draw) #draft
            continueRoutine = False
        
        
        
        # *mymouse* updates
        
        # if mymouse is starting this frame...
        if mymouse.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            mymouse.frameNStart = frameN  # exact frame index
            mymouse.tStart = t  # local t and not account for scr refresh
            mymouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mymouse, 'tStartRefresh')  # time at next scr refresh
            # update status
            mymouse.status = STARTED
            mymouse.mouseClock.reset()
            prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
        
        # *UndoButton* updates
        
        # if UndoButton is starting this frame...
        if UndoButton.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            UndoButton.frameNStart = frameN  # exact frame index
            UndoButton.tStart = t  # local t and not account for scr refresh
            UndoButton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(UndoButton, 'tStartRefresh')  # time at next scr refresh
            # update status
            UndoButton.status = STARTED
            UndoButton.setAutoDraw(True)
        
        # if UndoButton is active this frame...
        if UndoButton.status == STARTED:
            # update params
            pass
        
        # *UndoText* updates
        
        # if UndoText is starting this frame...
        if UndoText.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            UndoText.frameNStart = frameN  # exact frame index
            UndoText.tStart = t  # local t and not account for scr refresh
            UndoText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(UndoText, 'tStartRefresh')  # time at next scr refresh
            # update status
            UndoText.status = STARTED
            UndoText.setAutoDraw(True)
        
        # if UndoText is active this frame...
        if UndoText.status == STARTED:
            # update params
            pass
        
        # *timer* updates
        
        # if timer is starting this frame...
        if timer.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            timer.frameNStart = frameN  # exact frame index
            timer.tStart = t  # local t and not account for scr refresh
            timer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timer, 'tStartRefresh')  # time at next scr refresh
            # update status
            timer.status = STARTED
            timer.setAutoDraw(True)
        
        # if timer is active this frame...
        if timer.status == STARTED:
            # update params
            timer.setText(timeText, log=False)
        
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
                currentRoutine=DrawingTrial,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            DrawingTrial.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if DrawingTrial.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in DrawingTrial.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "DrawingTrial" ---
    for thisComponent in DrawingTrial.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for DrawingTrial
    DrawingTrial.tStop = globalClock.getTime(format='float')
    DrawingTrial.tStopRefresh = tThisFlipGlobal
    thisExp.addData('DrawingTrial.stopped', DrawingTrial.tStop)
    # Run 'End Routine' code from code_3
    
    #Store vars in Excel
    if ElaborationPhase== True:
        thisExp.addData('DrawingName', pic_elab)
    else:
        thisExp.addData('DrawingName', pic_draft)
    thisExp.addData('ActionsNotincldel', ActionsNotincldel)
    thisExp.addData('Actionsincldel', Actionsincldel)
    thisExp.addData('NoDels', NoDels)
    thisExp.addData('DrawRTs', DrawRTs)
    thisExp.addData('DelRTs', DelRTs)
    thisExp.addData('LineLengths', LineLengths)
    thisExp.addData('LineDurations', LineDurations)
    
    for i_pol in range(len(polygon_list)):
        polygon_list[i_pol].setAutoDraw(False)
        addname="Line"+str(i_pol)
        thisExp.addData(addname, polygon_list[i_pol].vertices.tolist())
    thisExp.addData('StartImage', CurrentDraw)
    thisExp.addData('ActionsNotincldel', ActionsNotincldel)
    # store data for thisExp (ExperimentHandler)
    thisExp.nextEntry()
    # the Routine "DrawingTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "DrawInstrux_2" ---
    # create an object to store info about Routine DrawInstrux_2
    DrawInstrux_2 = data.Routine(
        name='DrawInstrux_2',
        components=[DrawinstrucText_2, EnterToContinue_3, key_resp_2],
    )
    DrawInstrux_2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_2
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # Run 'Begin Routine' code from code_5
    Prac=0;
    # store start times for DrawInstrux_2
    DrawInstrux_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    DrawInstrux_2.tStart = globalClock.getTime(format='float')
    DrawInstrux_2.status = STARTED
    thisExp.addData('DrawInstrux_2.started', DrawInstrux_2.tStart)
    DrawInstrux_2.maxDuration = None
    # keep track of which components have finished
    DrawInstrux_2Components = DrawInstrux_2.components
    for thisComponent in DrawInstrux_2.components:
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
    
    # --- Run Routine "DrawInstrux_2" ---
    thisExp.currentRoutine = DrawInstrux_2
    DrawInstrux_2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *DrawinstrucText_2* updates
        
        # if DrawinstrucText_2 is starting this frame...
        if DrawinstrucText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DrawinstrucText_2.frameNStart = frameN  # exact frame index
            DrawinstrucText_2.tStart = t  # local t and not account for scr refresh
            DrawinstrucText_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DrawinstrucText_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            DrawinstrucText_2.status = STARTED
            DrawinstrucText_2.setAutoDraw(True)
        
        # if DrawinstrucText_2 is active this frame...
        if DrawinstrucText_2.status == STARTED:
            # update params
            pass
        
        # *EnterToContinue_3* updates
        
        # if EnterToContinue_3 is starting this frame...
        if EnterToContinue_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            EnterToContinue_3.frameNStart = frameN  # exact frame index
            EnterToContinue_3.tStart = t  # local t and not account for scr refresh
            EnterToContinue_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EnterToContinue_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            EnterToContinue_3.status = STARTED
            EnterToContinue_3.setAutoDraw(True)
        
        # if EnterToContinue_3 is active this frame...
        if EnterToContinue_3.status == STARTED:
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2.started')
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
                currentRoutine=DrawInstrux_2,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            DrawInstrux_2.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if DrawInstrux_2.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in DrawInstrux_2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "DrawInstrux_2" ---
    for thisComponent in DrawInstrux_2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for DrawInstrux_2
    DrawInstrux_2.tStop = globalClock.getTime(format='float')
    DrawInstrux_2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('DrawInstrux_2.stopped', DrawInstrux_2.tStop)
    thisExp.nextEntry()
    # the Routine "DrawInstrux_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_draw = data.TrialHandler2(
        name='trials_draw',
        nReps=1, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('DrawStims.xlsx'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(trials_draw)  # add the loop to the experiment
    thisTrials_draw = trials_draw.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_draw.rgb)
    if thisTrials_draw != None:
        for paramName in thisTrials_draw:
            globals()[paramName] = thisTrials_draw[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrials_draw in trials_draw:
        trials_draw.status = STARTED
        if hasattr(thisTrials_draw, 'status'):
            thisTrials_draw.status = STARTED
        currentLoop = trials_draw
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_draw.rgb)
        if thisTrials_draw != None:
            for paramName in thisTrials_draw:
                globals()[paramName] = thisTrials_draw[paramName]
        
        # --- Prepare to start Routine "cross" ---
        # create an object to store info about Routine cross
        cross = data.Routine(
            name='cross',
            components=[polygon_4],
        )
        cross.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_12
        # ### Copy&Rename all TTCT(orig)-Files ###
        
        #Make filename for current drawing draft
        if Prac:
            CurrentDraw=str(2)
            pic_draft = "P" + expInfo['participant'] + "_" + CurrentDraw + "_Practise.png" 
            Prac=False
        #Copy the current stimulus image to the sketch directory, with new filename
        else:
            CurrentDraw=str(DrawStim)
            pic_draft = "P" + expInfo['participant'] + "_" + CurrentDraw + "_draft.png" 
        
        #Copy the current stimulus image to the sketch directory, with new filename
        stim="Images\Image"+CurrentDraw+".png"
        #label new draft with file destination
        Draw = sketch_dir + "\\" + pic_draft
        ShowIm=stim
        
        
        
        win.mouseVisible = True 
        # store start times for cross
        cross.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        cross.tStart = globalClock.getTime(format='float')
        cross.status = STARTED
        thisExp.addData('cross.started', cross.tStart)
        cross.maxDuration = None
        # keep track of which components have finished
        crossComponents = cross.components
        for thisComponent in cross.components:
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
        
        # --- Run Routine "cross" ---
        thisExp.currentRoutine = cross
        cross.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_draw, 'status') and thisTrials_draw.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon_4* updates
            
            # if polygon_4 is starting this frame...
            if polygon_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_4.frameNStart = frameN  # exact frame index
                polygon_4.tStart = t  # local t and not account for scr refresh
                polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                polygon_4.status = STARTED
                polygon_4.setAutoDraw(True)
            
            # if polygon_4 is active this frame...
            if polygon_4.status == STARTED:
                # update params
                pass
            
            # if polygon_4 is stopping this frame...
            if polygon_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon_4.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon_4.tStop = t  # not accounting for scr refresh
                    polygon_4.tStopRefresh = tThisFlipGlobal  # on global time
                    polygon_4.frameNStop = frameN  # exact frame index
                    # update status
                    polygon_4.status = FINISHED
                    polygon_4.setAutoDraw(False)
            
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
                    currentRoutine=cross,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                cross.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if cross.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in cross.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "cross" ---
        for thisComponent in cross.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for cross
        cross.tStop = globalClock.getTime(format='float')
        cross.tStopRefresh = tThisFlipGlobal
        thisExp.addData('cross.stopped', cross.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if cross.maxDurationReached:
            routineTimer.addTime(-cross.maxDuration)
        elif cross.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "DrawingTrial" ---
        # create an object to store info about Routine DrawingTrial
        DrawingTrial = data.Routine(
            name='DrawingTrial',
            components=[image1, mymouse, UndoButton, UndoText, timer],
        )
        DrawingTrial.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        image1.setImage(ShowIm)
        # Run 'Begin Routine' code from code_3
        
        ##### Prepare some variables ######
        polygon_vertex = [(0,0)]
        polygon_list = []
        
        Empty_shapes = 100
        for i in range(Empty_shapes):
            polygon_list.append(visual.ShapeStim(win, vertices=polygon_vertex,closeShape=False,
                                                 fillColor=None, lineWidth=4, lineColor='black'))
        
        indx_shape = 0      # How many lines drawn so far
        Drawing = False #variable necessary to only add new lines when mouse stops being clicked, and to initialise
        #new lines when mouse is clicked again
        FirstUndoClick=True #this variable stops Undo from deleting multiple lines for as long as Undo button is clocked
        Exit=False # tells the task to take a screenshot and move on, when time limit reached
        
        # Prep some  Measurement vars
        Actionsincldel=0 #number of actions (lines drawn) including deleted ones
        ActionsNotincldel=0 #number of actions (lines drawn) not including deletes
        NoDels=0
        DrawRTs=[]
        DelRTs=[]
        LineLengths=[]
        LineDurations=[]
        
            
        ### GET TIMER READY ####
        startTime=globalClock.getTime()
        
        timeRemaining=SketchTime
        # setup some python lists for storing info about the mymouse
        gotValidClick = False  # until a click is received
        # store start times for DrawingTrial
        DrawingTrial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        DrawingTrial.tStart = globalClock.getTime(format='float')
        DrawingTrial.status = STARTED
        thisExp.addData('DrawingTrial.started', DrawingTrial.tStart)
        DrawingTrial.maxDuration = None
        # keep track of which components have finished
        DrawingTrialComponents = DrawingTrial.components
        for thisComponent in DrawingTrial.components:
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
        
        # --- Run Routine "DrawingTrial" ---
        thisExp.currentRoutine = DrawingTrial
        DrawingTrial.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_draw, 'status') and thisTrials_draw.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image1* updates
            
            # if image1 is starting this frame...
            if image1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image1.frameNStart = frameN  # exact frame index
                image1.tStart = t  # local t and not account for scr refresh
                image1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image1, 'tStartRefresh')  # time at next scr refresh
                # update status
                image1.status = STARTED
                image1.setAutoDraw(True)
            
            # if image1 is active this frame...
            if image1.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from code_3
            
               
            ###Timer#####
            Diff=globalClock.getTime()-startTime
            timeRemaining = SketchTime-math.floor(Diff) #this gives us a whole number for time 
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
            if timeRemaining<=0:
               Exit=True
            
            ######### START DRAWING TASK ##########
            # For some reason current polygon must be worked on individually, but isnt't saved back to polygon_list...
            polygon = polygon_list[indx_shape]
            ### DRAW LINES #####
            # If mouse is clicked, start/continue drawing
            if mymouse.isPressedIn(image1):
             # If mouse just clicked, start a new line (polygon), record RT
                if not Drawing:
                    polygon_vertex = []
                    Drawing = True #Prepare to recognise when mouse is not clicked
                    DrawRTs.append(globalClock.getTime()-startTime) #record RTs
                    LineStartTime=globalClock.getTime()
            
                 # Update current polygon, with current mouse position
                polygon_vertex.append(mymouse.getPos())
                polygon.vertices = polygon_vertex
            elif Drawing: #Once mouse stops being clicked, move on to next polygon
                    Drawing = False
                    LineLengths.append(len(polygon.vertices))
                    LineDurations.append(globalClock.getTime()-LineStartTime)
                    indx_shape += 1 #move on to a new shape
                    Actionsincldel +=1 #increase number of actions
                    ActionsNotincldel +=1 #increase number of actions
            
            
                ### Undo Button #####
            if mymouse.isPressedIn(UndoButton) and FirstUndoClick and indx_shape>0: #So one click at a time will remove one shape
                UndoButton.fillColor='white'
                indx_shape -= 1 #go back to previous shape
                polygon = polygon_list[indx_shape]
                polygon.vertices = [(0,0)] #Set current polygon back to previous one, and return to an empty set
                FirstUndoClick=False
                NoDels+=1  #increase number of deletes
                DelRTs.append(globalClock.getTime()-startTime)#record RTs
                ActionsNotincldel -=1 #decrease number of actions
            elif not mymouse.isPressedIn(UndoButton):
                UndoButton.fillColor='darkgray'
                FirstUndoClick=True
            
            
            ### Update Screen with lines #####
            #Draw all images, and prep back image so screenshot works
            image1.draw()
            # Draw every polygon done so far
            for i_pol in range(indx_shape+1): #for all drawn shapes including current one
                polygon_list[i_pol].setAutoDraw(True)
                polygon_list[i_pol].draw()
            
            
            if Exit:
                #### Take screenshot and crop this screenshot to get image
                win.getMovieFrame(buffer='back')
                win.saveMovieFrames(Draw)
                img=Image.open(Draw)
                area = (Left,Top,Right,Bottom) 
                cropped_img = img.crop(area)
                img=cropped_img.save(Draw) #draft
                continueRoutine = False
            
            
            
            # *mymouse* updates
            
            # if mymouse is starting this frame...
            if mymouse.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                mymouse.frameNStart = frameN  # exact frame index
                mymouse.tStart = t  # local t and not account for scr refresh
                mymouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mymouse, 'tStartRefresh')  # time at next scr refresh
                # update status
                mymouse.status = STARTED
                mymouse.mouseClock.reset()
                prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
            
            # *UndoButton* updates
            
            # if UndoButton is starting this frame...
            if UndoButton.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                UndoButton.frameNStart = frameN  # exact frame index
                UndoButton.tStart = t  # local t and not account for scr refresh
                UndoButton.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(UndoButton, 'tStartRefresh')  # time at next scr refresh
                # update status
                UndoButton.status = STARTED
                UndoButton.setAutoDraw(True)
            
            # if UndoButton is active this frame...
            if UndoButton.status == STARTED:
                # update params
                pass
            
            # *UndoText* updates
            
            # if UndoText is starting this frame...
            if UndoText.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                UndoText.frameNStart = frameN  # exact frame index
                UndoText.tStart = t  # local t and not account for scr refresh
                UndoText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(UndoText, 'tStartRefresh')  # time at next scr refresh
                # update status
                UndoText.status = STARTED
                UndoText.setAutoDraw(True)
            
            # if UndoText is active this frame...
            if UndoText.status == STARTED:
                # update params
                pass
            
            # *timer* updates
            
            # if timer is starting this frame...
            if timer.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                timer.frameNStart = frameN  # exact frame index
                timer.tStart = t  # local t and not account for scr refresh
                timer.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(timer, 'tStartRefresh')  # time at next scr refresh
                # update status
                timer.status = STARTED
                timer.setAutoDraw(True)
            
            # if timer is active this frame...
            if timer.status == STARTED:
                # update params
                timer.setText(timeText, log=False)
            
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
                    currentRoutine=DrawingTrial,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                DrawingTrial.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if DrawingTrial.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in DrawingTrial.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "DrawingTrial" ---
        for thisComponent in DrawingTrial.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for DrawingTrial
        DrawingTrial.tStop = globalClock.getTime(format='float')
        DrawingTrial.tStopRefresh = tThisFlipGlobal
        thisExp.addData('DrawingTrial.stopped', DrawingTrial.tStop)
        # Run 'End Routine' code from code_3
        
        #Store vars in Excel
        if ElaborationPhase== True:
            thisExp.addData('DrawingName', pic_elab)
        else:
            thisExp.addData('DrawingName', pic_draft)
        thisExp.addData('ActionsNotincldel', ActionsNotincldel)
        thisExp.addData('Actionsincldel', Actionsincldel)
        thisExp.addData('NoDels', NoDels)
        thisExp.addData('DrawRTs', DrawRTs)
        thisExp.addData('DelRTs', DelRTs)
        thisExp.addData('LineLengths', LineLengths)
        thisExp.addData('LineDurations', LineDurations)
        
        for i_pol in range(len(polygon_list)):
            polygon_list[i_pol].setAutoDraw(False)
            addname="Line"+str(i_pol)
            thisExp.addData(addname, polygon_list[i_pol].vertices.tolist())
        thisExp.addData('StartImage', CurrentDraw)
        thisExp.addData('ActionsNotincldel', ActionsNotincldel)
        # store data for trials_draw (TrialHandler)
        # the Routine "DrawingTrial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisTrials_draw as finished
        if hasattr(thisTrials_draw, 'status'):
            thisTrials_draw.status = FINISHED
        # if awaiting a pause, pause now
        if trials_draw.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            trials_draw.status = STARTED
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_draw'
    trials_draw.status = FINISHED
    
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
