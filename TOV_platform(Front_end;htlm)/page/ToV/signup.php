<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign Up Page</title>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="signup.css">
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
                    <button class="login">Login</button>
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
        <section class="signup-section">
            <h2>Sign Up</h2>
            <form action="process-signup.php" method="POST">
            <div class="signup-box">
                <h>You Are</h>
                <select name="User_type" required>
                    <option value="">Account Types : </option>
                    <option value="Vtuber">VTuber</option>
                    <option value="Artist">Artist</option>
                    <option value="Viewer">Viewer</option>
                </select>
                <label>Firstname</label>
                <input name="Fname" type="text" placeholder="Firstname" required />    
                <label>Lastname</label>    
                <input name="lname" type="text" placeholder="Lastname" required />        
                <label>Gender</label>
                <select name="gender" required>
                    <option>Gender : </option>
                    <option>Male</option>
                    <option>Female</option>
                    <option>LGBTQ+</option>
                </select>
                <label>Birthday</label>
                <input name="birthdate" type="date" placeholder="DD / MM / YYYY" required />
                <label>Email</label>
                <input name="email" type="email" placeholder="Example@gmail.com" required />
                <label>Phone Number</label>
                <input name="phone_num" type="tel" maxlength="10" placeholder="Phone Number" required />
                <label>Account Name</label>
                <input name="Acc_name" type="text" placeholder="Account Name" required />
                <label>Username</label>
                <div class="user">
                    <input name="User_name" type="text" placeholder="Username" required />
                    <span class="material-symbols-outlined"> person </span>
                </div>
                <label>Password</label>
                <div class="password">
                    <input name="password" type="password" placeholder="Password" required />
                    <span class="material-symbols-outlined"> lock </span>
                </div>
                <label>Confirm Password</label>
                <div class="password">
                    <input name="password1" type="password" placeholder="Password" required />
                    <span class="material-symbols-outlined"> lock </span>
                </div>
                <button type="submit" class="submit-btn">Submit</button>
            </div>
            </form>
        </section>
    </main>
    <script type="text/javascript" src="index.js"></script>
</body>

</html>