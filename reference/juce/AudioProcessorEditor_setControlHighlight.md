#### setControlHighlight()


 virtual void AudioProcessorEditor::setControlHighlight ( ParameterControlHighlightInfo ) virtual 
 

Some types of plugin can call this to suggest that the control for a particular parameter should be highlighted.Currently only AAX plugins will call this, and implementing it is optional.