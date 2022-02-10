<template>
  <b-overlay :show="loading" rounded="sm">
    <b-container fluid>
      <b-row class="text-center">
        <b-col>
          <h1>{{ title }}</h1>
        </b-col>
      </b-row>
      <b-row class="text-center">
        <b-col>
          <b-button variant="info" @click="startGame">Play</b-button>
          <b-button variant="light">How to play</b-button>
        </b-col>
      </b-row>
      <b-row class="text-center">
        <b-col> Games Played: {{ stats.totalGames }} </b-col>
        <b-col> Player Wins: {{ stats.playerWins }} </b-col>
        <b-col> Computer Wins: {{ stats.computerWins }} </b-col>
      </b-row>
      <b-row class="text-center" v-if="gameInProgress">
        <b-col> Game In Progress... </b-col>
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
      gameInProgress: false,
      playerSequence: [],
      computerSequence: [],
    };
  },
  computed: {
    title() {
      return this.$store.state.title;
    },
    stats() {
      return {
        totalGames: this.$store.state.totalGames,
        playerWins: this.$store.state.playerWins,
        computerWins: this.$store.state.computerWins,
      };
    },
  },
  methods: {
    startGame() {
      this.loading = true;
      setTimeout(() => {
        this.loading = false;
        this.gameInProgress = true;
        console.log("start game");
      }, 1000);
    },
  },
};
</script>
