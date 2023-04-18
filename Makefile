initialize_git:
        @echo "git init ..."
        git init
        sleep 1
        git add .
        sleep 1
        git commit -m "My first commit"
        sleep 1
        git branch -M  main
        sleep 1
        git remote add origin https://github.com/EDJINEDJA/MedicationLLMQA.git
        sleep 1
        git push origin main
        
pushing_git:
        @echo "pushing .."
        git add .
        git commit -m $(var)
        git push origin main

pulling_git:
        @echo "puliing .."
        git pull origin main

config:
        @echo "env setup ..."
        pipenv run pre-commit install
        pipenv run python-dotenv

run:
        python app.py

env:
        pipenv shell

setup: initialize_git config
