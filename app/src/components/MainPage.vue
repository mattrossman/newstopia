
<template>
  <v-card>
   <v-container fluid>
     <div class="circular" v-bind:style="{ backgroundImage: 'url(' + background + ')' }">app</div>
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
                <v-list-item-title class="headline">Amherst, MA</v-list-item-title>
                <v-list-item-subtitle>Tue, 2:15 PM, {{ output.currently.summary}}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>

            <v-card-text>
              <v-row align="center">
                <v-col class="display-3" cols="6">
    
                  {{ Math.round(output.currently.temperature) }}&deg;F
                </v-col>
                <v-col cols="6">
                  <v-img
                    src="/Users/ayushkhd/Documents/326-group-12/app/weather-pouring (3).png"
                    alt="Rainy image"
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
// import  mdiWeatherWindy from '@mdi/js';
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
      articles: null,
      output: null
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
    },
    // getWeather: function(){ 
    //   axios.get('https://api.darksky.net/forecast/5871dcff4e6467cfe993c8b6c5bcf9f6/42.3868,-72.5301')
    //     .then((response) => {
    //       this.output = response;
    //       // console.log(response.statusText);
    //       // console.log(response.config);
    //     }) }
  },
  mounted () {
    this.getArticles(0, [], []);
    axios
      .get('https://api.darksky.net/forecast/5871dcff4e6467cfe993c8b6c5bcf9f6/42.3868,-72.5301') 
      .then(response => (this.output = response.data))
  }
};
</script>
