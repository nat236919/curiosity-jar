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
          <b-col v-for="(color, i) in computerSequence" :key="i">
            <Card :color="color" />
          </b-col>
        </b-row>
      </div>
      <!-- Player Sequence -->
      <div class="sequence-container">
        <b-row>
          <p>Player Sequence:</p>
        </b-row>
        <b-row>
          <b-col v-for="(color, i) in playerSequence" :key="i">
            <Card :color="color" />
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
              <b-button variant="dark" @click="playerSelect('b')">
                <h3>B</h3>
              </b-button>
              <b-button variant="danger" @click="playerSelect('r')">
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
      deckLimit: 56,
      loading: false,
      gameInProgress: false,
      colors: ["b", "r"], // black and red
      decks: [],
      currentSequence: [],
      playerSequence: [null, null, null],
      computerSequence: [null, null, null],
    };
  },
  methods: {
    init() {
      this.decks = this.getRandomSequence(this.deckLimit);
      this.computerSequence = this.getRandomSequence();
    },
    getRandomColor() {
      return this.colors[Math.floor(Math.random() * this.colors.length)];
    },
    getRandomSequence(n = 3) {
      let sequence = [];
      for (let i = 0; i < n; i++) {
        sequence.push(this.getRandomColor());
      }
      return sequence;
    },
    playerSelect(color) {
      if (this.playerSequence.length < 3) {
        this.playerSequence.push(color);
      } else {
        // remove first item and add new item
        this.playerSequence.shift();
        this.playerSequence.push(color);
      }
    },
  },
  mounted() {
    this.init();
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