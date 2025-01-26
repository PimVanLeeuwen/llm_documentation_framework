

Uses of Package java.util.jar (Java Platform SE 8 )




<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="Uses of Package java.util.jar (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->

JavaScript is disabled on your browser.


Skip navigation links

OverviewPackageClassUseTreeDeprecatedIndexHelpJava™ PlatformStandard Ed. 8

PrevNextFramesNo FramesAll Classes
<!--
allClassesLink = document.getElementById("allclasses\_navbar\_top");
if(window==top) {
allClassesLink.style.display = "block";
}
else {
allClassesLink.style.display = "none";
}
//-->




Uses of Packagejava.util.jar

Packages that use java.util.jar PackageDescriptionjava.lang.instrumentProvides services that allow Java programming language agents to instrument programs running on the JVM.java.netProvides the classes for implementing networking applications.java.util.jarProvides classes for reading and writing the JAR (Java ARchive) file
format, which is based on the standard ZIP file format with an
optional manifest file.

Classes in java.util.jar used by java.lang.instrument Class and DescriptionJarFile
The `JarFile` class is used to read the contents of a jar file
from any file that can be opened with `java.io.RandomAccessFile`.

Classes in java.util.jar used by java.net Class and DescriptionAttributes
The Attributes class maps Manifest attribute names to associated string
values.JarEntry
This class is used to represent a JAR file entry.JarFile
The `JarFile` class is used to read the contents of a jar file
from any file that can be opened with `java.io.RandomAccessFile`.Manifest
The Manifest class is used to maintain Manifest entry names and their
associated Attributes.

Classes in java.util.jar used by java.util.jar Class and DescriptionAttributes
The Attributes class maps Manifest attribute names to associated string
values.Attributes.Name
The Attributes.Name class represents an attribute name stored in
this Map.JarEntry
This class is used to represent a JAR file entry.JarFile
The `JarFile` class is used to read the contents of a jar file
from any file that can be opened with `java.io.RandomAccessFile`.JarInputStream
The `JarInputStream` class is used to read the contents of
a JAR file from any input stream.JarOutputStream
The `JarOutputStream` class is used to write the contents
of a JAR file to any output stream.Manifest
The Manifest class is used to maintain Manifest entry names and their
associated Attributes.Pack200.Packer
The packer engine applies various transformations to the input JAR file,
making the pack stream highly compressible by a compressor such as
gzip or zip.Pack200.Unpacker
The unpacker engine converts the packed stream to a JAR file.


Skip navigation links

OverviewPackageClassUseTreeDeprecatedIndexHelpJava™ PlatformStandard Ed. 8

PrevNextFramesNo FramesAll Classes
<!--
allClassesLink = document.getElementById("allclasses\_navbar\_bottom");
if(window==top) {
allClassesLink.style.display = "block";
}
else {
allClassesLink.style.display = "none";
}
//-->



 Submit a bug or feature For further API reference and developer documentation, see Java SE Documentation. That documentation contains more detailed, developer-targeted descriptions, with conceptual overviews, definitions of terms, workarounds, and working code examples. Copyright © 1993, 2025, Oracle and/or its affiliates. All rights reserved. Use is subject to license terms. Also see the documentation redistribution policy. 

