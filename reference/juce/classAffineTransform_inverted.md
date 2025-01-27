#### inverted()


 AffineTransform AffineTransform::inverted ( ) const noexcept 
 

Returns a matrix which is the inverse operation of this one.Some matrices don't have an inverse in this case, the method will just return an identity transform.