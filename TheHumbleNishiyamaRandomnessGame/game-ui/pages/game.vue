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

      <!-- Controllers -->
      <b-row class="text-center">
        <b-col>
          <b-button
            pill
            variant="info"
            :disabled="!readyToStart"
            @click="startGame"
            size="lg"
            v-if="!gameInProgress"
          >
            Play
          </b-button>
          <b-button pill variant="warning" @click="resetGame" size="lg" v-else>
            Reset
          </b-button>
        </b-col>
      </b-row>

      <!-- Current Sequence -->
      <div class="sequence-container">
        <b-row>
          <p>Current Sequence:</p>
        </b-row>
        <b-row>
          <b-col v-for="(color, i) in currentSequence" :key="i">
            <Card :color="color" />
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
              <b-button
                variant="dark"
                :disabled="gameInProgress"
                @click="playerSelect('b')"
              >
                <h3>B</h3>
              </b-button>
              <b-button
                variant="danger"
                :disabled="gameInProgress"
                @click="playerSelect('r')"
              >
                <h3>R</h3>
              </b-button>
              <b-button
                variant="outline-warning"
                :disabled="!readyToAutoSelect"
                @click="getStrategicSequence"
              >
                <h3>Auto-select</h3>
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
    colors() {
      return Object.values(this.colorKey);
    },
    readyToAutoSelect() {
      return (
        !this.gameInProgress &&
        this.computerSequence.length === 3 &&
        !this.computerSequence.includes(null)
      );
    },
    readyToStart() {
      return (
        !this.gameInProgress &&
        this.playerSequence.length === 3 &&
        this.computerSequence.length === 3 &&
        !this.playerSequence.includes(null) &&
        !this.computerSequence.includes(null)
      );
    },
  },
  data() {
    return {
      deckLimit: 52,
      loading: false,
      gameInProgress: false,
      colorKey: {
        black: "b",
        red: "r",
      },
      deck: [],
      currentSequence: [null, null, null],
      playerSequence: [null, null, null],
      computerSequence: [null, null, null],
    };
  },
  methods: {
    init() {
      this.deck = this.getDeck();
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
    getColorSequence(color, n = 3) {
      let sequence = [];
      for (let i = 0; i < n; i++) {
        sequence.push(color);
      }
      return sequence;
    },
    getStrategicSequence() {
      if (!this.readyToAutoSelect) return;
      let altSequence = this.computerSequence[1] === "b" ? "r" : "b";
      this.playerSequence = [
        altSequence,
        this.computerSequence[0],
        this.computerSequence[1],
      ];
      this.makeToast("Auto-select", "info");
    },
    getDeck() {
      // Get 26 reds and 26 blacks in random order
      let blacks = this.getColorSequence(this.colorKey.black, 26);
      let reds = this.getColorSequence(this.colorKey.red, 26);
      let deck = this.shuffleArray(blacks.concat(reds));

      return deck;
    },
    shuffleArray(arr) {
      var j, x, index;
      for (index = arr.length - 1; index > 0; index--) {
        j = Math.floor(Math.random() * (index + 1));
        x = arr[index];
        arr[index] = arr[j];
        arr[j] = x;
      }
      return arr;
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
    startGame() {
      if (!this.readyToStart) return;

      // Update game states
      this.deck = this.getDeck();
      this.gameInProgress = true;
      let roundInProgress = true;
      this.$store.dispatch("incrementTotalGames");

      while (this.deck.length > 0 && roundInProgress) {
        // Get card to the current sequence
        let color = this.deck.pop();
        if (this.currentSequence.length < 3) {
          this.currentSequence.push(color);
        } else {
          this.currentSequence.shift();
          this.currentSequence.push(color);
        }

        // Check result
        // If the same sequences are selected, give a win to computer first
        if (this.currentSequence.join("") === this.computerSequence.join("")) {
          this.makeToast("Computer wins", "danger");
          this.$store.dispatch("incrementComputerWins");
          roundInProgress = false;
        } else if (
          this.currentSequence.join("") === this.playerSequence.join("")
        ) {
          this.makeToast("Player wins", "success");
          this.$store.dispatch("incrementPlayerWins");
          roundInProgress = false;
        }
      }
    },
    endGame() {
      this.gameInProgress = false;
    },
    resetGame() {
      this.makeToast("Reset", "warning");
      this.endGame();
      this.loading = true;
      this.currentSequence = [null, null, null];
      this.playerSequence = [null, null, null];
      this.computerSequence = this.getRandomSequence();
      this.loading = false;
    },
    makeToast(msg = "", type = "success") {
      this.$bvToast.toast(msg, {
        title: "System",
        variant: type,
        autoHideDelay: 2000,
      });
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
  padding: 50px;
}

.sequence-container {
  margin-top: 1rem;
}

.sequence-selection-container {
  text-align: center;
}
</style>