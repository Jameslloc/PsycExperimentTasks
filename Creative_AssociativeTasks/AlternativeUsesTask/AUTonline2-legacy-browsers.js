/******************* 
 * Autonline2 *
 *******************/


// store info about the experiment session:
let expName = 'AUTonline2';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
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
  color: new util.Color([0,0,0]),
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
flowScheduler.add(AUTinstruxRoutineBegin());
flowScheduler.add(AUTinstruxRoutineEachFrame());
flowScheduler.add(AUTinstruxRoutineEnd());
const AUTtrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(AUTtrialsLoopBegin(AUTtrialsLoopScheduler));
flowScheduler.add(AUTtrialsLoopScheduler);
flowScheduler.add(AUTtrialsLoopEnd);





flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'cond.xlsx', 'path': 'cond.xlsx'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);


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


var AUTinstruxClock;
var intrux;
var EntertoContinue;
var key_resp_2;
var AUTblankClock;
var text_5;
var AUTClock;
var AUTrespbox;
var InstruxAUT;
var AUTResp;
var AUTcueDisp;
var timeText_1;
var key_respAUT;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "AUTinstrux"
  AUTinstruxClock = new util.Clock();
  intrux = new visual.TextStim({
    win: psychoJS.window,
    name: 'intrux',
    text: "For the next task, you'll be asked to come up with as many original and creative uses for objects as you can.\n\nThe goal is to come up with *creative ideas*, which are ideas that strike people as clever, unusual, interesting, uncommon, humorous, innovative, or different.\n\nYou will have 3 minutes to type as many CREATIVE USES for each object as you can. \nDo not write simply properties of the object, or words associated with the object, but actual uses.\n\nPress ENTER after each use, to write the next one.\n\nYou will be asked to type uses for 2 different objects. ",
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
  
  // Initialize components for Routine "AUTblank"
  AUTblankClock = new util.Clock();
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
  
  // Initialize components for Routine "AUT"
  AUTClock = new util.Clock();
  AUTrespbox = new visual.Rect ({
    win: psychoJS.window, name: 'AUTrespbox', 
    width: [0.5, 0.25][0], height: [0.5, 0.25][1],
    ori: 0, 
    pos: [0, (- 0.25)], 
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
  
  InstruxAUT = new visual.TextStim({
    win: psychoJS.window,
    name: 'InstruxAUT',
    text: 'Think of as many creative uses as you can\nfor the following object: ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.25], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  AUTResp = new visual.TextStim({
    win: psychoJS.window,
    name: 'AUTResp',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.25)], draggable: false, height: 0.05,  wrapWidth: 0.48, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  AUTcueDisp = new visual.TextStim({
    win: psychoJS.window,
    name: 'AUTcueDisp',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Run 'Begin Experiment' code from AUTcode
  
  
  
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
  
  key_respAUT = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var routineForceEnded;
var AUTinstruxMaxDurationReached;
var _key_resp_2_allKeys;
var AUTtime;
var countdownStarted;
var CAPS;
var AUTinstruxMaxDuration;
var AUTinstruxComponents;
function AUTinstruxRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'AUTinstrux' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    AUTinstruxClock.reset();
    routineTimer.reset();
    AUTinstruxMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // Run 'Begin Routine' code from code
    AUTtime = 180;
    
    
    countdownStarted = false;
    CAPS = false;
    psychoJS.experiment.addData('AUTinstrux.started', globalClock.getTime());
    AUTinstruxMaxDuration = null
    // keep track of which components have finished
    AUTinstruxComponents = [];
    AUTinstruxComponents.push(intrux);
    AUTinstruxComponents.push(EntertoContinue);
    AUTinstruxComponents.push(key_resp_2);
    
    AUTinstruxComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function AUTinstruxRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'AUTinstrux' ---
    // get current time
    t = AUTinstruxClock.getTime();
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
    AUTinstruxComponents.forEach( function(thisComponent) {
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


function AUTinstruxRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'AUTinstrux' ---
    AUTinstruxComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('AUTinstrux.stopped', globalClock.getTime());
    key_resp_2.stop();
    // the Routine "AUTinstrux" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var AUTtrials;
function AUTtrialsLoopBegin(AUTtrialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    AUTtrials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'cond.xlsx',
      seed: undefined, name: 'AUTtrials'
    });
    psychoJS.experiment.addLoop(AUTtrials); // add the loop to the experiment
    currentLoop = AUTtrials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    AUTtrials.forEach(function() {
      snapshot = AUTtrials.getSnapshot();
    
      AUTtrialsLoopScheduler.add(importConditions(snapshot));
      AUTtrialsLoopScheduler.add(AUTblankRoutineBegin(snapshot));
      AUTtrialsLoopScheduler.add(AUTblankRoutineEachFrame());
      AUTtrialsLoopScheduler.add(AUTblankRoutineEnd(snapshot));
      const AUTrespsLoopScheduler = new Scheduler(psychoJS);
      AUTtrialsLoopScheduler.add(AUTrespsLoopBegin(AUTrespsLoopScheduler, snapshot));
      AUTtrialsLoopScheduler.add(AUTrespsLoopScheduler);
      AUTtrialsLoopScheduler.add(AUTrespsLoopEnd);
      AUTtrialsLoopScheduler.add(AUTtrialsLoopEndIteration(AUTtrialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var AUTresps;
function AUTrespsLoopBegin(AUTrespsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    AUTresps = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 100, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'AUTresps'
    });
    psychoJS.experiment.addLoop(AUTresps); // add the loop to the experiment
    currentLoop = AUTresps;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    AUTresps.forEach(function() {
      snapshot = AUTresps.getSnapshot();
    
      AUTrespsLoopScheduler.add(importConditions(snapshot));
      AUTrespsLoopScheduler.add(AUTRoutineBegin(snapshot));
      AUTrespsLoopScheduler.add(AUTRoutineEachFrame());
      AUTrespsLoopScheduler.add(AUTRoutineEnd(snapshot));
      AUTrespsLoopScheduler.add(AUTrespsLoopEndIteration(AUTrespsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function AUTrespsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(AUTresps);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function AUTrespsLoopEndIteration(scheduler, snapshot) {
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


async function AUTtrialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(AUTtrials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function AUTtrialsLoopEndIteration(scheduler, snapshot) {
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


var AUTblankMaxDurationReached;
var AUTblankMaxDuration;
var AUTblankComponents;
function AUTblankRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'AUTblank' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    AUTblankClock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    AUTblankMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('AUTblank.started', globalClock.getTime());
    AUTblankMaxDuration = null
    // keep track of which components have finished
    AUTblankComponents = [];
    AUTblankComponents.push(text_5);
    
    AUTblankComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function AUTblankRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'AUTblank' ---
    // get current time
    t = AUTblankClock.getTime();
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
    AUTblankComponents.forEach( function(thisComponent) {
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


function AUTblankRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'AUTblank' ---
    AUTblankComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('AUTblank.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (AUTblankMaxDurationReached) {
        AUTblankClock.add(AUTblankMaxDuration);
    } else {
        AUTblankClock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var AUTMaxDurationReached;
var shift_flag;
var Resptext;
var Key;
var RT1stKP;
var RTLastKP;
var startTime;
var _key_respAUT_allKeys;
var AUTMaxDuration;
var AUTComponents;
function AUTRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'AUT' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    AUTClock.reset();
    routineTimer.reset();
    AUTMaxDurationReached = false;
    // update component parameters for each repeat
    AUTcueDisp.setText(cue);
    // Run 'Begin Routine' code from AUTcode
    shift_flag = false;
    Resptext = "";
    Key=undefined;
    AUTResp.setText(Resptext)
    RT1stKP=0;
    
    RTLastKP=0
    
    if ((! countdownStarted)) {
        startTime = globalClock.getTime();
        countdownStarted = true;
    }
    
    psychoJS.eventManager.clearKeys();
    
    
    key_respAUT.keys = undefined;
    key_respAUT.rt = undefined;
    _key_respAUT_allKeys = [];
    psychoJS.experiment.addData('AUT.started', globalClock.getTime());
    AUTMaxDuration = null
    // keep track of which components have finished
    AUTComponents = [];
    AUTComponents.push(AUTrespbox);
    AUTComponents.push(InstruxAUT);
    AUTComponents.push(AUTResp);
    AUTComponents.push(AUTcueDisp);
    AUTComponents.push(timeText_1);
    AUTComponents.push(key_respAUT);
    
    AUTComponents.forEach( function(thisComponent) {
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
var Diff;
var timeRemaining;
var Minutes;
var Seconds;
var minstring;
var secstring;
var timeText;
function AUTRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'AUT' ---
    // get current time
    t = AUTClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *AUTrespbox* updates
    if (t >= 0.0 && AUTrespbox.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      AUTrespbox.tStart = t;  // (not accounting for frame time here)
      AUTrespbox.frameNStart = frameN;  // exact frame index
      
      AUTrespbox.setAutoDraw(true);
    }
    
    
    // if AUTrespbox is active this frame...
    if (AUTrespbox.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *InstruxAUT* updates
    if (t >= 0.0 && InstruxAUT.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstruxAUT.tStart = t;  // (not accounting for frame time here)
      InstruxAUT.frameNStart = frameN;  // exact frame index
      
      InstruxAUT.setAutoDraw(true);
    }
    
    
    // if InstruxAUT is active this frame...
    if (InstruxAUT.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *AUTResp* updates
    if (t >= 0.0 && AUTResp.status === PsychoJS.Status.NOT_STARTED) {
      // update params
      AUTResp.setText(Resptext, false);
      // keep track of start time/frame for later
      AUTResp.tStart = t;  // (not accounting for frame time here)
      AUTResp.frameNStart = frameN;  // exact frame index
      
      AUTResp.setAutoDraw(true);
    }
    
    
    // if AUTResp is active this frame...
    if (AUTResp.status === PsychoJS.Status.STARTED) {
      // update params
      AUTResp.setText(Resptext, false);
    }
    
    
    // *AUTcueDisp* updates
    if (t >= 0.0 && AUTcueDisp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      AUTcueDisp.tStart = t;  // (not accounting for frame time here)
      AUTcueDisp.frameNStart = frameN;  // exact frame index
      
      AUTcueDisp.setAutoDraw(true);
    }
    
    
    // if AUTcueDisp is active this frame...
    if (AUTcueDisp.status === PsychoJS.Status.STARTED) {
    }
    
    // Run 'Each Frame' code from AUTcode
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
    timeRemaining = (AUTtime - Math.floor((Diff / 1)));
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
        AUTresps.finished = true;
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
    
    
    // *key_respAUT* updates
    if (t >= 0.0 && key_respAUT.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_respAUT.tStart = t;  // (not accounting for frame time here)
      key_respAUT.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_respAUT.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_respAUT.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_respAUT.clearEvents(); });
    }
    
    // if key_respAUT is active this frame...
    if (key_respAUT.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_respAUT.getKeys({
        keyList: typeof [] === 'string' ? [[]] : [], 
        waitRelease: false
      });
      _key_respAUT_allKeys = _key_respAUT_allKeys.concat(theseKeys);
      if (_key_respAUT_allKeys.length > 0) {
        key_respAUT.keys = _key_respAUT_allKeys.map((key) => key.name);  // storing all keys
        key_respAUT.rt = _key_respAUT_allKeys.map((key) => key.rt);
        key_respAUT.duration = _key_respAUT_allKeys.map((key) => key.duration);
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
    AUTComponents.forEach( function(thisComponent) {
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


function AUTRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'AUT' ---
    AUTComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('AUT.stopped', globalClock.getTime());
    // Run 'End Routine' code from AUTcode
    if (key_respAUT.rt) {
        RT1stKP = key_respAUT.rt[0];
        RTLastKP = key_respAUT.rt.slice((- 1))[0];
    }
    
    psychoJS.experiment.addData("AUTresp", Resptext)
    psychoJS.experiment.addData("AUTRT1stKP", RT1stKP)
    psychoJS.experiment.addData("AUTRTLastKP", RTLastKP)
    psychoJS.experiment.addData("AUTcue", cue)
    Resptext = ''
    
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_respAUT.corr, level);
    }
    psychoJS.experiment.addData('key_respAUT.keys', key_respAUT.keys);
    if (typeof key_respAUT.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_respAUT.rt', key_respAUT.rt);
        psychoJS.experiment.addData('key_respAUT.duration', key_respAUT.duration);
        }
    
    key_respAUT.stop();
    // the Routine "AUT" was not non-slip safe, so reset the non-slip timer
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
