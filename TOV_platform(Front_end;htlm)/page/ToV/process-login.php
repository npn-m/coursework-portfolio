<?php

session_start();
require("connect.php");

if(isset($_POST["User_name"]) && isset($_POST["password"])){
    $User_name = $_POST["User_name"];
    $password = $_POST["password"];
    $query_check_user = "SELECT * FROM user_info WHERE User_name = '$User_name' AND password = '$password'";
    $call_back_check_user = mysqli_query($connect,$query_check_user);
    if(mysqli_num_rows($call_back_check_user) == 1){
        $result_check_user = mysqli_fetch_assoc($call_back_check_user);
        $_SESSION["ID"] = $result_check_user["ID"];
        $_SESSION["User_name"] = $result_check_user["User_name"];
        $_SESSION["User_type"] = $result_check_user["User_type"];
        $hash = $result_check_user["password"];
        
        if(password_verify($password,$hash)){

            if( $_SESSION["User_type"] =="Vtuber"){
                header('Location : Vtuber.php');
            }
            if( $_SESSION["User_type"] =="Artist"){
                header('Location : artist.php');
            }
            if( $_SESSION["User_type"] == "Viewer"){
                header('Location : viewer.php');
            }else{
                echo"<script>";
                echo"alert(\"User name or Password are incorrect.\");";
                echo "window.history.back()";
                echo "</script>";
            }
        }else{
            header('Location : login.php'); 
        }
    }else{
        header('Location : login.php'); 
    }
}else{
    header('Location : login.php');
}


?>
