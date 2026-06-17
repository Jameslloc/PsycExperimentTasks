/************************ 
 * Drawingtask2020 *
 ************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2026.1.3.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'DrawingTask2020';  // from the Builder filename that created this script
let expInfo = {
    'participant': '1',
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
flowScheduler.add(Fake_TrialRoutineBegin());
flowScheduler.add(Fake_TrialRoutineEachFrame());
flowScheduler.add(Fake_TrialRoutineEnd());
flowScheduler.add(DrawInstruxRoutineBegin());
flowScheduler.add(DrawInstruxRoutineEachFrame());
flowScheduler.add(DrawInstruxRoutineEnd());
flowScheduler.add(DrawInstrux_3RoutineBegin());
flowScheduler.add(DrawInstrux_3RoutineEachFrame());
flowScheduler.add(DrawInstrux_3RoutineEnd());
flowScheduler.add(crossRoutineBegin());
flowScheduler.add(crossRoutineEachFrame());
flowScheduler.add(crossRoutineEnd());
flowScheduler.add(DrawingTrialRoutineBegin());
flowScheduler.add(DrawingTrialRoutineEachFrame());
flowScheduler.add(DrawingTrialRoutineEnd());
flowScheduler.add(DrawInstrux_2RoutineBegin());
flowScheduler.add(DrawInstrux_2RoutineEachFrame());
flowScheduler.add(DrawInstrux_2RoutineEnd());
const trials_drawLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_drawLoopBegin(trials_drawLoopScheduler));
flowScheduler.add(trials_drawLoopScheduler);
flowScheduler.add(trials_drawLoopEnd);



flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'DrawStims.xlsx', 'path': 'DrawStims.xlsx'},
    {'name': 'Images/Image2.png', 'path': 'Images/Image2.png'},
    {'name': 'Images/Image3.png', 'path': 'Images/Image3.png'},
    {'name': 'Images/Image4.png', 'path': 'Images/Image4.png'},
    {'name': 'Images/Image5.png', 'path': 'Images/Image5.png'},
    {'name': 'Images/Image9.png', 'path': 'Images/Image9.png'},
    {'name': 'Images/Image13.png', 'path': 'Images/Image13.png'},
    {'name': 'Images/Image16.png', 'path': 'Images/Image16.png'},
    {'name': 'Images/Image18.png', 'path': 'Images/Image18.png'},
    {'name': 'Images/Image23.png', 'path': 'Images/Image23.png'},
    {'name': 'Images/Image26.png', 'path': 'Images/Image26.png'},
    {'name': 'Images/Image28.png', 'path': 'Images/Image28.png'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
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
var Pnum;
var CountBal;
var Prac;
var SketchTime;
var ElaborationPhase;
var Empty_shapes;
var range;
var roundOne;
var RepArray;
var Fake_TrialClock;
var image_2;
var image_3;
var image_4;
var image_5;
var image_9;
var image_13;
var image_16;
var image_18;
var image_23;
var image_26;
var image_28;
var DrawInstruxClock;
var DrawinstrucText;
var key_resp_5;
var EnterToContinue_2;
var DrawInstrux_3Clock;
var DrawinstrucText_3;
var key_resp;
var EnterToContinue;
var crossClock;
var polygon_4;
var DrawingTrialClock;
var image1;
var mymouse;
var UndoButton;
var UndoText;
var timer;
var DrawInstrux_2Clock;
var DrawinstrucText_2;
var EnterToContinue_3;
var key_resp_2;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "_settings"
  _settingsClock = new util.Clock();
  // Run 'Begin Experiment' code from code_7
  
  
  
  document.body.style.cursor='cursorurl';
  Pnum = Number.parseInt(Number.parseFloat(expInfo["participant"]));
  CountBal = (Pnum % 4);
  
  Prac=true;
  SketchTime=3
  
  ElaborationPhase = false;
  // don't need to do any file rearranging in the javascript
  
  class ShapeStimCustom extends visual.ShapeStim {
    _getPixiPolygon() {
      super._getPixiPolygon()
      this._pixiPolygon_px.closeStroke = this._closeShape;
      return this._pixiPolygon_px;
    }
  }
  
  
  Empty_shapes = 100;
  range = (start, stop, step = 1) =>
    Array(Math.ceil((stop - start) / step)).fill(start).map((x, y) => x + y * step)
    
  
  roundOne = (n, d) => Math.round(n * Math.pow(10, d)) / Math.pow(10, d)
  
  RepArray = (K,n=1) => Array.from({length:n}).map(x => K)
  // Initialize components for Routine "Fake_Trial"
  Fake_TrialClock = new util.Clock();
  image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_2', units : undefined, 
    image : 'Images/Image2.png', mask : undefined,
    anchor : 'center',
    ori : 0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  image_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_3', units : undefined, 
    image : 'Images/Image3.png', mask : undefined,
    anchor : 'center',
    ori : 0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  image_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_4', units : undefined, 
    image : 'Images/Image4.png', mask : undefined,
    anchor : 'center',
    ori : 0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  image_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_5', units : undefined, 
    image : 'Images/Image5.png', mask : undefined,
    anchor : 'center',
    ori : 0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  image_9 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_9', units : undefined, 
    image : 'Images/Image9.png', mask : undefined,
    anchor : 'center',
    ori : 0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  image_13 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_13', units : undefined, 
    image : 'Images/Image13.png', mask : undefined,
    anchor : 'center',
    ori : 0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  image_16 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_16', units : undefined, 
    image : 'Images/Image16.png', mask : undefined,
    anchor : 'center',
    ori : 0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -6.0 
  });
  image_18 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_18', units : undefined, 
    image : 'Images/Image18.png', mask : undefined,
    anchor : 'center',
    ori : 0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -7.0 
  });
  image_23 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_23', units : undefined, 
    image : 'Images/Image23.png', mask : undefined,
    anchor : 'center',
    ori : 0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -8.0 
  });
  image_26 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_26', units : undefined, 
    image : 'Images/Image26.png', mask : undefined,
    anchor : 'center',
    ori : 0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -9.0 
  });
  image_28 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_28', units : undefined, 
    image : 'Images/Image28.png', mask : undefined,
    anchor : 'center',
    ori : 0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -10.0 
  });
  // Initialize components for Routine "DrawInstrux"
  DrawInstruxClock = new util.Clock();
  DrawinstrucText = new visual.TextStim({
    win: psychoJS.window,
    name: 'DrawinstrucText',
    text: "The next task is a Drawing Task.\n\nIn the Drawing Task, you will be presented with a series of incomplete shapes. \n\nUsing each shape, you must produce the most creative drawing you can think of (the incomplete shape must be used as part of your drawing).\n\nYour drawings don't have to be pretty: they should simply show how creative and interesting your ideas are.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.1], draggable: false, height: 0.045,  wrapWidth: 1.2, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  EnterToContinue_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'EnterToContinue_2',
    text: 'Press ENTER to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.375)], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "DrawInstrux_3"
  DrawInstrux_3Clock = new util.Clock();
  DrawinstrucText_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'DrawinstrucText_3',
    text: 'You do not need to write a label for your drawing.\n\nYou will draw using the mouse, and will have 30 seconds to complete you drawing.\nPlease use all the time available to work on the most creative drawing you can.\n\nFirst, you will complete a 30 second practise drawing.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.1], draggable: false, height: 0.045,  wrapWidth: 1.2, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  EnterToContinue = new visual.TextStim({
    win: psychoJS.window,
    name: 'EnterToContinue',
    text: 'Press ENTER to begin the practise',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.375)], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "cross"
  crossClock = new util.Clock();
  polygon_4 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'polygon_4', units : 'height', 
    vertices: 'cross', size:[0.05, 0.05],
    ori: 0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1, 
    lineColor: new util.Color([(- 1), (- 1), (- 1)]), 
    fillColor: new util.Color([(- 1), (- 1), (- 1)]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: 0, 
    interpolate: true, 
  });
  
  // Initialize components for Routine "DrawingTrial"
  DrawingTrialClock = new util.Clock();
  image1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image1', units : 'height', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.6, 0.6],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  mymouse = new core.Mouse({
    win: psychoJS.window,
  });
  mymouse.mouseClock = new util.Clock();
  UndoButton = new visual.Rect ({
    win: psychoJS.window, name: 'UndoButton', units : 'height', 
    width: [0.24, 0.12][0], height: [0.24, 0.12][1],
    ori: 0, 
    pos: [(- 0.5), (- 0.35)], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color('darkgray'), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -3, 
    interpolate: true, 
  });
  
  UndoText = new visual.TextStim({
    win: psychoJS.window,
    name: 'UndoText',
    text: 'Undo Last',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), (- 0.35)], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  timer = new visual.TextStim({
    win: psychoJS.window,
    name: 'timer',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.5, (- 0.35)], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  // Initialize components for Routine "DrawInstrux_2"
  DrawInstrux_2Clock = new util.Clock();
  DrawinstrucText_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'DrawinstrucText_2',
    text: "That was the practise. Next are the 10 real trials.\n\nRemember- Using each shape, you must produce the most creative drawing you can think of (the incomplete shape must be used as part of your drawing).\n\nYour drawings don't have to be pretty: they should simply show how creative and interesting your ideas are.\n\nYou have 30 seconds per drawing, and should use all this time to work on your drawing.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.1], draggable: false, height: 0.045,  wrapWidth: 1.2, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  EnterToContinue_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'EnterToContinue_3',
    text: 'Press ENTER to begin',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.375)], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
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


var Fake_TrialMaxDurationReached;
var Fake_TrialMaxDuration;
var Fake_TrialComponents;
function Fake_TrialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Fake_Trial' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    Fake_TrialClock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    Fake_TrialMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('Fake_Trial.started', globalClock.getTime());
    Fake_TrialMaxDuration = null
    // keep track of which components have finished
    Fake_TrialComponents = [];
    Fake_TrialComponents.push(image_2);
    Fake_TrialComponents.push(image_3);
    Fake_TrialComponents.push(image_4);
    Fake_TrialComponents.push(image_5);
    Fake_TrialComponents.push(image_9);
    Fake_TrialComponents.push(image_13);
    Fake_TrialComponents.push(image_16);
    Fake_TrialComponents.push(image_18);
    Fake_TrialComponents.push(image_23);
    Fake_TrialComponents.push(image_26);
    Fake_TrialComponents.push(image_28);
    
    for (const thisComponent of Fake_TrialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function Fake_TrialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Fake_Trial' ---
    // get current time
    t = Fake_TrialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_2* updates
    if (t >= 0.0 && image_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_2.tStart = t;  // (not accounting for frame time here)
      image_2.frameNStart = frameN;  // exact frame index
      
      image_2.setAutoDraw(true);
    }
    
    
    // if image_2 is active this frame...
    if (image_2.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      image_2.tStop = t;  // not accounting for scr refresh
      image_2.frameNStop = frameN;  // exact frame index
      // update status
      image_2.status = PsychoJS.Status.FINISHED;
      image_2.setAutoDraw(false);
    }
    
    
    // *image_3* updates
    if (t >= 0.0 && image_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_3.tStart = t;  // (not accounting for frame time here)
      image_3.frameNStart = frameN;  // exact frame index
      
      image_3.setAutoDraw(true);
    }
    
    
    // if image_3 is active this frame...
    if (image_3.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      image_3.tStop = t;  // not accounting for scr refresh
      image_3.frameNStop = frameN;  // exact frame index
      // update status
      image_3.status = PsychoJS.Status.FINISHED;
      image_3.setAutoDraw(false);
    }
    
    
    // *image_4* updates
    if (t >= 0.0 && image_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_4.tStart = t;  // (not accounting for frame time here)
      image_4.frameNStart = frameN;  // exact frame index
      
      image_4.setAutoDraw(true);
    }
    
    
    // if image_4 is active this frame...
    if (image_4.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      image_4.tStop = t;  // not accounting for scr refresh
      image_4.frameNStop = frameN;  // exact frame index
      // update status
      image_4.status = PsychoJS.Status.FINISHED;
      image_4.setAutoDraw(false);
    }
    
    
    // *image_5* updates
    if (t >= 0.0 && image_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_5.tStart = t;  // (not accounting for frame time here)
      image_5.frameNStart = frameN;  // exact frame index
      
      image_5.setAutoDraw(true);
    }
    
    
    // if image_5 is active this frame...
    if (image_5.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      image_5.tStop = t;  // not accounting for scr refresh
      image_5.frameNStop = frameN;  // exact frame index
      // update status
      image_5.status = PsychoJS.Status.FINISHED;
      image_5.setAutoDraw(false);
    }
    
    
    // *image_9* updates
    if (t >= 0.0 && image_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_9.tStart = t;  // (not accounting for frame time here)
      image_9.frameNStart = frameN;  // exact frame index
      
      image_9.setAutoDraw(true);
    }
    
    
    // if image_9 is active this frame...
    if (image_9.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      image_9.tStop = t;  // not accounting for scr refresh
      image_9.frameNStop = frameN;  // exact frame index
      // update status
      image_9.status = PsychoJS.Status.FINISHED;
      image_9.setAutoDraw(false);
    }
    
    
    // *image_13* updates
    if (t >= 0.0 && image_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_13.tStart = t;  // (not accounting for frame time here)
      image_13.frameNStart = frameN;  // exact frame index
      
      image_13.setAutoDraw(true);
    }
    
    
    // if image_13 is active this frame...
    if (image_13.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_13.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      image_13.tStop = t;  // not accounting for scr refresh
      image_13.frameNStop = frameN;  // exact frame index
      // update status
      image_13.status = PsychoJS.Status.FINISHED;
      image_13.setAutoDraw(false);
    }
    
    
    // *image_16* updates
    if (t >= 0.0 && image_16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_16.tStart = t;  // (not accounting for frame time here)
      image_16.frameNStart = frameN;  // exact frame index
      
      image_16.setAutoDraw(true);
    }
    
    
    // if image_16 is active this frame...
    if (image_16.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_16.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      image_16.tStop = t;  // not accounting for scr refresh
      image_16.frameNStop = frameN;  // exact frame index
      // update status
      image_16.status = PsychoJS.Status.FINISHED;
      image_16.setAutoDraw(false);
    }
    
    
    // *image_18* updates
    if (t >= 0.0 && image_18.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_18.tStart = t;  // (not accounting for frame time here)
      image_18.frameNStart = frameN;  // exact frame index
      
      image_18.setAutoDraw(true);
    }
    
    
    // if image_18 is active this frame...
    if (image_18.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_18.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      image_18.tStop = t;  // not accounting for scr refresh
      image_18.frameNStop = frameN;  // exact frame index
      // update status
      image_18.status = PsychoJS.Status.FINISHED;
      image_18.setAutoDraw(false);
    }
    
    
    // *image_23* updates
    if (t >= 0.0 && image_23.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_23.tStart = t;  // (not accounting for frame time here)
      image_23.frameNStart = frameN;  // exact frame index
      
      image_23.setAutoDraw(true);
    }
    
    
    // if image_23 is active this frame...
    if (image_23.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_23.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      image_23.tStop = t;  // not accounting for scr refresh
      image_23.frameNStop = frameN;  // exact frame index
      // update status
      image_23.status = PsychoJS.Status.FINISHED;
      image_23.setAutoDraw(false);
    }
    
    
    // *image_26* updates
    if (t >= 0.0 && image_26.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_26.tStart = t;  // (not accounting for frame time here)
      image_26.frameNStart = frameN;  // exact frame index
      
      image_26.setAutoDraw(true);
    }
    
    
    // if image_26 is active this frame...
    if (image_26.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_26.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      image_26.tStop = t;  // not accounting for scr refresh
      image_26.frameNStop = frameN;  // exact frame index
      // update status
      image_26.status = PsychoJS.Status.FINISHED;
      image_26.setAutoDraw(false);
    }
    
    
    // *image_28* updates
    if (t >= 0.0 && image_28.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_28.tStart = t;  // (not accounting for frame time here)
      image_28.frameNStart = frameN;  // exact frame index
      
      image_28.setAutoDraw(true);
    }
    
    
    // if image_28 is active this frame...
    if (image_28.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_28.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      image_28.tStop = t;  // not accounting for scr refresh
      image_28.frameNStop = frameN;  // exact frame index
      // update status
      image_28.status = PsychoJS.Status.FINISHED;
      image_28.setAutoDraw(false);
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
    for (const thisComponent of Fake_TrialComponents)
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


function Fake_TrialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Fake_Trial' ---
    for (const thisComponent of Fake_TrialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Fake_Trial.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (Fake_TrialMaxDurationReached) {
        Fake_TrialClock.add(Fake_TrialMaxDuration);
    } else {
        Fake_TrialClock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var DrawInstruxMaxDurationReached;
var _key_resp_5_allKeys;
var DrawInstruxMaxDuration;
var DrawInstruxComponents;
function DrawInstruxRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'DrawInstrux' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    DrawInstruxClock.reset();
    routineTimer.reset();
    DrawInstruxMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    psychoJS.experiment.addData('DrawInstrux.started', globalClock.getTime());
    DrawInstruxMaxDuration = null
    // keep track of which components have finished
    DrawInstruxComponents = [];
    DrawInstruxComponents.push(DrawinstrucText);
    DrawInstruxComponents.push(key_resp_5);
    DrawInstruxComponents.push(EnterToContinue_2);
    
    for (const thisComponent of DrawInstruxComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function DrawInstruxRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'DrawInstrux' ---
    // get current time
    t = DrawInstruxClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *DrawinstrucText* updates
    if (t >= 0.0 && DrawinstrucText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      DrawinstrucText.tStart = t;  // (not accounting for frame time here)
      DrawinstrucText.frameNStart = frameN;  // exact frame index
      
      DrawinstrucText.setAutoDraw(true);
    }
    
    
    // if DrawinstrucText is active this frame...
    if (DrawinstrucText.status === PsychoJS.Status.STARTED) {
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
    
    
    // *EnterToContinue_2* updates
    if (t >= 0.0 && EnterToContinue_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      EnterToContinue_2.tStart = t;  // (not accounting for frame time here)
      EnterToContinue_2.frameNStart = frameN;  // exact frame index
      
      EnterToContinue_2.setAutoDraw(true);
    }
    
    
    // if EnterToContinue_2 is active this frame...
    if (EnterToContinue_2.status === PsychoJS.Status.STARTED) {
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
    for (const thisComponent of DrawInstruxComponents)
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


function DrawInstruxRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'DrawInstrux' ---
    for (const thisComponent of DrawInstruxComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('DrawInstrux.stopped', globalClock.getTime());
    key_resp_5.stop();
    // the Routine "DrawInstrux" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var DrawInstrux_3MaxDurationReached;
var _key_resp_allKeys;
var DrawInstrux_3MaxDuration;
var DrawInstrux_3Components;
function DrawInstrux_3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'DrawInstrux_3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    DrawInstrux_3Clock.reset();
    routineTimer.reset();
    DrawInstrux_3MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_2
    Prac=1;
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    psychoJS.experiment.addData('DrawInstrux_3.started', globalClock.getTime());
    DrawInstrux_3MaxDuration = null
    // keep track of which components have finished
    DrawInstrux_3Components = [];
    DrawInstrux_3Components.push(DrawinstrucText_3);
    DrawInstrux_3Components.push(key_resp);
    DrawInstrux_3Components.push(EnterToContinue);
    
    for (const thisComponent of DrawInstrux_3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function DrawInstrux_3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'DrawInstrux_3' ---
    // get current time
    t = DrawInstrux_3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *DrawinstrucText_3* updates
    if (t >= 0.0 && DrawinstrucText_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      DrawinstrucText_3.tStart = t;  // (not accounting for frame time here)
      DrawinstrucText_3.frameNStart = frameN;  // exact frame index
      
      DrawinstrucText_3.setAutoDraw(true);
    }
    
    
    // if DrawinstrucText_3 is active this frame...
    if (DrawinstrucText_3.status === PsychoJS.Status.STARTED) {
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
    
    
    // *EnterToContinue* updates
    if (t >= 0.0 && EnterToContinue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      EnterToContinue.tStart = t;  // (not accounting for frame time here)
      EnterToContinue.frameNStart = frameN;  // exact frame index
      
      EnterToContinue.setAutoDraw(true);
    }
    
    
    // if EnterToContinue is active this frame...
    if (EnterToContinue.status === PsychoJS.Status.STARTED) {
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
    for (const thisComponent of DrawInstrux_3Components)
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


function DrawInstrux_3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'DrawInstrux_3' ---
    for (const thisComponent of DrawInstrux_3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('DrawInstrux_3.stopped', globalClock.getTime());
    key_resp.stop();
    // the Routine "DrawInstrux_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var crossMaxDurationReached;
var CurrentDraw;
var stim;
var ShowIm;
var crossMaxDuration;
var crossComponents;
function crossRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'cross' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    crossClock.reset(routineTimer.getTime());
    routineTimer.add(2.000000);
    crossMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_12
    
    if (Prac) {
        var NUM=2;
        CurrentDraw = NUM.toString();
        Prac=false;
    } else {
        CurrentDraw = DrawStim.toString();
    }
    
    stim = (("Images/Image" + CurrentDraw) + ".png");
    ShowIm = stim;
    
    document.body.style.cursor = 'cursorurl';
    
    psychoJS.experiment.addData('cross.started', globalClock.getTime());
    crossMaxDuration = null
    // keep track of which components have finished
    crossComponents = [];
    crossComponents.push(polygon_4);
    
    for (const thisComponent of crossComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crossRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'cross' ---
    // get current time
    t = crossClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_4* updates
    if (t >= 0.0 && polygon_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_4.tStart = t;  // (not accounting for frame time here)
      polygon_4.frameNStart = frameN;  // exact frame index
      
      polygon_4.setAutoDraw(true);
    }
    
    
    // if polygon_4 is active this frame...
    if (polygon_4.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (polygon_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      polygon_4.tStop = t;  // not accounting for scr refresh
      polygon_4.frameNStop = frameN;  // exact frame index
      // update status
      polygon_4.status = PsychoJS.Status.FINISHED;
      polygon_4.setAutoDraw(false);
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
    for (const thisComponent of crossComponents)
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


function crossRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'cross' ---
    for (const thisComponent of crossComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('cross.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (crossMaxDurationReached) {
        crossClock.add(crossMaxDuration);
    } else {
        crossClock.add(2.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var DrawingTrialMaxDurationReached;
var polygon_vertex;
var polygon_list;
var CircleListList;
var CircleList;
var CircleCordsList;
var CircleSize;
var CircleEdges;
var CircleOpac;
var indx_shape;
var Drawing;
var FirstUndoClick;
var Exit;
var Actionsincldel;
var ActionsNotincldel;
var NoDels;
var DrawRTs;
var DelRTs;
var LineLengths;
var LineDurations;
var startTime;
var Diff;
var timeRemaining;
var gotValidClick;
var DrawingTrialMaxDuration;
var DrawingTrialComponents;
function DrawingTrialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'DrawingTrial' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    DrawingTrialClock.reset();
    routineTimer.reset();
    DrawingTrialMaxDurationReached = false;
    // update component parameters for each repeat
    image1.setImage(ShowIm);
    // Run 'Begin Routine' code from code_3
    class ShapeStimCustom extends visual.ShapeStim {
      _getPixiPolygon() {
        super._getPixiPolygon()
        this._pixiPolygon_px.closeStroke = this._closeShape;
        return this._pixiPolygon_px;
      }
    }
    
    polygon_vertex = [[0, 0]];
    polygon_vertex = [];
    polygon_list = [];
    Empty_shapes = 100;
    for (var i = 0, _pj_a = Empty_shapes; (i < _pj_a); i += 1) {
        let i_polygon = new ShapeStimCustom({win: psychoJS.window, 
        "vertices": polygon_vertex, 
        "closeShape": false, 
        "lineWidth": 4, 
        lineColor: new util.Color([-1, -1, -1])});
        i_polygon.setAutoDraw(false);
        polygon_list.push(i_polygon);
    }
    
    CircleListList = [];
    CircleList=[];
    CircleCordsList=[];
    
    CircleSize=[0.004,0.004];
    CircleEdges=99;
    CircleOpac=1;
    
    indx_shape = 0;
    Drawing = false;
    FirstUndoClick = true;
    Exit = false;
    Actionsincldel = 0;
    ActionsNotincldel = 0;
    NoDels = 0;
    DrawRTs = [];
    DelRTs = [];
    LineLengths = [];
    LineDurations = [];
    
    startTime = globalClock.getTime();
    Diff=0
    timeRemaining=SketchTime
    // setup some python lists for storing info about the mymouse
    gotValidClick = false; // until a click is received
    psychoJS.experiment.addData('DrawingTrial.started', globalClock.getTime());
    DrawingTrialMaxDuration = null
    // keep track of which components have finished
    DrawingTrialComponents = [];
    DrawingTrialComponents.push(image1);
    DrawingTrialComponents.push(mymouse);
    DrawingTrialComponents.push(UndoButton);
    DrawingTrialComponents.push(UndoText);
    DrawingTrialComponents.push(timer);
    
    for (const thisComponent of DrawingTrialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var Minutes;
var Seconds;
var minstring;
var secstring;
var timeText;
var polygon;
var LastMouse;
var MousePos;
var LineStartTime;
var CircleX;
function DrawingTrialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'DrawingTrial' ---
    // get current time
    t = DrawingTrialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image1* updates
    if (t >= 0.0 && image1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image1.tStart = t;  // (not accounting for frame time here)
      image1.frameNStart = frameN;  // exact frame index
      
      image1.setAutoDraw(true);
    }
    
    
    // if image1 is active this frame...
    if (image1.status === PsychoJS.Status.STARTED) {
    }
    
    // Run 'Each Frame' code from code_3
    var Diff, Minutes, Seconds, minstring, secstring, timeText, polygon;
    
    Diff = (globalClock.getTime() - startTime);
    timeRemaining = (SketchTime - Math.floor(Diff));
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
    //timeText = (ImageNum.toString() + "     " + ImageOrder[1].toString());
    
    if ((timeRemaining <= 0)) {
        Exit = true;
        continueRoutine = false;
    }
    polygon = polygon_list[indx_shape];
    if (mymouse.isPressedIn(image1)  && (timeRemaining > 0)) {
       LastMouse=MousePos;
        MousePos=mymouse.getPos();
        if ((! Drawing)) {
            Drawing = true;
            polygon_vertex = [];
            DrawRTs.push(globalClock.getTime() - startTime);
            LineStartTime = globalClock.getTime();
            //draw a circle
            CircleX = new visual.Polygon ({
            win: psychoJS.window, 
            name: 'polygon_2', units : 'height', 
            edges: CircleEdges, 
            size: CircleSize,
            ori: 0, 
            pos: MousePos,
            lineWidth: 1, 
            lineColor: new util.Color([-1, -1, -1]),
            fillColor: new util.Color([-1, -1, -1]),
            opacity: 1, depth: -1, interpolate: true,});
            CircleX.setAutoDraw(true);
            CircleList.push(CircleX); //draw a first circle, and push it to CircleList
            CircleCordsList.push(MousePos);
        } //and if already drawing
        polygon_vertex.push(mymouse.getPos());
        polygon.setVertices(polygon_vertex);
        if (LastMouse!=MousePos) {
            //if coords have changed,
        //draw another circle
            CircleX = new visual.Polygon ({
            win: psychoJS.window, 
            name: 'polygon_2', units : 'height', 
            edges: CircleEdges, 
            size: CircleSize,
            ori: 0, 
            pos: MousePos,
            lineWidth: 1, 
            lineColor: new util.Color([-1, -1, -1]),
            fillColor: new util.Color([-1, -1, -1]),
            opacity: 1, depth: -1, interpolate: true,});
            CircleX.setAutoDraw(true);
            CircleList.push(CircleX); //draw a first circle, and push it to CircleList
        }
    } else { //mouse stops being clicked
        if (Drawing) {
            Drawing = false;
            LineLengths.push(polygon.vertices.length);
            LineDurations.push((globalClock.getTime() - LineStartTime));
            indx_shape += 1;
            Actionsincldel += 1;
            ActionsNotincldel += 1;
            CircleListList.push(CircleList); //add new set of circles to circle list 
            CircleList=[];
        }
    }
    if (((mymouse.isPressedIn(UndoButton) && FirstUndoClick) && (indx_shape > 0))) {
        //UndoButton.fillColor = "white";
        indx_shape -= 1;
        polygon = polygon_list[indx_shape];
        polygon.vertices = [[0, 0]];
        FirstUndoClick = false;
        NoDels += 1;
        DelRTs.push((globalClock.getTime() - startTime));
        ActionsNotincldel -= 1;
        
        // set older circles to be not drawn
        for (var i_pol2 = 0, _pj_a2 = (CircleListList[indx_shape].length); (i_pol2 < _pj_a2); i_pol2 += 1) {
        CircleListList[indx_shape][i_pol2].setAutoDraw(false);
        CircleListList[indx_shape][i_pol2].opacity = 0;
        } 
        //remove last list of circles
        CircleListList[indx_shape]=[];
        CircleListList.pop();
        CircleCordsList.pop();//and list of coords
        
    } else if ((! mymouse.isPressedIn(UndoButton))) {
            //UndoButton.fillColor = "darkgray";
            FirstUndoClick = true;
        }
    
    
    image1.draw();
    for (var i_pol = 0, _pj_a = (indx_shape + 1); (i_pol < _pj_a); i_pol += 1) {
        polygon_list[i_pol].setAutoDraw(true);
        polygon_list[i_pol].draw();
    }
    //if (Exit) {
    //    continueRoutine = false;
    //}
    
    
    
    // *UndoButton* updates
    if (t >= 0 && UndoButton.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      UndoButton.tStart = t;  // (not accounting for frame time here)
      UndoButton.frameNStart = frameN;  // exact frame index
      
      UndoButton.setAutoDraw(true);
    }
    
    
    // if UndoButton is active this frame...
    if (UndoButton.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *UndoText* updates
    if (t >= 0 && UndoText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      UndoText.tStart = t;  // (not accounting for frame time here)
      UndoText.frameNStart = frameN;  // exact frame index
      
      UndoText.setAutoDraw(true);
    }
    
    
    // if UndoText is active this frame...
    if (UndoText.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *timer* updates
    if (t >= 0 && timer.status === PsychoJS.Status.NOT_STARTED) {
      // update params
      timer.setText(timeText, false);
      // keep track of start time/frame for later
      timer.tStart = t;  // (not accounting for frame time here)
      timer.frameNStart = frameN;  // exact frame index
      
      timer.setAutoDraw(true);
    }
    
    
    // if timer is active this frame...
    if (timer.status === PsychoJS.Status.STARTED) {
      // update params
      timer.setText(timeText, false);
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
    for (const thisComponent of DrawingTrialComponents)
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


var AllPolygonVertices;
function DrawingTrialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'DrawingTrial' ---
    for (const thisComponent of DrawingTrialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('DrawingTrial.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_3
    var addname, NoCircs, Temp
    psychoJS.experiment.addData("StartImage", CurrentDraw)
    
    AllPolygonVertices=[]
    
    psychoJS.experiment.addData("ActionsNotincldel", ActionsNotincldel)
    psychoJS.experiment.addData("Actionsincldel", Actionsincldel)
    psychoJS.experiment.addData("NoDels", NoDels)
    psychoJS.experiment.addData("DrawRTs", DrawRTs)
    psychoJS.experiment.addData("DelRTs", DelRTs)
    psychoJS.experiment.addData("LineLengths", LineLengths)
    psychoJS.experiment.addData("LineDurations", LineDurations)
        
    for (var i_pol = 0, _pj_a = indx_shape; (i_pol < _pj_a); i_pol += 1) {
        polygon_list[i_pol].setAutoDraw(false);
        //Temp=polygon_list[i_pol].vertices;
        //Temp=Temp.toString()
        AllPolygonVertices.push(polygon_list[i_pol].vertices);
        //addname = ("Line" + i_pol.toString());
        //psychoJS.experiment.addData(addname, polygon_list[i_pol].vertices)
    }
    
    for (var i_pol = 0, _pj_a = (CircleListList.length); (i_pol < _pj_a); i_pol += 1) {
        NoCircs=CircleListList[i_pol].length;
        for (var i_pol2 = 0, _pj_a2 = NoCircs; (i_pol2 < _pj_a2); i_pol2 += 1) {
        CircleListList[i_pol][i_pol2].setAutoDraw(false);
        }
    }
    
    
    psychoJS.experiment.addData("Circles", CircleCordsList);
    psychoJS.experiment.addData("Lines", AllPolygonVertices)
    //clear all circles
    CircleList=[];
    CircleListList=[];
    //psychoJS.window.color = (0, 0, 0)
    //psychoJS.window.clearBuffer({"color": true})
    //psychoJS.window.depthMask = true
    //psychoJS.window.clearBuffer({"color": false, "depth": true, "stencil": false});
    //psychoJS.window.flip({"clearBuffer": true});
    
    // store data for psychoJS.experiment (ExperimentHandler)
    // the Routine "DrawingTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var DrawInstrux_2MaxDurationReached;
var _key_resp_2_allKeys;
var DrawInstrux_2MaxDuration;
var DrawInstrux_2Components;
function DrawInstrux_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'DrawInstrux_2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    DrawInstrux_2Clock.reset();
    routineTimer.reset();
    DrawInstrux_2MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // Run 'Begin Routine' code from code_5
    Prac=0;
    psychoJS.experiment.addData('DrawInstrux_2.started', globalClock.getTime());
    DrawInstrux_2MaxDuration = null
    // keep track of which components have finished
    DrawInstrux_2Components = [];
    DrawInstrux_2Components.push(DrawinstrucText_2);
    DrawInstrux_2Components.push(EnterToContinue_3);
    DrawInstrux_2Components.push(key_resp_2);
    
    for (const thisComponent of DrawInstrux_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function DrawInstrux_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'DrawInstrux_2' ---
    // get current time
    t = DrawInstrux_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *DrawinstrucText_2* updates
    if (t >= 0.0 && DrawinstrucText_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      DrawinstrucText_2.tStart = t;  // (not accounting for frame time here)
      DrawinstrucText_2.frameNStart = frameN;  // exact frame index
      
      DrawinstrucText_2.setAutoDraw(true);
    }
    
    
    // if DrawinstrucText_2 is active this frame...
    if (DrawinstrucText_2.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *EnterToContinue_3* updates
    if (t >= 0.0 && EnterToContinue_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      EnterToContinue_3.tStart = t;  // (not accounting for frame time here)
      EnterToContinue_3.frameNStart = frameN;  // exact frame index
      
      EnterToContinue_3.setAutoDraw(true);
    }
    
    
    // if EnterToContinue_3 is active this frame...
    if (EnterToContinue_3.status === PsychoJS.Status.STARTED) {
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
    for (const thisComponent of DrawInstrux_2Components)
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


function DrawInstrux_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'DrawInstrux_2' ---
    for (const thisComponent of DrawInstrux_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('DrawInstrux_2.stopped', globalClock.getTime());
    key_resp_2.stop();
    // the Routine "DrawInstrux_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trials_draw;
function trials_drawLoopBegin(trials_drawLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_draw = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'DrawStims.xlsx',
      seed: undefined, name: 'trials_draw'
    });
    psychoJS.experiment.addLoop(trials_draw); // add the loop to the experiment
    currentLoop = trials_draw;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrials_draw of trials_draw) {
      snapshot = trials_draw.getSnapshot();
      trials_drawLoopScheduler.add(importConditions(snapshot));
      trials_drawLoopScheduler.add(crossRoutineBegin(snapshot));
      trials_drawLoopScheduler.add(crossRoutineEachFrame());
      trials_drawLoopScheduler.add(crossRoutineEnd(snapshot));
      trials_drawLoopScheduler.add(DrawingTrialRoutineBegin(snapshot));
      trials_drawLoopScheduler.add(DrawingTrialRoutineEachFrame());
      trials_drawLoopScheduler.add(DrawingTrialRoutineEnd(snapshot));
      trials_drawLoopScheduler.add(trials_drawLoopEndIteration(trials_drawLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_drawLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_draw);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_drawLoopEndIteration(scheduler, snapshot) {
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
