<?php
  session_start();
  if(isset($_GET['logout'])){
    session_destroy();
    unset($_SESSION['User_name']);
    header('Location : login.php ');
  }
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Page</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200"/>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="homepage.css">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <div class="navbar">
            <img class="image" src="logo.png"></img>
            <ul>
                <span class="material-symbols-outlined">home</span><t><a href="homepage.php">HOME</a></t>
                <t><a href="#">VTUBER</a></t>
                <t><a href="#">ARTIST</a></t>
                <div class="search-login">
                    <div class="search">
                        <input type="text" placeholder="Search" required />
                        <button>
                        <span class="icon material-symbols-outlined">search</span>
                        <span class="spinner"></span>
                        </button>
                    </div>
                    
                </div>
                <t><a href="login.php">
                    <button class="login">Log in</button>
                </a></t>
                <t><a href="signup.php">
                    <button class="signup">Sign Up</button>
                </a></t>
                <img class="profile-acc" src="51518.jpg"></img>
            </ul>
            </div>
        </div>
    </header>
    
  <div class="off-screen-menu">
      
      <ul>
        <li><img class="profile-pic" src="51518.jpg"></img>
        <li><a href="#">Account Name</a></li>
        <li><a href="#">Subscribed</a></li>
        <ul class="subscribed-list">
          <div class="sub-list"><img class="profile-sub" src="51518.jpg"></img><li>Account Name</li></div>
          <div class="sub-list"><img class="profile-sub" src="51518.jpg"></img><li>Account Name</li></div>
          <div class="sub-list"><img class="profile-sub" src="51518.jpg"></img><li>Account Name</li></div>
        </ul>
        <li><a href="#">Watching History</a></li>
        <li><a href="#">Playlist</a></li>
        <li><a href="#">Liked Video</a></li>
        <li><a href="homepage.php?Logout=1"><button class="logout-btn">Log out</button></a></li>
      </ul>
    
  </div>

    <div class="content">
      <h2>Trending</h2>
        <div class="video-grid">
          <div class="video-card"><img class="video" src="4007361.jpg"></img><br>Video Name<br>View Count / Release Date</div>
          <div class="video-card"><img class="video" src="4007361.jpg"></img><br>Video Name<br>View Count / Release Date</div>
          <div class="video-card"><img class="video" src="4007361.jpg"></img><br>Video Name<br>View Count / Release Date</div>
          <div class="video-card"><img class="video" src="4007361.jpg"></img><br>Video Name<br>View Count / Release Date</div>
        </div>

        <h2>Rookies</h2>
        <div class="video-grid">
          <div class="video-card"><img class="video" src="4553722.jpg"></img><br>Video Name<br>View Count / Release Date</div>
          <div class="video-card"><img class="video" src="4553722.jpg"></img><br>Video Name<br>View Count / Release Date</div>
          <div class="video-card"><img class="video" src="4553722.jpg"></img><br>Video Name<br>View Count / Release Date</div>
          <div class="video-card"><img class="video" src="4553722.jpg"></img><br>Video Name<br>View Count / Release Date</div>
        </div>
     
        <h2>Recommended</h2>
        <div class="video-grid">
          <div class="video-card"><img class="video" src="5323376.jpg"></img><br>Video Name<br>View Count / Release Date</div>
          <div class="video-card"><img class="video" src="5323376.jpg"></img><br>Video Name<br>View Count / Release Date</div>
          <div class="video-card"><img class="video" src="5323376.jpg"></img><br>Video Name<br>View Count / Release Date</div>
          <div class="video-card"><img class="video" src="5323376.jpg"></img><br>Video Name<br>View Count / Release Date</div>
        </div>
      
    </div>
</body>
<script> </script>
</html>
