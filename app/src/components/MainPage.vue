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
            <v-list-item two-line>
              <v-list-item-content>
                <v-list-item-title class="headline">San Francisco</v-list-item-title>
                <v-list-item-subtitle>Mon, 12:30 PM, Mostly sunny</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>

            <v-card-text>
              <v-row align="center">
                <v-col class="display-3" cols="6">
                  23&deg;C
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
                <v-icon>mdi-send</v-icon>
              </v-list-item-icon>
              <v-list-item-subtitle>23 km/h</v-list-item-subtitle>
            </v-list-item>

            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-cloud-download</v-icon>
              </v-list-item-icon>
              <v-list-item-subtitle>48%</v-list-item-subtitle>
            </v-list-item>

            <v-list class="transparent">
              <v-list-item
                v-for="item in forecast"
                :key="item.day"
              >
                <v-list-item-title>{{ item.day }}</v-list-item-title>

                <v-list-item-icon>
                  <v-icon>{{ item.icon }}</v-icon>
                </v-list-item-icon>

                <v-list-item-subtitle class="text-right">
                  {{ item.temp }}
                </v-list-item-subtitle>
              </v-list-item>
            </v-list>

            <v-divider></v-divider>

            <v-card-actions>
              <v-btn text>Full Report</v-btn>
            </v-card-actions>
          </v-card>

          <v-card>
            <v-card-title>News Sentiment</v-card-title>
            <v-card-text>
              <v-slider
                v-model="volume"
                append-icon="emoticon-outline"
                prepend-icon="emoticon-neutral-outline"
              ></v-slider>

            </v-card-text>
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
      labels: ['SU', 'MO', 'TU', 'WED', 'TH', 'FR', 'SA'],
      time: 0,
      forecast: [
        { day: 'Tuesday', icon: 'mdi-white-balance-sunny', temp: '24\xB0/12\xB0' },
        { day: 'Wednesday', icon: 'mdi-white-balance-sunny', temp: '22\xB0/14\xB0' },
        { day: 'Thursday', icon: 'mdi-cloud', temp: '25\xB0/15\xB0' },
      ],
      lorem: `Lorem ipsum dolor sit amet, mel at clita quando. Te sit oratio vituperatoribus, nam ad ipsum posidonium mediocritatem, explicari dissentiunt cu mea. Repudiare disputationi vim in, mollis iriure nec cu, alienum argumentum ius ad. Pri eu justo aeque torquatos.`,
      articles: null
  }),
  methods: {
    getArticles: function (threshold, whitelist, blacklist) {
      axios
        .post('http://127.0.0.1:5000/articles', {
          threshold: threshold,
          whitelist: whitelist,
          blacklist: blacklist
        })
        .then(response => (this.articles = response.data.articles))
    }
  },
  mounted () {
    this.getArticles(0, [], []);
  }
};
</script>
