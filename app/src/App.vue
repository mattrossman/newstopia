
<template>
  <v-app>
    <v-app-bar
      app
      color="pink"
      dark
       collapse-on-scroll
      scroll-target="#scrolling-techniques-2"
    >
      <div class="d-flex align-center">

        <h1 style="font-family: Copperplate;">Newstopia
           <small style="font-family: Helvetica;" class="text-muted font-weight-light">tailored just for you!</small>
        </h1>
      </div>
       <v-spacer></v-spacer>
  
        <!-- <v-btn icon>
          <v-icon>mdi-magnify</v-icon>
        </v-btn> -->
  
        <v-btn icon>
          <v-icon> mdi-account-heart</v-icon>
          <!-- mdi-heart -->
        </v-btn>

    </v-app-bar>

    <v-content>
      <MainPage/>
    </v-content>
  </v-app>
</template>

<script>
import MainPage from "./components/MainPage";

export default {
  name: 'Newstopia',
  title: 'Newstopia',

  components: {
    MainPage,
  },

  data: () => ({
  }),
};
</script>
