<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">

        <h1>Posty</h1>
      </div>

      <v-spacer></v-spacer>

      <v-avatar color="red">
        <span class="white--text headline">CJ</span>
      </v-avatar>

    </v-app-bar>

    <v-content>
      <MainPage/>
    </v-content>
  </v-app>
</template>

<script>
import MainPage from "./components/MainPage";

export default {
  name: 'App',

  components: {
    MainPage,
  },

  data: () => ({
    //
  }),
};
</script>
