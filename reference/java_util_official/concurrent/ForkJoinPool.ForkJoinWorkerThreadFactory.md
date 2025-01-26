

ForkJoinPool.ForkJoinWorkerThreadFactory (Java Platform SE 8 )






<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="ForkJoinPool.ForkJoinWorkerThreadFactory (Java Platform SE 8 )";
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
java.util.concurrentInterface ForkJoinPool.ForkJoinWorkerThreadFactory
Enclosing class:
ForkJoinPool


```
public static interface ForkJoinPool.ForkJoinWorkerThreadFactory
```
Factory for creating new `ForkJoinWorkerThread`s.
A `ForkJoinWorkerThreadFactory` must be defined and used
for `ForkJoinWorkerThread` subclasses that extend base
functionality or initialize threads with different contexts.

### Method Summary

All Methods Instance Methods Abstract Methods Modifier and TypeMethod and Description`ForkJoinWorkerThread``newThread(ForkJoinPool pool)`
Returns a new worker thread operating in the given pool.

### Method Detail

#### newThread

```
ForkJoinWorkerThread newThread(ForkJoinPool pool)
```
Returns a new worker thread operating in the given pool.
Parameters:
`pool` - the pool this thread works in
Returns:
the new worker thread
Throws:
`NullPointerException` - if the pool is null




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

