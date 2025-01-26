

ResourceBundleControlProvider (Java Platform SE 8 )






<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="ResourceBundleControlProvider (Java Platform SE 8 )";
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
java.util.spiInterface ResourceBundleControlProvider
```
public interface ResourceBundleControlProvider
```
An interface for service providers that provide implementations of `ResourceBundle.Control`. The default resource bundle loading
behavior of the `ResourceBundle.getBundle` factory methods that take
no `ResourceBundle.Control` instance can be modified with `ResourceBundleControlProvider` implementations.Provider implementations must be packaged using the Java Extension
Mechanism as installed extensions. Refer to `ServiceLoader`
for the extension packaging. Any installed `ResourceBundleControlProvider` implementations are loaded using `ServiceLoader` at the `ResourceBundle` class loading time.
Since:
1.8
See Also:
`ResourceBundle.getBundle`,
`ServiceLoader.loadInstalled(Class)`

### Method Summary

All Methods Instance Methods Abstract Methods Modifier and TypeMethod and Description`ResourceBundle.Control``getControl(String baseName)`
Returns a `ResourceBundle.Control` instance that is used
to handle resource bundle loading for the given `baseName`.

### Method Detail

#### getControl

```
ResourceBundle.Control getControl(String baseName)
```
Returns a `ResourceBundle.Control` instance that is used
to handle resource bundle loading for the given `baseName`. This method must return `null` if the given
`baseName` isn't handled by this provider.
Parameters:
`baseName` - the base name of the resource bundle
Returns:
a `ResourceBundle.Control` instance,
or `null` if the given `baseName` is not
applicable to this provider.
Throws:
`NullPointerException` - if `baseName` is `null`




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

