<template>
  <v-card>
   <v-container fluid>
     <h4>Top News</h4>
       <v-row>
        <v-col cols="8">
          <v-card>
            <v-card-text>
              <ul>
                <li v-for="article in articles" v-bind:key="article">
                  <div class="details">
                    <a :href="article.url">
                      {{ article.title }}
                    </a>
                    <p>{{ article.description }}
                    <p>{{ article.source.name }}</p>
                  </div>
                  <!-- <img :src="article.urlToImage" class="thumb"> -->
                </li>
              </ul>
            </v-card-text>
          </v-card>
        </v-col>

        <v-col cols="4">

          <v-card>
            <v-card-title>News Sentiment</v-card-title>
            <v-card-text>
              <v-slider
                v-model="sentiment"
                append-icon="mdi-emoticon-outline"
                prepend-icon="mdi-emoticon-neutral-outline"
                min=0 max=1 step=0.1
              ></v-slider>
              <v-combobox multiple
                        v-model="whitelist" 
                        label="Whitelist" 
                        append-icon
                        chips
                        deletable-chips
                        class="tag-input"
                        :search-input.sync="search" 
                        @keyup.tab="updateTags"
                        @paste="updateTags">
              </v-combobox>
              <v-combobox multiple
                        v-model="blacklist" 
                        label="Blacklist" 
                        append-icon
                        chips
                        deletable-chips
                        class="tag-input"
                        :search-input.sync="search" 
                        @keyup.tab="updateTags"
                        @paste="updateTags">
              </v-combobox>
              <v-btn small v-on:click="updateHandler">Update</v-btn>
            </v-card-text>
          </v-card>

          <v-card>
            <v-list-item two-line>
              <v-list-item-content>
                <v-list-item-title class="headline">Amherst, MA</v-list-item-title>
                <v-list-item-subtitle>{{output.currently.summary}}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>

            <v-card-text>
              <v-row align="center">
                <v-col class="display-3" cols="6">
                  {{Math.round(output.currently.temperature)}}&deg;F
                </v-col>
                <v-col cols="6">
                  <v-img
                    src="https://cdn.vuetifyjs.com/images/cards/sun.png"
                    alt="Sunny image"
                    width="92"
                  ></v-img>
                </v-col>
              </v-row>
            </v-card-text>

            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-weather-windy</v-icon>
              </v-list-item-icon>
              <v-list-item-subtitle>{{Math.round(output.currently.windSpeed)}} mph</v-list-item-subtitle>
               <v-list-item-icon>
                <v-icon>mdi-weather-pouring</v-icon>
              </v-list-item-icon>
              <v-list-item-subtitle>{{output.currently.precipProbability * 100}}%</v-list-item-subtitle>
            </v-list-item>

            <!-- <v-list-item>
             
            </v-list-item> -->

            <v-divider></v-divider>
          </v-card>

        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>
<style scoped>
/* ul {
  list-style-type: none;
}
img.thumb {
  width: 100px;
}
div.details {
  float: right;
  width: auto;
} */
</style>
<script>
import axios from 'axios'
export default {
  name: 'MainPage',

  data: () => ({
      
      articles: null,
      sentiment: null,
      whitelist: null,
      blacklist: null,
      output: null
  }),
  methods: {
    getArticles: function (threshold, whitelist, blacklist) {
      axios
        .post('https://orange-rattlesnake-51.localtunnel.me/articles', {
          threshold: threshold,
          whitelist: whitelist,
          blacklist: blacklist
        })
        .then(response => (this.articles = response.data.articles))
    },
    updateHandler: function(event) {
      this.getArticles(this.sentiment, this.whitelist, this.blacklist);
      window.console.log(`Button clicked: ${event.target.name}`)
      window.console.log(`Sentiment value: ${this.sentiment}`)
      window.console.log(`Whitelist: ${this.whitelist}`)
    }
  },
  mounted () {
    this.getArticles(null, null, null);
    axios
      .get('https://api.darksky.net/forecast/5871dcff4e6467cfe993c8b6c5bcf9f6/42.3868,-72.5301') 
      .then(response => (this.output = response.data))
  }
};
</script>
