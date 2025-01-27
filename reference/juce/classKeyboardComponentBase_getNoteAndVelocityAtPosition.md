#### getNoteAndVelocityAtPosition()


 NoteAndVelocity KeyboardComponentBase::getNoteAndVelocityAtPosition ( Point< float > position, 
 
 bool includeChildComponents = false ) 

Returns the note number and velocity for a given position within the component.If includeChildComponents is true then this will return a key obscured by any child components.