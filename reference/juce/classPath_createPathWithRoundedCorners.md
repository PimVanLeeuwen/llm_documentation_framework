#### createPathWithRoundedCorners()


 Path Path::createPathWithRoundedCorners ( float cornerRadius ) const 
 

Creates a version of this path where all sharp corners have been replaced by curves.Wherever two lines meet at an angle, this will replace the corner with a curve of the given radius.