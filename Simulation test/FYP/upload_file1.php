<?php
print_r($_FILES);
move_uploaded_file($_FILES["file"]["tmp_name"],"C:/Users/Lakshadeep/Google Drive/Final year project/Simulation test/" . $_FILES["file"]["name"]);
 
?>