# La doc de la doc

## Comment mettre à jour la doc?

### 1. Create new page

create a new `.md` file in the `/docs` folder of the project. Write down notes and information

### 2. Push the changes to GitLab pages
After the input, push to GitLab repository so they can be deployed to GitLab pages.

Add clear comments for `git commit -m "comments"` to be able to trace back what has been edited when you look back on your repo.

For an existing repo:
```bash
git add .
git commit -m "insert comment"
git push
```

### 3. Deploying (automatic)

`.gitlab-ci.yml` file is set up in the repository so GitLab automatically takes care of building and deploying the site whenever changes are pushed to the default branch.
In this case, the `main` branch has been mislabeled as `mai` and so all updates are pushed to `mai`.

GitLab CI/CD automatically triggers the pipeline and executes the steps defined in the `.gitlab-ci.yml` file, including building the site using MkDocs and deploying it to GitLab Pages.

It looks like this:
```yml
# The Docker image that will be used to build your app
image: python:3.12
# Functions that should be executed before the build script is run
before_script:
  - pip install mkdocs
  - pip install mkdocs-material
  - pip install mkdocs mkdocs-mermaid2-plugin --verbose
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

This configuration ensures that:

* The necessary tools (like MkDocs) are installed.
* The site is built and the generated files are moved to the public folder.
* The deployment happens automatically when you push to the default branch (mai).