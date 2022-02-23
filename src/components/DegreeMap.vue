<template>
  <div>
    <div class="chart">
      <div class="legend">
        <div class="legend-header">
          <h3>Legend</h3>
          <span
            v-if="showLegend == false"
            class="triangle-down"
            @click="showLegend = !showLegend"
          ></span>
          <span
            v-if="showLegend == true"
            class="triangle-up"
            @click="showLegend = !showLegend"
          ></span>
        </div>
        <div class="legend-inner" v-if="showLegend == true">
          <div class="legend-element">
            <span class="circle solid"></span>
            <p>Required</p>
          </div>
          <div class="legend-element">
            <span class="circle dotted"></span>
            <p>Elective</p>
          </div>
          <div class="legend-element">
            <span class="circle completed"></span>
            <p>Completed</p>
          </div>
          <div v-for="key of Object.entries(colorMapping)" :key="key">
            <div class="legend-element">
              <span
                class="circle"
                :style="
                  'background-color: ' +
                  key[1] +
                  '; border-color: ' +
                  key[1] +
                  '; border-style: solid'
                "
              ></span>
              <p>{{ key[0] }}</p>
            </div>
          </div>
          <p class="footnote">* Hover over nodes for course titles</p>
          <p class="footnote">* Double click nodes for more details</p>
        </div>
      </div>
      <div class="description">
        <course-description
          :course="highlightedCourse"
          :descriptions="descriptions"
        />
      </div>
      <div>
        <course-list
          :subject="subject"
          :courses="nodes"
          :colormap="colorMapping"
          @highlight-course="highlightHandler"
          @click-course="clickHandler"
        />
      </div>
    </div>
  </div>
</template>

<script>
import * as d3 from "d3";
import CourseDescription from "./CourseDescription.vue";
import CourseList from "./CourseList.vue";

let hovering = false;
let descriptionShowing = false;

function color(d, colorMapping) {
  return colorMapping[d.group];
}

function focusParents(parents, colorMapping) {
  for (let name of parents) {
    let parent = d3
      .select(`#${name.replace(/\s/g, "-")}`)
      .attr("fill", (d) => color(d, colorMapping));
    let prereqs = parent.data()[0].prereqs;
    if (prereqs.length != 0) {
      focusParents(prereqs, colorMapping);
    }
  }
}

function focusChildren(children) {
  for (let name of children) {
    let child = d3
      .select(`#${name.replace(/\s/g, "-")}`)
      .attr("fill", (d) => colorChildren(d));
    if (child.data()[0] != null) {
      let prereqFor = child.data()[0].prereqFor;
      if (prereqFor.length != 0) {
        focusChildren(prereqFor);
      }
    }
  }
}

function colorChildren() {
  return "gray";
}

export default {
  components: { CourseDescription, CourseList },
  props: ["propNodes", "propLinks", "subject", "descriptions"],
  data() {
    return {
      nodes: this.propNodes,
      links: this.propLinks,
      highlightedCourse: "",
      showLegend: true,
      colorMapping: {},
      descriptionShowing: false,
    };
  },
  mounted() {
    const height = window.innerHeight * 1.5;
    const width = window.innerWidth * 1.5;
    const radius = 30;
    let groups = [];

    // This populates prereqs for each node based on the links. This is
    // needed because of some changes made to the way the data is stored.
    this.nodes = this.propNodes;
    this.links = this.propLinks;
    for (let i = 0; i < this.links.length; i++) {
      for (let j = 0; j < this.nodes.length; j++) {
        if (
          this.links[i].target == this.nodes[j].id &&
          !this.nodes[j].prereqs.includes(this.links[i].source)
        ) {
          this.nodes[j].prereqs.push(this.links[i].source);
        }
        if (
          this.links[i].source == this.nodes[j].id &&
          !this.nodes[j].prereqFor.includes(this.links[i].target)
        ) {
          this.nodes[j].prereqFor.push(this.links[i].target);
        }
      }
    }

    for (let node of this.nodes) {
      if (!groups.includes(node.group)) {
        groups.push(node.group);
      }
    }

    for (let g of groups) {
      this.colorMapping[g] = "#" + Math.random().toString(16).substr(2, 6);
    }

    let colorMapping = this.colorMapping;

    let updateDescription = (name) => {
      this.highlightedCourse = name;
    };

    function color(d) {
      return colorMapping[d.group];
    }

    function colorChildren() {
      return "gray";
    }

    function outline(d) {
      if (d.elective == true) {
        return 5;
      } else {
        return 0;
      }
    }

    function outlineColor(d) {
      if (localStorage.getItem(d.id) == "complete") {
        return "#00ff00"; // green
      } else {
        return "#2c3e50"; // dark gray
      }
    }

    function chart(L, N) {
      const links = L.map((d) => Object.create(d));
      const nodes = N.map((d) => Object.create(d));

      const type = ["required"];

      const simulation = d3
        .forceSimulation(nodes)
        .force(
          "link",
          d3.forceLink(links).id((d) => d.id)
        )
        .force("charge", d3.forceManyBody().strength(-300))
        .force("x", d3.forceX())
        .force("y", d3.forceY())
        .force(
          "collide",
          d3.forceCollide(() => 65)
        );

      const svg = d3
        .create("svg")
        .attr("viewBox", [-width / 2, -height / 2, width, height]);

      svg
        .append("defs")
        .selectAll("marker")
        .data(type)
        .join("marker")
        .attr("id", (d) => `arrow-${d}`)
        .attr("viewBox", "0 -5 10 10")
        .attr("refX", radius + 15)
        .attr("refY", 0)
        .attr("markerWidth", 6)
        .attr("markerHeight", 6)
        .attr("orient", "auto")
        .append("path")
        .attr("fill", "gray")
        .attr("d", "M0,-5L10,0L0,5");

      const link = svg
        .append("g")
        .attr("fill", "none")
        .attr("stroke-width", 1.5)
        .selectAll("path")
        .data(links)
        .join("path")
        .attr("stroke", "gray")
        .attr(
          "marker-end",
          (d) => `url(${new URL(`#arrow-${d.type}`, location)})`
        );

      const node = svg
        .append("g")
        .attr("fill", "currentColor")
        .attr("stroke-linecap", "round")
        .attr("stroke-linejoin", "round")
        .selectAll("g")
        .data(nodes)
        .join("g")
        .call(drag(simulation));

      node
        .append("circle")
        .attr("stroke", (d) => outlineColor(d))
        .attr("stroke-width", 3)
        .attr("stroke-dasharray", (d) => outline(d))
        .attr("stroke-linecap", "round")
        .attr("r", radius)
        .attr("fill", (d) => color(d))
        .attr("id", (d) => d.id.replace(/\s/g, "-"));

      node.append("title").text((d) => d.id);

      node.on("dblclick", (e, d) => {
        updateDescription(nodes[d.index].id);
        d3.selectAll("circle").attr("fill", "white");
        d3.select(`#${d.id.replace(/\s/g, "-")}`).attr("fill", (d) => color(d));
        focusParents(d.prereqs, colorMapping);
        focusChildren(d.prereqFor);
        hovering = true;
        descriptionShowing = true;
      });

      node.on("mouseover", (e, d) => {
        function focusParents(parents) {
          for (let name of parents) {
            let parent = d3
              .select(`#${name.replace(/\s/g, "-")}`)
              .attr("fill", (d) => color(d));
            let prereqs = parent.data()[0].prereqs;
            if (prereqs.length != 0) {
              focusParents(prereqs);
            }
          }
        }

        function focusChildren(children) {
          for (let name of children) {
            let child = d3
              .select(`#${name.replace(/\s/g, "-")}`)
              .attr("fill", (d) => colorChildren(d));
            if (child.data()[0] != null) {
              let prereqFor = child.data()[0].prereqFor;
              if (prereqFor.length != 0) {
                focusChildren(prereqFor);
              }
            }
          }
        }

        // Color children and parent nodes
        if (descriptionShowing == false) {
          d3.selectAll("circle").attr("fill", "white");
          d3.select(`#${d.id.replace(/\s/g, "-")}`).attr("fill", (d) =>
            color(d)
          );
          focusParents(d.prereqs);
          focusChildren(d.prereqFor);
          hovering = true;
        }
      });

      node.on("mouseout", () => {
        hovering = false;
        if (descriptionShowing == false) {
          d3.selectAll("circle").attr("fill", (d) => color(d)); // Reset colors
        }
      });

      simulation.on("tick", () => {
        link.attr("d", linkArc);
        node.attr("transform", (d) => `translate(${d.x},${d.y})`);
      });

      svg.on("click", () => {
        if (hovering == false) {
          updateDescription("");
          descriptionShowing = false;
          d3.selectAll("circle").attr("fill", (d) => color(d)); // Reset colors
        }
      });

      return svg.node();
    }

    function linkArc(d) {
      return `M${d.source.x},${d.source.y}A0,0 0 0,1 ${d.target.x},${d.target.y}`;
    }

    function drag(simulation) {
      function dragstarted(event, d) {
        if (!event.active) simulation.alphaTarget(0.05).restart();
        d.fx = d.x;
        d.fy = d.y;
      }

      function dragged(event, d) {
        d.fx = event.x;
        d.fy = event.y;
      }

      function dragended(event, d) {
        if (!event.active) simulation.alphaTarget(0);
        d.fx = null;
        d.fy = null;
      }

      return d3
        .drag()
        .on("start", dragstarted)
        .on("drag", dragged)
        .on("end", dragended);
    }
    document
      .querySelector("div.chart")
      .appendChild(chart(this.links, this.nodes));
  },
  methods: {
    clickHandler(course) {
      let updateDescription = (name) => {
        this.highlightedCourse = name;
      };

      let colorMap = this.colorMapping;

      updateDescription(course.id);
      d3.selectAll("circle").attr("fill", "white");
      d3.select(`#${course.id.replace(/\s/g, "-")}`).attr("fill", (d) =>
        color(d, colorMap)
      );
      focusParents(course.prereqs, colorMap);
      focusChildren(course.prereqFor);
      descriptionShowing = true;
    },
    highlightHandler(course) {
      if (!descriptionShowing) {
        let colorMap = this.colorMapping;
        d3.selectAll("circle").attr("fill", "white");
        d3.select(`#${course.id.replace(/\s/g, "-")}`).attr("fill", (d) =>
          color(d, colorMap)
        );
        focusParents(course.prereqs, colorMap);
        focusChildren(course.prereqFor);
        hovering = true;
      }
    },
  },
};
</script>

<style scoped>
.description {
  position: fixed;
  left: 250px;
  top: 100px;
}

.legend {
  position: fixed;
  right: 10px;
  top: 100px;
  width: 200px;
  display: flex;
  flex-direction: column;
  border: 3px solid #2c3e50;
  border-radius: 15px;
  padding: 10px;
  text-align: left;
  background-color: rgba(255, 255, 255, 0.7);
}

.legend h3 {
  margin: auto;
}

.footnote {
  font-size: 0.6em;
  line-height: 1em;
  text-align: left;
}

.circle {
  width: 2em;
  height: 2em;
  border-radius: 100px;
  margin-right: 10px;
}

.solid {
  border-color: #2c3e50;
  border-style: solid;
}

.completed {
  border-color: rgb(0, 255, 0);
  border-style: solid;
}

.dotted {
  border-color: #2c3e50;
  border-style: dotted;
}

.legend-element {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin: 0;
  font-size: 0.75em;
  line-height: 0.75em;
}

.legend-header {
  display: flex;
  flex-direction: row;
  align-items: flex-end;
  justify-content: flex-start;
}

.triangle-down {
  border-right: 10px solid transparent;
  border-left: 10px solid transparent;
  border-bottom: 5px solid transparent;
  border-top: 15px solid #2c3e50;
  cursor: pointer;
}

.triangle-up {
  border-right: 10px solid transparent;
  border-left: 10px solid transparent;
  border-top: 5px solid transparent;
  border-bottom: 15px solid #2c3e50;
  cursor: pointer;
}

.tooltip {
  color: red;
}
</style>