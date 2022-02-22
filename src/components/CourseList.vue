<template>
  <div>
    <div class="course-list">
      <h1>Course List</h1>
      <div class="scrollable">
        <div>
          <div
            class="course-button"
            v-for="course in courses"
            :key="course.id"
            @click="$emit('clickCourse', course)"
            @mouseover="$emit('highlightCourse', course)"
            :style="'background-color: ' + colormap[course.group] + ';'"
          >
            <span
              :style="
                'color: ' +
                (colormap[course.group] != null
                  ? parseInt('0x' + colormap[course.group].slice(1, 3)) +
                      parseInt('0x' + colormap[course.group].slice(3, 5)) +
                      parseInt('0x' + colormap[course.group].slice(5, 7)) <
                    (255 * 3) / 2
                    ? 'white'
                    : 'black'
                  : 'white') +
                ';'
              "
            >
              {{ course.id }}
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["courses", "subject", "colormap"],
  emits: ["highlightCourse", "clickCourse"],
};
</script>

<style scoped>
.course-list {
  position: fixed;
  left: 10px;
  top: 100px;
  width: 200px;
  display: flex;
  flex-direction: column;
  border: 3px solid #2c3e50;
  border-radius: 15px;
  padding: 10px;
  text-align: left;
  bottom: 100px;
  background-color: rgba(255, 255, 255, 0.7);
}

.scrollable {
  overflow-y: scroll;
  direction: rtl;
  scrollbar-width: thin;
  scrollbar-color: #2c3e50;
}

.scrollable::-webkit-scrollbar {
  width: 5px;
}

.scrollable::-webkit-scrollbar-thumb {
  background-color: #2c3e50;
  border-radius: 10px;
}

.course-button {
  color: white;
  background-color: #2c3e50;
  padding: 10px;
  margin: 5px;
  cursor: pointer;
  border-radius: 5px;
}

.course-button:hover {
  background-color: #54789c;
}
</style>