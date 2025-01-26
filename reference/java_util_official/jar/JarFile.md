

JarFile (Java Platform SE 8 )












<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="JarFile (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10,"i1":10,"i2":10,"i3":10,"i4":10,"i5":10};
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
java.util.jarClass JarFile
java.lang.Objectjava.util.zip.ZipFilejava.util.jar.JarFile
All Implemented Interfaces:
Closeable, AutoCloseable


```
public class JarFile
extends ZipFile
```
The `JarFile` class is used to read the contents of a jar file
from any file that can be opened with `java.io.RandomAccessFile`.
It extends the class `java.util.zip.ZipFile` with support
for reading an optional `Manifest` entry. The
`Manifest` can be used to specify meta-information about the
jar file and its entries.Unless otherwise noted, passing a null argument to a constructor
or method in this class will cause a `NullPointerException` to be
thrown.
If the verify flag is on when opening a signed jar file, the content of the
file is verified against its signature embedded inside the file. Please note
that the verification process does not include validating the signer's
certificate. A caller should inspect the return value of
`JarEntry.getCodeSigners()` to further determine if the signature
can be trusted.
Since:
1.2
See Also:
`Manifest`,
`ZipFile`,
`JarEntry`

### Field Summary

Fields Modifier and TypeField and Description`static int``CENATT``static int``CENATX``static int``CENCOM``static int``CENCRC``static int``CENDSK``static int``CENEXT``static int``CENFLG``static int``CENHDR``static int``CENHOW``static int``CENLEN``static int``CENNAM``static int``CENOFF``static long``CENSIG``static int``CENSIZ``static int``CENTIM``static int``CENVEM``static int``CENVER``static int``ENDCOM``static int``ENDHDR``static int``ENDOFF``static long``ENDSIG``static int``ENDSIZ``static int``ENDSUB``static int``ENDTOT``static int``EXTCRC``static int``EXTHDR``static int``EXTLEN``static long``EXTSIG``static int``EXTSIZ``static int``LOCCRC``static int``LOCEXT``static int``LOCFLG``static int``LOCHDR``static int``LOCHOW``static int``LOCLEN``static int``LOCNAM``static long``LOCSIG``static int``LOCSIZ``static int``LOCTIM``static int``LOCVER``static String``MANIFEST_NAME`
The JAR manifest file name.

### Fields inherited from class java.util.zip.ZipFile

`OPEN_DELETE, OPEN_READ`

### Constructor Summary

Constructors Constructor and Description`JarFile(File file)`
Creates a new `JarFile` to read from the specified
`File` object.`JarFile(File file,
boolean verify)`
Creates a new `JarFile` to read from the specified
`File` object.`JarFile(File file,
boolean verify,
int mode)`
Creates a new `JarFile` to read from the specified
`File` object in the specified mode.`JarFile(String name)`
Creates a new `JarFile` to read from the specified
file `name`.`JarFile(String name,
boolean verify)`
Creates a new `JarFile` to read from the specified
file `name`.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`Enumeration<JarEntry>``entries()`
Returns an enumeration of the zip file entries.`ZipEntry``getEntry(String name)`
Returns the `ZipEntry` for the given entry name or
`null` if not found.`InputStream``getInputStream(ZipEntry ze)`
Returns an input stream for reading the contents of the specified
zip file entry.`JarEntry``getJarEntry(String name)`
Returns the `JarEntry` for the given entry name or
`null` if not found.`Manifest``getManifest()`
Returns the jar file manifest, or `null` if none.`Stream<JarEntry>``stream()`
Return an ordered `Stream` over the ZIP file entries.

### Methods inherited from class java.util.zip.ZipFile

`close, finalize, getComment, getName, size`

### Methods inherited from class java.lang.Object

`clone, equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Field Detail

#### MANIFEST\_NAME

```
public static final String MANIFEST_NAME
```
The JAR manifest file name.
See Also:
Constant Field Values

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

#### JarFile

```
public JarFile(String name)
        throws IOException
```
Creates a new `JarFile` to read from the specified
file `name`. The `JarFile` will be verified if
it is signed.
Parameters:
`name` - the name of the jar file to be opened for reading
Throws:
`IOException` - if an I/O error has occurred
`SecurityException` - if access to the file is denied
by the SecurityManager

#### JarFile

```
public JarFile(String name,
               boolean verify)
        throws IOException
```
Creates a new `JarFile` to read from the specified
file `name`.
Parameters:
`name` - the name of the jar file to be opened for reading
`verify` - whether or not to verify the jar file if
it is signed.
Throws:
`IOException` - if an I/O error has occurred
`SecurityException` - if access to the file is denied
by the SecurityManager

#### JarFile

```
public JarFile(File file)
        throws IOException
```
Creates a new `JarFile` to read from the specified
`File` object. The `JarFile` will be verified if
it is signed.
Parameters:
`file` - the jar file to be opened for reading
Throws:
`IOException` - if an I/O error has occurred
`SecurityException` - if access to the file is denied
by the SecurityManager

#### JarFile

```
public JarFile(File file,
               boolean verify)
        throws IOException
```
Creates a new `JarFile` to read from the specified
`File` object.
Parameters:
`file` - the jar file to be opened for reading
`verify` - whether or not to verify the jar file if
it is signed.
Throws:
`IOException` - if an I/O error has occurred
`SecurityException` - if access to the file is denied
by the SecurityManager.

#### JarFile

```
public JarFile(File file,
               boolean verify,
               int mode)
        throws IOException
```
Creates a new `JarFile` to read from the specified
`File` object in the specified mode. The mode argument
must be either OPEN\_READ or OPEN\_READ | OPEN\_DELETE.
Parameters:
`file` - the jar file to be opened for reading
`verify` - whether or not to verify the jar file if
it is signed.
`mode` - the mode in which the file is to be opened
Throws:
`IOException` - if an I/O error has occurred
`IllegalArgumentException` - if the mode argument is invalid
`SecurityException` - if access to the file is denied
by the SecurityManager
Since:
1.3

### Method Detail

#### getManifest

```
public Manifest getManifest()
                     throws IOException
```
Returns the jar file manifest, or `null` if none.
Returns:
the jar file manifest, or `null` if none
Throws:
`IllegalStateException` - may be thrown if the jar file has been closed
`IOException` - if an I/O error has occurred

#### getJarEntry

```
public JarEntry getJarEntry(String name)
```
Returns the `JarEntry` for the given entry name or
`null` if not found.
Parameters:
`name` - the jar file entry name
Returns:
the `JarEntry` for the given entry name or
`null` if not found.
Throws:
`IllegalStateException` - may be thrown if the jar file has been closed
See Also:
`JarEntry`

#### getEntry

```
public ZipEntry getEntry(String name)
```
Returns the `ZipEntry` for the given entry name or
`null` if not found.
Overrides:
`getEntry` in class `ZipFile`
Parameters:
`name` - the jar file entry name
Returns:
the `ZipEntry` for the given entry name or
`null` if not found
Throws:
`IllegalStateException` - may be thrown if the jar file has been closed
See Also:
`ZipEntry`

#### entries

```
public Enumeration<JarEntry> entries()
```
Returns an enumeration of the zip file entries.
Overrides:
`entries` in class `ZipFile`
Returns:
an enumeration of the ZIP file entries

#### stream

```
public Stream<JarEntry> stream()
```
Description copied from class: `ZipFile`
Return an ordered `Stream` over the ZIP file entries.
Entries appear in the `Stream` in the order they appear in
the central directory of the ZIP file.
Overrides:
`stream` in class `ZipFile`
Returns:
an ordered `Stream` of entries in this ZIP file

#### getInputStream

```
public InputStream getInputStream(ZipEntry ze)
                           throws IOException
```
Returns an input stream for reading the contents of the specified
zip file entry.
Overrides:
`getInputStream` in class `ZipFile`
Parameters:
`ze` - the zip file entry
Returns:
an input stream for reading the contents of the specified
zip file entry
Throws:
`ZipException` - if a zip file format error has occurred
`IOException` - if an I/O error has occurred
`SecurityException` - if any of the jar file entries
are incorrectly signed.
`IllegalStateException` - may be thrown if the jar file has been closed




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

