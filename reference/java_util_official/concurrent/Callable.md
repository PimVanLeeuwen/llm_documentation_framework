

Callable (Java Platform SE 8 )






<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="Callable (Java Platform SE 8 )";
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
java.util.concurrentInterface Callable<V>
Type Parameters:
`V` - the result type of method `call`

All Known Subinterfaces:
DocumentationTool.DocumentationTask, JavaCompiler.CompilationTask

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.


```
@FunctionalInterface
public interface Callable<V>
```
A task that returns a result and may throw an exception.
Implementors define a single method with no arguments called
`call`.The `Callable` interface is similar to `Runnable`, in that both are designed for classes whose
instances are potentially executed by another thread. A
`Runnable`, however, does not return a result and cannot
throw a checked exception.The `Executors` class contains utility methods to
convert from other common forms to `Callable` classes.
Since:
1.5
See Also:
`Executor`

### Method Summary

All Methods Instance Methods Abstract Methods Modifier and TypeMethod and Description`V``call()`
Computes a result, or throws an exception if unable to do so.

### Method Detail

#### call

```
V call()
throws Exception
```
Computes a result, or throws an exception if unable to do so.
Returns:
computed result
Throws:
`Exception` - if unable to compute a result




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

