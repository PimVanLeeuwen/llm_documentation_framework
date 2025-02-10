#### returnKeyPressed()


 virtual void ListBoxModel::returnKeyPressed ( int lastRowSelected ) virtual 
 

Override this to be informed when the return key is pressed.If no rows are selected when they press the key, this won't be called.Parameters

 lastRowSelected the last row that had been selected when they pressed the key if there are multiple selections, this might not be very useful 
 


Reimplemented in FileSearchPathListComponent, and TableListBox.