#### moveKeyboardFocusToSibling()


 void Component::moveKeyboardFocusToSibling ( bool moveToNext ) 
 

Tries to move the keyboard focus to one of this component's siblings.This will try to move focus to either the next or previous component, as determined by the getNextComponent() and getPreviousComponent() implementations of the ComponentTraverser returned by createKeyboardFocusTraverser().This is the method that is used when shifting focus by pressing the tab key.Parameters

 moveToNext if true, the focus will move forwards; if false, it will move backwards 
 



See alsograbKeyboardFocus, giveAwayKeyboardFocus, setFocusContainerType, setWantsKeyboardFocus