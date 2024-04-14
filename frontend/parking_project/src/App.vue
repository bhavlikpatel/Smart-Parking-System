<template>
  <v-app>
    <router-view />
    <SnackBar
      v-model="showToastMessage"
      :color="snackBarColor"
      :message="snackbarMessage"
    />
    <DefaultLoader :isLoader="showLoader" />
    <!-- <div class="text-center">
      <v-overlay :value="!isOnline"
        ><h5 class="light_grey--text text-h3 font-weight-medium">
          {{ statusMessage }}
        </h5></v-overlay
      >
    </div> -->
  </v-app>
</template>

<script>
import SnackBar from "@/components/common/SnackBar.vue";
import { bus } from "@/main.js";
import DefaultLoader from "@/components/common/DefaultLoader.vue";

export default {
  name: "App",

  components: {
    SnackBar,
    DefaultLoader,
  },
  data: () => ({
    showToastMessage: false,
    snackBarColor: "primary",
    snackbarMessage: "",
    showLoader: false,
    isOnline: navigator.onLine ? true : false,
  }),
  computed: {
    statusMessage() {
      if (!this.isOnline) {
        return "You're Offline";
      } else {
        return console.log("");
      }
    },
  },
  mounted() {
    bus.$on("showToastMessage", ({ color, message }) => {
      this.snackBarColor = color;
      this.snackbarMessage = message;
      this.showToastMessage = true;
    });
    bus.$on("showLoader", (value) => {
      this.showLoader = value;
    });
  },
  beforeDestroy() {
    bus.$off("showToastMessage");
    bus.$off("showLoader");
  },
};
</script>
<style lang="scss">
@import "assets/scss/global";
</style>
