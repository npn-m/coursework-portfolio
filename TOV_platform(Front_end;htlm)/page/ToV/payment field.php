<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Payment Information</title>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="paymentfield.css">
    <link rel="stylesheet" href="homepage.css">
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

    <main>
        <section class="payment-section">
            <h2>Payment Information</h2>
            <div class="payment-box">
                <label>Firstname</label>
                <input type="text" placeholder="Firstname">
                <label>Lastname</label>
                <input type="text" placeholder="Lastname">
                <label>Email</label>
                <input type="email" placeholder="Example@gmail.com">
                <label>Username</label>
                <input type="text" placeholder="@Username">
                <label>Password</label>
                <input type="password" placeholder="Password">
                
                <div class="card-info">
                    <h3>My Card <span>Debit / Credit Card ( VISA / Master Card )</span></h3>
                    <p>Make an auto payment through debit / credit card</p>
                    <label>Name On Card</label>
                    <input type="text" placeholder="Firstname Lastname">
                    <label>Card Number</label>
                    <div class="card-number">
                        <input type="text" maxlength="16" placeholder="XXXX-XXXX-XXXX-XXXX">
                    </div>
                    <label>Expiry Date</label>
                    <div class="exdate">
                        <input type="text" maxlength="2" placeholder="MM"><label>/</label>
                        <input type="text" maxlength="2" placeholder="YY">
                    </div>
                </div>
                <button onclick="history.back()" class="submit-btn">Submit</button>
            </div>
        </section>
    </main>
</body>
</html>
