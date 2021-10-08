# [collecobrary](https://curated-courses.herokuapp.com/) [![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=Make%20learning%20fun%20and%20easy&url=https://github.com/nietsymerej/collecobrary&hashtags=github,education,vuejs,webdev,developers)

[![Vue](https://img.shields.io/badge/vue-%5E3.0.0-informational)](https://github.com/vuejs/vue)
[![d3](https://img.shields.io/badge/d3-%5E7.0.3-informational)](https://github.com/d3/d3)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](https://github.com/nietsymerej/collecobrary/blob/master/LICENSE)
[![](https://img.shields.io/github/last-commit/nietsymerej/collecobrary)](https://github.com/nietsymerej/collecobrary)

**The goal of this project is to make online learning easy and fun by presenting the best free online courses in an appealing and intuitive way.**

It is very much in its infancy. As such, it could really use your help and input.

![collecobrary_node_hover_and_dblclick](https://user-images.githubusercontent.com/78166995/134691867-8195d604-d28e-43b7-8476-bb21f9ce4f39.PNG)

## Table of Contents

- [About](#about)
- [Quickstart](#quickstart)
- [Contributing](#contributing)


## About

The idea for this project spawned from my own frustration with the current online learning landscape. As [Reich and Ruipérez-Valiente](https://www.umt.edu/provost/docs/MOOC-pivot.pdf) point out, some online education platforms have massive audiences, which signals that there is quite a demand for online education. Yet, according to the article, user retention rates are ultra low.

![science-screenshot](https://user-images.githubusercontent.com/78166995/136632980-cdc27747-8ab8-4fdb-9d21-62d2c7564406.PNG)

According to my own research, this is because MOOCs are shit, as are many other resources. Detailing all of the ways in which every platform is lacking would take ages, but at a high level I have 3 criticisms:

### Three problems this project aims to solve

1. **Poor quality.** Many platforms have high variability when it comes to course quality, and many courses designed for online learners are significantly dumbed down.
2. **Too many choices.** Some platforms provide thousands of courses. We don't need 100 different Calc I courses; the top three will suffice.
3. **No structure or progression.** It is hard to know what you don't know, and many platforms don't lay out equivalencies, prerequisites, or roadmaps guiding students through broad subject, making it difficult to come up with a study plan.

While some existing products contain one or two of these elements, none has all three. The goal of this project is to create a free resource that satisfies this trilemma. I have made a start, but with a little help it could be so much better.

## Quickstart

If it is your first time contributing, you might want to see [contributing](#contributing) to get a sense of the project first before starting.

### Project setup

#### First, clone the repo and install dependencies:
```
git clone https://github.com/nietsymerej/collecobrary.git
cd collecobrary
npm install
```

#### Now you are ready to go. To run the server in development mode:
```
npm run serve
```

This will run the server on localhost:8080 and provide hot-reloads when saving files.

#### To compile and minify for production:
```
npm run build
```

#### To run the linter:
```
npm run lint
```

Once everything checks out locally, you can merge your pull request with the master to redeploy the live website. We can set up a test server later if we need to.

## Contributing

If you want to help contribute, here are a few things that would really make an impact:

1. Have a good idea for how the project can be better? Please share it!
2. Know of an excellent online course? Please share it!
3. You can code? Help code new features or clean up the codebase!
4. You think this project is cool? Share it with friends!
5. Do you think you can help in another way? Please share your idea!


Feel free to say hello and ask if you have any questions or comments. All feedback is welcome and encouraged. If you decide to help, check out [CONTRIBUTING.md](https://github.com/nietsymerej/collecobrary/blob/master/CONTRIBUTING.md) to see more details about the project.


## Currently on my to-do list

2. Make a CONTRIBUTING.md
4. Refactor digraph code into separate script
