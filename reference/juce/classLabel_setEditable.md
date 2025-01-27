#### setEditable()


 void Label::setEditable ( bool editOnSingleClick, 
 
 bool editOnDoubleClick = false, 
 bool lossOfFocusDiscardsChanges = false ) 

Makes the label turn into a TextEditor when clicked.By default this is turned off.If turned on, then single or doubleclicking will turn the label into an editor. If the user then changes the text, then the ChangeBroadcaster base class will be used to send change messages to any listeners that have registered.If the user changes the text, the textWasEdited() method will be called afterwards, and subclasses can override this if they need to do anything special.Parameters

 editOnSingleClick if true, just clicking once on the label will start editing the text 
 
 editOnDoubleClick if true, a doubleclick is needed to start editing 
 lossOfFocusDiscardsChanges if true, clicking somewhere else while the text is being edited will discard any changes; if false, then this will commit the changes. 



See alsoshowEditor, setEditorColours, TextEditor