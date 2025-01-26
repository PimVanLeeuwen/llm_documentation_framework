

JarInputStream (Java Platform SE 8 )










<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="JarInputStream (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10,"i1":10,"i2":10,"i3":10,"i4":10};
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
java.util.jarClass JarInputStream
java.lang.Objectjava.io.InputStreamjava.io.FilterInputStreamjava.util.zip.InflaterInputStreamjava.util.zip.ZipInputStreamjava.util.jar.JarInputStream
All Implemented Interfaces:
Closeable, AutoCloseable


```
public class JarInputStream
extends ZipInputStream
```
The `JarInputStream` class is used to read the contents of
a JAR file from any input stream. It extends the class
`java.util.zip.ZipInputStream` with support for reading
an optional `Manifest` entry. The `Manifest`
can be used to store meta-information about the JAR file and its entries.
Since:
1.2
See Also:
`Manifest`,
`ZipInputStream`

### Field Summary

Fields Modifier and TypeField and Description`static int``CENATT``static int``CENATX``static int``CENCOM``static int``CENCRC``static int``CENDSK``static int``CENEXT``static int``CENFLG``static int``CENHDR``static int``CENHOW``static int``CENLEN``static int``CENNAM``static int``CENOFF``static long``CENSIG``static int``CENSIZ``static int``CENTIM``static int``CENVEM``static int``CENVER``static int``ENDCOM``static int``ENDHDR``static int``ENDOFF``static long``ENDSIG``static int``ENDSIZ``static int``ENDSUB``static int``ENDTOT``static int``EXTCRC``static int``EXTHDR``static int``EXTLEN``static long``EXTSIG``static int``EXTSIZ``static int``LOCCRC``static int``LOCEXT``static int``LOCFLG``static int``LOCHDR``static int``LOCHOW``static int``LOCLEN``static int``LOCNAM``static long``LOCSIG``static int``LOCSIZ``static int``LOCTIM``static int``LOCVER`

### Fields inherited from class java.util.zip.InflaterInputStream

`buf, inf, len`

### Fields inherited from class java.io.FilterInputStream

`in`

### Constructor Summary

Constructors Constructor and Description`JarInputStream(InputStream in)`
Creates a new `JarInputStream` and reads the optional
manifest.`JarInputStream(InputStream in,
boolean verify)`
Creates a new `JarInputStream` and reads the optional
manifest.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`protected ZipEntry``createZipEntry(String name)`
Creates a new `JarEntry` (`ZipEntry`) for the
specified JAR file entry name.`Manifest``getManifest()`
Returns the `Manifest` for this JAR file, or
`null` if none.`ZipEntry``getNextEntry()`
Reads the next ZIP file entry and positions the stream at the
beginning of the entry data.`JarEntry``getNextJarEntry()`
Reads the next JAR file entry and positions the stream at the
beginning of the entry data.`int``read(byte[] b,
int off,
int len)`
Reads from the current JAR file entry into an array of bytes.

### Methods inherited from class java.util.zip.ZipInputStream

`available, close, closeEntry, skip`

### Methods inherited from class java.util.zip.InflaterInputStream

`fill, mark, markSupported, read, reset`

### Methods inherited from class java.io.FilterInputStream

`read`

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

#### JarInputStream

```
public JarInputStream(InputStream in)
               throws IOException
```
Creates a new `JarInputStream` and reads the optional
manifest. If a manifest is present, also attempts to verify
the signatures if the JarInputStream is signed.
Parameters:
`in` - the actual input stream
Throws:
`IOException` - if an I/O error has occurred

#### JarInputStream

```
public JarInputStream(InputStream in,
                      boolean verify)
               throws IOException
```
Creates a new `JarInputStream` and reads the optional
manifest. If a manifest is present and verify is true, also attempts
to verify the signatures if the JarInputStream is signed.
Parameters:
`in` - the actual input stream
`verify` - whether or not to verify the JarInputStream if
it is signed.
Throws:
`IOException` - if an I/O error has occurred

### Method Detail

#### getManifest

```
public Manifest getManifest()
```
Returns the `Manifest` for this JAR file, or
`null` if none.
Returns:
the `Manifest` for this JAR file, or
`null` if none.

#### getNextEntry

```
public ZipEntry getNextEntry()
                      throws IOException
```
Reads the next ZIP file entry and positions the stream at the
beginning of the entry data. If verification has been enabled,
any invalid signature detected while positioning the stream for
the next entry will result in an exception.
Overrides:
`getNextEntry` in class `ZipInputStream`
Returns:
the next ZIP file entry, or null if there are no more entries
Throws:
`ZipException` - if a ZIP file error has occurred
`IOException` - if an I/O error has occurred
`SecurityException` - if any of the jar file entries
are incorrectly signed.

#### getNextJarEntry

```
public JarEntry getNextJarEntry()
                         throws IOException
```
Reads the next JAR file entry and positions the stream at the
beginning of the entry data. If verification has been enabled,
any invalid signature detected while positioning the stream for
the next entry will result in an exception.
Returns:
the next JAR file entry, or null if there are no more entries
Throws:
`ZipException` - if a ZIP file error has occurred
`IOException` - if an I/O error has occurred
`SecurityException` - if any of the jar file entries
are incorrectly signed.

#### read

```
public int read(byte[] b,
                int off,
                int len)
         throws IOException
```
Reads from the current JAR file entry into an array of bytes.
If `len` is not zero, the method
blocks until some input is available; otherwise, no
bytes are read and `0` is returned.
If verification has been enabled, any invalid signature
on the current entry will be reported at some point before the
end of the entry is reached.
Overrides:
`read` in class `ZipInputStream`
Parameters:
`b` - the buffer into which the data is read
`off` - the start offset in the destination array `b`
`len` - the maximum number of bytes to read
Returns:
the actual number of bytes read, or -1 if the end of the
entry is reached
Throws:
`NullPointerException` - If `b` is `null`.
`IndexOutOfBoundsException` - If `off` is negative,
`len` is negative, or `len` is greater than
`b.length - off`
`ZipException` - if a ZIP file error has occurred
`IOException` - if an I/O error has occurred
`SecurityException` - if any of the jar file entries
are incorrectly signed.
See Also:
`FilterInputStream.in`

#### createZipEntry

```
protected ZipEntry createZipEntry(String name)
```
Creates a new `JarEntry` (`ZipEntry`) for the
specified JAR file entry name. The manifest attributes of
the specified JAR file entry name will be copied to the new
`JarEntry`.
Overrides:
`createZipEntry` in class `ZipInputStream`
Parameters:
`name` - the name of the JAR/ZIP file entry
Returns:
the `JarEntry` object just created




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

