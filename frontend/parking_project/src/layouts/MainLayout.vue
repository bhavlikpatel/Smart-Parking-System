<template>
  <v-app>
    <NavigationDrawer />
    <Header />
    <v-main style="position: relative">
      <v-container
        fluid
        class="pa-0"
        style="height: 100% !important; position: absolute"
      >
        <router-view />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import Header from "@/components/common/Header.vue";
import NavigationDrawer from "@/components/common/NavigationDrawer.vue";

export default {
  name: "mainLayout",
  components: {
    Header,
    NavigationDrawer,
  },
  data() {
    return {
      isLoader: false,
    };
  },
  methods: {
    showLoader(value) {
      this.isLoader = value;
    },
    checkIfLoggedIn() {
      let user = localStorage.getItem("user");
      if (!user) {
        if (this.$route.path !== "/app/login") {
          this.$router.push({ path: "/app/login" });
        }
      } else {
        const user_detail = JSON.parse(localStorage.getItem("user_detail"));

        if (
          this.$route.fullPath == "/app" &&
          user_detail["user_type"] == "admin"
        ) {
          this.$router.push({ path: "/app/admin" });
        }
        if (
          this.$route.fullPath == "/app" &&
          user_detail["user_type"] == "normal_user"
        ) {
          this.$router.push({ path: "/app/client" });
        }
      }
    },
  },
  beforeDestroy() {
    this.checkIfLoggedIn();
  },
};
</script>
