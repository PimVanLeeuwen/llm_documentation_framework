#### getActiveEditor()


 AudioProcessorEditor \* AudioProcessor::getActiveEditor ( ) const noexcept 
 

Returns the active editor, if there is one.Bear in mind this can return nullptr even if an editor has previously been opened.Note that you should only call this method from the message thread as the active editor may be deleted by the message thread, causing a dangling pointer.