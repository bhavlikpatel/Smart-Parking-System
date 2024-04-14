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
            <v-col cols="9" lg="9">
              <v-row>
                <v-col cols="3" class="pa-1">
                  <v-select
                    name="vehicle_type"
                    clearable
                    label="Vehicle Type*"
                    :items="vehicleType"
                    outlined
                    v-model="slotFormDetails.vehicle_type"
                    :menu-props="{ offsetY: true }"
                    item-text="label"
                    item-value="value"
                    :error-messages="
                      formErrors && formErrors.vehicle_type
                        ? formErrors.vehicle_type
                        : ''
                    "
                    :rules="[(val) => !!val || 'Vehicle Type is required']"
                    @change="
                      formErrors && formErrors.vehicle_type
                        ? delete formErrors.vehicle_type
                        : ''
                    "
                  ></v-select>
                </v-col>
                <v-col cols="3" class="pa-1">
                  <v-text-field
                    outlined
                    type="text"
                    name="vehicle_plat_no"
                    label="Vehicle Plat No*"
                    v-model="slotFormDetails.vehicle_plat_no"
                    required
                    :rules="[(v) => !!v || 'Vehicle Plat Number is required']"
                    :error-messages="
                      formErrors && formErrors.vehicle_plat_no
                        ? formErrors.vehicle_plat_no
                        : ''
                    "
                    @input="
                      formErrors && formErrors.vehicle_plat_no
                        ? delete formErrors.vehicle_plat_no
                        : ''
                    "
                /></v-col>
                <v-col cols="3" class="pa-1">
                  <v-text-field
                    outlined
                    name="contact_number"
                    min="0"
                    label="Contact Number*"
                    v-model="slotFormDetails.contact_number"
                    required
                    :rules="[
                      (v) => !!v || 'contact number is required',
                      (v) =>
                        !/[^0-9]/.test(v) || 'only numeric values are allowed',
                      (v) =>
                        (v && 10 <= v.length && v.length <= 10) ||
                        'contact number must be 10 digits only',
                    ]"
                    :error-messages="
                      formErrors && formErrors.contact_number
                        ? formErrors.contact_number
                        : ''
                    "
                    @input="
                      formErrors && formErrors.contact_number
                        ? delete formErrors.contact_number
                        : ''
                    "
                /></v-col>
                <v-col cols="3" class="pa-1">
                  <DatePicker
                    outlined
                    type="date"
                    name="slot_date"
                    label="Slot Date"
                    v-model="slotFormDetails.slot_date"
                    :min="returnToday()"
                  />
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="3" class="pa-1" v-if="PlotList">
                  <TheSelect
                    v-model="slotFormDetails.plot"
                    :itemsList="PlotList"
                    label="Select Plot"
                    :multiple="false"
                    itemText="plot_name"
                    itemValue="id"
                    class="mb-4 background-white"
                    @change="getSlotList($event)"
                  />
                </v-col>
                <v-col cols="3" class="pa-1" v-if="FixedSlotList">
                  <TheSelect
                    v-model="slotFormDetails.fixed_slot"
                    :itemsList="FixedSlotList"
                    label="Select slot"
                    :multiple="false"
                    itemText="id"
                    itemValue="id"
                    class="mb-4 background-white"
                    @change="getBookedSlotTimeWindows($event)"
                  />
                </v-col>
                <v-col cols="3" class="pa-1">
                  <TimePicker
                    outlined
                    name="from_time"
                    label="From Time*"
                    v-model="slotFormDetails.from_time"
                    :error-messages="
                      formErrors && formErrors.from_time
                        ? formErrors.from_time
                        : ''
                    "
                    :rules="[(val) => !!val || 'From Time  is required']"
                    @change="getPaymentDetail()"
                  />
                </v-col>
                <v-col cols="3" class="pa-1">
                  <TimePicker
                    outlined
                    name="to_time"
                    label="To Time*"
                    v-model="slotFormDetails.to_time"
                    :error-messages="
                      formErrors && formErrors.to_time ? formErrors.to_time : ''
                    "
                    :rules="[(val) => !!val || 'To Time is required']"
                    :min="slotFormDetails.from_time"
                    @change="getPaymentDetail()"
                  />
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="3" class="pa-1">
                  <v-select
                    name="payment_type"
                    clearable
                    label="payment type*"
                    :items="paymentType"
                    outlined
                    v-model="slotFormDetails.payment_method"
                    :menu-props="{ offsetY: true }"
                    item-text="label"
                    item-value="value"
                    :error-messages="
                      formErrors && formErrors.payment_method
                        ? formErrors.payment_method
                        : ''
                    "
                    :rules="[(val) => !!val || 'Payment Type is required']"
                    @change="
                      formErrors && formErrors.payment_method
                        ? delete formErrors.payment_method
                        : ''
                    "
                  ></v-select>
                </v-col>
                <v-col cols="3" class="pa-1">
                  <v-text-field
                    type="number"
                    name="amount"
                    class="remove-number-spinners"
                    :min="0"
                    label="Payment Amount*"
                    :rules="[
                      (val) => !!val || 'Aayment Amount is required',
                      (val) =>
                        val > 0 || 'payment amount should be greater than 0',
                    ]"
                    outlined
                    v-model="slotFormDetails.amount"
                    :error-messages="
                      formErrors && formErrors.amount ? formErrors.amount : ''
                    "
                    @input="
                      formErrors && formErrors.amount
                        ? delete formErrors.amount
                        : ''
                    "
                  />
                </v-col>
              </v-row>
            </v-col>
            <v-col cols="3" lg="3">
              <v-card
                elevation="3"
                class="px-4 py-4 text-center"
                color="#EEEEEE"
                style="height: auto"
              >
                <v-row
                  v-show="slotFormDetails.plot && slotFormDetails.fixed_slot"
                >
                  <v-card-title
                    ><v-icon class="text-primary">mdi-clock</v-icon>Booked Slot
                    Time Windows</v-card-title
                  >
                </v-row>
                <div
                  v-show="
                    slotFormDetails.plot &&
                    slotFormDetails.fixed_slot &&
                    slotObject &&
                    slotObject.length == 0
                  "
                  class="pa-4 mx-2 primary text-no-wrap rounded-pill elevation-7"
                >
                  <span class="text-white">Slot Empty For 24 Hours</span>
                </div>
                <v-row
                  v-show="slotFormDetails.plot && slotFormDetails.fixed_slot"
                  v-for="(slot, i) in slotObject"
                  :key="i"
                >
                  <v-list-item-content class="mx-4 text-white">
                    <div
                      class="pa-4 primary text-no-wrap rounded-pill elevation-7"
                    >
                      <v-icon class="text-white">mdi-clock</v-icon>
                      {{ slot.from_time }} to
                      {{ slot.to_time }}
                    </div>
                  </v-list-item-content>
                </v-row>
                <v-row>
                  <v-card-title
                    ><v-icon class="text-primary">mdi-cash</v-icon>Payment
                    Information</v-card-title
                  >
                </v-row>
                <v-row>
                  <v-list-item-content class="mx-4 text-white">
                    <div
                      class="pa-4 primary text-no-wrap rounded-pill elevation-7"
                    >
                      <v-icon class="text-white">mdi-cash</v-icon>
                      <span> Rs. 30 - Upto 2 Hours</span>
                    </div>
                  </v-list-item-content>
                </v-row>
                <v-row>
                  <v-list-item-content class="mx-4 text-white">
                    <div
                      class="pa-4 primary text-no-wrap rounded-pill elevation-7"
                    >
                      <v-icon class="text-white">mdi-cash</v-icon>
                      <span> Rs. 50 - For 2 to 6 Hours</span>
                    </div>
                  </v-list-item-content>
                </v-row>
                <v-row>
                  <v-list-item-content class="mx-4 text-white">
                    <div
                      class="pa-4 primary text-no-wrap rounded-pill elevation-7"
                    >
                      <v-icon class="text-white">mdi-cash</v-icon>
                      <span> Rs. 100 - For 6 to 12 Hours</span>
                    </div>
                  </v-list-item-content>
                </v-row>
                <v-row>
                  <v-list-item-content class="mx-4 text-white">
                    <div
                      class="pa-4 primary text-no-wrap rounded-pill elevation-7"
                    >
                      <v-icon class="text-white">mdi-cash</v-icon>
                      <span> Rs. 150 - For 12 to 24 Hours</span>
                    </div>
                  </v-list-item-content>
                </v-row>
              </v-card>
            </v-col>
          </v-row>
        </v-form></template
      >
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
import TheSelect from "@/components/BaseComponents/TheSelect.vue";
import { bus } from "@/main";
import DatePicker from "@/components/BaseComponents/DatePicker.vue";
import TimePicker from "@/components/BaseComponents/TimePicker.vue";
import { paymentType, vehicleType } from "@/utils/choices.js";

export default {
  layout: "MainLayout",
  components: {
    BaseFormLayout,
    TheSelect,
    DatePicker,
    TimePicker,
  },
  props: {
    formType: {
      required: true,
      default: "Add",
    },
    fixed_slot: {
      required: false,
    },
    plot_id: {
      required: false,
    },
  },
  data() {
    return {
      returnToday,
      paymentType,
      vehicleType,
      // Common Form Detail Defined
      formErrors: {},
      nonFieldError: [],
      isValid: false,
      backRoute: { path: "/app/admin/slots" },
      slotFormDetails: {
        payment_method: "CASH",
        vehicle_type: "FOUR_WHEELER",
        amount: 0,
        is_booked: true,
        slot_date: returnToday(),
      },

      // Select List Detail Defined
      FixedSlotList: [],
      slotObject: [],
      PlotList: [],
    };
  },

  methods: {
    getPaymentDetail() {
      if (this.slotFormDetails.from_time && this.slotFormDetails.to_time) {
        const params = {
          from_time: this.slotFormDetails.from_time,
          to_time: this.slotFormDetails.to_time,
        };
        this.$api.slot
          .getPaymentDetail(params)
          .then((result) => {
            this.slotFormDetails.amount = result.data.amount;
          })
          .catch((err) => {
            console.error(err);
            // bus.$emit("showLoader", false);
          });
      }
    },
    getSlotList() {
      const params = {
        plot: this.slotFormDetails.plot,
      };
      this.$api.slot
        .getFixedSlotList(params)
        .then((result) => {
          bus.$emit("showLoader", false);
          this.FixedSlotList = result.data;
        })
        .catch((err) => {
          console.error(err);
          bus.$emit("showLoader", false);
        });
    },
    getBookedSlotTimeWindows(slot_id) {
      const params = {
        slot_id: slot_id,
        slot_date: this.slotFormDetails.slot_date,
      };
      this.$api.slot
        .getTimeWindows(params)
        .then((result) => {
          bus.$emit("showLoader", false);
          this.slotObject = result.data;
          console.log(this.slotObject.length);
        })
        .catch((err) => {
          console.error(err);
          bus.$emit("showLoader", false);
        });
    },
    submitSlotForm() {
      if (this.formType == "Add") {
        bus.$emit("showLoader", true);
        this.$api.slot
          .addSlot(this.slotFormDetails)
          .then(async () => {
            bus.$emit("showLoader", false);
            bus.$emit("showToastMessage", {
              message: "slot created successfully",
              color: "success",
            });
            this.resetForm();
            this.$router.push({
              path: "/app/admin/slots",
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
    getAllFixedSlots() {
      this.$api.slot
        .getFixedSlotList({})
        .then((result) => {
          bus.$emit("showLoader", false);
          this.FixedSlotList = result.data;
          this.slotFormDetails.fixed_slot = this.fixed_slot;
        })
        .catch((err) => {
          console.error(err);
          bus.$emit("showLoader", false);
        });
    },
    resetForm() {
      this.slotFormDetails = {
        is_booked: false,
      };
      this.formErrors = {};
      this.nonFieldError = [];
      this.$refs.slotForm1.reset();
    },
    getPlotList() {
      this.$api.slot
        .getPlotList({})
        .then((result) => {
          bus.$emit("showLoader", false);
          if (result.data) {
            this.PlotList = result.data;
            this.slotFormDetails.plot = this.plot_id;
          }
        })
        .catch((err) => {
          console.error(err);
          bus.$emit("showLoader", false);
        });
    },
  },
  mounted() {
    this.getPlotList();
    this.getAllFixedSlots();
  },
};
</script>

<style scoped></style>
