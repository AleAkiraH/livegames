<template>
  <div>
    <label>Minimo tempo corrido:</label>
    <Input id="txtinput1" type="text" :value="min_t_corrido"></Input>
    <label>Maximo tempo corrido:</label>
    <Input id="txtinput2" type="text" :value="max_t_corrido"></Input>
    <label>total de gols:</label>
    <Input id="txtinput4" type="text" :value="total_gols"></Input>
    <base-button block type="success" @click="post_live_game()"
      >LiveGame!</base-button
    >
    <div>
      <table class="table">
        <thead>
          <tr>
            <th class="text-center">Campeonato</th>
            <th class="text-center">Confronto</th>
            <th class="text-center">placar</th>
            <th class="text-center">Tempo de jogo</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in items" :key="item.competicao">
            <!-- {{ item.competicao }} -->
            <td class="text-center" v-text="item.competicao"></td>
            <td class="text-center" v-text="item.confronto"></td>
            <td class="text-center" v-text="item.placar"></td>
            <td class="text-center" v-text="item.tempo_de_jogo"></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [],
      min_t_corrido: 0,
      max_t_corrido: 99,
      total_gols: ''
    };
  },
  name: "home",
  components: {},
  methods: {
    pollData() {
      this.polling = setInterval(() => {
        this.post_live_game();
        try {
          if (this.items.length > 0) {
            // alert("Atencao oportunidade");
          }
        } finally {
        }
      }, 30000);
    },
    post_live_game() {
      this.min_t_corrido = document.getElementById('txtinput1').value
      this.max_t_corrido = document.getElementById('txtinput2').value
      this.total_gols = document.getElementById('txtinput4').value
      var axios = require("axios");

      var params = {
        url: "https://apilivegames.herokuapp.com/live_games/",
        method: "post",
        data: {
          min_inicio: this.min_t_corrido,
          min_fim: this.max_t_corrido,
	  totalgols: this.total_gols
        },
      };
      axios(params)
        .then((response) => {
          this.items = response.data.lista_de_jogos;
          // console.log("----");
        })
        .catch(function (e) {});
    },
    forconsolelog() {},
  },
  created() {
    this.pollData();
  },
};
</script>
