
// Import dependencies
const express = require("express");
const session = require("express-session");
// Create Express app
const app = express();
app.use(
// Configure session middleware 
 session({ secret: "mySecretKey", resave: false, saveUninitialized: false, }) );
// Route to set session data
app.get("/setSession", (req, res) => { req.session.username = "johnDoe"; res.send("Session data set"); });

// Route to retrieve session data 
 app.get("/getSession", (req, res) => {
     const username = req.session.username;
     res.send("Username: " + username); 
    });

// Route to destroy session

app.get("/destroySession", (req, res) =>{ 
    req.session.destroy((err) => { 
        if (err) {
             console.error("Error destroying session:", err); 
             res.status(500).send("Error destroying session"); 
            } else { 
                res.send("Session destroyed"); 
            }
    });
});

// Start the server

app.listen(3000, () => { 
    console.log("Server is running on port 3000"); 
});