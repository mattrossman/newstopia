<template>
  <v-app>
    <v-app-bar
      app
      color="light purple"
      dark
    >
      <div class="d-flex align-center">

        <h1>Newstopia</h1>
      </div>

      <v-spacer></v-spacer>

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
