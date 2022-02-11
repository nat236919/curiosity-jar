<template>
  <b-overlay :show="loading" rounded="sm">
    <b-container class="index" fluid>
      <b-row class="text-center">
        <b-col>
          <h1>{{ title }}</h1>
        </b-col>
      </b-row>
      <b-row class="text-center">
        <b-col>
          <b-button variant="info" @click="startGame">Play</b-button>
          <b-button variant="outline-dark" @click="goToHowToPlay">How to play</b-button>
        </b-col>
      </b-row>
    </b-container>
  </b-overlay>
</template>

<script>
export default {
  name: "IndexPage",
  data() {
    return {
      loading: false,
    };
  },
  computed: {
    title() {
      return this.$store.state.title;
    },
  },
  methods: {
    startGame() {
      this.loading = true;
      setTimeout(() => {
        this.loading = false;
        this.$router.push("/game");
      }, 1000);
    },
    goToHowToPlay() {
      this.$router.push("/how-to-play");
    },
  },
};
</script>

<style scoped>
.index {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>