<template>
  <div class="login-main">
    <v-img :src="bgImage" class="login-bg-image"></v-img>

    <v-row
      style="width: 100% !important"
      class="px-6 mb-0 mb-sm-12 pb-sm-12 mb-md-0 px-md-16 py-md-16"
    >
      <v-col cols="6" md="4"></v-col>
      <v-col cols="4" md="4">
        <v-card class="login-card" style="height:580px;">
          <div class="d-flex justify-center py-5">
            <h1 class="primary--text">Register</h1>
          </div>
          <v-form>
            <v-text-field
              v-model.trim="first_name"
              prepend-inner-icon="mdi-alpha-f-circle"
              name="first_name"
              label="First Name"
              :error-messages="formError.first_name"
              @input="delete formError.first_name"
              outlined
              type="text"
            ></v-text-field>
            <v-text-field
              v-model.trim="last_name"
              prepend-inner-icon="mdi-alpha-l-circle"
              name="last_name"
              label="Last Name"
              :error-messages="formError.last_name"
              @input="delete formError.last_name"
              outlined
              type="text"
            ></v-text-field>
            <v-text-field
              v-model.trim="username"
              prepend-inner-icon="mdi-account"
              name="username"
              label="Username*"
              :rules="[(v) => !!v || 'Username is required']"
              :error-messages="formError.username"
              @input="delete formError.username"
              outlined
              type="text"
            ></v-text-field>
            <v-text-field
              v-model.trim="email"
              prepend-inner-icon="mdi-email"
              name="email"
              label="Email"
              :error-messages="formError.email"
              @input="delete formError.email"
              outlined
              type="text"
            ></v-text-field>
            <v-text-field
              v-model="password"
              prepend-inner-icon="mdi-lock-outline"
              :append-icon="viewPassword ? 'mdi-eye' : 'mdi-eye-off'"
              name="password"
              label="Password*"
              :rules="[(v) => !!v || 'Password is required']"
              :type="viewPassword ? 'text' : 'password'"
              @click:append="viewPassword = !viewPassword"
              :error-messages="formError.password"
              @input="delete formError.password"
              outlined
            ></v-text-field>
            <v-text-field
              v-model="password2"
              prepend-inner-icon="mdi-lock-outline"
              :append-icon="viewPassword2 ? 'mdi-eye' : 'mdi-eye-off'"
              name="password2"
              label="Re- enter Password*"
              :rules="[(v) => !!v || 'Conform Password is required']"
              :type="viewPassword2 ? 'text' : 'password'"
              @click:append="viewPassword2 = !viewPassword2"
              :error-messages="formError.password2"
              @input="delete formError.password2"
              outlined
            ></v-text-field>
            <v-card-actions class="justify-center">
              <v-btn
                elevation="0"
                class="py-6 login-btn"
                style="width: 100%"
                color="primary"
                @click.prevent="onSubmit()"
              >
                Register
              </v-btn>
            </v-card-actions>
          </v-form>
          <div class="d-flex justify-center">
            Please go to,
            <router-link class="ml-2" to="/app/login">
              <a href="">login page</a>
            </router-link>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { bus } from "@/main";
import bgColor from "@/static/bg_image.png";
import bgRotationImage from "@/static/bg_image.png";

export default {
  name: "RegisterIndex",

  data() {
    return {
      bgImage: bgColor,
      bgRotationImage: bgRotationImage,
      viewPassword: false,
      viewPassword2: false,
      username: "",
      password: "",
      first_name: "",
      last_name: "",
      email: "",
      password2: "",
      formError: {
        first_name: null,
        last_name: null,
        email: null,
        username: null,
        password: null,
        password2: null,
      },
    };
  },
  methods: {
    mapHeight() {
      return window.innerWidth;
    },
    onSubmit() {
      this.$api.auth
        .register({
          first_name: this.first_name,
          last_name: this.last_name,
          username: this.username,
          email: this.email,
          password: this.password,
          password2: this.password2,
        })
        .then((success) => {
          localStorage.setItem("user", success.data.token);
          bus.$emit("showToastMessage", {
              message: "User Created successfully",
              color: "success",
            });
          this.$router.push({ path: "/app/login" });
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
  }
};
</script>

