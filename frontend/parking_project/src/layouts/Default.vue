<template>
  <div>
    <router-view />
  </div>
</template>

<script>
export default {
  name: "mainDefault",
  methods: {
    checkIfLoggedIn() {
      let user = localStorage.getItem("user");
      if (!user) {
        if (this.$route.path !== "/app/login") {
          this.$router.push({ path: "/app/login" });
        }
      } else {
        const user_detail = JSON.parse(localStorage.getItem("user_detail"));
        if (
          ["/app", "/app/admin"].indexOf(this.$route.path) > -1 &&
          user_detail["user_type"] == "admin"
        ) {
          this.$router.push({ path: "/app/admin/dashboard" });
        }
        if (
          ["/app", "/app/client"].indexOf(this.$route.path) > -1 &&
          user_detail["user_type"] == "normal_user"
        ) {
          this.$router.push({ path: "/app/client/dashboard" });
        }
      }
    },
  },
  beforeMount() {
    this.checkIfLoggedIn();
  },
};
</script>

<style></style>
