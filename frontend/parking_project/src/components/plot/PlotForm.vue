<template>
  <div ref="slotForm">
    <BaseFormLayout
      :title="`${formType} slot`.toLowerCase()"
      :backRoute="backRoute"
      :nonFieldError="nonFieldError"
    >
      <template #formContent>
        <v-form
          v-model="isValid"
          ref="slotForm1"
          name="slotForm"
          id="slotForm"
          autocomplete="off"
        >
          <v-row class="pa-8">
            <v-col cols="12" lg="12">
              <v-row>
                <v-col cols="3" class="pa-1">
                  <v-text-field
                    outlined
                    type="text"
                    name="plot_name"
                    label="Plot Name*"
                    v-model="plotFormDetails.plot_name"
                    required
                    :rules="[(v) => !!v || 'Plot Name is required']"
                    :error-messages="
                      formErrors && formErrors.plot_name
                        ? formErrors.plot_name
                        : ''
                    "
                    @input="
                      formErrors && formErrors.plot_name
                        ? delete formErrors.plot_name
                        : ''
                    "
                /></v-col>
                <v-col cols="3" class="pa-1">
                  <v-text-field
                    outlined
                    type="text"
                    name="plot_id"
                    label="Plot Id*"
                    v-model="plotFormDetails.plot_id"
                    required
                    :rules="[(v) => !!v || 'Plot Id is required']"
                    :error-messages="
                      formErrors && formErrors.plot_id ? formErrors.plot_id : ''
                    "
                    @input="
                      formErrors && formErrors.plot_id
                        ? delete formErrors.plot_id
                        : ''
                    "
                /></v-col>
                <v-col cols="3" class="pa-1">
                  <v-text-field
                    outlined
                    type="text"
                    name="city"
                    label="Plot City*"
                    v-model="plotFormDetails.city"
                    required
                    :rules="[(v) => !!v || 'Plot City is required']"
                    :error-messages="
                      formErrors && formErrors.city ? formErrors.city : ''
                    "
                    @input="
                      formErrors && formErrors.city
                        ? delete formErrors.city
                        : ''
                    "
                /></v-col>
                <v-col cols="3" class="pa-1">
                  <v-text-field
                    outlined
                    type="text"
                    name="plot_address"
                    label="Plot Address*"
                    v-model="plotFormDetails.plot_address"
                    required
                    :rules="[(v) => !!v || 'Plot Address is required']"
                    :error-messages="
                      formErrors && formErrors.plot_address
                        ? formErrors.plot_address
                        : ''
                    "
                    @input="
                      formErrors && formErrors.plot_address
                        ? delete formErrors.plot_address
                        : ''
                    " /></v-col
              ></v-row>
            </v-col>
          </v-row> </v-form
      ></template>
      <template #formActions>
        <v-btn
          type="submit"
          :disabled="!isValid"
          width="9%"
          class="primary mr-3"
          @click.prevent="submitPlotForm()"
        >
          <span>Submit</span>
        </v-btn>
      </template>
    </BaseFormLayout>
  </div>
</template>

<script>
import BaseFormLayout from "@/components/common/Layouts/BaseFormLayout.vue";
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
      // Common Form Detail Defined
      formErrors: {},
      nonFieldError: [],
      isValid: false,
      backRoute: { path: "/app/admin/plots" },
      plotFormDetails: {},
    };
  },

  methods: {
    submitPlotForm() {
      if (this.formType == "Add") {
        bus.$emit("showLoader", true);
        this.$api.plot
          .addPlot(this.plotFormDetails)
          .then(async () => {
            bus.$emit("showLoader", false);
            bus.$emit("showToastMessage", {
              message: "plot created successfully",
              color: "success",
            });
            this.resetForm();
            this.$router.push({
              path: "/app/admin/plots",
            });
          })
          .catch((err) => {
            bus.$emit("showLoader", false);
            if ("non_field_errors" in err.data) {
              this.nonFieldError = err.data.non_field_errors;
            }
            this.formErrors = err.data;
          });
      } else {
        bus.$emit("showLoader", true);
        this.$api.plot
          .updatePlot(this.plotFormDetails)
          .then(async () => {
            bus.$emit("showLoader", false);
            bus.$emit("showToastMessage", {
              message: "plot updated successfully",
              color: "success",
            });
            this.$router.push({
              path: "/app/admin/plots",
            });
          })
          .catch((err) => {
            this.formErrors = err.data;
            bus.$emit("showLoader", false);
          });
      }
    },
    resetForm() {
      this.plotFormDetails = {};
      this.formErrors = {};
      this.nonFieldError = [];
      this.$refs.slotForm1.reset();
    },
    populateForm(id) {
      this.$api.plot
        .getPlotObject(id)
        .then((result) => {
          this.plotFormDetails = result.data;          
        })
        .catch(() => {
          bus.$emit("showToastMessage", {
            message: this.$i18n.t("couldn't fetch data"),
            color: "error",
          });
        });
    },
  },
  mounted() {
    if ("id" in this.$route.params) {
      this.populateForm(this.$route.params.id);
    }
  },
};
</script>

<style scoped>
</style>