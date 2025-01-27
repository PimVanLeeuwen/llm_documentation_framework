```
public class TooManyListenersException
extends Exception
```
The  `TooManyListenersException`  Exception is used as part of
the Java Event model to annotate and implement a unicast special case of
a multicast Event Source.The presence of a "throws TooManyListenersException" clause on any given
concrete implementation of the normally multicast "void addXyzEventListener"
event listener registration pattern is used to annotate that interface as
implementing a unicast Listener special case, that is, that one and only
one Listener may be registered on the particular event listener source
concurrently.
Since:
JDK1.1
See Also:
`EventObject`,
`EventListener`,
Serialized Form
