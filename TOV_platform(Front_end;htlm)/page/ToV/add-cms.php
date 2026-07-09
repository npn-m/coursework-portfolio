<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Commission Page</title>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="edit.css">
    <link rel="stylesheet" href="cms-add.css">
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
        <div class="edit-header"><h1><span class="material-symbols-outlined">edit_square</span> New Commission</h1></div>

        <div class ="edit-content">
            <div class="cms-info">
                <div class="info-input"><label>Commission Name</label><input type="text" placeholder="Commission Name"></div>

                <label>Category</label>
                <div class="category-tags">
                    <span class="tag">category <span class="material-symbols-outlined">close</span></span>
                    <span class="tag">category <span class="material-symbols-outlined">close</span></span>
                </div>
            
                <div class="price-description">
                    <div class="price-field">
                        <label>Price</label>
                        <input type="text" placeholder="Price">
                    </div>
                    
                    <div class="description-field">
                        <label>Describe</label>
                        <textarea maxlength="400" cols="90" placeholder="Describe"></textarea>
                    </div>
                </div>
            
                <div class="work-example-section">
                    <label>WORK EXAMPLE</label>
                    <div class="work-example">
                        <div class="work-icon">
                        <input type="file" id="image" name="profile" accept="image/png, image/jpeg" style="display:none"/>
                        <label for="image"><span class="material-symbols-outlined">add</span></label>
                        </div>
                    </div>
                </div>
            
                <div class="buttons">
                    <a href="artist_edit.php">
                        <button class="cancel-btn1">CANCEL</button>
                    </a>
                    <a href="artist_edit.php">
                        <button class="ok-btn1">OK</button>
                    </a>
                </div>
            </div>
        </div>
    </main>
</body>
</html>
