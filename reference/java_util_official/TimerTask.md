

TimerTask (Java Platform SE 8 )








<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="TimerTask (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10,"i1":6,"i2":10};
var tabs = {65535:["t0","All Methods"],2:["t2","Instance Methods"],4:["t3","Abstract Methods"],8:["t4","Concrete Methods"]};
var altColor = "altColor";
var rowColor = "rowColor";
var tableTab = "tableTab";
var activeTableTab = "activeTableTab";

JavaScript is disabled on your browser.


Skip navigation links

OverviewPackageClassUseTreeDeprecatedIndexHelpJava™ PlatformStandard Ed. 8

Prev ClassNext ClassFramesNo FramesAll Classes
<!--
allClassesLink = document.getElementById("allclasses\_navbar\_top");
if(window==top) {
allClassesLink.style.display = "block";
}
else {
allClassesLink.style.display = "none";
}
//-->


Summary:Nested |Field |Constr |MethodDetail:Field |Constr |Method




compact1, compact2, compact3
java.utilClass TimerTask
java.lang.Objectjava.util.TimerTask
All Implemented Interfaces:
Runnable


```
public abstract class TimerTask
extends Object
implements Runnable
```
A task that can be scheduled for one-time or repeated execution by a Timer.
Since:
1.3
See Also:
`Timer`

### Constructor Summary

Constructors ModifierConstructor and Description`protected` `TimerTask()`
Creates a new timer task.

### Method Summary

All Methods Instance Methods Abstract Methods Concrete Methods Modifier and TypeMethod and Description`boolean``cancel()`
Cancels this timer task.`abstract void``run()`
The action to be performed by this timer task.`long``scheduledExecutionTime()`
Returns the scheduled execution time of the most recent
actual execution of this task.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Constructor Detail

#### TimerTask

```
protected TimerTask()
```
Creates a new timer task.

### Method Detail

#### run

```
public abstract void run()
```
The action to be performed by this timer task.
Specified by:
`run` in interface `Runnable`
See Also:
`Thread.run()`

#### cancel

```
public boolean cancel()
```
Cancels this timer task. If the task has been scheduled for one-time
execution and has not yet run, or has not yet been scheduled, it will
never run. If the task has been scheduled for repeated execution, it
will never run again. (If the task is running when this call occurs,
the task will run to completion, but will never run again.)Note that calling this method from within the run method of
a repeating timer task absolutely guarantees that the timer task will
not run again.This method may be called repeatedly; the second and subsequent
calls have no effect.
Returns:
true if this task is scheduled for one-time execution and has
not yet run, or this task is scheduled for repeated execution.
Returns false if the task was scheduled for one-time execution
and has already run, or if the task was never scheduled, or if
the task was already cancelled. (Loosely speaking, this method
returns true if it prevents one or more scheduled
executions from taking place.)

#### scheduledExecutionTime

```
public long scheduledExecutionTime()
```
Returns the scheduled execution time of the most recent
actual execution of this task. (If this method is invoked
while task execution is in progress, the return value is the scheduled
execution time of the ongoing task execution.)This method is typically invoked from within a task's run method, to
determine whether the current execution of the task is sufficiently
timely to warrant performing the scheduled activity:
```

   public void run() {
       if (System.currentTimeMillis() - scheduledExecutionTime() >=
           MAX_TARDINESS)
               return;  // Too late; skip this execution.
       // Perform the task
   }
 
```
This method is typically not used in conjunction with
fixed-delay execution repeating tasks, as their scheduled
execution times are allowed to drift over time, and so are not terribly
significant.
Returns:
the time at which the most recent execution of this task was
scheduled to occur, in the format returned by Date.getTime().
The return value is undefined if the task has yet to commence
its first execution.
See Also:
`Date.getTime()`




Skip navigation links

OverviewPackageClassUseTreeDeprecatedIndexHelpJava™ PlatformStandard Ed. 8

Prev ClassNext ClassFramesNo FramesAll Classes
<!--
allClassesLink = document.getElementById("allclasses\_navbar\_bottom");
if(window==top) {
allClassesLink.style.display = "block";
}
else {
allClassesLink.style.display = "none";
}
//-->


Summary:Nested |Field |Constr |MethodDetail:Field |Constr |Method


 Submit a bug or feature For further API reference and developer documentation, see Java SE Documentation. That documentation contains more detailed, developer-targeted descriptions, with conceptual overviews, definitions of terms, workarounds, and working code examples. Copyright © 1993, 2025, Oracle and/or its affiliates. All rights reserved. Use is subject to license terms. Also see the documentation redistribution policy. 

