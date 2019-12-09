<template>
  <v-card>
   <v-container fluid>
     <h4>Top News</h4>
       <v-row>
        <v-col cols="8">
          <v-card>
            <v-card-text>
              <v-list three-line>
                <template v-for="article in articles">
                  <!-- <v-subheader
                    v-if="item.header"
                    :key="item.header"
                    v-text="item.header"
                  ></v-subheader>

                  <v-divider
                    v-else-if="item.divider"
                    :key="index"
                    :inset="item.inset"
                  ></v-divider> -->

                  <v-list-item
                    :key="article.title"
                  >
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
                  </v-list-item>
                </template>
              </v-list>
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

            <v-divider></v-divider>

            <v-card-actions>
              <v-btn text>Full Report</v-btn>
            </v-card-actions>
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
      items: [
        { header: 'Today' },
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
          title: 'Brunch this weekend?',
          subtitle: "<span class='text--primary'>Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?",
        },
        { divider: true, inset: true },
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
          title: 'Summer BBQ <span class="grey--text text--lighten-1">4</span>',
          subtitle: "<span class='text--primary'>to Alex, Scott, Jennifer</span> &mdash; Wish I could come, but I'm out of town this weekend.",
        },
        { divider: true, inset: true },
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
          title: 'Oui oui',
          subtitle: "<span class='text--primary'>Sandra Adams</span> &mdash; Do you have Paris recommendations? Have you ever been?",
        },
        { divider: true, inset: true },
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg',
          title: 'Birthday gift',
          subtitle: "<span class='text--primary'>Trevor Hansen</span> &mdash; Have any ideas about what we should get Heidi for her birthday?",
        },
        { divider: true, inset: true },
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/5.jpg',
          title: 'Recipe to try',
          subtitle: "<span class='text--primary'>Britta Holt</span> &mdash; We should eat this: Grate, Squash, Corn, and tomatillo Tacos.",
        },
      ],
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
    updateHandler: function(event) {
      this.getArticles(this.sentiment, this.whitelist, this.blacklist);
      window.console.log(`Button clicked: ${event.target.name}`)
      window.console.log(`Sentiment value: ${this.sentiment}`)
      window.console.log(`Whitelist: ${this.whitelist}`)
    }
  },
  mounted () {
    this.getArticles(null, null, null);
  }
};
</script>
