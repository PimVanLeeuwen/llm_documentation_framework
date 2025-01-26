

ThreadPoolExecutor.AbortPolicy (Java Platform SE 8 )






<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="ThreadPoolExecutor.AbortPolicy (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10};
var tabs = {65535:["t0","All Methods"],2:["t2","Instance Methods"],8:["t4","Concrete Methods"]};
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
java.util.concurrentClass ThreadPoolExecutor.AbortPolicy
java.lang.Objectjava.util.concurrent.ThreadPoolExecutor.AbortPolicy
All Implemented Interfaces:
RejectedExecutionHandler

Enclosing class:
ThreadPoolExecutor


```
public static class ThreadPoolExecutor.AbortPolicy
extends Object
implements RejectedExecutionHandler
```
A handler for rejected tasks that throws a
`RejectedExecutionException`.

### Constructor Summary

Constructors Constructor and Description`AbortPolicy()`
Creates an `AbortPolicy`.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`void``rejectedExecution(Runnable r,
ThreadPoolExecutor e)`
Always throws RejectedExecutionException.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Constructor Detail

#### AbortPolicy

```
public AbortPolicy()
```
Creates an `AbortPolicy`.

### Method Detail

#### rejectedExecution

```
public void rejectedExecution(Runnable r,
                              ThreadPoolExecutor e)
```
Always throws RejectedExecutionException.
Specified by:
`rejectedExecution` in interface `RejectedExecutionHandler`
Parameters:
`r` - the runnable task requested to be executed
`e` - the executor attempting to execute this task
Throws:
`RejectedExecutionException` - always




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

