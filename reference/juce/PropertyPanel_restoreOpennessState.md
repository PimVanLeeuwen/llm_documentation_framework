#### restoreOpennessState()


 void PropertyPanel::restoreOpennessState ( const XmlElement & newState ) 
 

Restores a previously saved arrangement of open/closed sections.This will try to restore a snapshot of the panel's state that was created by the getOpennessState() method. If any of the sections named in the original XML aren't present, they will be ignored.See alsogetOpennessState