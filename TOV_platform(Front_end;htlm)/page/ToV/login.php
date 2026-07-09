
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Page</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200"/>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="login.css">
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

    <main>
        <section class="login-section">
            <h2><h>Log In</h></h2>
            
            <div class="login-box">
                <form method="POST" action="process-login.php" >
                    <label>Username</label>
                    <div class="user">
                        <input name="User_name" type="text" placeholder="Username" required />
                        <span class="material-symbols-outlined"> person </span>
                        <button>
                        <span class="material-symbols-outlined"> close </span>
                        </button>
                    </div>
                    <label>Password</label>
                    <div class="password">
                        <input name="password" type="password" placeholder="Password" required />
                        <span class="material-symbols-outlined"> lock </span>
                    </div>
                    <button type="submit" class="login-btn">Login</button>
                    <p><f href="#">Forgot password?</f></p>
                </form>
            </div>
           
        </section>

        <section class="signup-section">
            <h2><h>Sign Up</h></h2>
            <a href="signup.php"><button class="signup-btn">Create New Account</button></a>
        </section>
    </main>
    <script type="text/javascript" src="index.js"></script>
</body>
</html>
