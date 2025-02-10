#### setLowestVisibleKey()


 void KeyboardComponentBase::setLowestVisibleKey ( int noteNumber ) 
 

If the keyboard extends beyond the size of the component, this will scroll it to show the given key at the start.Whenever the keyboard's position is changed, this will use the ChangeBroadcaster base class to send a callback to any ChangeListeners that have been registered.