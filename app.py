# importing modules
from flask import Flask,request,redirect,render_template, jsonify,session, send_file, url_for
from helpers import is_valid_email, login_required, allowed_file
from cs50 import SQL
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import uuid
import os
from flask_mail import Mail, Message

#database
db = SQL("sqlite:///sharegamez.db")

# app
app = Flask(__name__, static_url_path='/static')

#for files
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER





#for mail service
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'sharegamezinfo@gmail.com'
app.config['MAIL_PASSWORD'] = "bekhgedytmlddprd"
app.config['MAIL_USE_TLS'] = True  # Use TLS for secure connection
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Home route
@app.route("/",methods=["POST","GET"])
def index():
    #inport games by rating
    gamestop = db.execute("SELECT * FROM games ORDER BY rating DESC  LIMIT 3")
    games =[]
    if len(gamestop) >= 1:
        games.append(gamestop[0])
    if len(gamestop) >= 2:
        games.append(gamestop[1])
    if len(gamestop) >= 3:
       games.append(gamestop[2])
    
      
    if request.method == "POST":
        return render_template("index.html")
    else:
        return render_template("index.html",games=games)



@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact",methods=["POST","GET"])
def contact():
    if request.method == "POST":
        #get name
        name = request.form.get("name")
        if not name:
            return render_template("contact.html",message="name")
        
        #get email
        email = request.form.get("email")
        if not is_valid_email(email):
            return render_template("contact.html",message="email")
        
        #get message
        message = request.form.get("message")
        if not message:
            return render_template("contact.html",message="message")
        
        
        # send email contact
        msg = Message("Thanks for contacting us "+ name,sender='sharegamezinfo@gmail.com', recipients=["sharegamezinfo@gmail.com",email])
        msg.body = """Your message was:
        
        """+message+"""
        
        
        
        
        
        We will inform you about our respond"""
         
        mail.send(msg)
        return redirect("/")
    else:
        return render_template("contact.html")

#return games in json file
@app.route("/returngames")
def returngames():
    games = db.execute("SELECT * FROM games")
    games_list = [dict(row) for row in games]
    return jsonify(games_list)

# search for games
@app.route("/games")
def games():
    return render_template("games.html")



@app.route('/game/<int:game_id>',methods=["POST","GET"])
def game_page(game_id):
    game = db.execute("SELECT *FROM games WHERE id=?",game_id)[0]
    if request.method == "POST":
        rating = request.form.get("userRating")
        rating= int(rating)
        current_rating = db.execute("SELECT rating FROM games WHERE id = ?",game_id)[0]["rating"]
        total = 0
        if not current_rating:
            total = rating
        else:
            current_rating = float(current_rating)
            total = round((current_rating +rating)/2,2)
            
          
        
        db.execute("UPDATE games SET rating =? WHERE id=?",total,game_id)
        return render_template("game_page.html", game=game)
    else:
        return render_template("game_page.html", game=game)
        



#login route
@app.route("/login",methods=["POST","GET"])
def login():
    if request.method =="POST":
       #check username
       email = request.form.get("email")
       emails = []
       for row in db.execute("SELECT email FROM users"):
           emails.append(row["email"])
       if not email or email not in emails:
           return render_template("login.html",message="email")
       
       #check password
       password = request.form.get("password")
       if not password:
            return render_template("login.html",message="password")
        
        # check user
       user = db.execute("SELECT * FROM users WHERE email = ?",email)
       if len(user) != 1 or not check_password_hash(user[0]["hash"],password):
           return render_template("login.html",message="password")
       
       #set user
       session["user_id"] = user[0]["id"]
       
       return redirect("/")
       
        
    else:
        if "user_id" in session:
            return redirect("/")
        return render_template("login.html")

#register route
@app.route("/register",methods=["POST","GET"])
def register():
    if request.method == "POST":
        # check email
        email = request.form.get("email")
        emails = []
        for row in db.execute("SELECT email FROM users"):
            emails.append(row["email"])
        if not email or not is_valid_email(email)or email in emails:
            return render_template("register.html",message="email")
        
        # check username
        usernames=[]
        for row in db.execute("SELECT username FROM users"):
            usernames.append(row["username"])
        username = request.form.get("username")
        if not username or username in usernames:
            return render_template("register.html",message="username")
        
        #check password
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if not password:
            return render_template("register.html",message="password")
        if password != confirmation or not confirmation:
            return render_template("register.html",message="confirmation")
        
        #add to user
        db.execute("INSERT INTO users(email,username,hash) VALUES(?,?,?)",email,username,generate_password_hash(password))
        
        #send registration email
        msg = Message("You are registered", sender='sharegamezinfo@gmail.com', recipients=["sharegamezinfo@gmail.com",email])
        msg.body = """Thank you for registering
        
        
        
        ShareGamez.co"""
        mail.send(msg)
        
        #redirect to login page
        return redirect("/login")
    else:
        return render_template("register.html")
    
@app.route("/logout")
def logout():
    #log player out
    session.clear()
    
    return redirect("/")


@app.route("/upload",methods=["POST","GET"])
@login_required
def upload():
    if request.method == "POST":
        if "file" not in request.files:
            return "No file part"
        
        #upload file
        file = request.files["file"]
        if file.filename == "":
            return render_template("upload.html",message="file")
        
        # get game name
        gamename = request.form.get("gamename")
        gamenames =[]
        for row in db.execute("SELECT name FROM games"):
            gamenames.append(row["name"])
        if not gamename or gamename in gamenames:
            return render_template("upload.html",message="gamename")
        
        #save file
        if file:
            #generate unique filename
            unique_filename = str(uuid.uuid4())
            file_extension = os.path.splitext(file.filename)[1]
            filename = unique_filename + file_extension
            
            #save file
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            
            #add game to games
            db.execute("INSERT INTO games(user_id,name,filename) VALUES(?,?,?)",session["user_id"],gamename,filename)
            
            
            return render_template("upload.html",message="uploaded")
        

        
    else:
        return render_template("upload.html")
    
@app.route("/mygames",methods=["POST","GET"])
@login_required
def mygames():
    if request.method == "POST":
        delete = request.form.get("delete")
        if delete:
            os.remove(app.config['UPLOAD_FOLDER']+"/"+db.execute("SELECT filename FROM games WHERE id=?",delete)[0]["filename"])
            db.execute("DELETE FROM games WHERE id=?",delete)
            
        return redirect("/mygames")
    else:
        # render user gamesa
        mygames = db.execute("SELECT *FROM games WHERE user_id =?",session["user_id"])
        return render_template("mygame.html",games=mygames)



    


#edit my game
@app.route("/editgame/<int:game_id>",methods =["POST","GET"])
def editgame(game_id):
    game = db.execute("SELECT * FROM games WHERE id=?",game_id)[0]
    if request.method == "POST":

        
        
        #get file
        if "image-file" not in request.files:
            return render_template("editgame.html",game=game,message="file")
        
        file = request.files["image-file"]
        if file.filename == '' or not allowed_file(file.filename):
            return render_template("editgame.html",game=game,message="file")
        
        
        if file:
            #generate unique filename
            unique_filename = str(uuid.uuid4())
            file_extension = os.path.splitext(file.filename)[1]
            filename = unique_filename + file_extension
            
            #save file
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            
        if db.execute("SELECT image FROM games WHERE id=?",game["id"])[0]["image"]:
            os.remove(app.config['UPLOAD_FOLDER']+"/"+db.execute("SELECT image FROM games WHERE id=?",game["id"])[0]["image"])
        
        db.execute("UPDATE games SET image =? WHERE id=?",filename,game_id)
        return redirect("/game/"+str(game_id))
    else:
        return render_template("editgame.html",game=game)

#edit description
@app.route("/editgamedescription/<int:game_id>",methods=["POST","GET"])
def editdesc(game_id):
    #get description
    description = request.form.get("description")
    db.execute("UPDATE games SET description=? WHERE id=?",description,game_id)
    return redirect("/game/"+str(game_id))




@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    # Create the path to the file
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # Check if the file exists
    if not os.path.exists(file_path):
        return "File not found"

    # Send the file to the user for download
    return send_file(file_path, as_attachment=True)

#profile route
@app.route("/profile")
def profile():
    user = db.execute("SELECT *FROM users WHERE id=?", session["user_id"])[0]
    return render_template("profile.html",user=user)

#edit profile
@app.route("/editprofile",methods=["POST","GET"])
def editprof():
    user = db.execute("SELECT *FROM users WHERE id=?", session["user_id"])[0]
    if request.method == "POST":
        #check username
        nusername = request.form.get("username")
        usernames = []
        for row in db.execute("SELECT username FROM users"):
            usernames.append(row["username"])
        if nusername in usernames or not nusername:
            return render_template("editprofile.html",user=user,message="username")
        
        #update username
        db.execute("UPDATE users SET username=? WHERE id=?",nusername,session["user_id"])
        return redirect("/profile")
        

    else:
        return render_template("editprofile.html",user=user)

if __name__ == "__main__":
    app.run(debug = True)