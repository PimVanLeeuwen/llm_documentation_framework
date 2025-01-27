#### isNull()


 bool Image::isNull ( ) const noexcept 
 

Returns true if this image is not valid.If you create an Image with the default constructor, it has no size or content, and is null until you reassign it to an Image which contains some actual data. The isNull() method is the opposite of isValid().See alsoisValid