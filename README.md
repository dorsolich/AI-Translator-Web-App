# AI-Translator-Web-App
Web app developed using Flask framework that uses DeepL API to translate any input text to an user-specified language.
Feel free to clone de repo, set-up the project and try it yourself.

# Project set-up

## 1. Create a virtual environment & install requirements

To create a virtual environment, open up a bash terminal and cd to the project root directory (AI-Translator-Web-App).
On the terminal, do:

```
python -m venv .venv
.venv/Scripts/activate
```
Then, instal the requirements:

```
pip install -r requirements
```

## 2. Authentication Key for DeepL API (DEEPL_SECRET_KEY)

DeepL is a machine translation provider. Their service can be accessible via API. 
They have developed official libraries for the DeepL API. In this application, I am using the Pypi package, as I am building it with Python.
For more information, visit: https://www.deepl.com/docs-api. To access the API, you need to get a Authentication Key for DeepL API that is provided to you when you create an account.



### 2.1 Get your Authentication Key for DeepL API

Go to https://www.deepl.com/pro-api?cta=header-pro-api/ and sign up for free.
You will find your Authentication Key for DeepL API in your Account Details. Copy to clipboard the Authentication Key.
Your Authentication Key is private and you should not share it with anyone.



### 2.2 Set up you Authentication Key for DeepL API as an Environment Variable.

On the bash terminal with cd into root directory (AI-Translator-Web-App), set-up your secret Authentication Key for DeepL API as an environment variable called DEEPL_SECRET_KEY:

```
setx DEEPL_SECRET_KEY {paste-the-key}
```
To make sure that is correctly set-up, re-start the terminal and do:

```
echo $DEEPL_SECRET_KEY
```

# Run the app

On the bash terminal (root directory), do:

```
set FLASK_ENV=development
```

```
flask run
```

Try it yourself!

Provate voi stessi!

ぜひお試しください。

Попробуйте сами!

Pruébelo usted mismo.

Versuchen Sie es selbst!

