# Canvas modules to static Vuepress website
This repository is a fork of [Roland Hoffman's repository](https://github.com/r-hoffmann/canvas-api), with minor updates to this readme and vuepress2pdf.py to make it work on UvA's Information Theory 2019-2020 course. This repository contains all elements needed to generate a static site from a course of Canvas. For now it contains the course Information Theory 2018-2019 taught at the UvA, which can be served immediately.

# Information Theory 2018-2019
If you just want to use this repository for Information Theory, follow the following steps.
1. Clone this repository, e.g. 
`git clone https://github.com/r-hoffmann/canvas-api.git`
2. Go to the root directory of the static website and serve it, e.g. 
`cd canvas-api/docs/.vuepress/dist`
`python3 -m http.server 80`
If the port 80 is already used, change it appropriately. 
3. Now you can go to your browser and browse to `locahost:80` (or another port if you have chosen to in the last step)

# Convert other course to vuepress and pdf
It is possible to generate a pdf for another course with this repository. First we obtain the canvas content with the following commands.
1. Clone this repository, e.g. 
`git clone https://github.com/r-hoffmann/canvas-api.git`
2. Copy the sample_local_settings.py to local_settings.py, e.g. 
`cp sample_local_settings.py local_settings.py`
3. Obtain a Canvas API Token and paste this in the previously created file, you might also want to change the course id in the same file.
4. Retrieve the contents from the Canvas servers and store them in the `docs` directory. Just run `python vuepress_pages.py`

Now we have a local copy of the Canvas pages in the `docs` directory, each chapter and section should have its own subdirectory. The markdown files are supported by https://github.com/vuejs/vuepress and we can serve this directory like the previous section. The next steps will convert the vuepress pages to a pdf, note that this part uses yarn, but npm can also be used.

5. Install the npm packages, e.g. run `yarn add vuepress` in the root directory
6. Start the local server, e.g. `yarn run docs:dev`. This will output an IP: `VuePress dev server listening at http://localhost:8080/`.
7. Scrape the local server, convert these to pdf files and merge these. This can easily be done with a Python script, be sure to give the IP as a parameter, e.g. `python vuepress2pdf.py http://localhost:8080`. Note that this script requires a few Python packages which should be installed with `pip install --user <package-name>`.
8. Done! The pdf is in `./pdf/Information Theory.pdf`, all seperate sections can be found in the same directory.
