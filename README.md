## This is a super simple django blog web application😜.

## Requirements
- Install Python to your PC.
- Download any text editor (like [Visual Studio Code](https://code.visualstudio.com/download)) and install it.
- Install Postgresql. Probably no need to say download first.

## Running Locally
1. Clone project.
2. Open `cmd/terminal/cmder` and go to the project directory.
3. Create a virtual env using this command `virtualenv env_name`.If you don't have `virtualenv` installed, just run this `pip install virtualenv` first.
4. After that activate virtual env.
5. And then run `pip install -r requirements.txt`
6. You must have to configure your database using your credentials in `settings.py` file.
6. Finally run `python manage.py runserver` command.

## Workflow
These are the basic steps/rules to follow when working on the codebase:
1. For everything you plan to push to `master` create a new branch for it, either name it `feature/{feature-name}` or `bug/{bug-name}`.
2. Open Project in a Text Editor(vscode).
3. You should now have the project locally running and you can start making changes to push in to your new branch.
4. Once you think your changes are done, make a pull request on Github and assign a member to review your code. Once approved, you will be able to merge it into `master`.
