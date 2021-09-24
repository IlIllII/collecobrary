# collecobrary

**Website presenting university degree roadmaps that contain 100% online, free college courses.**

The idea of this project is to present a collection of college courses sourced from OCW and university course webpages.

This repo is a webpage mostly geared toward the visualization aspects of the project. I made the curricula digraph visualization using d3. My other repo, curated-courses, contains other content of the website and was actually a past version. Sometime in the future I may marry these two projects to make a full featured website.

## Current Features

The landing page, shown below, is comprised of a list of subject areas, with each subhject being a button that, when pushed, generates a digraph depicting the curriculum. The list is automatically generated from the data files. This is an imporvement from a previous version of the project where the buttons were hardcoded in.

![collecobrary_landing_page](https://user-images.githubusercontent.com/78166995/134688002-efaaefe0-bb3d-48cb-95e9-4b7bc75737b0.PNG)

Next, is the curriculum digraph itself. It is made using d3 and is basically a force directed graph where physics forces act on each node and edge to control the appearance of the graph, with only the topology being defined by the data. This is an improvement from a previous version, since now you don't have to determine x and y coordinates for each course, although the graph can get convoluted as interconnections grow. One solution to this is to prune redundant edges, though sometimes high interconnectivity cannot be avoided if a course has many prereqs.

Additionally, right now the category colors for the legend are randomly generated. I think that it would be better if I hardcoded a color for each category so then users can easily remember which courses are which since I don't have labels on the nodes, but as categories grow I would run out of colors. Randomness makes it easier from a design perspective, but may not be that user friendly.

![collecobrary_course_digraph](https://user-images.githubusercontent.com/78166995/134689102-3f8a7a37-615b-4f93-8181-24e9717dc839.PNG)

Finally, when you hover over a node, a tooltip reveals the name of the course and parent and child prereqs change their coloring. If you double click a node, a description and link to the course appears.

![collecobrary_digraph_hover](https://user-images.githubusercontent.com/78166995/134690221-18796d3e-f08a-4931-8da4-f563456456f0.PNG)

These features are alright, but there are still some improvements I can make for v3. These include:

- Displaying course titles when cursor is in the neighborhood of a course rather than directly on hover. This would allow users to more quickly explore the graph.
- Somehow highlight starting courses, perhaps by bolding their outlines or making the edges of the graph thicker. This would help visualize the flow of the graph. Since it is acyclic, there is a definite direction that is hard to grasp in the current design.
- It would be useful if there was a sidebar you could scroll to look at all of the courses, sorted by chronological order or network hops from a starting node. This sidebar would interface with course hovering to make the structure of the degree roadmap mopre obvious.
- Finally, it may be benficial to have an about section for each graph, explaining curriculum choices and why the courses are arranged the way that they are.

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
