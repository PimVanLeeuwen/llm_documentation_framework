#### setDefaultLookAndFeel()


 void Desktop::setDefaultLookAndFeel ( LookAndFeel \* newDefaultLookAndFeel ) 
 

Changes the default lookandfeel.Parameters

 newDefaultLookAndFeel the new lookandfeel object to use if this is set to nullptr, it will revert to using the system's default one. The object passedin must be deleted by the caller when it's no longer needed. 
 



See alsogetDefaultLookAndFeel