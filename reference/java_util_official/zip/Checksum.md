

Checksum (Java Platform SE 8 )








<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="Checksum (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":6,"i1":6,"i2":6,"i3":6};
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
java.util.zipInterface Checksum
All Known Implementing Classes:
Adler32, CRC32


```
public interface Checksum
```
An interface representing a data checksum.

### Method Summary

All Methods Instance Methods Abstract Methods Modifier and TypeMethod and Description`long``getValue()`
Returns the current checksum value.`void``reset()`
Resets the checksum to its initial value.`void``update(byte[] b,
int off,
int len)`
Updates the current checksum with the specified array of bytes.`void``update(int b)`
Updates the current checksum with the specified byte.

### Method Detail

#### update

```
void update(int b)
```
Updates the current checksum with the specified byte.
Parameters:
`b` - the byte to update the checksum with

#### update

```
void update(byte[] b,
            int off,
            int len)
```
Updates the current checksum with the specified array of bytes.
Parameters:
`b` - the byte array to update the checksum with
`off` - the start offset of the data
`len` - the number of bytes to use for the update

#### getValue

```
long getValue()
```
Returns the current checksum value.
Returns:
the current checksum value

#### reset

```
void reset()
```
Resets the checksum to its initial value.



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

