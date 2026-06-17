/*********** 
 * Ts *
 ***********/


// store info about the experiment session:
let expName = 'TS';  // from the Builder filename that created this script
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
flowScheduler.add(TypingSpeedInstruxRoutineBegin());
flowScheduler.add(TypingSpeedInstruxRoutineEachFrame());
flowScheduler.add(TypingSpeedInstruxRoutineEnd());
flowScheduler.add(GetReadyRoutineBegin());
flowScheduler.add(GetReadyRoutineEachFrame());
flowScheduler.add(GetReadyRoutineEnd());
const TStrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(TStrialsLoopBegin(TStrialsLoopScheduler));
flowScheduler.add(TStrialsLoopScheduler);
flowScheduler.add(TStrialsLoopEnd);


flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'TS.xlsx', 'path': 'TS.xlsx'},
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


var TypingSpeedInstruxClock;
var TStext;
var key_resp_22;
var EnterToContinue_20;
var GetReadyClock;
var GetReadyText;
var TypingSpeedClock;
var TScueDisp;
var polygon_6;
var key_respTS;
var TSrespDisp;
var Timer_2;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "TypingSpeedInstrux"
  TypingSpeedInstruxClock = new util.Clock();
  TStext = new visual.TextStim({
    win: psychoJS.window,
    name: 'TStext',
    text: "For this task, you'll be asked to type as many words as you can in 30 seconds. \n\nEach screen will show a word. Please type out the exact word shown, in the text field and then press ENTER. \nA new word will then appear. \n\nThis will continue for 30 seconds, so please type as many as you can within that time.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.1], draggable: false, height: 0.04,  wrapWidth: 1.2, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_22 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  EnterToContinue_20 = new visual.TextStim({
    win: psychoJS.window,
    name: 'EnterToContinue_20',
    text: 'Press ENTER to begin the task',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "GetReady"
  GetReadyClock = new util.Clock();
  GetReadyText = new visual.TextStim({
    win: psychoJS.window,
    name: 'GetReadyText',
    text: 'Get ready',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "TypingSpeed"
  TypingSpeedClock = new util.Clock();
  // Run 'Begin Experiment' code from TScode
  
  
  TScueDisp = new visual.TextStim({
    win: psychoJS.window,
    name: 'TScueDisp',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.1], draggable: false, height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  polygon_6 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_6', 
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
  
  key_respTS = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  TSrespDisp = new visual.TextStim({
    win: psychoJS.window,
    name: 'TSrespDisp',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.2)], draggable: false, height: 0.075,  wrapWidth: 0.4, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  Timer_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Timer_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.5, (- 0.35)], draggable: false, height: 0.09,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var routineForceEnded;
var TypingSpeedInstruxMaxDurationReached;
var _key_resp_22_allKeys;
var Taskstart;
var TStime;
var CAPS;
var range;
var roundOne;
var RepArray;
var TypingSpeedInstruxMaxDuration;
var TypingSpeedInstruxComponents;
function TypingSpeedInstruxRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'TypingSpeedInstrux' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    TypingSpeedInstruxClock.reset();
    routineTimer.reset();
    TypingSpeedInstruxMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_22.keys = undefined;
    key_resp_22.rt = undefined;
    _key_resp_22_allKeys = [];
    // Run 'Begin Routine' code from code_43
    document.body.style.cursor='none';
    
    
    psychoJS.experiment.addData("TaskID", 15)
    Taskstart=globalClock.getTime()
    
    TStime=30
    
    
    CAPS=false
    
    range = (start, stop, step = 1) =>
      Array(Math.ceil((stop - start) / step)).fill(start).map((x, y) => x + y * step)
      
    roundOne = (n, d) => Math.round(n * Math.pow(10, d)) / Math.pow(10, d)
    
    RepArray = (K,n=1) => Array.from({length:n}).map(x => K)
    psychoJS.experiment.addData('TypingSpeedInstrux.started', globalClock.getTime());
    TypingSpeedInstruxMaxDuration = null
    // keep track of which components have finished
    TypingSpeedInstruxComponents = [];
    TypingSpeedInstruxComponents.push(TStext);
    TypingSpeedInstruxComponents.push(key_resp_22);
    TypingSpeedInstruxComponents.push(EnterToContinue_20);
    
    TypingSpeedInstruxComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function TypingSpeedInstruxRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'TypingSpeedInstrux' ---
    // get current time
    t = TypingSpeedInstruxClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *TStext* updates
    if (t >= 0.0 && TStext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TStext.tStart = t;  // (not accounting for frame time here)
      TStext.frameNStart = frameN;  // exact frame index
      
      TStext.setAutoDraw(true);
    }
    
    
    // if TStext is active this frame...
    if (TStext.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_resp_22* updates
    if (t >= 0.5 && key_resp_22.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_22.tStart = t;  // (not accounting for frame time here)
      key_resp_22.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_22.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_22.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_22.clearEvents(); });
    }
    
    // if key_resp_22 is active this frame...
    if (key_resp_22.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_22.getKeys({
        keyList: typeof 'return' === 'string' ? ['return'] : 'return', 
        waitRelease: false
      });
      _key_resp_22_allKeys = _key_resp_22_allKeys.concat(theseKeys);
      if (_key_resp_22_allKeys.length > 0) {
        key_resp_22.keys = _key_resp_22_allKeys[_key_resp_22_allKeys.length - 1].name;  // just the last key pressed
        key_resp_22.rt = _key_resp_22_allKeys[_key_resp_22_allKeys.length - 1].rt;
        key_resp_22.duration = _key_resp_22_allKeys[_key_resp_22_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *EnterToContinue_20* updates
    if (t >= 0.0 && EnterToContinue_20.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      EnterToContinue_20.tStart = t;  // (not accounting for frame time here)
      EnterToContinue_20.frameNStart = frameN;  // exact frame index
      
      EnterToContinue_20.setAutoDraw(true);
    }
    
    
    // if EnterToContinue_20 is active this frame...
    if (EnterToContinue_20.status === PsychoJS.Status.STARTED) {
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
    TypingSpeedInstruxComponents.forEach( function(thisComponent) {
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


function TypingSpeedInstruxRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'TypingSpeedInstrux' ---
    TypingSpeedInstruxComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('TypingSpeedInstrux.stopped', globalClock.getTime());
    key_resp_22.stop();
    // the Routine "TypingSpeedInstrux" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var GetReadyMaxDurationReached;
var GetReadyMaxDuration;
var GetReadyComponents;
function GetReadyRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'GetReady' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    GetReadyClock.reset(routineTimer.getTime());
    routineTimer.add(2.000000);
    GetReadyMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('GetReady.started', globalClock.getTime());
    GetReadyMaxDuration = null
    // keep track of which components have finished
    GetReadyComponents = [];
    GetReadyComponents.push(GetReadyText);
    
    GetReadyComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function GetReadyRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'GetReady' ---
    // get current time
    t = GetReadyClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *GetReadyText* updates
    if (t >= 0.0 && GetReadyText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      GetReadyText.tStart = t;  // (not accounting for frame time here)
      GetReadyText.frameNStart = frameN;  // exact frame index
      
      GetReadyText.setAutoDraw(true);
    }
    
    
    // if GetReadyText is active this frame...
    if (GetReadyText.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (GetReadyText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      GetReadyText.tStop = t;  // not accounting for scr refresh
      GetReadyText.frameNStop = frameN;  // exact frame index
      // update status
      GetReadyText.status = PsychoJS.Status.FINISHED;
      GetReadyText.setAutoDraw(false);
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
    GetReadyComponents.forEach( function(thisComponent) {
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


var startTime;
function GetReadyRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'GetReady' ---
    GetReadyComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('GetReady.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_44
    startTime = globalClock.getTime();
    
    if (routineForceEnded) {
        routineTimer.reset();} else if (GetReadyMaxDurationReached) {
        GetReadyClock.add(GetReadyMaxDuration);
    } else {
        GetReadyClock.add(2.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var TStrials;
function TStrialsLoopBegin(TStrialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    TStrials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'TS.xlsx',
      seed: undefined, name: 'TStrials'
    });
    psychoJS.experiment.addLoop(TStrials); // add the loop to the experiment
    currentLoop = TStrials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    TStrials.forEach(function() {
      snapshot = TStrials.getSnapshot();
    
      TStrialsLoopScheduler.add(importConditions(snapshot));
      TStrialsLoopScheduler.add(TypingSpeedRoutineBegin(snapshot));
      TStrialsLoopScheduler.add(TypingSpeedRoutineEachFrame());
      TStrialsLoopScheduler.add(TypingSpeedRoutineEnd(snapshot));
      TStrialsLoopScheduler.add(TStrialsLoopEndIteration(TStrialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function TStrialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(TStrials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function TStrialsLoopEndIteration(scheduler, snapshot) {
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


var TypingSpeedMaxDurationReached;
var shift_flag;
var Resptext;
var Key;
var charlim;
var RT1stKP;
var RTLastKP;
var _key_respTS_allKeys;
var TypingSpeedMaxDuration;
var TypingSpeedComponents;
function TypingSpeedRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'TypingSpeed' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    TypingSpeedClock.reset();
    routineTimer.reset();
    TypingSpeedMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from TScode
    //is shift pressed?
    shift_flag = false;
    //#set response text as empty
    Resptext = " ";
    TSrespDisp.setText(Resptext)
    Key=undefined;
    
    charlim=30
    
    //set 1st and last key press times
    RT1stKP=0;
    RTLastKP=0
    
    psychoJS.eventManager.clearKeys();
    
    TScueDisp.setText(TSstim);
    key_respTS.keys = undefined;
    key_respTS.rt = undefined;
    _key_respTS_allKeys = [];
    psychoJS.experiment.addData('TypingSpeed.started', globalClock.getTime());
    TypingSpeedMaxDuration = null
    // keep track of which components have finished
    TypingSpeedComponents = [];
    TypingSpeedComponents.push(TScueDisp);
    TypingSpeedComponents.push(polygon_6);
    TypingSpeedComponents.push(key_respTS);
    TypingSpeedComponents.push(TSrespDisp);
    TypingSpeedComponents.push(Timer_2);
    
    TypingSpeedComponents.forEach( function(thisComponent) {
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
function TypingSpeedRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'TypingSpeed' ---
    // get current time
    t = TypingSpeedClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from TScode
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
    timeRemaining = (TStime - Math.floor(Diff));
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
        if (((keys[i] === "return") && (Resptext.length >= 2))  || (timeRemaining <= 0)) {
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
        TStrials.finished=true;
    }
    
    
    
    // *TScueDisp* updates
    if (t >= 0 && TScueDisp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TScueDisp.tStart = t;  // (not accounting for frame time here)
      TScueDisp.frameNStart = frameN;  // exact frame index
      
      TScueDisp.setAutoDraw(true);
    }
    
    
    // if TScueDisp is active this frame...
    if (TScueDisp.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *polygon_6* updates
    if (t >= 0.0 && polygon_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_6.tStart = t;  // (not accounting for frame time here)
      polygon_6.frameNStart = frameN;  // exact frame index
      
      polygon_6.setAutoDraw(true);
    }
    
    
    // if polygon_6 is active this frame...
    if (polygon_6.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_respTS* updates
    if (t >= 0.0 && key_respTS.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_respTS.tStart = t;  // (not accounting for frame time here)
      key_respTS.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      key_respTS.clock.reset();
      key_respTS.start();
      key_respTS.clearEvents();
    }
    
    // if key_respTS is active this frame...
    if (key_respTS.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_respTS.getKeys({
        keyList: typeof [] === 'string' ? [[]] : [], 
        waitRelease: false
      });
      _key_respTS_allKeys = _key_respTS_allKeys.concat(theseKeys);
      if (_key_respTS_allKeys.length > 0) {
        key_respTS.keys = _key_respTS_allKeys.map((key) => key.name);  // storing all keys
        key_respTS.rt = _key_respTS_allKeys.map((key) => key.rt);
        key_respTS.duration = _key_respTS_allKeys.map((key) => key.duration);
      }
    }
    
    
    // *TSrespDisp* updates
    if (t >= 0.0 && TSrespDisp.status === PsychoJS.Status.NOT_STARTED) {
      // update params
      TSrespDisp.setText(Resptext, false);
      // keep track of start time/frame for later
      TSrespDisp.tStart = t;  // (not accounting for frame time here)
      TSrespDisp.frameNStart = frameN;  // exact frame index
      
      TSrespDisp.setAutoDraw(true);
    }
    
    
    // if TSrespDisp is active this frame...
    if (TSrespDisp.status === PsychoJS.Status.STARTED) {
      // update params
      TSrespDisp.setText(Resptext, false);
    }
    
    
    // *Timer_2* updates
    if (t >= 0.0 && Timer_2.status === PsychoJS.Status.NOT_STARTED) {
      // update params
      Timer_2.setText(timeText, false);
      // keep track of start time/frame for later
      Timer_2.tStart = t;  // (not accounting for frame time here)
      Timer_2.frameNStart = frameN;  // exact frame index
      
      Timer_2.setAutoDraw(true);
    }
    
    
    // if Timer_2 is active this frame...
    if (Timer_2.status === PsychoJS.Status.STARTED) {
      // update params
      Timer_2.setText(timeText, false);
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
    TypingSpeedComponents.forEach( function(thisComponent) {
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
function TypingSpeedRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'TypingSpeed' ---
    TypingSpeedComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('TypingSpeed.stopped', globalClock.getTime());
    // Run 'End Routine' code from TScode
    if (key_respTS.rt) {
        RT1stKP = key_respTS.rt[0];
        RTLastKP = key_respTS.rt.slice((- 1))[0];
    }
    
    psychoJS.experiment.addData("TSinput", Resptext)
    psychoJS.experiment.addData("TSRT1stKP", RT1stKP)
    psychoJS.experiment.addData("TSRTLastKP", RTLastKP)
    PrevResp=Resptext
    Resptext = " "
    
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_respTS.corr, level);
    }
    psychoJS.experiment.addData('key_respTS.keys', key_respTS.keys);
    if (typeof key_respTS.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_respTS.rt', key_respTS.rt);
        psychoJS.experiment.addData('key_respTS.duration', key_respTS.duration);
        }
    
    key_respTS.stop();
    // the Routine "TypingSpeed" was not non-slip safe, so reset the non-slip timer
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
