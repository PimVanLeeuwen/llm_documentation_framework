#### setModel()


 void TableListBox::setModel ( TableListBoxModel \* newModel ) 
 

Changes the TableListBoxModel that is being used for this table.The TableListBox does not take ownership of the model it's the caller's responsibility to manage its lifetime and make sure it doesn't get deleted while still being used.