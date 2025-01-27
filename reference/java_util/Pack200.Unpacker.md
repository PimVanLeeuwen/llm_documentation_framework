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
