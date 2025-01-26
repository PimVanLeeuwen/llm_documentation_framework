

Pack200.Unpacker (Java Platform SE 8 )














<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="Pack200.Unpacker (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":50,"i1":6,"i2":50,"i3":6,"i4":6};
var tabs = {65535:["t0","All Methods"],2:["t2","Instance Methods"],4:["t3","Abstract Methods"],16:["t5","Default Methods"],32:["t6","Deprecated Methods"]};
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
java.util.jarInterface Pack200.Unpacker
Enclosing class:
Pack200


```
public static interface Pack200.Unpacker
```
The unpacker engine converts the packed stream to a JAR file.
An instance of the engine can be obtained
using `Pack200.newUnpacker()`.Every JAR file produced by this engine will include the string
"PACK200" as a zip file comment.
This allows a deployer to detect if a JAR archive was packed and unpacked.Note: Unless otherwise noted, passing a null argument to a
constructor or method in this class will cause a `NullPointerException`
to be thrown.This version of the unpacker is compatible with all previous versions.
Since:
1.5

### Field Summary

Fields Modifier and TypeField and Description`static String``DEFLATE_HINT`
Property indicating that the unpacker should
ignore all transmitted values for DEFLATE\_HINT,
replacing them by the given value, `TRUE` or `FALSE`.`static String``FALSE`
The string "false", a possible value for certain properties.`static String``KEEP`
The string "keep", a possible value for certain properties.`static String``PROGRESS`
The unpacker's progress as a percentage, as periodically
updated by the unpacker.`static String``TRUE`
The string "true", a possible value for certain properties.

### Method Summary

All Methods Instance Methods Abstract Methods Default Methods Deprecated Methods Modifier and TypeMethod and Description`default void``addPropertyChangeListener(PropertyChangeListener listener)`
Deprecated. 
The dependency on `PropertyChangeListener` creates
a significant impediment to future modularization of the
Java platform. This method will be removed in a future
release.
Applications that need to monitor progress of the
unpacker can poll the value of the `PROGRESS` property instead.
`SortedMap<String,String>``properties()`
Get the set of this engine's properties.`default void``removePropertyChangeListener(PropertyChangeListener listener)`
Deprecated. 
The dependency on `PropertyChangeListener` creates
a significant impediment to future modularization of the
Java platform. This method will be removed in a future
release.
`void``unpack(File in,
JarOutputStream out)`
Read a Pack200 archive, and write the encoded JAR to
a JarOutputStream.`void``unpack(InputStream in,
JarOutputStream out)`
Read a Pack200 archive, and write the encoded JAR to
a JarOutputStream.

### Field Detail

#### KEEP

```
static final String KEEP
```
The string "keep", a possible value for certain properties.
See Also:
`DEFLATE_HINT`,
Constant Field Values

#### TRUE

```
static final String TRUE
```
The string "true", a possible value for certain properties.
See Also:
`DEFLATE_HINT`,
Constant Field Values

#### FALSE

```
static final String FALSE
```
The string "false", a possible value for certain properties.
See Also:
`DEFLATE_HINT`,
Constant Field Values

#### DEFLATE\_HINT

```
static final String DEFLATE_HINT
```
Property indicating that the unpacker should
ignore all transmitted values for DEFLATE\_HINT,
replacing them by the given value, `TRUE` or `FALSE`.
The default value is the special string `KEEP`,
which asks the unpacker to preserve all transmitted
deflation hints.
See Also:
Constant Field Values

#### PROGRESS

```
static final String PROGRESS
```
The unpacker's progress as a percentage, as periodically
updated by the unpacker.
Values of 0 - 100 are normal, and -1 indicates a stall.
Progress can be monitored by polling the value of this
property.At a minimum, the unpacker must set progress to 0
at the beginning of a packing operation, and to 100
at the end.
See Also:
Constant Field Values

### Method Detail

#### properties

```
SortedMap<String,String> properties()
```
Get the set of this engine's properties. This set is
a "live view", so that changing its
contents immediately affects the Packer engine, and
changes from the engine (such as progress indications)
are immediately visible in the map.The property map may contain pre-defined implementation
specific and default properties. Users are encouraged to
read the information and fully understand the implications,
before modifying pre-existing properties.Implementation specific properties are prefixed with a
package name associated with the implementor, beginning
with com. or a similar prefix.
All property names beginning with pack. and
unpack. are reserved for use by this API.Unknown properties may be ignored or rejected with an
unspecified error, and invalid entries may cause an
unspecified error to be thrown.
Returns:
A sorted association of option key strings to option values.

#### unpack

```
void unpack(InputStream in,
            JarOutputStream out)
     throws IOException
```
Read a Pack200 archive, and write the encoded JAR to
a JarOutputStream.
The entire contents of the input stream will be read.
It may be more efficient to read the Pack200 archive
to a file and pass the File object, using the alternate
method described below.Closes its input but not its output. (The output can accumulate more elements.)
Parameters:
`in` - an InputStream.
`out` - a JarOutputStream.
Throws:
`IOException` - if an error is encountered.

#### unpack

```
void unpack(File in,
            JarOutputStream out)
     throws IOException
```
Read a Pack200 archive, and write the encoded JAR to
a JarOutputStream.Does not close its output. (The output can accumulate more elements.)
Parameters:
`in` - a File.
`out` - a JarOutputStream.
Throws:
`IOException` - if an error is encountered.

#### addPropertyChangeListener

```
@Deprecated
default void addPropertyChangeListener(PropertyChangeListener listener)
```
Deprecated. The dependency on `PropertyChangeListener` creates
a significant impediment to future modularization of the
Java platform. This method will be removed in a future
release.
Applications that need to monitor progress of the
unpacker can poll the value of the `PROGRESS` property instead.
Registers a listener for PropertyChange events on the properties map.
This is typically used by applications to update a progress bar.The default implementation of this method does nothing and has
no side-effects.WARNING: This method is omitted from the interface
declaration in all subset Profiles of Java SE that do not include
the `java.beans` package.
Parameters:
`listener` - An object to be invoked when a property is changed.
See Also:
`properties()`,
`PROGRESS`

#### removePropertyChangeListener

```
@Deprecated
default void removePropertyChangeListener(PropertyChangeListener listener)
```
Deprecated. The dependency on `PropertyChangeListener` creates
a significant impediment to future modularization of the
Java platform. This method will be removed in a future
release.
Remove a listener for PropertyChange events, added by
the `addPropertyChangeListener(java.beans.PropertyChangeListener)`.The default implementation of this method does nothing and has
no side-effects.WARNING: This method is omitted from the interface
declaration in all subset Profiles of Java SE that do not include
the `java.beans` package.
Parameters:
`listener` - The PropertyChange listener to be removed.
See Also:
`addPropertyChangeListener(java.beans.PropertyChangeListener)`




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

