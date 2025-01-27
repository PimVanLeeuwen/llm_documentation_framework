```
public abstract class AbstractPreferences
extends Preferences
```
This class provides a skeletal implementation of the `Preferences`
class, greatly easing the task of implementing it.This class is for Preferences implementers only.
Normal users of the Preferences facility should have no need to
consult this documentation. The `Preferences` documentation
should suffice.Implementors must override the nine abstract service-provider interface
(SPI) methods: `getSpi(String)`, `putSpi(String,String)`,
`removeSpi(String)`, `childSpi(String)`, `removeNodeSpi()`, `keysSpi()`, `childrenNamesSpi()`, `syncSpi()` and `flushSpi()`. All of the concrete methods specify
precisely how they are implemented atop these SPI methods. The implementor
may, at his discretion, override one or more of the concrete methods if the
default implementation is unsatisfactory for any reason, such as
performance.The SPI methods fall into three groups concerning exception
behavior. The getSpi method should never throw exceptions, but it
doesn't really matter, as any exception thrown by this method will be
intercepted by `get(String,String)`, which will return the specified
default value to the caller. The removeNodeSpi, keysSpi,
childrenNamesSpi, syncSpi and flushSpi methods are specified
to throw `BackingStoreException`, and the implementation is required
to throw this checked exception if it is unable to perform the operation.
The exception propagates outward, causing the corresponding API method
to fail.The remaining SPI methods `putSpi(String,String)`, `removeSpi(String)` and `childSpi(String)` have more complicated
exception behavior. They are not specified to throw
BackingStoreException, as they can generally obey their contracts
even if the backing store is unavailable. This is true because they return
no information and their effects are not required to become permanent until
a subsequent call to `Preferences.flush()` or
`Preferences.sync()`. Generally speaking, these SPI methods should not
throw exceptions. In some implementations, there may be circumstances
under which these calls cannot even enqueue the requested operation for
later processing. Even under these circumstances it is generally better to
simply ignore the invocation and return, rather than throwing an
exception. Under these circumstances, however, all subsequent invocations
of flush() and sync should return false, as
returning true would imply that all previous operations had
successfully been made permanent.There is one circumstance under which putSpi, removeSpi and
childSpi should throw an exception: if the caller lacks
sufficient privileges on the underlying operating system to perform the
requested operation. This will, for instance, occur on most systems
if a non-privileged user attempts to modify system preferences.
(The required privileges will vary from implementation to
implementation. On some implementations, they are the right to modify the
contents of some directory in the file system; on others they are the right
to modify contents of some key in a registry.) Under any of these
circumstances, it would generally be undesirable to let the program
continue executing as if these operations would become permanent at a later
time. While implementations are not required to throw an exception under
these circumstances, they are encouraged to do so. A `SecurityException` would be appropriate.Most of the SPI methods require the implementation to read or write
information at a preferences node. The implementor should beware of the
fact that another VM may have concurrently deleted this node from the
backing store. It is the implementation's responsibility to recreate the
node if it has been deleted.Implementation note: In Sun's default Preferences
implementations, the user's identity is inherited from the underlying
operating system and does not change for the lifetime of the virtual
machine. It is recognized that server-side Preferences
implementations may have the user identity change from request to request,
implicitly passed to Preferences methods via the use of a
static `ThreadLocal` instance. Authors of such implementations are
strongly encouraged to determine the user at the time preferences
are accessed (for example by the `get(String,String)` or `put(String,String)` method) rather than permanently associating a user
with each Preferences instance. The latter behavior conflicts
with normal Preferences usage and would lead to great confusion.
Since:
1.4
See Also:
`Preferences`
