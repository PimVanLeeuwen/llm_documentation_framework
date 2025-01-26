

ThreadFactory (Java Platform SE 8 )






<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="ThreadFactory (Java Platform SE 8 )";
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
java.util.concurrentInterface ThreadFactory
```
public interface ThreadFactory
```
An object that creates new threads on demand. Using thread factories
removes hardwiring of calls to `new Thread`,
enabling applications to use special thread subclasses, priorities, etc.The simplest implementation of this interface is just:
```
 
 class SimpleThreadFactory implements ThreadFactory {
   public Thread newThread(Runnable r) {
     return new Thread(r);
   }
 }
```
The `Executors.defaultThreadFactory()` method provides a more
useful simple implementation, that sets the created thread context
to known values before returning it.
Since:
1.5

### Method Summary

All Methods Instance Methods Abstract Methods Modifier and TypeMethod and Description`Thread``newThread(Runnable r)`
Constructs a new `Thread`.

### Method Detail

#### newThread

```
Thread newThread(Runnable r)
```
Constructs a new `Thread`. Implementations may also initialize
priority, name, daemon status, `ThreadGroup`, etc.
Parameters:
`r` - a runnable to be executed by new thread instance
Returns:
constructed thread, or `null` if the request to
create a thread is rejected




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

