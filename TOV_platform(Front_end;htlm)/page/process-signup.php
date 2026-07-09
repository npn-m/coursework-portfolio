<?php

$open_connect = 1;
require('connect.php');

if(isset($_POST['User_type']) && isset($_POST['Fname']) && isset($_POST['lname']) && isset($_POST['gender']) && isset($_POST['birthdate']) && isset($_POST['email']) && isset($_POST['phone_num'])
&& isset($_POST['Acc_name']) && isset($_POST['User_name']) && isset($_POST['password']) && isset($_POST['password1']))

{
     $User_type = htmlspecialchars(mysqli_real_escape_string($connect, $_POST['User_type']));
     $Fname = htmlspecialchars(mysqli_real_escape_string($connect, $_POST['Fname']));
     $lname = htmlspecialchars(mysqli_real_escape_string($connect, $_POST['lname']));
     $gender = htmlspecialchars(mysqli_real_escape_string($connect, $_POST['gender']));
     $birthdate = htmlspecialchars(mysqli_real_escape_string($connect, $_POST['birthdate']));
     $email = htmlspecialchars(mysqli_real_escape_string($connect, $_POST['email']));
     $phone_num = htmlspecialchars(mysqli_real_escape_string($connect, $_POST['phone_num']));
     $Acc_name = htmlspecialchars(mysqli_real_escape_string($connect, $_POST['Acc_name']));
     $User_name = htmlspecialchars(mysqli_real_escape_string($connect, $_POST['User_name']));
     $password = htmlspecialchars(mysqli_real_escape_string($connect, $_POST['password']));
     $password1 = htmlspecialchars(mysqli_real_escape_string($connect, $_POST['password1']));

    
     if(empty($User_type)){
        die(header('Location: signup.php')); 
     }elseif(empty($Fname)){
        die(header('Location: signup.php')); 
     }elseif(empty($lname)){
        die(header('Location: signup.php')); 
     }elseif(empty($gender)){
        die(header('Location: signup.php'));
    }elseif(empty($birthdate)){
        die(header('Location: signup.php'));
    }elseif(empty($email)){
        die(header('Location: signup.php'));
    }elseif(empty($phone_num)){
        die(header('Location: signup.php'));
    }elseif(empty($Acc_name)){
        die(header('Location: signup.php'));
    }elseif(empty($User_name)){
        die(header('Location: signup.php')); 
     }elseif($password != $password1){
        die(header('Location: signup.php')); 
     }else{
         $query_check_email = "SELECT email FROM user_info WHERE email = '$email'";
         $call_back_query_check_email = mysqli_query($connect, $query_check_email);
         if(mysqli_num_rows($call_back_query_check_email) > 0){
            die(header('Location: signup.php')); 
         }
        else{
            $query_check_User_name = "SELECT User_name FROM user_info WHERE User_name = '$User_name'";
            $call_back_query_check_User_name = mysqli_query($connect, $query_check_User_name);
            if(mysqli_num_rows($call_back_query_check_User_name) > 0){
               die(header('Location: signup.php')); 
            }
             $query_create_User_info = "INSERT INTO User_info VALUES ('', '$User_type', '$Fname', '$lname', '$gender', '$birthdate',
              '$email', '$phone_num', '$Acc_name', '$User_name','$password','default_profile.jpg','default_cover.jpg','')";
             $call_back_create_User_info = mysqli_query($connect, $query_create_User_info);
             if($call_back_create_User_info){
                 die(header('Location: login.php')); 
             }else{
                die(header('Location: signup.php')); 
             }
         
     }
    }
}else{
    die(header('Location: signup.php')); 
}

?>