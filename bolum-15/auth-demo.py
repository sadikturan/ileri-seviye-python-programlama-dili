import pyrebase

firebaseConfig = {
  "apiKey": "",
  "authDomain": "",
  "projectId": "",
  "storageBucket": "",
  "messagingSenderId": "",
  "appId": "",
  "databaseURL" : ""
}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()

def signUp():
    email = input("email: ")
    password = input("password: ")

    auth.create_user_with_email_and_password(email, password)
    print("kullanıcı oluşturuldu.")

def login():
    email = input("email: ")
    password = input("password: ")

    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print(user)
        print(auth.get_account_info(user["idToken"]))
        print("login yapıldı")
    except:
        print("hatalı email yada parola")

# signUp()
login()