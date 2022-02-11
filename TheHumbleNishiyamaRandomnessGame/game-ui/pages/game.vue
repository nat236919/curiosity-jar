<template>
  <b-overlay :show="loading" rounded="sm">
    <b-container class="game" fluid>
      <!-- Stats -->
      <b-row class="text-center">
        <b-col>
          <h4>Games Played: {{ stats.totalGames }}</h4></b-col
        >
        <b-col>
          <h4>Player Wins: {{ stats.playerWins }}</h4></b-col
        >
        <b-col>
          <h4>Computer Wins: {{ stats.computerWins }}</h4></b-col
        >
      </b-row>

      <hr />

      <!-- Current Sequence -->
      <div class="sequence-container">
        <b-row>
          <p>Current Sequence:</p>
        </b-row>
        <b-row>
          <b-col v-for="i in 3" :key="i">
            <Card />
          </b-col>
        </b-row>
      </div>
      <!-- Computer Sequence -->
      <div class="sequence-container">
        <b-row>
          <p>Computer Sequence:</p>
        </b-row>
        <b-row>
          <b-col v-for="i in 3" :key="i">
            <Card />
          </b-col>
        </b-row>
      </div>
      <!-- Player Sequence -->
      <div class="sequence-container">
        <b-row>
          <p>Player Sequence:</p>
        </b-row>
        <b-row>
          <b-col v-for="i in 3" :key="i">
            <Card color="r" />
          </b-col>
        </b-row>
      </div>

      <hr />

      <!-- Selection -->
      <div class="sequence-selection-container">
        <b-row>
          <b-col>
            <p>Select a sequence</p>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <b-button-group size="lg">
              <b-button variant="dark" @click="">
                <h3>B</h3>
              </b-button>
              <b-button variant="danger" @click="">
                <h3>R</h3>
              </b-button>
            </b-button-group>
          </b-col>
        </b-row>
      </div>
    </b-container>
  </b-overlay>
</template>

<script>
export default {
  name: "Game",
  computed: {
    stats() {
      return {
        totalGames: this.$store.state.totalGames,
        playerWins: this.$store.state.playerWins,
        computerWins: this.$store.state.computerWins,
      };
    },
  },
  data() {
    return {
      loading: false,
      gameInProgress: false,
      playerSequence: [],
      computerSequence: [],
    };
  },
};
</script>

<style scoped>
.game {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.sequence-container {
  margin-top: 1rem;
}

.sequence-selection-container {
  text-align: center;
}
</style>