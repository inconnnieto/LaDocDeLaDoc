# 2_Secunda

### brief:
Vous devez créer votre propre site de documentation et le 
mettre en ligne.

La première doc que vous allez y mettre devra concerner 
la doc elle-même : “Comment mettre à jour la doc ? “.

### my attempt
I have chosen to use MkDocs to work with Markdown files. MkDocs is a static site generator designed for project documentation. MkDocs is a python-based tool so first step is to check if Python is installed

### 1. Check if Python is installed
in [Prima](1_Prima.md) I have written a script to check what version of Python was installed in PowerShell. if not, install Python here

### 2. Install MkDocs
open a terminal window
```bash
pip install mkdocs
```
this installs MkDocs with all required dependencies

if this does not work try
```bash
python3 -m pip install mkdocs
```

#### 2.1 Check installation
```bash
mkdocs --version
```
should return version number

### 3. Create my documentation site
navigate to the folder where I wanted to my project.

I called my documentation ma_doc

```bash
mkdocs new ma_doc
```

This created a new directory called `ma_doc` with the basic structure of a MkDocs site.

Navigate to the new project folder:
```bash
cd ma_doc
```

Preview site locally:

Before pushing anything to GitLab, I wanted to see how the site looked locally. 

```bash
mkdocs serve
```
This started local development server where I could view my site by navigating to http://127.0.0.1:8000/ in a web browser.

### 4. Linking MkDocs to GitLab pages
#### 4.1 Initialised a Git repository.

Inside my `ma_doc` folder I initialised a new Git repository
```bash
git init
```
#### 4.2 Create a new GitLab project
On GitLab, I created a new project nad named it Prairie IA.

#### 4.3 Add remote GitLab repository
linked my local repository to the remote GitLab repository
```bash
git remote add origin https://gitlab.com/prairie-ia/ma_doc.git 
```

#### 4.4 Push the code to GitLab
```bash
git add .
git commit -m "initial commit Prairie IA"
git push -u origin master
```

### 5 Setting up GitLab Pages for automatic deployment

automatically deploy my MkDocs site whenever I push changes to the repository using `.gitlab-ci.yml` file.

#### 5.1 Create a `.gitlab-ci.yml` file
In the root of my project direcoty I created a `.gitlab-ci.yml` file
```yaml
# The Docker image that will be used to build your app
image: python:3.12
# Functions that should be executed before the build script is run
before_script:
  - pip install mkdocs
  - pip install mkdocs-material
  - pip install "mkdocs-material[imaging]"
pages:
  script:
    - mkdocs build
    - mv site public
  artifacts:
    paths:
      # The folder that contains the files to be exposed at the Page URL
      - public
  rules:
    # This ensures that only pushes to the default branch will trigger
    # a pages deploy
    - if: $CI_COMMIT_REF_NAME == $CI_DEFAULT_BRANCH
```

#### 5.2 push the file to GitLab 
#### 5.3 GitLab automatically builds and deploys the site

Now, every time I push changes to the default branch (mai), GitLab CI/CD will automatically:

1. Install MkDocs (if not already installed).
2. Build the site with the mkdocs build command.
3. Move the generated files to the public folder.
4. Deploy the public folder to GitLab Pages.