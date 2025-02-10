#### autoSizeColumn()


 void TableListBox::autoSizeColumn ( int columnId ) 
 

Resizes a column to fit its contents.This uses TableListBoxModel::getColumnAutoSizeWidth() to find the best width, and applies that to the column.See alsoautoSizeAllColumns, TableHeaderComponent::setColumnWidth