#### getClippedLine()


 Line< float > Path::getClippedLine ( Line< float > line, 
 
 bool keepSectionOutsidePath ) const 

Cuts off parts of a line to keep the parts that are either inside or outside this path.Note that this isn't smart enough to cope with situations where the line would need to be cut into multiple pieces to correctly clip against a reentrant shape.Parameters

 line the line to clip 
 
 keepSectionOutsidePath if true, it's the section outside the path that will be kept; if false its the section inside the path