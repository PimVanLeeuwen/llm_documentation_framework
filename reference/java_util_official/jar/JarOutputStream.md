

JarOutputStream (Java Platform SE 8 )






<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="JarOutputStream (Java Platform SE 8 )";
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
java.util.jarClass JarOutputStream
java.lang.Objectjava.io.OutputStreamjava.io.FilterOutputStreamjava.util.zip.DeflaterOutputStreamjava.util.zip.ZipOutputStreamjava.util.jar.JarOutputStream
All Implemented Interfaces:
Closeable, Flushable, AutoCloseable


```
public class JarOutputStream
extends ZipOutputStream
```
The `JarOutputStream` class is used to write the contents
of a JAR file to any output stream. It extends the class
`java.util.zip.ZipOutputStream` with support
for writing an optional `Manifest` entry. The
`Manifest` can be used to specify meta-information about
the JAR file and its entries.
Since:
1.2
See Also:
`Manifest`,
`ZipOutputStream`

### Field Summary

Fields Modifier and TypeField and Description`static int``CENATT``static int``CENATX``static int``CENCOM``static int``CENCRC``static int``CENDSK``static int``CENEXT``static int``CENFLG``static int``CENHDR``static int``CENHOW``static int``CENLEN``static int``CENNAM``static int``CENOFF``static long``CENSIG``static int``CENSIZ``static int``CENTIM``static int``CENVEM``static int``CENVER``static int``ENDCOM``static int``ENDHDR``static int``ENDOFF``static long``ENDSIG``static int``ENDSIZ``static int``ENDSUB``static int``ENDTOT``static int``EXTCRC``static int``EXTHDR``static int``EXTLEN``static long``EXTSIG``static int``EXTSIZ``static int``LOCCRC``static int``LOCEXT``static int``LOCFLG``static int``LOCHDR``static int``LOCHOW``static int``LOCLEN``static int``LOCNAM``static long``LOCSIG``static int``LOCSIZ``static int``LOCTIM``static int``LOCVER`

### Fields inherited from class java.util.zip.ZipOutputStream

`DEFLATED, STORED`

### Fields inherited from class java.util.zip.DeflaterOutputStream

`buf, def`

### Fields inherited from class java.io.FilterOutputStream

`out`

### Constructor Summary

Constructors Constructor and Description`JarOutputStream(OutputStream out)`
Creates a new `JarOutputStream` with no manifest.`JarOutputStream(OutputStream out,
Manifest man)`
Creates a new `JarOutputStream` with the specified
`Manifest`.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`void``putNextEntry(ZipEntry ze)`
Begins writing a new JAR file entry and positions the stream
to the start of the entry data.

### Methods inherited from class java.util.zip.ZipOutputStream

`close, closeEntry, finish, setComment, setLevel, setMethod, write`

### Methods inherited from class java.util.zip.DeflaterOutputStream

`deflate, flush, write`

### Methods inherited from class java.io.FilterOutputStream

`write`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

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

#### JarOutputStream

```
public JarOutputStream(OutputStream out,
                       Manifest man)
                throws IOException
```
Creates a new `JarOutputStream` with the specified
`Manifest`. The manifest is written as the first
entry to the output stream.
Parameters:
`out` - the actual output stream
`man` - the optional `Manifest`
Throws:
`IOException` - if an I/O error has occurred

#### JarOutputStream

```
public JarOutputStream(OutputStream out)
                throws IOException
```
Creates a new `JarOutputStream` with no manifest.
Parameters:
`out` - the actual output stream
Throws:
`IOException` - if an I/O error has occurred

### Method Detail

#### putNextEntry

```
public void putNextEntry(ZipEntry ze)
                  throws IOException
```
Begins writing a new JAR file entry and positions the stream
to the start of the entry data. This method will also close
any previous entry. The default compression method will be
used if no compression method was specified for the entry.
The current time will be used if the entry has no set modification
time.
Overrides:
`putNextEntry` in class `ZipOutputStream`
Parameters:
`ze` - the ZIP/JAR entry to be written
Throws:
`ZipException` - if a ZIP error has occurred
`IOException` - if an I/O error has occurred




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

