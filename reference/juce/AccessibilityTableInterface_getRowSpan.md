#### getRowSpan()


 virtual Optional< Span > AccessibilityTableInterface::getRowSpan ( const AccessibilityHandler & ) const pure virtual 
 

Given the handler of one of the cells in the table, returns the rows covered by that cell, or null if the cell does not exist in the table.This function replaces the getRowIndex and getRowSpan functions from AccessibilityCellInterface. Most of the time, it's easier for the table itself to keep track of cell locations, than to delegate to the individual cells.