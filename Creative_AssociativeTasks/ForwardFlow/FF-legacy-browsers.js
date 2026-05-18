/*********** 
 * Ff *
 ***********/


// store info about the experiment session:
let expName = 'FF';  // from the Builder filename that created this script
let expInfo = {
    'participant': '1',
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
flowScheduler.add(FFinstruxRoutineBegin());
flowScheduler.add(FFinstruxRoutineEachFrame());
flowScheduler.add(FFinstruxRoutineEnd());
flowScheduler.add(FFinstrux_2RoutineBegin());
flowScheduler.add(FFinstrux_2RoutineEachFrame());
flowScheduler.add(FFinstrux_2RoutineEnd());
flowScheduler.add(FFblankRoutineBegin());
flowScheduler.add(FFblankRoutineEachFrame());
flowScheduler.add(FFblankRoutineEnd());
const FFpractiseLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(FFpractiseLoopBegin(FFpractiseLoopScheduler));
flowScheduler.add(FFpractiseLoopScheduler);
flowScheduler.add(FFpractiseLoopEnd);


flowScheduler.add(FFinstrux_4RoutineBegin());
flowScheduler.add(FFinstrux_4RoutineEachFrame());
flowScheduler.add(FFinstrux_4RoutineEnd());
const FFtrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(FFtrialsLoopBegin(FFtrialsLoopScheduler));
flowScheduler.add(FFtrialsLoopScheduler);
flowScheduler.add(FFtrialsLoopEnd);






flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'FFcues.xlsx', 'path': 'FFcues.xlsx'},
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


var FFinstruxClock;
var intrux;
var EntertoContinue;
var key_resp_2;
var FFinstrux_2Clock;
var intrux_2;
var EntertoContinue_2;
var key_resp_3;
var FFblankClock;
var text_5;
var FFClock;
var CAPS;
var firsttrial;
var FFcueword;
var FFcueDisp;
var polygon;
var key_respFF;
var FFrespDisp;
var FFinstrux_4Clock;
var intrux_4;
var EntertoContinue_4;
var key_resp_5;
var NextFFInstruxClock;
var intrux_5;
var EntertoContinue_5;
var key_resp_9;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "FFinstrux"
  FFinstruxClock = new util.Clock();
  intrux = new visual.TextStim({
    win: psychoJS.window,
    name: 'intrux',
    text: 'In the next task you will be shown a single word, and you must type the next word that follows from it in your mind. \n\nOnce you type the word, it will be shown on the screen. You must then think of another word that follows from this word, and so on.\n\nKeep typing the next word that comes to mind after the previous word until the trial ends (after 20 words).\n\nPlease type only single words, and avoid saying proper nouns such as names, cities, or brands (e.g., “John”, “Paris”, “Nike”).',
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
  
  // Initialize components for Routine "FFinstrux_2"
  FFinstrux_2Clock = new util.Clock();
  intrux_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'intrux_2',
    text: "First, you will complete a small practise.\n\nYou'll be shown a single word, and have to think of the first word that comes to mind, and type it. Then you type the next word that follows from that word, until you make a small chain of associations.",
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
    text: 'Press ENTER to begin.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.35)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "FFblank"
  FFblankClock = new util.Clock();
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.15,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "FF"
  FFClock = new util.Clock();
  // Run 'Begin Experiment' code from FFcode_3
  
  var CAPS, firsttrial;
  CAPS = false;
  firsttrial = true;
  FFcueword=" "
  FFcueDisp = new visual.TextStim({
    win: psychoJS.window,
    name: 'FFcueDisp',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.1], draggable: false, height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  polygon = new visual.Rect ({
    win: psychoJS.window, name: 'polygon', 
    width: [0.45, 0.17][0], height: [0.45, 0.17][1],
    ori: 0, 
    pos: [0, (- 0.2)], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color([1, 1, 1]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -2, 
    interpolate: true, 
  });
  
  key_respFF = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  FFrespDisp = new visual.TextStim({
    win: psychoJS.window,
    name: 'FFrespDisp',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.2)], draggable: false, height: 0.075,  wrapWidth: 0.4, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "FFinstrux_4"
  FFinstrux_4Clock = new util.Clock();
  intrux_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'intrux_4',
    text: 'That is the end of the practise. Next are the real trials, which will be 19 words long. There will be 3 trials in total.\n\nRemember: you will be shown a single word, and you must type the next word that follows in your mind. Keep typing the next word that comes to mind after the previous word until the trial ends.\n\nPlease type only single words, and avoid saying proper nouns such as names, cities, or brands (e.g., “John”, “Paris”, “Nike”).',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.1], draggable: false, height: 0.035,  wrapWidth: 1.2, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  EntertoContinue_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'EntertoContinue_4',
    text: 'Press SPACE to begin',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.35)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "NextFFInstrux"
  NextFFInstruxClock = new util.Clock();
  intrux_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'intrux_5',
    text: '\nPress SPACE to see another starting word',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.035,  wrapWidth: 0.7, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  EntertoContinue_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'EntertoContinue_5',
    text: 'Press SPACE to begin',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.35)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_9 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var routineForceEnded;
var FFinstruxMaxDurationReached;
var _key_resp_2_allKeys;
var FFPrac;
var FFinstruxMaxDuration;
var FFinstruxComponents;
function FFinstruxRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'FFinstrux' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    FFinstruxClock.reset();
    routineTimer.reset();
    FFinstruxMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // Run 'Begin Routine' code from code
    document.body.style.cursor='none';
    FFPrac=true
    psychoJS.experiment.addData('FFinstrux.started', globalClock.getTime());
    FFinstruxMaxDuration = null
    // keep track of which components have finished
    FFinstruxComponents = [];
    FFinstruxComponents.push(intrux);
    FFinstruxComponents.push(EntertoContinue);
    FFinstruxComponents.push(key_resp_2);
    
    FFinstruxComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function FFinstruxRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'FFinstrux' ---
    // get current time
    t = FFinstruxClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *intrux* updates
    if (t >= 0.0 && intrux.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      intrux.tStart = t;  // (not accounting for frame time here)
      intrux.frameNStart = frameN;  // exact frame index
      
      intrux.setAutoDraw(true);
    }
    
    
    // if intrux is active this frame...
    if (intrux.status === PsychoJS.Status.STARTED) {
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
    FFinstruxComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FFinstruxRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'FFinstrux' ---
    FFinstruxComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('FFinstrux.stopped', globalClock.getTime());
    key_resp_2.stop();
    // the Routine "FFinstrux" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var FFinstrux_2MaxDurationReached;
var _key_resp_3_allKeys;
var FFinstrux_2MaxDuration;
var FFinstrux_2Components;
function FFinstrux_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'FFinstrux_2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    FFinstrux_2Clock.reset();
    routineTimer.reset();
    FFinstrux_2MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    psychoJS.experiment.addData('FFinstrux_2.started', globalClock.getTime());
    FFinstrux_2MaxDuration = null
    // keep track of which components have finished
    FFinstrux_2Components = [];
    FFinstrux_2Components.push(intrux_2);
    FFinstrux_2Components.push(EntertoContinue_2);
    FFinstrux_2Components.push(key_resp_3);
    
    FFinstrux_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function FFinstrux_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'FFinstrux_2' ---
    // get current time
    t = FFinstrux_2Clock.getTime();
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
    FFinstrux_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FFinstrux_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'FFinstrux_2' ---
    FFinstrux_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('FFinstrux_2.stopped', globalClock.getTime());
    key_resp_3.stop();
    // the Routine "FFinstrux_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var FFblankMaxDurationReached;
var FFblankMaxDuration;
var FFblankComponents;
function FFblankRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'FFblank' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    FFblankClock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    FFblankMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_4
    firsttrial = true;
    
    psychoJS.experiment.addData('FFblank.started', globalClock.getTime());
    FFblankMaxDuration = null
    // keep track of which components have finished
    FFblankComponents = [];
    FFblankComponents.push(text_5);
    
    FFblankComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function FFblankRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'FFblank' ---
    // get current time
    t = FFblankClock.getTime();
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
    FFblankComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FFblankRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'FFblank' ---
    FFblankComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('FFblank.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (FFblankMaxDurationReached) {
        FFblankClock.add(FFblankMaxDuration);
    } else {
        FFblankClock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var FFpractise;
function FFpractiseLoopBegin(FFpractiseLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    FFpractise = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 6, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'FFpractise'
    });
    psychoJS.experiment.addLoop(FFpractise); // add the loop to the experiment
    currentLoop = FFpractise;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    FFpractise.forEach(function() {
      snapshot = FFpractise.getSnapshot();
    
      FFpractiseLoopScheduler.add(importConditions(snapshot));
      FFpractiseLoopScheduler.add(FFRoutineBegin(snapshot));
      FFpractiseLoopScheduler.add(FFRoutineEachFrame());
      FFpractiseLoopScheduler.add(FFRoutineEnd(snapshot));
      FFpractiseLoopScheduler.add(FFpractiseLoopEndIteration(FFpractiseLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function FFpractiseLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(FFpractise);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function FFpractiseLoopEndIteration(scheduler, snapshot) {
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


var FFtrials;
function FFtrialsLoopBegin(FFtrialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    FFtrials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'FFcues.xlsx',
      seed: undefined, name: 'FFtrials'
    });
    psychoJS.experiment.addLoop(FFtrials); // add the loop to the experiment
    currentLoop = FFtrials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    FFtrials.forEach(function() {
      snapshot = FFtrials.getSnapshot();
    
      FFtrialsLoopScheduler.add(importConditions(snapshot));
      FFtrialsLoopScheduler.add(FFblankRoutineBegin(snapshot));
      FFtrialsLoopScheduler.add(FFblankRoutineEachFrame());
      FFtrialsLoopScheduler.add(FFblankRoutineEnd(snapshot));
      const FFrespsLoopScheduler = new Scheduler(psychoJS);
      FFtrialsLoopScheduler.add(FFrespsLoopBegin(FFrespsLoopScheduler, snapshot));
      FFtrialsLoopScheduler.add(FFrespsLoopScheduler);
      FFtrialsLoopScheduler.add(FFrespsLoopEnd);
      FFtrialsLoopScheduler.add(NextFFInstruxRoutineBegin(snapshot));
      FFtrialsLoopScheduler.add(NextFFInstruxRoutineEachFrame());
      FFtrialsLoopScheduler.add(NextFFInstruxRoutineEnd(snapshot));
      FFtrialsLoopScheduler.add(FFtrialsLoopEndIteration(FFtrialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var FFresps;
function FFrespsLoopBegin(FFrespsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    FFresps = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 19, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'FFresps'
    });
    psychoJS.experiment.addLoop(FFresps); // add the loop to the experiment
    currentLoop = FFresps;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    FFresps.forEach(function() {
      snapshot = FFresps.getSnapshot();
    
      FFrespsLoopScheduler.add(importConditions(snapshot));
      FFrespsLoopScheduler.add(FFRoutineBegin(snapshot));
      FFrespsLoopScheduler.add(FFRoutineEachFrame());
      FFrespsLoopScheduler.add(FFRoutineEnd(snapshot));
      FFrespsLoopScheduler.add(FFrespsLoopEndIteration(FFrespsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function FFrespsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(FFresps);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function FFrespsLoopEndIteration(scheduler, snapshot) {
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


async function FFtrialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(FFtrials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function FFtrialsLoopEndIteration(scheduler, snapshot) {
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


var FFMaxDurationReached;
var shift_flag;
var Resptext;
var Key;
var charlim;
var RT1stKP;
var RTLastKP;
var _key_respFF_allKeys;
var FFMaxDuration;
var FFComponents;
function FFRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'FF' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    FFClock.reset();
    routineTimer.reset();
    FFMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from FFcode_3
    //is shift pressed?
    shift_flag = false;
    //#set response text as empty
    Resptext = "";
    FFrespDisp.setText(Resptext)
    Key=undefined;
    
    charlim=30
    
    //set 1st and last key press times
    RT1stKP=0;
    RTLastKP=0
    
    psychoJS.eventManager.clearKeys();
    
    if (FFPrac==true) {
        FFcueword="snow";
    } 
    if (FFPrac==false) {
        FFcueword=FFcue;
    }
    
    if ((firsttrial === false)) {
        FFcueword = PrevResp;
    }
    firsttrial = false;
    FFcueDisp.setText(FFcueword);
    key_respFF.keys = undefined;
    key_respFF.rt = undefined;
    _key_respFF_allKeys = [];
    psychoJS.experiment.addData('FF.started', globalClock.getTime());
    FFMaxDuration = null
    // keep track of which components have finished
    FFComponents = [];
    FFComponents.push(FFcueDisp);
    FFComponents.push(polygon);
    FFComponents.push(key_respFF);
    FFComponents.push(FFrespDisp);
    
    FFComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var _pj;
var keys;
var n;
var i;
function FFRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'FF' ---
    // get current time
    t = FFClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from FFcode_3
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
    
    
    // Text entry
    while ((i < n)) {
        if (((keys[i] === "return") && (Resptext.length >= 1))) {
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
    
    
    
    
    // *FFcueDisp* updates
    if (t >= 0 && FFcueDisp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      FFcueDisp.tStart = t;  // (not accounting for frame time here)
      FFcueDisp.frameNStart = frameN;  // exact frame index
      
      FFcueDisp.setAutoDraw(true);
    }
    
    
    // if FFcueDisp is active this frame...
    if (FFcueDisp.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *polygon* updates
    if (t >= 0.0 && polygon.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon.tStart = t;  // (not accounting for frame time here)
      polygon.frameNStart = frameN;  // exact frame index
      
      polygon.setAutoDraw(true);
    }
    
    
    // if polygon is active this frame...
    if (polygon.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_respFF* updates
    if (t >= 0.0 && key_respFF.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_respFF.tStart = t;  // (not accounting for frame time here)
      key_respFF.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      key_respFF.clock.reset();
      key_respFF.start();
      key_respFF.clearEvents();
    }
    
    // if key_respFF is active this frame...
    if (key_respFF.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_respFF.getKeys({
        keyList: typeof [] === 'string' ? [[]] : [], 
        waitRelease: false
      });
      _key_respFF_allKeys = _key_respFF_allKeys.concat(theseKeys);
      if (_key_respFF_allKeys.length > 0) {
        key_respFF.keys = _key_respFF_allKeys.map((key) => key.name);  // storing all keys
        key_respFF.rt = _key_respFF_allKeys.map((key) => key.rt);
        key_respFF.duration = _key_respFF_allKeys.map((key) => key.duration);
      }
    }
    
    
    // *FFrespDisp* updates
    if (t >= 0.0 && FFrespDisp.status === PsychoJS.Status.NOT_STARTED) {
      // update params
      FFrespDisp.setText(Resptext, false);
      // keep track of start time/frame for later
      FFrespDisp.tStart = t;  // (not accounting for frame time here)
      FFrespDisp.frameNStart = frameN;  // exact frame index
      
      FFrespDisp.setAutoDraw(true);
    }
    
    
    // if FFrespDisp is active this frame...
    if (FFrespDisp.status === PsychoJS.Status.STARTED) {
      // update params
      FFrespDisp.setText(Resptext, false);
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
    FFComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var PrevResp;
function FFRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'FF' ---
    FFComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('FF.stopped', globalClock.getTime());
    // Run 'End Routine' code from FFcode_3
    if (key_respFF.rt) {
        RT1stKP = key_respFF.rt[0];
        RTLastKP = key_respFF.rt.slice((- 1))[0];
    }
    
    psychoJS.experiment.addData("FFresp", Resptext)
    psychoJS.experiment.addData("FFRT1stKP", RT1stKP)
    psychoJS.experiment.addData("FFRTLastKP", RTLastKP)
    PrevResp=Resptext
    Resptext = ''
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_respFF.corr, level);
    }
    psychoJS.experiment.addData('key_respFF.keys', key_respFF.keys);
    if (typeof key_respFF.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_respFF.rt', key_respFF.rt);
        psychoJS.experiment.addData('key_respFF.duration', key_respFF.duration);
        }
    
    key_respFF.stop();
    // the Routine "FF" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var FFinstrux_4MaxDurationReached;
var _key_resp_5_allKeys;
var FFtrialnum;
var FFinstrux_4MaxDuration;
var FFinstrux_4Components;
function FFinstrux_4RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'FFinstrux_4' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    FFinstrux_4Clock.reset();
    routineTimer.reset();
    FFinstrux_4MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    // Run 'Begin Routine' code from code_3
    FFPrac = false;
    FFtrialnum = 0;
    
    psychoJS.experiment.addData('FFinstrux_4.started', globalClock.getTime());
    FFinstrux_4MaxDuration = null
    // keep track of which components have finished
    FFinstrux_4Components = [];
    FFinstrux_4Components.push(intrux_4);
    FFinstrux_4Components.push(EntertoContinue_4);
    FFinstrux_4Components.push(key_resp_5);
    
    FFinstrux_4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function FFinstrux_4RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'FFinstrux_4' ---
    // get current time
    t = FFinstrux_4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *intrux_4* updates
    if (t >= 0.0 && intrux_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      intrux_4.tStart = t;  // (not accounting for frame time here)
      intrux_4.frameNStart = frameN;  // exact frame index
      
      intrux_4.setAutoDraw(true);
    }
    
    
    // if intrux_4 is active this frame...
    if (intrux_4.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *EntertoContinue_4* updates
    if (t >= 0 && EntertoContinue_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      EntertoContinue_4.tStart = t;  // (not accounting for frame time here)
      EntertoContinue_4.frameNStart = frameN;  // exact frame index
      
      EntertoContinue_4.setAutoDraw(true);
    }
    
    
    // if EntertoContinue_4 is active this frame...
    if (EntertoContinue_4.status === PsychoJS.Status.STARTED) {
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
        keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
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
    FFinstrux_4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FFinstrux_4RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'FFinstrux_4' ---
    FFinstrux_4Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('FFinstrux_4.stopped', globalClock.getTime());
    key_resp_5.stop();
    // the Routine "FFinstrux_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var NextFFInstruxMaxDurationReached;
var _key_resp_9_allKeys;
var NextFFInstruxMaxDuration;
var NextFFInstruxComponents;
function NextFFInstruxRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'NextFFInstrux' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    NextFFInstruxClock.reset();
    routineTimer.reset();
    NextFFInstruxMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_9.keys = undefined;
    key_resp_9.rt = undefined;
    _key_resp_9_allKeys = [];
    // Run 'Begin Routine' code from code_2
    FFtrialnum += 1;
    if ((FFtrialnum === 2)) {
        (continueRoutine === false);
    }
    
    psychoJS.experiment.addData('NextFFInstrux.started', globalClock.getTime());
    NextFFInstruxMaxDuration = null
    // keep track of which components have finished
    NextFFInstruxComponents = [];
    NextFFInstruxComponents.push(intrux_5);
    NextFFInstruxComponents.push(EntertoContinue_5);
    NextFFInstruxComponents.push(key_resp_9);
    
    NextFFInstruxComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function NextFFInstruxRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'NextFFInstrux' ---
    // get current time
    t = NextFFInstruxClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *intrux_5* updates
    if (t >= 0.0 && intrux_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      intrux_5.tStart = t;  // (not accounting for frame time here)
      intrux_5.frameNStart = frameN;  // exact frame index
      
      intrux_5.setAutoDraw(true);
    }
    
    
    // if intrux_5 is active this frame...
    if (intrux_5.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *EntertoContinue_5* updates
    if (t >= 0 && EntertoContinue_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      EntertoContinue_5.tStart = t;  // (not accounting for frame time here)
      EntertoContinue_5.frameNStart = frameN;  // exact frame index
      
      EntertoContinue_5.setAutoDraw(true);
    }
    
    
    // if EntertoContinue_5 is active this frame...
    if (EntertoContinue_5.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_resp_9* updates
    if (t >= 0.5 && key_resp_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_9.tStart = t;  // (not accounting for frame time here)
      key_resp_9.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_9.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.clearEvents(); });
    }
    
    // if key_resp_9 is active this frame...
    if (key_resp_9.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_9.getKeys({
        keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
        waitRelease: false
      });
      _key_resp_9_allKeys = _key_resp_9_allKeys.concat(theseKeys);
      if (_key_resp_9_allKeys.length > 0) {
        key_resp_9.keys = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].name;  // just the last key pressed
        key_resp_9.rt = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].rt;
        key_resp_9.duration = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].duration;
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
    NextFFInstruxComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function NextFFInstruxRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'NextFFInstrux' ---
    NextFFInstruxComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('NextFFInstrux.stopped', globalClock.getTime());
    key_resp_9.stop();
    // the Routine "NextFFInstrux" was not non-slip safe, so reset the non-slip timer
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
