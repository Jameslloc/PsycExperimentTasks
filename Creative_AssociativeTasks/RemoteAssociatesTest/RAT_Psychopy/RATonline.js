/****************** 
 * Ratonline *
 ******************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2026.1.3.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'RATonline';  // from the Builder filename that created this script
let expInfo = {
    'participant': '99',
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
flowScheduler.add(_settingsRoutineBegin());
flowScheduler.add(_settingsRoutineEachFrame());
flowScheduler.add(_settingsRoutineEnd());
flowScheduler.add(RAT_instruxRoutineBegin());
flowScheduler.add(RAT_instruxRoutineEachFrame());
flowScheduler.add(RAT_instruxRoutineEnd());
flowScheduler.add(RATinstrux_2RoutineBegin());
flowScheduler.add(RATinstrux_2RoutineEachFrame());
flowScheduler.add(RATinstrux_2RoutineEnd());
const RATpractrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(RATpractrialsLoopBegin(RATpractrialsLoopScheduler));
flowScheduler.add(RATpractrialsLoopScheduler);
flowScheduler.add(RATpractrialsLoopEnd);




flowScheduler.add(RATinstrux_3RoutineBegin());
flowScheduler.add(RATinstrux_3RoutineEachFrame());
flowScheduler.add(RATinstrux_3RoutineEnd());
const RATtrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(RATtrialsLoopBegin(RATtrialsLoopScheduler));
flowScheduler.add(RATtrialsLoopScheduler);
flowScheduler.add(RATtrialsLoopEnd);



flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'RATPraccues.xlsx', 'path': 'RATPraccues.xlsx'},
    {'name': 'RATcues.xlsx', 'path': 'RATcues.xlsx'},
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


var _settingsClock;
var CAPS;
var RATtime;
var charlim;
var RAT_instruxClock;
var RATintrux;
var EntertoContinue;
var key_resp_2;
var RATinstrux_2Clock;
var RATintrux2;
var EntertoContinue_2;
var key_resp_3;
var RATblankClock;
var text_5;
var RATClock;
var RATrespbox;
var InstruxRAT;
var RATResp;
var timer_1;
var key_resp;
var RATcueDisp;
var RATcueDisp_3;
var RATcueDisp_4;
var RATpracAnsClock;
var RATcueDisp_2;
var RATcueDisp_5;
var RATcueDisp_6;
var text;
var InstruxRAT_2;
var RATinstrux_3Clock;
var RATintrux3;
var EntertoContinue_3;
var key_resp_5;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "_settings"
  _settingsClock = new util.Clock();
  // Run 'Begin Experiment' code from code
  
  //var CAPS, countdownStarted;
  CAPS = false;
  
  function shuffleArray(array) {
      for (var i = array.length - 1; i > 0; i--) {
          var j = Math.floor(Math.random() * (i + 1));
          var temp = array[i];
          array[i] = array[j];
          array[j] = temp;
      }
  }
  
  document.body.style.cursor='none';
  RATtime=30;
  charlim=25;
  
  // Initialize components for Routine "RAT_instrux"
  RAT_instruxClock = new util.Clock();
  RATintrux = new visual.TextStim({
    win: psychoJS.window,
    name: 'RATintrux',
    text: "For the next task, you'll be shown 3 unrelated cue words, and you must find a 4th word that relates to all 3 words shown. See the example below:\n\n\nCues:\n\nCHOCOLATE       FORTUNE       TIN \n\n\nSolution:\n\nCOOKIE\n\n\nCookie is the correct answer because it relates to all 3 cue words.\n",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.1], draggable: false, height: 0.03,  wrapWidth: 1.2, ori: 0,
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
    pos: [0, (- 0.3)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "RATinstrux_2"
  RATinstrux_2Clock = new util.Clock();
  RATintrux2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'RATintrux2',
    text: 'You will have 30 seconds per problem to think of an answer.\n\nAs soon as you think you have the correct answer, type it in the box and press ENTER.\n\nYou will then see the next problem.\n\nPress ENTER now to see some practise trials.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.1], draggable: false, height: 0.03,  wrapWidth: 1.2, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  EntertoContinue_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'EntertoContinue_2',
    text: 'Press ENTER to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "RATblank"
  RATblankClock = new util.Clock();
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.15,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "RAT"
  RATClock = new util.Clock();
  RATrespbox = new visual.Rect ({
    win: psychoJS.window, name: 'RATrespbox', 
    width: [0.33, 0.13][0], height: [0.33, 0.13][1],
    ori: 0, 
    pos: [0, (- 0.2)], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color([1, 1, 1]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -1, 
    interpolate: true, 
  });
  
  InstruxRAT = new visual.TextStim({
    win: psychoJS.window,
    name: 'InstruxRAT',
    text: 'Think of a word that relates to all of these words:',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.25], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  RATResp = new visual.TextStim({
    win: psychoJS.window,
    name: 'RATResp',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.2)], draggable: false, height: 0.05,  wrapWidth: 0.3, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  timer_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'timer_1',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.5, (- 0.35)], draggable: false, height: 0.08,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  RATcueDisp = new visual.TextStim({
    win: psychoJS.window,
    name: 'RATcueDisp',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.07,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  RATcueDisp_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'RATcueDisp_3',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.3), 0], draggable: false, height: 0.07,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -7.0 
  });
  
  RATcueDisp_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'RATcueDisp_4',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0], draggable: false, height: 0.07,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -8.0 
  });
  
  // Initialize components for Routine "RATpracAns"
  RATpracAnsClock = new util.Clock();
  RATcueDisp_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'RATcueDisp_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.07,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  RATcueDisp_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'RATcueDisp_5',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.3), 0], draggable: false, height: 0.07,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  RATcueDisp_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'RATcueDisp_6',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0], draggable: false, height: 0.07,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.2)], draggable: false, height: 0.07,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  InstruxRAT_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'InstruxRAT_2',
    text: 'Correct Answer:',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], draggable: false, height: 0.07,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "RATinstrux_3"
  RATinstrux_3Clock = new util.Clock();
  RATintrux3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'RATintrux3',
    text: 'That is the end of the practise trials. There will now be 10 real trials. You will no longer be shown the correct answer.\n\nRemember: the solution word must relate to all 3 cue words.\n\nYou will have 30 seconds per problem to think of an answer.\n\nAs soon as you think you have the correct answer, type it in the box and press ENTER.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.1], draggable: false, height: 0.03,  wrapWidth: 1.2, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  EntertoContinue_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'EntertoContinue_3',
    text: 'Press ENTER to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var routineForceEnded;
var _settingsMaxDurationReached;
var _settingsMaxDuration;
var _settingsComponents;
function _settingsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine '_settings' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    _settingsClock.reset();
    routineTimer.reset();
    _settingsMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('_settings.started', globalClock.getTime());
    _settingsMaxDuration = null
    // keep track of which components have finished
    _settingsComponents = [];
    
    for (const thisComponent of _settingsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function _settingsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine '_settings' ---
    // get current time
    t = _settingsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
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
    for (const thisComponent of _settingsComponents)
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


function _settingsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine '_settings' ---
    for (const thisComponent of _settingsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('_settings.stopped', globalClock.getTime());
    // the Routine "_settings" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var RAT_instruxMaxDurationReached;
var _key_resp_2_allKeys;
var RAT_instruxMaxDuration;
var RAT_instruxComponents;
function RAT_instruxRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'RAT_instrux' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    RAT_instruxClock.reset();
    routineTimer.reset();
    RAT_instruxMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    psychoJS.experiment.addData('RAT_instrux.started', globalClock.getTime());
    RAT_instruxMaxDuration = null
    // keep track of which components have finished
    RAT_instruxComponents = [];
    RAT_instruxComponents.push(RATintrux);
    RAT_instruxComponents.push(EntertoContinue);
    RAT_instruxComponents.push(key_resp_2);
    
    for (const thisComponent of RAT_instruxComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function RAT_instruxRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'RAT_instrux' ---
    // get current time
    t = RAT_instruxClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *RATintrux* updates
    if (t >= 0.0 && RATintrux.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RATintrux.tStart = t;  // (not accounting for frame time here)
      RATintrux.frameNStart = frameN;  // exact frame index
      
      RATintrux.setAutoDraw(true);
    }
    
    
    // if RATintrux is active this frame...
    if (RATintrux.status === PsychoJS.Status.STARTED) {
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
    for (const thisComponent of RAT_instruxComponents)
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


function RAT_instruxRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'RAT_instrux' ---
    for (const thisComponent of RAT_instruxComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('RAT_instrux.stopped', globalClock.getTime());
    key_resp_2.stop();
    // the Routine "RAT_instrux" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var RATinstrux_2MaxDurationReached;
var _key_resp_3_allKeys;
var RATinstrux_2MaxDuration;
var RATinstrux_2Components;
function RATinstrux_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'RATinstrux_2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    RATinstrux_2Clock.reset();
    routineTimer.reset();
    RATinstrux_2MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    psychoJS.experiment.addData('RATinstrux_2.started', globalClock.getTime());
    RATinstrux_2MaxDuration = null
    // keep track of which components have finished
    RATinstrux_2Components = [];
    RATinstrux_2Components.push(RATintrux2);
    RATinstrux_2Components.push(EntertoContinue_2);
    RATinstrux_2Components.push(key_resp_3);
    
    for (const thisComponent of RATinstrux_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function RATinstrux_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'RATinstrux_2' ---
    // get current time
    t = RATinstrux_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *RATintrux2* updates
    if (t >= 0.0 && RATintrux2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RATintrux2.tStart = t;  // (not accounting for frame time here)
      RATintrux2.frameNStart = frameN;  // exact frame index
      
      RATintrux2.setAutoDraw(true);
    }
    
    
    // if RATintrux2 is active this frame...
    if (RATintrux2.status === PsychoJS.Status.STARTED) {
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
    
    
    // *key_resp_3* updates
    if (t >= 0.5 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }
    
    // if key_resp_3 is active this frame...
    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({
        keyList: typeof 'return' === 'string' ? ['return'] : 'return', 
        waitRelease: false
      });
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        key_resp_3.duration = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].duration;
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
    for (const thisComponent of RATinstrux_2Components)
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


function RATinstrux_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'RATinstrux_2' ---
    for (const thisComponent of RATinstrux_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('RATinstrux_2.stopped', globalClock.getTime());
    key_resp_3.stop();
    // the Routine "RATinstrux_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var RATpractrials;
function RATpractrialsLoopBegin(RATpractrialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    RATpractrials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'RATPraccues.xlsx',
      seed: undefined, name: 'RATpractrials'
    });
    psychoJS.experiment.addLoop(RATpractrials); // add the loop to the experiment
    currentLoop = RATpractrials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisRATpractrial of RATpractrials) {
      snapshot = RATpractrials.getSnapshot();
      RATpractrialsLoopScheduler.add(importConditions(snapshot));
      RATpractrialsLoopScheduler.add(RATblankRoutineBegin(snapshot));
      RATpractrialsLoopScheduler.add(RATblankRoutineEachFrame());
      RATpractrialsLoopScheduler.add(RATblankRoutineEnd(snapshot));
      RATpractrialsLoopScheduler.add(RATRoutineBegin(snapshot));
      RATpractrialsLoopScheduler.add(RATRoutineEachFrame());
      RATpractrialsLoopScheduler.add(RATRoutineEnd(snapshot));
      RATpractrialsLoopScheduler.add(RATpracAnsRoutineBegin(snapshot));
      RATpractrialsLoopScheduler.add(RATpracAnsRoutineEachFrame());
      RATpractrialsLoopScheduler.add(RATpracAnsRoutineEnd(snapshot));
      RATpractrialsLoopScheduler.add(RATpractrialsLoopEndIteration(RATpractrialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function RATpractrialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(RATpractrials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function RATpractrialsLoopEndIteration(scheduler, snapshot) {
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


var RATtrials;
function RATtrialsLoopBegin(RATtrialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    RATtrials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'RATcues.xlsx',
      seed: undefined, name: 'RATtrials'
    });
    psychoJS.experiment.addLoop(RATtrials); // add the loop to the experiment
    currentLoop = RATtrials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisRATtrial of RATtrials) {
      snapshot = RATtrials.getSnapshot();
      RATtrialsLoopScheduler.add(importConditions(snapshot));
      RATtrialsLoopScheduler.add(RATblankRoutineBegin(snapshot));
      RATtrialsLoopScheduler.add(RATblankRoutineEachFrame());
      RATtrialsLoopScheduler.add(RATblankRoutineEnd(snapshot));
      RATtrialsLoopScheduler.add(RATRoutineBegin(snapshot));
      RATtrialsLoopScheduler.add(RATRoutineEachFrame());
      RATtrialsLoopScheduler.add(RATRoutineEnd(snapshot));
      RATtrialsLoopScheduler.add(RATtrialsLoopEndIteration(RATtrialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function RATtrialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(RATtrials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function RATtrialsLoopEndIteration(scheduler, snapshot) {
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


var RATblankMaxDurationReached;
var CueString;
var RATblankMaxDuration;
var RATblankComponents;
function RATblankRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'RATblank' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    RATblankClock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    RATblankMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_5
    CueString = [Cue1, Cue2, Cue3];
    function shuffleArray(array) {
        for (var i = array.length - 1; i > 0; i--) {
            var j = Math.floor(Math.random() * (i + 1));
            var temp = array[i];
            array[i] = array[j];
            array[j] = temp;
        }
    }
    shuffleArray(CueString);
    
    psychoJS.experiment.addData('RATblank.started', globalClock.getTime());
    RATblankMaxDuration = null
    // keep track of which components have finished
    RATblankComponents = [];
    RATblankComponents.push(text_5);
    
    for (const thisComponent of RATblankComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function RATblankRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'RATblank' ---
    // get current time
    t = RATblankClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_5* updates
    if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index
      
      text_5.setAutoDraw(true);
    }
    
    
    // if text_5 is active this frame...
    if (text_5.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      text_5.tStop = t;  // not accounting for scr refresh
      text_5.frameNStop = frameN;  // exact frame index
      // update status
      text_5.status = PsychoJS.Status.FINISHED;
      text_5.setAutoDraw(false);
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
    for (const thisComponent of RATblankComponents)
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


function RATblankRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'RATblank' ---
    for (const thisComponent of RATblankComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('RATblank.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (RATblankMaxDurationReached) {
        RATblankClock.add(RATblankMaxDuration);
    } else {
        RATblankClock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var RATMaxDurationReached;
var shift_flag;
var Resptext;
var Key;
var RT1stKP;
var FirstKey;
var RTLastKP;
var startTime;
var _key_resp_allKeys;
var RATMaxDuration;
var RATComponents;
function RATRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'RAT' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    RATClock.reset();
    routineTimer.reset();
    RATMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from RATcode
    //is shift pressed?
    shift_flag = false;
    //#set response text as empty
    Resptext = "";
    RATResp.setText(Resptext)
    Key=undefined;
    
    //set 1st and last key press times
    RT1stKP=0;
    FirstKey=false;
    RTLastKP=0
    
    //start time for countdown/ trial timer
    startTime = globalClock.getTime();
    
    psychoJS.eventManager.clearKeys();
    
    
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    RATcueDisp.setText(CueString[0]);
    RATcueDisp_3.setText(CueString[1]);
    RATcueDisp_4.setText(CueString[2]);
    psychoJS.experiment.addData('RAT.started', globalClock.getTime());
    RATMaxDuration = null
    // keep track of which components have finished
    RATComponents = [];
    RATComponents.push(RATrespbox);
    RATComponents.push(InstruxRAT);
    RATComponents.push(RATResp);
    RATComponents.push(timer_1);
    RATComponents.push(key_resp);
    RATComponents.push(RATcueDisp);
    RATComponents.push(RATcueDisp_3);
    RATComponents.push(RATcueDisp_4);
    
    for (const thisComponent of RATComponents)
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
function RATRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'RAT' ---
    // get current time
    t = RATClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from RATcode
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
    
    // Timer
    Diff = (globalClock.getTime() - startTime);
    timeRemaining = (RATtime - Math.floor(Diff));
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
    
    // Text entry
    while ((i < n)) {
        if ((((keys[i] === "return") && (Resptext.length >= 1)) || (timeRemaining <= 0))) {
            RTLastKP=Diff;
            continueRoutine = false;
            break;
        } else if (((keys[i] === "space") && (Resptext.length < charlim))) {
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
        } else if (((keys[i] === "period") && (Resptext.length < charlim))) {
            Resptext += ".";
            i = (i + 1);
        } else if (((keys[i] === "minus") && (Resptext.length < charlim))) {
            Resptext += "-";
            i = (i + 1);
        } else if (((keys[i] === "comma") && (Resptext.length < charlim))) {
            Resptext += ",";
            i = (i + 1);
        } else if (_pj.in_es6(keys[i], ["lshift", "rshift"])) {
            shift_flag = true;
            i = (i + 1);
        } else if (((keys[i] === "semicolon") && (Resptext.length < charlim))) {
            if ((shift_flag === false)) {
                Resptext += ";";
            } else {
                Resptext += ":";
                shift_flag = false;
            }
            i = (i + 1);
        } else if (((keys[i] === "apostrophe") && (Resptext.length < charlim))) {
            if ((shift_flag === false)) {
                Resptext += "'";
            } else {
                Resptext += "\"";
                shift_flag = false;
            }
            i += 1;
        } else if (((keys[i] === "slash") && (Resptext.length < charlim))) {
            if ((shift_flag === false)) {
                Resptext += "/";
            } else {
                Resptext += "?";
                shift_flag = false;
            }
            i = (i + 1);
        } else if ((((keys[i] === "1") && (Resptext.length < charlim)) && (shift_flag === true))) {
                Resptext += "!";
                shift_flag = false;
                i = (i + 1);
        } else {
            if (((Resptext.length < charlim) && (keys[i].length === 1))) {
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
        continueRoutine = false;
    }
    
    
    // *RATrespbox* updates
    if (t >= 0.0 && RATrespbox.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RATrespbox.tStart = t;  // (not accounting for frame time here)
      RATrespbox.frameNStart = frameN;  // exact frame index
      
      RATrespbox.setAutoDraw(true);
    }
    
    
    // if RATrespbox is active this frame...
    if (RATrespbox.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *InstruxRAT* updates
    if (t >= 0.0 && InstruxRAT.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstruxRAT.tStart = t;  // (not accounting for frame time here)
      InstruxRAT.frameNStart = frameN;  // exact frame index
      
      InstruxRAT.setAutoDraw(true);
    }
    
    
    // if InstruxRAT is active this frame...
    if (InstruxRAT.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *RATResp* updates
    if (t >= 0 && RATResp.status === PsychoJS.Status.NOT_STARTED) {
      // update params
      RATResp.setText(Resptext, false);
      // keep track of start time/frame for later
      RATResp.tStart = t;  // (not accounting for frame time here)
      RATResp.frameNStart = frameN;  // exact frame index
      
      RATResp.setAutoDraw(true);
    }
    
    
    // if RATResp is active this frame...
    if (RATResp.status === PsychoJS.Status.STARTED) {
      // update params
      RATResp.setText(Resptext, false);
    }
    
    
    // *timer_1* updates
    if (t >= 0.0 && timer_1.status === PsychoJS.Status.NOT_STARTED) {
      // update params
      timer_1.setText(timeText, false);
      // keep track of start time/frame for later
      timer_1.tStart = t;  // (not accounting for frame time here)
      timer_1.frameNStart = frameN;  // exact frame index
      
      timer_1.setAutoDraw(true);
    }
    
    
    // if timer_1 is active this frame...
    if (timer_1.status === PsychoJS.Status.STARTED) {
      // update params
      timer_1.setText(timeText, false);
    }
    
    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
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
        keyList: typeof [] === 'string' ? [[]] : [], 
        waitRelease: false
      });
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys.map((key) => key.name);  // storing all keys
        key_resp.rt = _key_resp_allKeys.map((key) => key.rt);
        key_resp.duration = _key_resp_allKeys.map((key) => key.duration);
      }
    }
    
    
    // *RATcueDisp* updates
    if (t >= 0.0 && RATcueDisp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RATcueDisp.tStart = t;  // (not accounting for frame time here)
      RATcueDisp.frameNStart = frameN;  // exact frame index
      
      RATcueDisp.setAutoDraw(true);
    }
    
    
    // if RATcueDisp is active this frame...
    if (RATcueDisp.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *RATcueDisp_3* updates
    if (t >= 0.0 && RATcueDisp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RATcueDisp_3.tStart = t;  // (not accounting for frame time here)
      RATcueDisp_3.frameNStart = frameN;  // exact frame index
      
      RATcueDisp_3.setAutoDraw(true);
    }
    
    
    // if RATcueDisp_3 is active this frame...
    if (RATcueDisp_3.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *RATcueDisp_4* updates
    if (t >= 0.0 && RATcueDisp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RATcueDisp_4.tStart = t;  // (not accounting for frame time here)
      RATcueDisp_4.frameNStart = frameN;  // exact frame index
      
      RATcueDisp_4.setAutoDraw(true);
    }
    
    
    // if RATcueDisp_4 is active this frame...
    if (RATcueDisp_4.status === PsychoJS.Status.STARTED) {
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
    for (const thisComponent of RATComponents)
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


function RATRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'RAT' ---
    for (const thisComponent of RATComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('RAT.stopped', globalClock.getTime());
    // Run 'End Routine' code from RATcode
    if (key_resp.rt) {
        RT1stKP = key_resp.rt[0];
        RTLastKP = key_resp.rt.slice((- 1))[0];
    }
    
    psychoJS.experiment.addData("RATresp", Resptext)
    psychoJS.experiment.addData("RT1stKP", RT1stKP)
    psychoJS.experiment.addData("RTLastKP", RTLastKP)
    psychoJS.experiment.addData("RATcue", CueString)
    Resptext = ''
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        psychoJS.experiment.addData('key_resp.duration', key_resp.duration);
        }
    
    key_resp.stop();
    // the Routine "RAT" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var RATpracAnsMaxDurationReached;
var RATpracAnsMaxDuration;
var RATpracAnsComponents;
function RATpracAnsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'RATpracAns' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    RATpracAnsClock.reset(routineTimer.getTime());
    routineTimer.add(3.000000);
    RATpracAnsMaxDurationReached = false;
    // update component parameters for each repeat
    RATcueDisp_2.setText(CueString[0]);
    RATcueDisp_5.setText(CueString[1]);
    RATcueDisp_6.setText(CueString[2]);
    text.setText(Answer);
    psychoJS.experiment.addData('RATpracAns.started', globalClock.getTime());
    RATpracAnsMaxDuration = null
    // keep track of which components have finished
    RATpracAnsComponents = [];
    RATpracAnsComponents.push(RATcueDisp_2);
    RATpracAnsComponents.push(RATcueDisp_5);
    RATpracAnsComponents.push(RATcueDisp_6);
    RATpracAnsComponents.push(text);
    RATpracAnsComponents.push(InstruxRAT_2);
    
    for (const thisComponent of RATpracAnsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function RATpracAnsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'RATpracAns' ---
    // get current time
    t = RATpracAnsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *RATcueDisp_2* updates
    if (t >= 0.0 && RATcueDisp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RATcueDisp_2.tStart = t;  // (not accounting for frame time here)
      RATcueDisp_2.frameNStart = frameN;  // exact frame index
      
      RATcueDisp_2.setAutoDraw(true);
    }
    
    
    // if RATcueDisp_2 is active this frame...
    if (RATcueDisp_2.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (RATcueDisp_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      RATcueDisp_2.tStop = t;  // not accounting for scr refresh
      RATcueDisp_2.frameNStop = frameN;  // exact frame index
      // update status
      RATcueDisp_2.status = PsychoJS.Status.FINISHED;
      RATcueDisp_2.setAutoDraw(false);
    }
    
    
    // *RATcueDisp_5* updates
    if (t >= 0.0 && RATcueDisp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RATcueDisp_5.tStart = t;  // (not accounting for frame time here)
      RATcueDisp_5.frameNStart = frameN;  // exact frame index
      
      RATcueDisp_5.setAutoDraw(true);
    }
    
    
    // if RATcueDisp_5 is active this frame...
    if (RATcueDisp_5.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (RATcueDisp_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      RATcueDisp_5.tStop = t;  // not accounting for scr refresh
      RATcueDisp_5.frameNStop = frameN;  // exact frame index
      // update status
      RATcueDisp_5.status = PsychoJS.Status.FINISHED;
      RATcueDisp_5.setAutoDraw(false);
    }
    
    
    // *RATcueDisp_6* updates
    if (t >= 0.0 && RATcueDisp_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RATcueDisp_6.tStart = t;  // (not accounting for frame time here)
      RATcueDisp_6.frameNStart = frameN;  // exact frame index
      
      RATcueDisp_6.setAutoDraw(true);
    }
    
    
    // if RATcueDisp_6 is active this frame...
    if (RATcueDisp_6.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (RATcueDisp_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      RATcueDisp_6.tStop = t;  // not accounting for scr refresh
      RATcueDisp_6.frameNStop = frameN;  // exact frame index
      // update status
      RATcueDisp_6.status = PsychoJS.Status.FINISHED;
      RATcueDisp_6.setAutoDraw(false);
    }
    
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }
    
    
    // if text is active this frame...
    if (text.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      text.tStop = t;  // not accounting for scr refresh
      text.frameNStop = frameN;  // exact frame index
      // update status
      text.status = PsychoJS.Status.FINISHED;
      text.setAutoDraw(false);
    }
    
    
    // *InstruxRAT_2* updates
    if (t >= 0.0 && InstruxRAT_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstruxRAT_2.tStart = t;  // (not accounting for frame time here)
      InstruxRAT_2.frameNStart = frameN;  // exact frame index
      
      InstruxRAT_2.setAutoDraw(true);
    }
    
    
    // if InstruxRAT_2 is active this frame...
    if (InstruxRAT_2.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (InstruxRAT_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      InstruxRAT_2.tStop = t;  // not accounting for scr refresh
      InstruxRAT_2.frameNStop = frameN;  // exact frame index
      // update status
      InstruxRAT_2.status = PsychoJS.Status.FINISHED;
      InstruxRAT_2.setAutoDraw(false);
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
    for (const thisComponent of RATpracAnsComponents)
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


function RATpracAnsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'RATpracAns' ---
    for (const thisComponent of RATpracAnsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('RATpracAns.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (RATpracAnsMaxDurationReached) {
        RATpracAnsClock.add(RATpracAnsMaxDuration);
    } else {
        RATpracAnsClock.add(3.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var RATinstrux_3MaxDurationReached;
var _key_resp_5_allKeys;
var RATinstrux_3MaxDuration;
var RATinstrux_3Components;
function RATinstrux_3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'RATinstrux_3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    RATinstrux_3Clock.reset();
    routineTimer.reset();
    RATinstrux_3MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    psychoJS.experiment.addData('RATinstrux_3.started', globalClock.getTime());
    RATinstrux_3MaxDuration = null
    // keep track of which components have finished
    RATinstrux_3Components = [];
    RATinstrux_3Components.push(RATintrux3);
    RATinstrux_3Components.push(EntertoContinue_3);
    RATinstrux_3Components.push(key_resp_5);
    
    for (const thisComponent of RATinstrux_3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function RATinstrux_3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'RATinstrux_3' ---
    // get current time
    t = RATinstrux_3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *RATintrux3* updates
    if (t >= 0.0 && RATintrux3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RATintrux3.tStart = t;  // (not accounting for frame time here)
      RATintrux3.frameNStart = frameN;  // exact frame index
      
      RATintrux3.setAutoDraw(true);
    }
    
    
    // if RATintrux3 is active this frame...
    if (RATintrux3.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *EntertoContinue_3* updates
    if (t >= 0 && EntertoContinue_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      EntertoContinue_3.tStart = t;  // (not accounting for frame time here)
      EntertoContinue_3.frameNStart = frameN;  // exact frame index
      
      EntertoContinue_3.setAutoDraw(true);
    }
    
    
    // if EntertoContinue_3 is active this frame...
    if (EntertoContinue_3.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_resp_5* updates
    if (t >= 0.5 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }
    
    // if key_resp_5 is active this frame...
    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({
        keyList: typeof 'return' === 'string' ? ['return'] : 'return', 
        waitRelease: false
      });
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
        key_resp_5.duration = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].duration;
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
    for (const thisComponent of RATinstrux_3Components)
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


function RATinstrux_3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'RATinstrux_3' ---
    for (const thisComponent of RATinstrux_3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('RATinstrux_3.stopped', globalClock.getTime());
    key_resp_5.stop();
    // the Routine "RATinstrux_3" was not non-slip safe, so reset the non-slip timer
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
