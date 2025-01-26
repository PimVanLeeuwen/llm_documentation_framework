

RunnableScheduledFuture (Java Platform SE 8 )






<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="RunnableScheduledFuture (Java Platform SE 8 )";
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
java.util.concurrentInterface RunnableScheduledFuture<V>
Type Parameters:
`V` - The result type returned by this Future's `get` method

All Superinterfaces:
Comparable<Delayed>, Delayed, Future<V>, Runnable, RunnableFuture<V>, ScheduledFuture<V>


```
public interface RunnableScheduledFuture<V>
extends RunnableFuture<V>, ScheduledFuture<V>
```
A `ScheduledFuture` that is `Runnable`. Successful
execution of the `run` method causes completion of the
`Future` and allows access to its results.
Since:
1.6
See Also:
`FutureTask`,
`Executor`

### Method Summary

All Methods Instance Methods Abstract Methods Modifier and TypeMethod and Description`boolean``isPeriodic()`
Returns `true` if this task is periodic.

### Methods inherited from interface java.util.concurrent.RunnableFuture

`run`

### Methods inherited from interface java.util.concurrent.Delayed

`getDelay`

### Methods inherited from interface java.lang.Comparable

`compareTo`

### Methods inherited from interface java.util.concurrent.Future

`cancel, get, get, isCancelled, isDone`

### Method Detail

#### isPeriodic

```
boolean isPeriodic()
```
Returns `true` if this task is periodic. A periodic task may
re-run according to some schedule. A non-periodic task can be
run only once.
Returns:
`true` if this task is periodic




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

