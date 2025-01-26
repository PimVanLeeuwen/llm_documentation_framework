

ScheduledFuture (Java Platform SE 8 )





<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="ScheduledFuture (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->

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
java.util.concurrentInterface ScheduledFuture<V>
Type Parameters:
`V` - The result type returned by this Future

All Superinterfaces:
Comparable<Delayed>, Delayed, Future<V>

All Known Subinterfaces:
RunnableScheduledFuture<V>


```
public interface ScheduledFuture<V>
extends Delayed, Future<V>
```
A delayed result-bearing action that can be cancelled.
Usually a scheduled future is the result of scheduling
a task with a `ScheduledExecutorService`.
Since:
1.5

### Method Summary

### Methods inherited from interface java.util.concurrent.Delayed

`getDelay`

### Methods inherited from interface java.lang.Comparable

`compareTo`

### Methods inherited from interface java.util.concurrent.Future

`cancel, get, get, isCancelled, isDone`



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

