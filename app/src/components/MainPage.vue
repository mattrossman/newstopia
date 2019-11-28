<template>
  <v-card>
   <v-container fluid>
     <h4>Top News</h4>
       <v-row>
        <v-col cols="8">
          <v-card>
            <v-card-title>
              <a href="https://www.npr.org/2019/11/27/783236569/bomb-cyclone-whips-through-the-west-as-winter-storms-snarl-thanksgiving-travel"
              target="_blank">
                'Bomb Cyclone' Whips Though The West As Winter Storm Snarl Thanksgiving Travel
              </a>
            </v-card-title>
            <v-card-subtitle>NPR * 2 hours ago</v-card-subtitle>
            <v-card-text>
              <ul>
                <li>
                  <a href="https://www.cnn.com/2019/11/26/weather/denver-airport-thanksgiving-travel-trnd/index.html">
                    Storm leaves over 1,100 stranded on Denver International Airport
                  </a>
                  <p>CNN * Yesterday</p>
                </li>
                <li>
                  <a href="https://www.wmtw.com/article/maine-rain-snow-to-impact-thanksgiving-week-travel-update2/29958760">
                    Impact Weather: Many Mainers to wake up to a white Thanksgiving
                  </a>
                  <p>WMTW Portland * 2 hours ago</p>
                </li>
                <li>
                  <a href="https://www.bloomberg.com/news/articles/2019-11-26/snow-snarls-thanksgiving-travel-with-flights-canceled-in-denver">
                    Weather Thanksgiving 2019: Snow Snarls Travel, Cancels Fights
                  </a>
                  <p>Bloomberg * Yesterday</p>
                </li>
              </ul>
            </v-card-text>
            <v-card-actions>
              <v-btn
                text
                color="deep-purple accent-4"
              >
                Learn More
              </v-btn>
            </v-card-actions>
          </v-card>

          <v-card>
            <v-card-title>
              <a href="https://techcrunch.com/2019/11/27/alexa-is-about-to-be-very-disappointed/"
              target="_blank">
                Alexa is about to be very disappointed
              </a>
            </v-card-title>
            <v-card-subtitle>Tech Crunch * 1 hour ago</v-card-subtitle>
            <v-card-text>
              <ul>
                <li>
                  <a href="https://gizmodo.com/amazon-quietly-reveals-plan-to-put-alexa-in-almost-ever-1840046869">
                    Amazon Quietly Reveals Plan to Put Alexa in Almost Everything
                  </a>
                  <p>Gizmodo * Yesterday </p>
                </li>
              </ul>
            </v-card-text>
            <v-card-actions>
              <v-btn
                text
                color="deep-purple accent-4"
              >
                Learn More
              </v-btn>
            </v-card-actions>
          </v-card>

          <v-card>
            <v-card-title>
              <a href="https://www.cnn.com/2019/11/27/business/manchester-city-silver-lake/index.html"
              target="_blank">
                Star Wars script wound up on eBay after John Boyega partied and forgot about it
              </a>
            </v-card-title>
            <v-card-subtitle>CNN * 4 hours ago</v-card-subtitle>
            <v-card-text>
              <ul>
                <li>
                  <a href="https://io9.gizmodo.com/who-had-bets-on-john-boyega-leaking-the-rise-of-skywalk-1840066358">
                    Star Wars Rise of Skywalker Script Leak: It Was John Boyega
                  </a>
                  <p>Gizmodo * 1 hour ago</p>
                </li>
              </ul>
            </v-card-text>
            <v-card-actions>
              <v-btn
                text
                color="deep-purple accent-4"
              >
                Learn More
              </v-btn>
            </v-card-actions>
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
<script>
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
      lorem: `Lorem ipsum dolor sit amet, mel at clita quando. Te sit oratio vituperatoribus, nam ad ipsum posidonium mediocritatem, explicari dissentiunt cu mea. Repudiare disputationi vim in, mollis iriure nec cu, alienum argumentum ius ad. Pri eu justo aeque torquatos.`
  }),
};
</script>
