<template>
  <div class="how-to-play">
    <b-row class="text-center">
      <b-col>
        Two players play the game using an ordinary deck of cards. The cards
        will be dealt out in a row, one after another. Before the dealing
        begins, each player claims an ordered sequence of colors that might turn
        up, for example “red black red” (RBR) or “black red red” (BRR). As the
        cards are dealt, if three successive cards turn up in one of these
        sequences, the player who claimed it gets to collect those three cards
        as a trick, and the dealing continues. When all 52 cards have been
        dealt, the player who has collected the most tricks wins. (In a typical
        game, 7 to 9 tricks are won.)
      </b-col>
    </b-row>
    <b-row>
      <b-col>
        <b-button class="back-home-btn" variant="outline-primary" href="/">
          < Back to home
        </b-button>
      </b-col>
    </b-row>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.how-to-play {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 50px;
}

.back-home-btn {
  margin-top: 50px;
}
</style>