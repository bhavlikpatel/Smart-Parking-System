<template>
  <div>
    <v-row>
      <v-app-bar :clipped-left="true" :clipped-right="true" fixed app>
        <v-toolbar-title class="d-flex">
          <img :src="logo" height="40px" class="py-1" />
        </v-toolbar-title>
        <v-spacer />
        <div class="mx-2">
          <v-icon class="text-primary">mdi-account</v-icon>
          <span class="pl-2 text-grey text-capitalize">{{ userDetail.username }}</span>
        </div>
        <div class="mx-2" @click="logout()">
          <a>
            <v-icon class="text-primary">mdi-logout</v-icon>
            <span class="pl-2 text-capitalize">Logout</span></a
          >
        </div>
      </v-app-bar>
    </v-row>
  </div>
</template>

<script>
import Logo from "@/static/logo.png";
import { userLogout } from "@/utils/functions.js";
export default {
  name: "CommonHeader",
  data() {
    return {
      logo: Logo,
      userLogout,
      userDetail: {},
    };
  },
  methods: {
    logout() {
      this.userLogout();
    },
    getUserDetails() {
      const user_detail = JSON.parse(localStorage.getItem("user_detail"));
      this.$api.profile
        .getProfileDetail(user_detail["user_id"])
        .then((result) => {
          this.userDetail = result.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  mounted() {
    this.getUserDetails();
  },
};
</script>

<style scoped>
</style>