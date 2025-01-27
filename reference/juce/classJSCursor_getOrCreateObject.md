#### getOrCreateObject()


 JSObject JSCursor::getOrCreateObject ( ) const 
 

Returns an owning reference to the Javascript Object at the cursor's location.If there is no Object at the location but the cursor is valid, a new Object will be created.You must only call this function on a valid JSCursor.By creating an owning reference, you can create a new JSCursor object that owns the underlying object and is guaranteed to remain in a valid state e.g.JSCursor rootCursor { engine.getRootObject() };
auto nonOwningCursor = rootCursor["path"]["to"]["object"];
 
jassert (nonOwningCursor.isValid());
 
JSCursor owningCursor { nonOwningCursor.getOrCreateObject(); };
engine.execute (arbitraryScript);
 
// owningCursor is guaranteed to remain valid even after subsequent script evaluations
jassert (owningCursor.isValid());
JSCursorA highlevel wrapper around an owning root JSObject and a hierarchical path relative to it.Definition juce\_JSCursor.h:55
jassert#define jassert(expression)Platformindependent assertion macro.Definition juce\_PlatformDefs.h:177
See alsoisValid