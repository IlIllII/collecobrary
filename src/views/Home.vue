<template>
  <div>
    <div class="subject-select" v-if="subjectSelect">
      <h1>Shapes of Knowledge</h1>
      <h5>
        Say hi ❤ - <a href="https://discord.gg/fbbYhvkaBx">Discord</a> |
        <a href="https://github.com/IlIllII/collecobrary">Github</a>
      </h5>
      <hr width="250" />
      <div>
        <h2>What would you like to learn?</h2>
        <div class="subject-container">
          <div
            class="subject-listing"
            v-for="subject in subjects"
            :key="subject"
            @click="createMap(subject.id)"
          >
            <span>{{ subject.id }}</span>
          </div>
        </div>
      </div>
    </div>
    <div class="degree-map" v-if="!subjectSelect">
      <div class="title-header">
        <h1>{{ selectedSubject }}</h1>
      </div>
      <DegreeMap
        :propNodes="nodes"
        :propLinks="links"
        :descriptions="descriptions"
        :subject="selectedSubject"
      />
      <span class="back" @click="goBack"></span>
    </div>
  </div>
</template>

<script>
import subjects from "@/assets/subjects.json";
import masterNodes from "@/assets/masterNodes.json";
import masterLinks from "@/assets/masterLinks.json";
import descriptions from "@/assets/descriptions.json";
import DegreeMap from "@/components/DegreeMap.vue";

// console.log(masterNodes);
// console.log(masterLinks);
// console.log(descriptions);

// Alphabetically sort subjects for display
let sortedSubjects = subjects.sort((a, b) => a.id.localeCompare(b.id));

export default {
  name: "Home",
  components: {
    DegreeMap,
  },
  data() {
    return {
      subjects: sortedSubjects,
      subjectSelect: true,
      selectedSubject: "",
      nodes: [],
      links: [],
      descriptions: descriptions,
    };
  },
  methods: {
    goBack() {
      this.subjectSelect = true;
      this.selectedSubject = "";
      this.nodes = [];
      this.links = [];
    },
    createMap(subjectID) {
      this.subjectSelect = false;
      this.selectedSubject = subjectID;

      // Find course list from subjects.json
      let courses;
      for (let subject of this.subjects) {
        if (subjectID == subject.id) {
          courses = subject.courses;
        }
      }

      for (let course of courses) {
        for (let link of masterLinks) {
          if (course.id == link.target) {
            for (let c of courses) {
              if (c.id == link.source) {
                link.type = "required";
                this.links.push(link);
              }
            }
          }
        }
        for (let node of masterNodes) {
          if (course.id == node.id) {
            node.elective = course.elective;
            this.nodes.push(node);
          }
          if (localStorage.getItem(course.id) == null) {
            localStorage.setItem(course.id, "incomplete");
          }
        }
      }
    },
  },
};
</script>

<style scoped>
.back {
  position: fixed;
  left: 25px;
  top: 25px;
  margin-top: 5px;
  border-bottom: 10px solid transparent;
  border-left: 5px solid transparent;
  border-top: 10px solid transparent;
  border-right: 15px solid #2c3e50;
  cursor: pointer;
}

.title-header {
  position: fixed;
  top: 10px;
  left: 0px;
  right: 0px;
  margin: auto;
}

.subject-select {
  margin-top: 100px;
}

.subject-listing {
  color: white;
  background-color: #2c3e50;
  max-width: 20em;
  width: fit-content;
  padding: 10px;
  margin: 5px;
  cursor: pointer;
  border-radius: 5px;
}

.subject-listing:hover {
  transform: scale(1.05);
}

.subject-container {
  margin: auto;
  max-width: 700px;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
}
</style>>
