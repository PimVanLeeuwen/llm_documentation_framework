#### hankel()


template<typename ElementType > 

 static Matrix dsp::Matrix< ElementType >::hankel ( const Matrix< ElementType > & vector, size\_t size, size\_t offset = 0 ) static 
 

Creates a squared size x size Hankel Matrix from a vector with an optional offset.Parameters

 vector The vector from which the Hankel matrix should be generated. Its number of rows should be at least 2 \* (size 1) + 1 
 
 size The size of resulting square matrix. 
 offset An optional offset into the given vector.