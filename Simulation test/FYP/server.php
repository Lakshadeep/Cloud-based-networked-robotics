<?php

if(isset($_POST['sensor_values'] ) and $_POST['sequence']){

$sensor_raw =  $_POST['sensor_values'] ; 
$sequence =   $_POST['sequence'] ; 

$sensor_array = explode(",",$sensor_raw);

//echo sizeof($sensor_array) ;
//echo $sensor_array[0];

if($sequence == '1'){
    echo "1,2";
   
}else if($sequence == '2'){
      $right_sensor = $sensor_array[0];
      $left_sensor = $sensor_array[1];

      $value = system("C:\Users\Lakshadeep\Google Drive\Final year project\Simulation test\Circle_detection.exe");
      
      if($value == 0){      
     

      if($right_sensor == '1' and $left_sensor == '1'){
           echo "5,1";
      }else if($right_sensor == '0' and $left_sensor == '1'){
           echo "2,1";
      }else if($right_sensor == '1' and $left_sensor == '0'){
           echo "3,1";
      }else if($right_sensor == '0' and $left_sensor == '0'){
           echo "4,1";
      }
     
     }else{

           echo "6,1";
     } 
}
}
?>