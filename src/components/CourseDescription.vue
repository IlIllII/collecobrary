<template>
<div>
    <div class="description" v-if="course != ''">
        <h3>{{course}}</h3>
        <p><strong>Description:</strong></p>
        <p>{{descriptions[course].description}}</p>
        <hr>
        <p>Provided by: <span v-for="equivalent of descriptions[course].courses" v-bind:key="equivalent.index">
            <span> | </span>
            <a :class="{active: (idx == equivalent.index)}" style="cursor: pointer" @click="idx = equivalent.index">{{equivalent.institution}}</a>
        </span>
        <span> | </span>
        </p>
        <p>{{descriptions[course].courses[idx].description}}</p>
        <p><a target="_blank" :href="descriptions[course].courses[idx].url">Go to course -&gt;</a></p>
        <button @click="complete()">
            <span v-if="show()">Toggle Incomplete</span>
            <span v-if="!show()">Toggle Complete</span>
        </button>
    </div>
</div>
  
</template>

<script>
export default {
    props: ["course", "descriptions"],
    data() {
        return {
            idx: 0
        }
    },
    methods: {
        complete() {
            if (localStorage.getItem(this.course) == "incomplete") {
                localStorage.setItem(this.course, "complete")
            } else {
                localStorage.setItem(this.course, "incomplete")
            }
            this.$forceUpdate()
        },
        show() {
            return localStorage.getItem(this.course) == "complete"
        }
    }
}
</script>

<style scoped>
.description {
    width: 300px;
    background-color: white;
    border: 3px solid #2c3e50;
    border-radius: 15px;
    padding: 10px;
    color: #2c3e50;
}

h3 {
    margin: 0 0 10px 0;
    text-align: left;
}

p {
    margin: 0 0 10px 0;
    font-size: 0.75em;
    line-height: 1.5em;
    text-align: left;
}

.active {
    font-weight: bold;
    color: #92fccc;
    background-color: #2c3e50;
    border-radius: 4px;
    padding: 2px 4px 5px 4px;
}
</style>