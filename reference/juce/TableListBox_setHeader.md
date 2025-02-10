#### setHeader()


 void TableListBox::setHeader ( std::unique\_ptr< TableHeaderComponent > newHeader ) 
 

Sets the header component to use for the table.The table will take ownership of the component that you pass in, and will delete it when it's no longer needed. The pointer passed in may not be null.