<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>viewer-edit Profile</title>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="edit.css">
    <link rel="stylesheet" href="profile.css">
    <link rel="stylesheet" href="homepage.css">
    <link
    rel="stylesheet"
    href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200"
    />
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

    <main>
        <div class="edit-header"><h1><span class="material-symbols-outlined">edit_square</span> EDIT</h1></div>
        <div class="edit-content">
            <div class="profile-edit">
                <label>Profile</label>
                <div class="profile-avatar">
                    <div class="avatar-icon">
                        <input type="file" id="image" name="profile" accept="image/png, image/jpeg" style="display:none"/>
                        <label for="image"><span class="material-symbols-outlined">upload</span></label>
                    </div>
                </div>

                <label>Cover</label>
                <div class="cover-photo">
                    <div class="cover-icon">
                        <input type="file" id="image" name="profile" accept="image/png, image/jpeg" style="display:none"/>
                        <label for="image"><span class="material-symbols-outlined">upload</span></label>
                    </div>
                </div>
            </div>
        
            <div class="form-section">
                <div class="name-edit">
                    <label>Account Name</label>
                    <input type="text" placeholder="Account Name">
                    <label>Username</label>
                    <input type="text" placeholder="@Username">
                </div>
                <label>Category</label>
                <div class="category-tags">
                    <span class="tag">category <span class="material-symbols-outlined">close</span></span>
                    <span class="tag">category <span class="material-symbols-outlined">close</span></span>
                </div>
              
                <label>About Me</label>
                <textarea maxlength="400" placeholder="Describe about yourself (not more than 400 characters)"></textarea>
            </div>
            <a href="viewer.php"><button class="confirm-btn">Confirm</button></a>
        </div>  
        
    </main>
</body>
<script scr="index.js"></script>
</html>