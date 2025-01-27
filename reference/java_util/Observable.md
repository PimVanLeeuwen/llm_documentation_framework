```
public class Observable
extends Object
```
This class represents an observable object, or "data"
in the model-view paradigm. It can be subclassed to represent an
object that the application wants to have observed.An observable object can have one or more observers. An observer
may be any object that implements interface Observer. After an
observable instance changes, an application calling the
`Observable`'s `notifyObservers` method
causes all of its observers to be notified of the change by a call
to their `update` method.The order in which notifications will be delivered is unspecified.
The default implementation provided in the Observable class will
notify Observers in the order in which they registered interest, but
subclasses may change this order, use no guaranteed order, deliver
notifications on separate threads, or may guarantee that their
subclass follows this order, as they choose.Note that this notification mechanism has nothing to do with threads
and is completely separate from the wait and notify
mechanism of class Object.When an observable object is newly created, its set of observers is
empty. Two observers are considered the same if and only if the
equals method returns true for them.
Since:
JDK1.0
See Also:
`notifyObservers()`,
`notifyObservers(java.lang.Object)`,
`Observer`,
`Observer.update(java.util.Observable, java.lang.Object)`
