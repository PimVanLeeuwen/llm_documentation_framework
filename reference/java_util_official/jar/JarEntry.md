

JarEntry (Java Platform SE 8 )








<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="JarEntry (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10,"i1":10,"i2":10};
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
java.util.jarClass JarEntry
java.lang.Objectjava.util.zip.ZipEntryjava.util.jar.JarEntry
All Implemented Interfaces:
Cloneable


```
public class JarEntry
extends ZipEntry
```
This class is used to represent a JAR file entry.

### Field Summary

Fields Modifier and TypeField and Description`static int``CENATT``static int``CENATX``static int``CENCOM``static int``CENCRC``static int``CENDSK``static int``CENEXT``static int``CENFLG``static int``CENHDR``static int``CENHOW``static int``CENLEN``static int``CENNAM``static int``CENOFF``static long``CENSIG``static int``CENSIZ``static int``CENTIM``static int``CENVEM``static int``CENVER``static int``ENDCOM``static int``ENDHDR``static int``ENDOFF``static long``ENDSIG``static int``ENDSIZ``static int``ENDSUB``static int``ENDTOT``static int``EXTCRC``static int``EXTHDR``static int``EXTLEN``static long``EXTSIG``static int``EXTSIZ``static int``LOCCRC``static int``LOCEXT``static int``LOCFLG``static int``LOCHDR``static int``LOCHOW``static int``LOCLEN``static int``LOCNAM``static long``LOCSIG``static int``LOCSIZ``static int``LOCTIM``static int``LOCVER`

### Fields inherited from class java.util.zip.ZipEntry

`DEFLATED, STORED`

### Constructor Summary

Constructors Constructor and Description`JarEntry(JarEntry je)`
Creates a new `JarEntry` with fields taken from the
specified `JarEntry` object.`JarEntry(String name)`
Creates a new `JarEntry` for the specified JAR file
entry name.`JarEntry(ZipEntry ze)`
Creates a new `JarEntry` with fields taken from the
specified `ZipEntry` object.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`Attributes``getAttributes()`
Returns the `Manifest` `Attributes` for this
entry, or `null` if none.`Certificate[]``getCertificates()`
Returns the `Certificate` objects for this entry, or
`null` if none.`CodeSigner[]``getCodeSigners()`
Returns the `CodeSigner` objects for this entry, or
`null` if none.

### Methods inherited from class java.util.zip.ZipEntry

`clone, getComment, getCompressedSize, getCrc, getCreationTime, getExtra, getLastAccessTime, getLastModifiedTime, getMethod, getName, getSize, getTime, hashCode, isDirectory, setComment, setCompressedSize, setCrc, setCreationTime, setExtra, setLastAccessTime, setLastModifiedTime, setMethod, setSize, setTime, toString`

### Methods inherited from class java.lang.Object

`equals, finalize, getClass, notify, notifyAll, wait, wait, wait`

### Field Detail

#### LOCSIG

```
public static final long LOCSIG
```
See Also:
Constant Field Values

#### EXTSIG

```
public static final long EXTSIG
```
See Also:
Constant Field Values

#### CENSIG

```
public static final long CENSIG
```
See Also:
Constant Field Values

#### ENDSIG

```
public static final long ENDSIG
```
See Also:
Constant Field Values

#### LOCHDR

```
public static final int LOCHDR
```
See Also:
Constant Field Values

#### EXTHDR

```
public static final int EXTHDR
```
See Also:
Constant Field Values

#### CENHDR

```
public static final int CENHDR
```
See Also:
Constant Field Values

#### ENDHDR

```
public static final int ENDHDR
```
See Also:
Constant Field Values

#### LOCVER

```
public static final int LOCVER
```
See Also:
Constant Field Values

#### LOCFLG

```
public static final int LOCFLG
```
See Also:
Constant Field Values

#### LOCHOW

```
public static final int LOCHOW
```
See Also:
Constant Field Values

#### LOCTIM

```
public static final int LOCTIM
```
See Also:
Constant Field Values

#### LOCCRC

```
public static final int LOCCRC
```
See Also:
Constant Field Values

#### LOCSIZ

```
public static final int LOCSIZ
```
See Also:
Constant Field Values

#### LOCLEN

```
public static final int LOCLEN
```
See Also:
Constant Field Values

#### LOCNAM

```
public static final int LOCNAM
```
See Also:
Constant Field Values

#### LOCEXT

```
public static final int LOCEXT
```
See Also:
Constant Field Values

#### EXTCRC

```
public static final int EXTCRC
```
See Also:
Constant Field Values

#### EXTSIZ

```
public static final int EXTSIZ
```
See Also:
Constant Field Values

#### EXTLEN

```
public static final int EXTLEN
```
See Also:
Constant Field Values

#### CENVEM

```
public static final int CENVEM
```
See Also:
Constant Field Values

#### CENVER

```
public static final int CENVER
```
See Also:
Constant Field Values

#### CENFLG

```
public static final int CENFLG
```
See Also:
Constant Field Values

#### CENHOW

```
public static final int CENHOW
```
See Also:
Constant Field Values

#### CENTIM

```
public static final int CENTIM
```
See Also:
Constant Field Values

#### CENCRC

```
public static final int CENCRC
```
See Also:
Constant Field Values

#### CENSIZ

```
public static final int CENSIZ
```
See Also:
Constant Field Values

#### CENLEN

```
public static final int CENLEN
```
See Also:
Constant Field Values

#### CENNAM

```
public static final int CENNAM
```
See Also:
Constant Field Values

#### CENEXT

```
public static final int CENEXT
```
See Also:
Constant Field Values

#### CENCOM

```
public static final int CENCOM
```
See Also:
Constant Field Values

#### CENDSK

```
public static final int CENDSK
```
See Also:
Constant Field Values

#### CENATT

```
public static final int CENATT
```
See Also:
Constant Field Values

#### CENATX

```
public static final int CENATX
```
See Also:
Constant Field Values

#### CENOFF

```
public static final int CENOFF
```
See Also:
Constant Field Values

#### ENDSUB

```
public static final int ENDSUB
```
See Also:
Constant Field Values

#### ENDTOT

```
public static final int ENDTOT
```
See Also:
Constant Field Values

#### ENDSIZ

```
public static final int ENDSIZ
```
See Also:
Constant Field Values

#### ENDOFF

```
public static final int ENDOFF
```
See Also:
Constant Field Values

#### ENDCOM

```
public static final int ENDCOM
```
See Also:
Constant Field Values

### Constructor Detail

#### JarEntry

```
public JarEntry(String name)
```
Creates a new `JarEntry` for the specified JAR file
entry name.
Parameters:
`name` - the JAR file entry name
Throws:
`NullPointerException` - if the entry name is `null`
`IllegalArgumentException` - if the entry name is longer than
0xFFFF bytes.

#### JarEntry

```
public JarEntry(ZipEntry ze)
```
Creates a new `JarEntry` with fields taken from the
specified `ZipEntry` object.
Parameters:
`ze` - the `ZipEntry` object to create the
`JarEntry` from

#### JarEntry

```
public JarEntry(JarEntry je)
```
Creates a new `JarEntry` with fields taken from the
specified `JarEntry` object.
Parameters:
`je` - the `JarEntry` to copy

### Method Detail

#### getAttributes

```
public Attributes getAttributes()
                         throws IOException
```
Returns the `Manifest` `Attributes` for this
entry, or `null` if none.
Returns:
the `Manifest` `Attributes` for this
entry, or `null` if none
Throws:
`IOException` - if an I/O error has occurred

#### getCertificates

```
public Certificate[] getCertificates()
```
Returns the `Certificate` objects for this entry, or
`null` if none. This method can only be called once
the `JarEntry` has been completely verified by reading
from the entry input stream until the end of the stream has been
reached. Otherwise, this method will return `null`.The returned certificate array comprises all the signer certificates
that were used to verify this entry. Each signer certificate is
followed by its supporting certificate chain (which may be empty).
Each signer certificate and its supporting certificate chain are ordered
bottom-to-top (i.e., with the signer certificate first and the (root)
certificate authority last).
Returns:
the `Certificate` objects for this entry, or
`null` if none.

#### getCodeSigners

```
public CodeSigner[] getCodeSigners()
```
Returns the `CodeSigner` objects for this entry, or
`null` if none. This method can only be called once
the `JarEntry` has been completely verified by reading
from the entry input stream until the end of the stream has been
reached. Otherwise, this method will return `null`.The returned array comprises all the code signers that have signed
this entry.
Returns:
the `CodeSigner` objects for this entry, or
`null` if none.
Since:
1.5




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

