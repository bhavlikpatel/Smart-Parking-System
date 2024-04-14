<template>
  <div class="login-main">
    <v-img
      :src="mapHeight < 786 ? bgRotationImage : bgImage"
      class="login-bg-image"
    ></v-img>

    <v-row
      style="width: 100% !important"
      class="px-6 mb-0 mb-sm-12 pb-sm-12 mb-md-0 px-md-16 py-md-16"
    >
      <v-col cols="1" class="display-sm-none"> </v-col>
      <v-col
        cols="7"
        class="d-none pt-12 d-md-flex flex-column justify-space-between"
      >
        <div>
          <!-- <v-img :src="logo" class="login-logo-image mt-16" contain></v-img> -->
        </div>
        <!-- <div class="mx-auto">
          <v-row style="width: 300px">
            <v-col cols="3">
              <v-icon color="white" large>mdi-facebook</v-icon>
            </v-col>
            <v-col cols="3">
              <v-icon color="white" large>mdi-twitter</v-icon>
            </v-col>
            <v-col cols="3">
              <v-icon color="white" large>mdi-instagram</v-icon>
            </v-col>
            <v-col cols="3">
              <v-icon color="white" large>mdi-youtube</v-icon>
            </v-col>
          </v-row>
        </div> -->
      </v-col>
      <v-col cols="12" md="4">
        <v-card class="login-card">
          <v-card-title class="d-flex flex-column">
            <div class="d-flex justify-center">
              <h1 class="login-title primary--text">Welcome</h1>
            </div>
            <!-- <hr class="login-hr" /> -->
            <div class="d-flex justify-center w-100 mb-10">
              <v-img :src="RedLogo" height="60" contain></v-img>
            </div>
          </v-card-title>
          <v-card-text>
            <v-form>
              <v-card class="custom-shadow-login" elevation="0">
                <v-card-text>
                  <v-text-field
                    v-model.trim="username"
                    prepend-inner-icon="mdi-account-circle"
                    autocomplete="new-password"
                    name="username"
                    label="Username"
                    :rules="[(v) => !!v || 'Username is required']"
                    :error-messages="formError.username"
                    @input="delete formError.username"
                    outlined
                    type="text"
                  ></v-text-field>

                  <v-text-field
                    v-model="password"
                    prepend-inner-icon="mdi-lock-outline"
                    autocomplete="new-password"
                    :append-icon="viewPassword ? 'mdi-eye' : 'mdi-eye-off'"
                    name="password"
                    label="Password"
                    :rules="[(v) => !!v || 'Password is required']"
                    :type="viewPassword ? 'text' : 'password'"
                    @click:append="viewPassword = !viewPassword"
                    :error-messages="formError.password"
                    @input="delete formError.password"
                    outlined
                    @keydown.enter="onSubmit()"
                  ></v-text-field>
                </v-card-text>
                <v-card-actions class="justify-center">
                  <v-btn
                    elevation="0"
                    class="py-6 login-btn"
                    style="width: 100%"
                    color="primary"
                    @click.prevent="onSubmit()"
                  >
                    Login
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-form>
            <div class="d-flex justify-center">
              New User,
              <router-link class="ml-2" to="/app/register">  Please Sign Up? </router-link>
            </div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
/* eslint-disable vue/no-unused-components */
import bgColor from "@/static/bg_image.png";
import bgRotationImage from "@/static/bg_image.png";
import whiteLogo from "@/static/logo.png";
import RedLogo from "@/static/logo.png";
import { bus } from "@/main";

export default {
  name: "mainLogin",
  layout: "authentication",
  data() {
    return {
      bgImage: bgColor,
      bgRotationImage: bgRotationImage,
      logo: whiteLogo,
      RedLogo: RedLogo,
      viewPassword: false,
      username: "",
      password: "",
      formError: {
        username: null,
        password: null,
      },
    };
  },
  methods: {
    checkIfLoggedIn() {
      let user = localStorage.getItem("user");
      if (!user) {
        if (this.$route.path !== "/app/login") {
          this.$router.push({ path: "/app/login" });
        }
        if (this.$route.path == "/app/login") {
          this.$router.push({ path: "/app/register" });
        }
      } else {
        const user_detail = JSON.parse(localStorage.getItem("user_detail"));

        if (this.$route.fullPath == "/app" && user_detail['user_type'] == "admin") {
          this.$router.push({ path: "/app/admin" });
        }
        if (this.$route.fullPath == "/app" && user_detail['user_type'] == "normal_user") {
          this.$router.push({ path: "/app/client" });
        }
      }
    },
    mapHeight() {
      return window.innerWidth;
    },
    onSubmit() {
      this.$api.auth
        .login({
          username: this.username,
          password: this.password,
        })
        .then((success) => {
          const user_detail = {
            user_id: success.data.user_id,
            username: success.data.username,
            user_type: success.data.user_type,
          };
          localStorage.setItem("user", success.data.token);
          localStorage.setItem("user_detail", JSON.stringify(user_detail));
          if (success.data.user_type == "admin")
          {
            this.$router.push({ path: "/app/admin/dashboard" });
          }
          else{
            this.$router.push({ path: "/app/client/dashboard" });
          }
          // this.$api.profile
          //   .getProfileObject()
          //   .then((result) => {
          //     localStorage.setItem("userdetails", JSON.stringify(result.data));
          //     localStorage.setItem(
          //       "selectedBranch",
          //       JSON.stringify(result.data.user_branches[0])
          //     );
          //     localStorage.setItem(
          //       "permissions",
          //       JSON.stringify(result.data.permissions)
          //     );

          //     let user_permissions = result.data.permissions;
          //     let support_permissions = user_permissions["ticket"];
          //     delete user_permissions["ticket"];
          //     delete user_permissions["orderadhoc"];

          //     let has_support_permissions = Object.values(
          //       support_permissions
          //     ).some((perm) => perm == true);

          //     let has_other_permissions = [];

          //     Object.keys(user_permissions).forEach((key) => {
          //       has_other_permissions.push(
          //         Object.values(user_permissions[key])
          //       );
          //     });

          //     let CountModuleAllow = 0;
          //     if (
          //       CountModuleAllow <= 1 &&
          //       has_support_permissions &&
          //       !has_other_permissions
          //         .flat()
          //         .every((permission) => permission == true)
          //     ) {
          //       this.$router.push({ path: "/app/admin/support" });
          //     } else {
          //       this.$router.push({ path: "/app/admin/dashboard" });
          //     }
          //   })
          //   .catch((err) => {
          //     console.error(err);
          //     bus.$emit("showToastMessage", {
          //       message: "Something went wrong",
          //       color: "error",
          //     });
          //   });
        })
        .catch((err) => {
          if ("non_field_errors" in err.data) {
            bus.$emit("showToastMessage", {
              message: err.data["non_field_errors"][0],
              color: "error",
            });
          }
          this.formError = err.data;
        });
    },
  },
  mounted() {
    this.mapHeight();
  },
  beforeDestroy() {
    this.checkIfLoggedIn();
  },
};
</script>

<style lang="scss">
@import "@/assets/scss/variables.scss";
.login-main {
  overflow: hidden;
}
@media screen and (max-width: 768px) {
  .login-main {
    display: flex;
    align-items: flex-end;
    height: 100vh;
  }
}
.login-card {
  padding: 0px 48px;
  min-height: 80vh;
}

@media screen and (max-width: 1400px) {
  .login-card {
    padding: 0px 28px;
  }
}
@media screen and (max-width: 768px) {
  .login-card {
    min-height: auto;
    padding: 0px 8px 40px 8px;
    margin-bottom: 10%;
  }
}

input {
  background-color: white !important;
}

.custom-shadow-login {
  box-shadow: 0px 0px 47px -20px rgba(5, 5, 5, 0.5),
    0px -2px 12px -10px rgba(5, 5, 5, 0.3) !important;
}
.login-bg-image {
  position: fixed;
  height: 100vh !important;
  width: 100vw !important;
}
.login-title {
  text-align: center;
  text-transform: uppercase;
  font-weight: 100 !important;
  padding: 40px 0px;
  font-size: 38px;
  margin: 32px 0;
}

@media screen and (max-width: 1400px) {
  .login-title {
    font-size: 26px !important ;
    margin: 0px 0;
  }
}
@media screen and (max-width: 768px) {
  .login-title {
    font-size: 30px !important ;
    margin: 0px 0;
  }
}

.login-hr {
  width: 30%;
  margin-top: 24px;
  margin-bottom: 36px;
  background-color: map-get($colors-custom, "solid", "primary") !important;
}

@media screen and (max-width: 1400px) {
  .login-hr {
    margin-top: 14px;
    margin-bottom: 6px;
  }
}
.login-logo-image {
  height: 70px;
}
.login-btn {
  text-transform: uppercase !important;
}
</style>
