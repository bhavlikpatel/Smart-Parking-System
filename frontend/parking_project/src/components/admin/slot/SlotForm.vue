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
                  <v-select
                    name="plot_id"
                    clearable
                    label="Plot*"
                    :items="PlotList"
                    outlined
                    v-model="slotFormDetails.plot_id"
                    :menu-props="{ offsetY: true }"
                    item-text="plot_name"
                    item-value="id"
                    :error-messages="
                      formErrors && formErrors.plot_id ? formErrors.plot_id : ''
                    "
                    :rules="[(val) => !!val || 'Plot is required']"
                    @change="
                      formErrors && formErrors.plot_id
                        ? delete formErrors.plot_id
                        : ''
                    "
                  ></v-select>
                </v-col>
                <v-col cols="3" class="pa-1">
                  <v-text-field
                    outlined
                    type="number"
                    name="slot_size"
                    label="Slot Size*"
                    v-model="slotFormDetails.slot_size"
                    required
                    :rules="[(v) => !!v || 'Slot Size is required']"
                    :error-messages="
                      formErrors && formErrors.slot_size
                        ? formErrors.slot_size
                        : ''
                    "
                    @input="
                      formErrors && formErrors.slot_size
                        ? delete formErrors.slot_size
                        : ''
                    "
                /></v-col>
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
          @click.prevent="submitSlotForm()"
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
      isValid: false,
      backRoute: { path: "/app/admin/fixed_slots" },
      slotFormDetails: {},

      // Select List Detail Defined
      FixedSlotList: [],
      PlotList: [],
      slotObject: [],
    };
  },

  methods: {
    submitSlotForm() {
      if (this.formType == "Add") {
        bus.$emit("showLoader", true);
        this.$api.adminSlot
          .adminAddSlots(this.slotFormDetails)
          .then(async (res) => {
            bus.$emit("showLoader", false);
            bus.$emit("showToastMessage", {
              message: res.data.message,
              color: "success",
            });
            this.resetForm();
            this.$router.push({
              path: "/app/admin/fixed_slots",
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
    getPlotList() {
      this.$api.slot
        .getPlotList({})
        .then((result) => {
          bus.$emit("showLoader", false);
          if (result.data) {
            this.PlotList = result.data;
          }
        })
        .catch((err) => {
          console.error(err);
          bus.$emit("showLoader", false);
        });
    },
    resetForm() {
      this.slotFormDetails = {};
      this.formErrors = {};
      this.nonFieldError = [];
      this.$refs.slotForm1.reset();
    },
  },
  mounted() {
    this.getPlotList();
  },
};
</script>

<style scoped>
</style>