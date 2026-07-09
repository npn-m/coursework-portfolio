<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Viewer Profile</title>
  <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="profile.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200"/>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap" rel="stylesheet">
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
</body>
    <main>
    <div class="profile-header">
        <img class="banner" src="cover.jpg"></img>
        <img class="avatar" src="51518.jpg"></img>
        <div class="profile-info">
            <div class="details">
                <h2>Account Name
                    <span>@username</span> 
                </h2>
                <br><p>subscribe count · user category</p></br>
            </div>
            <a href="viewer-edit.php" style="color:white;">
                <span class="material-symbols-outlined">edit_square</span>
            </a>
        </div>
            <button class="subscribe-btn">Subscribe</button>
    </div>

    <div class="content">
        <div class="section-title">
            <a href="#">About</a>
        </div>
        </div>
        <div class="about-section">
            <p>Content about the user goes here...</p>
        </div>
    </div>
    </main>
</html>
