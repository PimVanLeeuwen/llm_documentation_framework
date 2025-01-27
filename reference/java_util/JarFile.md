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
