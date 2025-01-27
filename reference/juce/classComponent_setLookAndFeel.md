#### setLookAndFeel()


 void Component::setLookAndFeel ( LookAndFeel \* newLookAndFeel ) 
 

Sets the look and feel to use for this component.This will also change the look and feel for any child components that haven't had their look set explicitly.The object passed in will not be deleted by the component, so it's the caller's responsibility to manage it. It may be used at any time until this component has been deleted.Calling this method will also invoke the sendLookAndFeelChange() method.See alsogetLookAndFeel, lookAndFeelChanged, sendLookAndFeelChange