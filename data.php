<?php
$con=mysqli_connect("localhost","root","") or die("unable to connect");
mysqli_select_db($con,"pg");

if (isset($_POST['submit-1'])) {

  $name=$_POST['name'];
  $email=$_POST['email'];
  $address=$_POST['address'];
  $password=$_POST['password'];

  $query="insert into pgdata(name,email,address,password) values ('$name','$email','$address','$password')";
  $runquery=mysqli_query($con,$query);
  if($runquery){
    echo '<script>alert("registration successful")</script>';
  
  }

}

 ?>
