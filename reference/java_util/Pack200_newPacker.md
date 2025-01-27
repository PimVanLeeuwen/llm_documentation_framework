#### newPacker

```
public static Pack200.Packer newPacker()
```
Obtain new instance of a class that implements Packer.If the system property java.util.jar.Pack200.Packer
is defined, then the value is taken to be the fully-qualified name
of a concrete implementation class, which must implement Packer.
This class is loaded and instantiated. If this process fails
then an unspecified error is thrown.If an implementation has not been specified with the system
property, then the system-default implementation class is instantiated,
and the result is returned.Note: The returned object is not guaranteed to operate
correctly if multiple threads use it at the same time.
A multi-threaded application should either allocate multiple
packer engines, or else serialize use of one engine with a lock.
Returns:
A newly allocated Packer engine.

