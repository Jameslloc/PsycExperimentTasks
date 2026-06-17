/********************** 
 * Verbalfluency *
 **********************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2026.1.3.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'VerbalFluency';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
    'session': '001',
};
let PILOTING = util.getUrlParameters().has('__pilotToken');

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(VFinstruxRoutineBegin());
flowScheduler.add(VFinstruxRoutineEachFrame());
flowScheduler.add(VFinstruxRoutineEnd());
flowScheduler.add(VFinstrux_2RoutineBegin());
flowScheduler.add(VFinstrux_2RoutineEachFrame());
flowScheduler.add(VFinstrux_2RoutineEnd());
const VFtrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(VFtrialsLoopBegin(VFtrialsLoopScheduler));
flowScheduler.add(VFtrialsLoopScheduler);
flowScheduler.add(VFtrialsLoopEnd);






flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'VFconds.xlsx', 'path': 'VFconds.xlsx'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2026.1.3';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var VFinstruxClock;
var instrux;
var EntertoContinue;
var key_resp_2;
var VFinstrux_2Clock;
var intrux_2;
var EntertoContinue_2;
var key_resp;
var getreadyVFClock;
var InstruxVF_2;
var text_2;
var VFClock;
var VFrespbox;
var InstruxVF;
var VFResp;
var VFcueDisp;
var countdownStarted;
var CAPS;
var timeText_1;
var key_respVF;
var NextTrialVFClock;
var keeptracknumind;
var intrux_14;
var key_resp_20;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "VFinstrux"
  VFinstruxClock = new util.Clock();
  instrux = new visual.TextStim({
    win: psychoJS.window,
    name: 'instrux',
    text: 'Well done so far.\n\nIn the next task, you will be given a category, and you must type as many items from that category as you can. \n\nFor instance, if the category is "words beginning with F" you should type as many words that begin with F as you can.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.1], draggable: false, height: 0.035,  wrapWidth: 1.2, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  EntertoContinue = new visual.TextStim({
    win: psychoJS.window,
    name: 'EntertoContinue',
    text: 'Press ENTER to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.35)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "VFinstrux_2"
  VFinstrux_2Clock = new util.Clock();
  intrux_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'intrux_2',
    text: 'Do not enter the same item twice, or the same root word with different suffixes (e.g., if you list "fox", do not list "foxes" in the same round).\n\nYou will have 60 seconds to type as many items from the category as you can. Press ENTER after typing each word.\n\nThere will be 3 categories in total.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.1], draggable: false, height: 0.035,  wrapWidth: 1.2, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  EntertoContinue_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'EntertoContinue_2',
    text: 'Press ENTER to begin',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.35)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "getreadyVF"
  getreadyVFClock = new util.Clock();
  InstruxVF_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'InstruxVF_2',
    text: 'Type as many words as you can that are in the category shown. Press ENTER after each word. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.25], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.15,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "VF"
  VFClock = new util.Clock();
  VFrespbox = new visual.Rect ({
    win: psychoJS.window, name: 'VFrespbox', 
    width: [0.45, 0.17][0], height: [0.45, 0.17][1],
    ori: 0, 
    pos: [0, (- 0.22)], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color([1, 1, 1]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: 0, 
    interpolate: true, 
  });
  
  InstruxVF = new visual.TextStim({
    win: psychoJS.window,
    name: 'InstruxVF',
    text: 'Type as many words as you can that are in the category shown. Press ENTER after each word. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.25], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  VFResp = new visual.TextStim({
    win: psychoJS.window,
    name: 'VFResp',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.22)], draggable: false, height: 0.05,  wrapWidth: 0.48, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  VFcueDisp = new visual.TextStim({
    win: psychoJS.window,
    name: 'VFcueDisp',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.08,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Run 'Begin Experiment' code from VFcode
  
  var CAPS, countdownStarted;
  countdownStarted = false;
  CAPS = false;
  
  timeText_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'timeText_1',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.5, (- 0.3)], draggable: false, height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  key_respVF = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "NextTrialVF"
  NextTrialVFClock = new util.Clock();
  // Run 'Begin Experiment' code from code_13
  keeptracknumind = 0;
  
  intrux_14 = new visual.TextStim({
    win: psychoJS.window,
    name: 'intrux_14',
    text: 'Press ENTER to begin the next trial.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.035,  wrapWidth: 1.2, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_20 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var routineForceEnded;
var VFinstruxMaxDurationReached;
var _key_resp_2_allKeys;
var VFtime;
var VFinstruxMaxDuration;
var VFinstruxComponents;
function VFinstruxRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'VFinstrux' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    VFinstruxClock.reset();
    routineTimer.reset();
    VFinstruxMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // Run 'Begin Routine' code from code
    document.body.style.cursor='none';
    VFtime=60
    psychoJS.experiment.addData('VFinstrux.started', globalClock.getTime());
    VFinstruxMaxDuration = null
    // keep track of which components have finished
    VFinstruxComponents = [];
    VFinstruxComponents.push(instrux);
    VFinstruxComponents.push(EntertoContinue);
    VFinstruxComponents.push(key_resp_2);
    
    for (const thisComponent of VFinstruxComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function VFinstruxRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'VFinstrux' ---
    // get current time
    t = VFinstruxClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instrux* updates
    if (t >= 0.0 && instrux.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instrux.tStart = t;  // (not accounting for frame time here)
      instrux.frameNStart = frameN;  // exact frame index
      
      instrux.setAutoDraw(true);
    }
    
    
    // if instrux is active this frame...
    if (instrux.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *EntertoContinue* updates
    if (t >= 0 && EntertoContinue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      EntertoContinue.tStart = t;  // (not accounting for frame time here)
      EntertoContinue.frameNStart = frameN;  // exact frame index
      
      EntertoContinue.setAutoDraw(true);
    }
    
    
    // if EntertoContinue is active this frame...
    if (EntertoContinue.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_resp_2* updates
    if (t >= 0.5 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }
    
    // if key_resp_2 is active this frame...
    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({
        keyList: typeof 'return' === 'string' ? ['return'] : 'return', 
        waitRelease: false
      });
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        key_resp_2.duration = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    document.body.style.cursor='none';
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of VFinstruxComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function VFinstruxRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'VFinstrux' ---
    for (const thisComponent of VFinstruxComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('VFinstrux.stopped', globalClock.getTime());
    key_resp_2.stop();
    // the Routine "VFinstrux" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var VFinstrux_2MaxDurationReached;
var _key_resp_allKeys;
var VFinstrux_2MaxDuration;
var VFinstrux_2Components;
function VFinstrux_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'VFinstrux_2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    VFinstrux_2Clock.reset();
    routineTimer.reset();
    VFinstrux_2MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    psychoJS.experiment.addData('VFinstrux_2.started', globalClock.getTime());
    VFinstrux_2MaxDuration = null
    // keep track of which components have finished
    VFinstrux_2Components = [];
    VFinstrux_2Components.push(intrux_2);
    VFinstrux_2Components.push(EntertoContinue_2);
    VFinstrux_2Components.push(key_resp);
    
    for (const thisComponent of VFinstrux_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function VFinstrux_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'VFinstrux_2' ---
    // get current time
    t = VFinstrux_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *intrux_2* updates
    if (t >= 0.0 && intrux_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      intrux_2.tStart = t;  // (not accounting for frame time here)
      intrux_2.frameNStart = frameN;  // exact frame index
      
      intrux_2.setAutoDraw(true);
    }
    
    
    // if intrux_2 is active this frame...
    if (intrux_2.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *EntertoContinue_2* updates
    if (t >= 0 && EntertoContinue_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      EntertoContinue_2.tStart = t;  // (not accounting for frame time here)
      EntertoContinue_2.frameNStart = frameN;  // exact frame index
      
      EntertoContinue_2.setAutoDraw(true);
    }
    
    
    // if EntertoContinue_2 is active this frame...
    if (EntertoContinue_2.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_resp* updates
    if (t >= 0.5 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }
    
    // if key_resp is active this frame...
    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({
        keyList: typeof 'return' === 'string' ? ['return'] : 'return', 
        waitRelease: false
      });
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        key_resp.duration = _key_resp_allKeys[_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of VFinstrux_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function VFinstrux_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'VFinstrux_2' ---
    for (const thisComponent of VFinstrux_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('VFinstrux_2.stopped', globalClock.getTime());
    key_resp.stop();
    // the Routine "VFinstrux_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var VFtrials;
function VFtrialsLoopBegin(VFtrialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    VFtrials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'VFconds.xlsx',
      seed: undefined, name: 'VFtrials'
    });
    psychoJS.experiment.addLoop(VFtrials); // add the loop to the experiment
    currentLoop = VFtrials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisVFtrial of VFtrials) {
      snapshot = VFtrials.getSnapshot();
      VFtrialsLoopScheduler.add(importConditions(snapshot));
      VFtrialsLoopScheduler.add(getreadyVFRoutineBegin(snapshot));
      VFtrialsLoopScheduler.add(getreadyVFRoutineEachFrame());
      VFtrialsLoopScheduler.add(getreadyVFRoutineEnd(snapshot));
      const VFrespsLoopScheduler = new Scheduler(psychoJS);
      VFtrialsLoopScheduler.add(VFrespsLoopBegin(VFrespsLoopScheduler, snapshot));
      VFtrialsLoopScheduler.add(VFrespsLoopScheduler);
      VFtrialsLoopScheduler.add(VFrespsLoopEnd);
      VFtrialsLoopScheduler.add(NextTrialVFRoutineBegin(snapshot));
      VFtrialsLoopScheduler.add(NextTrialVFRoutineEachFrame());
      VFtrialsLoopScheduler.add(NextTrialVFRoutineEnd(snapshot));
      VFtrialsLoopScheduler.add(VFtrialsLoopEndIteration(VFtrialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var VFresps;
function VFrespsLoopBegin(VFrespsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    VFresps = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 100, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'VFresps'
    });
    psychoJS.experiment.addLoop(VFresps); // add the loop to the experiment
    currentLoop = VFresps;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisVFresp of VFresps) {
      snapshot = VFresps.getSnapshot();
      VFrespsLoopScheduler.add(importConditions(snapshot));
      VFrespsLoopScheduler.add(VFRoutineBegin(snapshot));
      VFrespsLoopScheduler.add(VFRoutineEachFrame());
      VFrespsLoopScheduler.add(VFRoutineEnd(snapshot));
      VFrespsLoopScheduler.add(VFrespsLoopEndIteration(VFrespsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function VFrespsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(VFresps);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function VFrespsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function VFtrialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(VFtrials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function VFtrialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var getreadyVFMaxDurationReached;
var getreadyVFMaxDuration;
var getreadyVFComponents;
function getreadyVFRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'getreadyVF' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    getreadyVFClock.reset(routineTimer.getTime());
    routineTimer.add(3.500000);
    getreadyVFMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('getreadyVF.started', globalClock.getTime());
    getreadyVFMaxDuration = null
    // keep track of which components have finished
    getreadyVFComponents = [];
    getreadyVFComponents.push(InstruxVF_2);
    getreadyVFComponents.push(text_2);
    
    for (const thisComponent of getreadyVFComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function getreadyVFRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'getreadyVF' ---
    // get current time
    t = getreadyVFClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *InstruxVF_2* updates
    if (t >= 0.5 && InstruxVF_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstruxVF_2.tStart = t;  // (not accounting for frame time here)
      InstruxVF_2.frameNStart = frameN;  // exact frame index
      
      InstruxVF_2.setAutoDraw(true);
    }
    
    
    // if InstruxVF_2 is active this frame...
    if (InstruxVF_2.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (InstruxVF_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      InstruxVF_2.tStop = t;  // not accounting for scr refresh
      InstruxVF_2.frameNStop = frameN;  // exact frame index
      // update status
      InstruxVF_2.status = PsychoJS.Status.FINISHED;
      InstruxVF_2.setAutoDraw(false);
    }
    
    
    // *text_2* updates
    if (t >= 0.5 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }
    
    
    // if text_2 is active this frame...
    if (text_2.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      text_2.tStop = t;  // not accounting for scr refresh
      text_2.frameNStop = frameN;  // exact frame index
      // update status
      text_2.status = PsychoJS.Status.FINISHED;
      text_2.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of getreadyVFComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function getreadyVFRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'getreadyVF' ---
    for (const thisComponent of getreadyVFComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('getreadyVF.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (getreadyVFMaxDurationReached) {
        getreadyVFClock.add(getreadyVFMaxDuration);
    } else {
        getreadyVFClock.add(3.500000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var VFMaxDurationReached;
var shift_flag;
var Resptext;
var Key;
var RT1stKP;
var RTLastKP;
var startTime;
var _key_respVF_allKeys;
var VFMaxDuration;
var VFComponents;
function VFRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'VF' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    VFClock.reset();
    routineTimer.reset();
    VFMaxDurationReached = false;
    // update component parameters for each repeat
    VFcueDisp.setText(VFcond);
    // Run 'Begin Routine' code from VFcode
    shift_flag = false;
    Resptext = "";
    Key=undefined;
    VFResp.setText(Resptext)
    RT1stKP=0;
    
    RTLastKP=0
    
    if ((! countdownStarted)) {
        startTime = globalClock.getTime();
        countdownStarted = true;
    }
    
    psychoJS.eventManager.clearKeys();
    
    
    key_respVF.keys = undefined;
    key_respVF.rt = undefined;
    _key_respVF_allKeys = [];
    psychoJS.experiment.addData('VF.started', globalClock.getTime());
    VFMaxDuration = null
    // keep track of which components have finished
    VFComponents = [];
    VFComponents.push(VFrespbox);
    VFComponents.push(InstruxVF);
    VFComponents.push(VFResp);
    VFComponents.push(VFcueDisp);
    VFComponents.push(timeText_1);
    VFComponents.push(key_respVF);
    
    for (const thisComponent of VFComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var _pj;
var keys;
var n;
var i;
var Diff;
var timeRemaining;
var Minutes;
var Seconds;
var minstring;
var secstring;
var timeText;
function VFRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'VF' ---
    // get current time
    t = VFClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *VFrespbox* updates
    if (t >= 0.0 && VFrespbox.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      VFrespbox.tStart = t;  // (not accounting for frame time here)
      VFrespbox.frameNStart = frameN;  // exact frame index
      
      VFrespbox.setAutoDraw(true);
    }
    
    
    // if VFrespbox is active this frame...
    if (VFrespbox.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *InstruxVF* updates
    if (t >= 0.0 && InstruxVF.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstruxVF.tStart = t;  // (not accounting for frame time here)
      InstruxVF.frameNStart = frameN;  // exact frame index
      
      InstruxVF.setAutoDraw(true);
    }
    
    
    // if InstruxVF is active this frame...
    if (InstruxVF.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *VFResp* updates
    if (t >= 0.0 && VFResp.status === PsychoJS.Status.NOT_STARTED) {
      // update params
      VFResp.setText(Resptext, false);
      // keep track of start time/frame for later
      VFResp.tStart = t;  // (not accounting for frame time here)
      VFResp.frameNStart = frameN;  // exact frame index
      
      VFResp.setAutoDraw(true);
    }
    
    
    // if VFResp is active this frame...
    if (VFResp.status === PsychoJS.Status.STARTED) {
      // update params
      VFResp.setText(Resptext, false);
    }
    
    
    // *VFcueDisp* updates
    if (t >= 0.0 && VFcueDisp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      VFcueDisp.tStart = t;  // (not accounting for frame time here)
      VFcueDisp.frameNStart = frameN;  // exact frame index
      
      VFcueDisp.setAutoDraw(true);
    }
    
    
    // if VFcueDisp is active this frame...
    if (VFcueDisp.status === PsychoJS.Status.STARTED) {
    }
    
    // Run 'Each Frame' code from VFcode
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    keys = psychoJS.eventManager.getKeys();
    n = keys.length;
    i = 0;
    
    Diff = (globalClock.getTime() - startTime);
    timeRemaining = (VFtime - Math.floor((Diff / 1)));
    Minutes = Number.parseInt((timeRemaining / 60.0));
    Seconds = Number.parseInt((timeRemaining - (Minutes * 60.0)));
    if ((Minutes < 10)) {
        minstring = ("0" + Minutes.toString());
    } else {
        minstring = Minutes.toString();
    }
    if ((Seconds < 10)) {
        secstring = ("0" + Seconds.toString());
    } else {
        secstring = Seconds.toString();
    }
    timeText = ((minstring + ":") + secstring);
    
    while ((i < n)) {
        if ((((keys[i] === "return") && (Resptext.length >= 1)) || (timeRemaining <= 0))) {
            continueRoutine = false;
            break;
        } else if (((keys[i] === "space") && (Resptext.length < 80))) {
            Resptext += " ";
            i = (i + 1);
        } else if ((keys[i] === "backspace")) {
            Resptext = Resptext.slice(0, (- 1));
            i = (i + 1);
        } else if ((keys[i] === "capslock")) {
            if ((CAPS === true)) {
                CAPS = false;
            } else if ((CAPS === false)) {
                CAPS = true;
            }
            i = (i + 1);
        } else if (((keys[i] === "period") && (Resptext.length < 80))) {
            Resptext += ".";
            i = (i + 1);
        } else if (((keys[i] === "minus") && (Resptext.length < 80))) {
            Resptext += "-";
            i = (i + 1);
        } else if (((keys[i] === "comma") && (Resptext.length < 80))) {
            Resptext += ",";
            i = (i + 1);
        } else if (_pj.in_es6(keys[i], ["lshift", "rshift"])) {
            shift_flag = true;
            i = (i + 1);
        } else if (((keys[i] === "semicolon") && (Resptext.length < 80))) {
            if ((shift_flag === false)) {
                Resptext += ";";
            } else {
                Resptext += ":";
                shift_flag = false;
            }
            i = (i + 1);
        } else if (((keys[i] === "apostrophe") && (Resptext.length < 80))) {
            if ((shift_flag === false)) {
                Resptext += "'";
            } else {
                Resptext += "\"";
                shift_flag = false;
            }
            i += 1;
        } else if (((keys[i] === "slash") && (Resptext.length < 80))) {
            if ((shift_flag === false)) {
                Resptext += "/";
            } else {
                Resptext += "?";
                shift_flag = false;
            }
            i = (i + 1);
        } else if ((((keys[i] === "1") && (Resptext.length < 80)) && (shift_flag === true))) {
                Resptext += "!";
                shift_flag = false;
                i = (i + 1);
        } else {
            if (((Resptext.length < 80) && (keys[i].length === 1))) {
                Key = keys[i];
                if ((CAPS || shift_flag)) {
                    Resptext += Key.toUpperCase();
                    shift_flag = false;
                } else {
                    Resptext += Key;
                }
             }
             Key = undefined;
             i = (i + 1);
        }
    }
    
    if ((timeRemaining <= 0)) {
        VFresps.finished = true;
        continueRoutine = false;
        countdownStarted = false;
    }
    
    
    // *timeText_1* updates
    if (t >= 0.0 && timeText_1.status === PsychoJS.Status.NOT_STARTED) {
      // update params
      timeText_1.setText(timeText, false);
      // keep track of start time/frame for later
      timeText_1.tStart = t;  // (not accounting for frame time here)
      timeText_1.frameNStart = frameN;  // exact frame index
      
      timeText_1.setAutoDraw(true);
    }
    
    
    // if timeText_1 is active this frame...
    if (timeText_1.status === PsychoJS.Status.STARTED) {
      // update params
      timeText_1.setText(timeText, false);
    }
    
    
    // *key_respVF* updates
    if (t >= 0.0 && key_respVF.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_respVF.tStart = t;  // (not accounting for frame time here)
      key_respVF.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_respVF.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_respVF.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_respVF.clearEvents(); });
    }
    
    // if key_respVF is active this frame...
    if (key_respVF.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_respVF.getKeys({
        keyList: typeof [] === 'string' ? [[]] : [], 
        waitRelease: false
      });
      _key_respVF_allKeys = _key_respVF_allKeys.concat(theseKeys);
      if (_key_respVF_allKeys.length > 0) {
        key_respVF.keys = _key_respVF_allKeys.map((key) => key.name);  // storing all keys
        key_respVF.rt = _key_respVF_allKeys.map((key) => key.rt);
        key_respVF.duration = _key_respVF_allKeys.map((key) => key.duration);
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of VFComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function VFRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'VF' ---
    for (const thisComponent of VFComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('VF.stopped', globalClock.getTime());
    // Run 'End Routine' code from VFcode
    if (key_respVF.rt) {
        RT1stKP = key_respVF.rt[0];
        RTLastKP = key_respVF.rt.slice((- 1))[0];
    }
    
    psychoJS.experiment.addData("VFresp", Resptext)
    psychoJS.experiment.addData("VFRT1stKP", RT1stKP)
    psychoJS.experiment.addData("VFRTLastKP", RTLastKP)
    psychoJS.experiment.addData("VFcue", VFcond)
    Resptext = ''
    
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_respVF.corr, level);
    }
    psychoJS.experiment.addData('key_respVF.keys', key_respVF.keys);
    if (typeof key_respVF.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_respVF.rt', key_respVF.rt);
        psychoJS.experiment.addData('key_respVF.duration', key_respVF.duration);
        }
    
    key_respVF.stop();
    // the Routine "VF" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var NextTrialVFMaxDurationReached;
var blahtext;
var _key_resp_20_allKeys;
var NextTrialVFMaxDuration;
var NextTrialVFComponents;
function NextTrialVFRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'NextTrialVF' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    NextTrialVFClock.reset();
    routineTimer.reset();
    NextTrialVFMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_13
    keeptracknumind += 1;
    if ((keeptracknumind === 3)) {
        continueRoutine = false;
    }
    blahtext = keeptracknumind.toString();
    
    key_resp_20.keys = undefined;
    key_resp_20.rt = undefined;
    _key_resp_20_allKeys = [];
    psychoJS.experiment.addData('NextTrialVF.started', globalClock.getTime());
    NextTrialVFMaxDuration = null
    // keep track of which components have finished
    NextTrialVFComponents = [];
    NextTrialVFComponents.push(intrux_14);
    NextTrialVFComponents.push(key_resp_20);
    
    for (const thisComponent of NextTrialVFComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function NextTrialVFRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'NextTrialVF' ---
    // get current time
    t = NextTrialVFClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *intrux_14* updates
    if (t >= 0.0 && intrux_14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      intrux_14.tStart = t;  // (not accounting for frame time here)
      intrux_14.frameNStart = frameN;  // exact frame index
      
      intrux_14.setAutoDraw(true);
    }
    
    
    // if intrux_14 is active this frame...
    if (intrux_14.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_resp_20* updates
    if (t >= 0.5 && key_resp_20.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_20.tStart = t;  // (not accounting for frame time here)
      key_resp_20.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_20.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_20.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_20.clearEvents(); });
    }
    
    // if key_resp_20 is active this frame...
    if (key_resp_20.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_20.getKeys({
        keyList: typeof 'return' === 'string' ? ['return'] : 'return', 
        waitRelease: false
      });
      _key_resp_20_allKeys = _key_resp_20_allKeys.concat(theseKeys);
      if (_key_resp_20_allKeys.length > 0) {
        key_resp_20.keys = _key_resp_20_allKeys[_key_resp_20_allKeys.length - 1].name;  // just the last key pressed
        key_resp_20.rt = _key_resp_20_allKeys[_key_resp_20_allKeys.length - 1].rt;
        key_resp_20.duration = _key_resp_20_allKeys[_key_resp_20_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of NextTrialVFComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function NextTrialVFRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'NextTrialVF' ---
    for (const thisComponent of NextTrialVFComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('NextTrialVF.stopped', globalClock.getTime());
    key_resp_20.stop();
    // the Routine "NextTrialVF" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
