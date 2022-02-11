<template>
  <b-card class="card mb-4" :class="classColorName">
    <b-card-title>
      <h1>{{ cardTitle }}</h1>
    </b-card-title>
  </b-card>
</template>

<script>
export default {
  name: "Card",
  props: {
    color: {
      type: String,
      default: "",
    },
  },
  computed: {
    colorName() {
      let colorName = null;
      if (this.color === "r") colorName = "red";
      else if (this.color === "b") colorName = "black";
      return colorName;
    },
    classColorName() {
      return `card ${this.colorName}`;
    },
    cardTitle() {
      let title = "?";
      if (this.color === "r") {
        title = "R";
      } else if (this.color === "b") {
        title = "B";
      }
      return title;
    },
  },
};
</script>

<style scoped>
.card {
  background-color: #eeeeee;
  text-align: center;
}

.black {
  background-color: #343a40;
  color: #f7f7f7;
}

.red {
  background-color: #dc3545;
  color: #f7f7f7;
}
</style>