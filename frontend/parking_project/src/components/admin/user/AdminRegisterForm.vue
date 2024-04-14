<template>
  <div ref="adminForm">
    <BaseFormLayout
      :title="`${formType} User`.toLowerCase()"
      :backRoute="backRoute"
      :nonFieldError="nonFieldError"
    >
      <template #formContent>
        <v-form
          v-model="isValid"
          ref="adminForm1"
          name="adminForm"
          id="adminForm"
          autocomplete="off"
        >
          <v-row class="pa-8">
            <v-col cols="12" lg="12">
              <v-row>
                <v-col cols="3" class="pa-1">
                  <v-text-field
              v-model.trim="userFormDetails.first_name"
              prepend-inner-icon="mdi-alpha-f-circle"
              name="first_name"
              label="First Name*"
              :rules="[(v) => !!v || 'First Name is required']"
              :error-messages="formErrors.first_name"
              @input="delete formErrors.first_name"
              outlined
              type="text"
            ></v-text-field>
              </v-col>
                <v-col cols="3" class="pa-1">
            <v-text-field
              v-model.trim="userFormDetails.last_name"
              prepend-inner-icon="mdi-alpha-l-circle"
              name="last_name"
              label="Last Name*"
              :rules="[(v) => !!v || 'Last Name is required']"
              :error-messages="formErrors.last_name"
              @input="delete formErrors.last_name"
              outlined
              type="text"
            ></v-text-field>
              </v-col>
                <v-col cols="3" class="pa-1">
            <v-text-field
              v-model.trim="userFormDetails.username"
              prepend-inner-icon="mdi-account"
              name="username"
              label="Username*"
              :rules="[(v) => !!v || 'Username is required']"
              :error-messages="formErrors.username"
              @input="delete formErrors.username"
              outlined
              type="text"
            ></v-text-field>
              </v-col>
                <v-col cols="3" class="pa-1">
            <v-text-field
              v-model.trim="userFormDetails.email"
              prepend-inner-icon="mdi-email"
              name="email"
              label="Email*"
              :rules="[(v) => !!v || 'Username is required']"
              :error-messages="formErrors.email"
              @input="delete formErrors.email"
              outlined
              type="text"
            ></v-text-field>
              </v-col>
                <v-col cols="3" class="pa-1">
            <v-text-field
              v-model="userFormDetails.password"
              prepend-inner-icon="mdi-lock-outline"
              :append-icon="viewPassword ? 'mdi-eye' : 'mdi-eye-off'"
              name="password"
              label="Password*"
              :rules="[(v) => !!v || 'Password is required']"
              :type="viewPassword ? 'text' : 'password'"
              @click:append="viewPassword = !viewPassword"
              :error-messages="formErrors.password"
              @input="delete formErrors.password"
              outlined
            ></v-text-field>
              </v-col>
                <v-col cols="3" class="pa-1">
            <v-text-field
              v-model="userFormDetails.password2"
              prepend-inner-icon="mdi-lock-outline"
              :append-icon="viewPassword2 ? 'mdi-eye' : 'mdi-eye-off'"
              name="password2"
              label="Re- enter Password*"
              :rules="[(v) => !!v || 'Conform Password is required']"
              :type="viewPassword2 ? 'text' : 'password'"
              @click:append="viewPassword2 = !viewPassword2"
              :error-messages="formErrors.password2"
              @input="delete formErrors.password2"
              outlined
            ></v-text-field>
            
                </v-col>
              </v-row>
            </v-col>
          </v-row> </v-form
      ></template>
      <template #formActions>
        <v-btn
          type="submit"
          :disabled="!isValid"
          width="9%"
          class="primary mr-3"
          @click.prevent="submitUserForm()"
        >
          <span>Submit</span>
        </v-btn>
      </template>
    </BaseFormLayout>
  </div>
</template>

<script>
import BaseFormLayout from "@/components/common/Layouts/BaseFormLayout.vue";
import { returnToday } from "@/assets/utils.js";
import { bus } from "@/main";

export default {
  layout: "MainLayout",
  components: {
    BaseFormLayout,
  },
  props: {
    formType: {
      required: true,
      default: "Add",
    },
    slot_id: {
      required: false,
    },
  },
  data() {
    return {
      returnToday,
      // Common Form Detail Defined
      formErrors: {},
      nonFieldError: [],
      viewPassword: false,
      viewPassword2: false,
      isValid: false,
      backRoute: { path: "/app/admin/fixed_slots" },
      userFormDetails: {},

      // Select List Detail Defined
      FixedSlotList: [],
      PlotList: [],
      slotObject: [],
    };
  },

  methods: {
    submitUserForm() {
      if (this.formType == "Add") {
        bus.$emit("showLoader", true);
        this.$api.adminUser.
          createAdminUser(this.userFormDetails)
          .then(async () => {
            bus.$emit("showLoader", false);
            bus.$emit("showToastMessage", {
              message: "Admin User Created Successfully",
              color: "success",
            });
            this.resetForm();
            this.$router.push({
              path: "/app/admin/users",
            });
          })
          .catch((err) => {
            bus.$emit("showLoader", false);
            if ("non_field_errors" in err.data) {
              this.nonFieldError = err.data.non_field_errors;
            }
            this.formErrors = err.data;
          });
      }
      // else {
      //   bus.$emit("showLoader", true);
      //   this.$api.order
      //     .updateOrder(this.orderFormDetails)
      //     .then(async () => {
      //       bus.$emit("showLoader", false);
      //       if (this.deleteItems && this.deleteItems.length > 0) {
      //         this.deleteOrderItem();
      //       }
      //       bus.$emit("showToastMessage", {
      //         message: this.$i18n.t("order updated successfully"),
      //         color: "success",
      //       });
      //       this.$router.push({
      //         path: "/app/admin/orders",
      //       });
      //     })
      //     .catch((err) => {
      //       this.formErrors = err.data;
      //       bus.$emit("showLoader", false);
      //     });
      // }
    },
    resetForm() {
      this.userFormDetails = {};
      this.formErrors = {};
      this.nonFieldError = [];
      this.$refs.adminForm1.reset();
    },
  }
};
</script>

<style scoped>
</style>