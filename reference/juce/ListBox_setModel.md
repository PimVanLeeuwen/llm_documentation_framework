#### setModel()


 void ListBox::setModel ( ListBoxModel \* newModel ) 
 

Changes the current data model to display.The ListBoxModel instance must stay alive for as long as the ListBox holds a pointer to it. Be careful to destroy the ListBox before the ListBoxModel, or to call ListBox::setModel (nullptr) before destroying the ListBoxModel.