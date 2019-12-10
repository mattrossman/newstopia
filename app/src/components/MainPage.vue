<template>
  <v-card>
   <v-container fluid>
     <h4>Top News</h4>
       <v-row>
        <v-col cols="12" sm="8">
          <v-card>
            <v-card-text>
              <v-list three-line>
                <template v-for="article in articles">

                  <v-list-item
                    :key="article.title"
                    :href="article.url"
                    target="_blank"
                  >
                    <!-- :style="{backgroundColor: getColorForPercentage(article.sentiment)}" -->
                    <v-list-item-avatar>
                      <v-img :src="article.urlToImage"></v-img>
                    </v-list-item-avatar>

                    <v-list-item-content>
                      <v-list-item-title v-html="article.title"></v-list-item-title>
                      <v-list-item-subtitle>
                        <span class='text--primary'>{{ article.source.name }}</span> &mdash;
                        {{ article.description }}
                      </v-list-item-subtitle>
                    </v-list-item-content>
                    <v-list-item-icon>
                      <p :style="{
                        backgroundColor: getColorForPercentage(article.sentiment),
                        padding: '10px',
                        'border-radius': '50%',
                        width: '50px',
                        height: '50px',
                        'line-height': '30px',
                        'text-align': 'center',
                        }">
                        {{ Math.round((article.sentiment * 100)) }}%
                      </p>
                    </v-list-item-icon>
                  </v-list-item>
                </template>
              </v-list>
            </v-card-text>
          </v-card>
        </v-col>

        <v-col cols="12" sm="4">

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
      percentColors: [
        { pct: 0.0, color: { r: 0xff, g: 0xda, b: 0xd1 } },
        { pct: 0.5, color: { r: 0xff, g: 0xfe, b: 0xd1 } },
        { pct: 1.0, color: { r: 0x94, g: 0xd4, b: 0xa5 } }
      ],
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
    },
    getColorForPercentage: function(pct) {
    for (var i = 1; i < this.percentColors.length - 1; i++) {
        if (pct < this.percentColors[i].pct) {
            break;
        }
    }
    var lower = this.percentColors[i - 1];
    var upper = this.percentColors[i];
    var range = upper.pct - lower.pct;
    var rangePct = (pct - lower.pct) / range;
    var pctLower = 1 - rangePct;
    var pctUpper = rangePct;
    var color = {
        r: Math.floor(lower.color.r * pctLower + upper.color.r * pctUpper),
        g: Math.floor(lower.color.g * pctLower + upper.color.g * pctUpper),
        b: Math.floor(lower.color.b * pctLower + upper.color.b * pctUpper)
    };
    return 'rgb(' + [color.r, color.g, color.b].join(',') + ')';
    // or output as hex if preferred
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
