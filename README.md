<!-- Header -->
<div id="top" align="center">
  <br />

  <!-- Logo -->
  <img src="static/main/img/logo.png" alt="Logo" width="200" height="200">

  <!-- Title -->
  ### OACPL

  <!-- Description -->
  **Deprecated:** Ontario Association of Child Protection Lawyers

  <!-- Repo badges -->
  [![Version](https://img.shields.io/badge/dynamic/json.svg?label=Version&style=for-the-badge&url=https://git.zakscode.com/api/v1/repos/ztimson/oacpl/tags&query=$[0].name)](https://git.zakscode.com/ztimson/oacpl/tags)
  [![Pull Requests](https://img.shields.io/badge/dynamic/json.svg?label=Pull%20Requests&style=for-the-badge&url=https://git.zakscode.com/api/v1/repos/ztimson/oacpl&query=open_pr_counter)](https://git.zakscode.com/ztimson/oacpl/pulls)
  [![Issues](https://img.shields.io/badge/dynamic/json.svg?label=Issues&style=for-the-badge&url=https://git.zakscode.com/api/v1/repos/ztimson/oacpl&query=open_issues_count)](https://git.zakscode.com/ztimson/oacpl/issues)

  <!-- Links -->

  ---
  <div>
    <a href="https://git.zakscode.com/ztimson/oacpl/releases" target="_blank">Release Notes</a>
    • <a href="https://git.zakscode.com/ztimson/oacpl/issues/new?template=.github%2fissue_template%2fbug.md" target="_blank">Report a Bug</a>
    • <a href="https://git.zakscode.com/ztimson/oacpl/issues/new?template=.github%2fissue_template%2fenhancement.md" target="_blank">Request a Feature</a>
  </div>

  ---
</div>

## Table of Contents
- [OACPL](#top)
    - [About](#about)
        - [Built With](#built-with)
    - [Setup](#setup)
        - [Production](#production)
        - [Development](#development)
    - [License](#license)

## About

**Deprecated**

A Django website for the Ontario Ascociation of Child Protection Lawyers which not only acts as a landing page for the non-profit but also provides the following services:

- Member enrollment & profile pages
- Public FAQ forum to ask registered lawyers questions
- Event calendar & registration
- Newsletters & press releases
- Case law directory allowing lawyers to quickly search and find president for cases
- An expert lookup directory so that lawyers can research expert witnesses before putting them on the stand

### Built With
[![Django](https://img.shields.io/badge/django-0C4B33?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
[![Docker](https://img.shields.io/badge/Docker-384d54?style=for-the-badge&logo=docker)](https://docker.com/)
[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python)](https://www.python.org/)

## Setup

<details>
<summary>
  <h3 id="production" style="display: inline">
    Production
  </h3>
</summary>

#### Prerequisites
- [Docker](https://docs.docker.com/install/)

#### Instructions
1. Run the docker image: `docker run -p 80:8000 git.zakscode.com/ztimson/oacpl:latest`
2. Open [http://localhost](http://localhost)
</details>

<details>
<summary>
  <h3 id="development" style="display: inline">
    Development
  </h3>
</summary>

#### Prerequisites
- [Python](https://www.python.org/downloads/)

#### Instructions
1. Install the dependencies: `pip install -r requirements.txt`
2. Run database migrations: `python3 manage.py makemigrations && python3 manage.py migrate`
3. Collect static files: `python3 manage.py collectstatic`
4. Start server: `python3 manage.py runserver 0.0.0.0:8000`
5. Open http://localhost:8000

</details>

## License
Copyright © 2023 Zakary Timson | All Rights Reserved

See the [license](./LICENSE) for more information.
