export const state = () => ({
  title: "The Humble Nishiyama Randomness Game",
  totalGames: 0,
  playerWins: 0,
  computerWins: 0,
});

export const mutations = {
  incrementTotalGames(state) {
    state.totalGames++;
  },
  incrementPlayerWins(state) {
    state.playerWins++;
  },
  incrementComputerWins(state) {
    state.computerWins++;
  },
  resetStats(state) {
    state.totalGames = 0;
    state.playerWins = 0;
    state.computerWins = 0;
  },
};

export const actions = {
  incrementTotalGames({ commit }) {
    commit("incrementTotalGames");
  },
  incrementPlayerWins({ commit }) {
    commit("incrementPlayerWins");
  },
  incrementComputerWins({ commit }) {
    commit("incrementComputerWins");
  },
  resetStats({ commit }) {
    commit("resetStats");
  },
};
