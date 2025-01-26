

RejectedExecutionHandler (Java Platform SE 8 )






<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="RejectedExecutionHandler (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":6};
var tabs = {65535:["t0","All Methods"],2:["t2","Instance Methods"],4:["t3","Abstract Methods"]};
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
java.util.concurrentInterface RejectedExecutionHandler
All Known Implementing Classes:
ThreadPoolExecutor.AbortPolicy, ThreadPoolExecutor.CallerRunsPolicy, ThreadPoolExecutor.DiscardOldestPolicy, ThreadPoolExecutor.DiscardPolicy


```
public interface RejectedExecutionHandler
```
A handler for tasks that cannot be executed by a `ThreadPoolExecutor`.
Since:
1.5

### Method Summary

All Methods Instance Methods Abstract Methods Modifier and TypeMethod and Description`void``rejectedExecution(Runnable r,
ThreadPoolExecutor executor)`
Method that may be invoked by a `ThreadPoolExecutor` when
`execute` cannot accept a
task.

### Method Detail

#### rejectedExecution

```
void rejectedExecution(Runnable r,
                       ThreadPoolExecutor executor)
```
Method that may be invoked by a `ThreadPoolExecutor` when
`execute` cannot accept a
task. This may occur when no more threads or queue slots are
available because their bounds would be exceeded, or upon
shutdown of the Executor.In the absence of other alternatives, the method may throw
an unchecked `RejectedExecutionException`, which will be
propagated to the caller of `execute`.
Parameters:
`r` - the runnable task requested to be executed
`executor` - the executor attempting to execute this task
Throws:
`RejectedExecutionException` - if there is no remedy




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

