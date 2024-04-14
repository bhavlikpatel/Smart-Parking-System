<template>
  <v-dialog max-width="800px" v-model="showDialog">
    <v-card v-if="customerAddressObj">
      <v-card-title class="primary text-white">
        {{ customerAddressObj.id }} Details
        <v-spacer></v-spacer>
        <v-btn icon class="text-white" @click="showDialog = false">
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-card-title>
      <v-card-text class="pa-5">
        <v-row>
          <v-col cols="6 border-right-grey">
            <span class="text-h6 font-weight-bold">Customer Name :</span>
            <span class="text-h6 font-weight-bold">{{
              customerAddressObj.id
            }}</span>
          </v-col>
          <v-col cols="6">
            <span class="text-h6 font-weight-bold">Contact Number :</span>
            <span class="text-h6 font-weight-bold">{{
              customerAddressObj.id
            }}</span>
          </v-col>
          <!-- <v-col cols="6 border-right-grey">
            <span class="text-h6 font-weight-bold">Contact Email :</span>
            <span class="text-h6 font-weight-bold">{{
              customerAddressObj.contact_email
            }}</span>
          </v-col>
          <v-col cols="6 ">
            <span class="text-h6 font-weight-bold">Customer Segment :</span>
            <span class="text-h6 font-weight-bold">{{
              customerAddressObj.customer_segment
            }}</span>
          </v-col>
          <v-col cols="6 border-right-grey">
            <span class="text-h6 font-weight-bold">Customer Sub Segment :</span>
            <span class="text-h6 font-weight-bold">{{
              customerAddressObj.customer_sub_segment
            }}</span>
          </v-col>
          <v-col cols="6 ">
            <span class="text-h6 font-weight-bold">Address :</span>
            <span class="text-h6 font-weight-bold">{{
              customerAddressObj.address
            }}</span>
          </v-col>
          <v-col cols="6 border-right-grey">
            <span class="text-h6 font-weight-bold">Processing Time :</span>
            <span class="text-h6 font-weight-bold">{{
              customerAddressObj.processing_time
            }}</span>
          </v-col>
          <v-col cols="6">
            <span class="text-h6 font-weight-bold">Extra Info :</span>
            <span class="text-h6 font-weight-bold">{{
              customerAddressObj.extra_info
            }}</span>
           </v-col> -->
        </v-row>
        <!-- <v-row>
          <v-col
            cols="12"
            class="d-flex justify-center text-h5 deep-purple white--text"
            >Time Slots</v-col
          >
          <v-col cols="6">From Time</v-col>
          <v-col cols="6">To Time</v-col>
        </v-row> -->
        <!-- <div v-if="customerAddressObj.time_slots">
          <v-row v-for="(slot, i) in customerAddressObj.time_slots" :key="i">
            <v-col cols="6 border-right-grey">
              <span class="text-h6 font-weight-bold">{{ slot.from_time }}</span>
            </v-col>
            <v-col cols="6 border-right-grey">
              <span class="text-h6 font-weight-bold">{{ slot.to_time }}</span>
            </v-col>
          </v-row> 
        </div> -->
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: "SlotDetails",
  props: {
    value: {
      type: Boolean,
    },
    SlotID: {
      type: Number,
    },
  },
  data() {
    return {
      customerAddressObj: null,
    };
  },
  watch: {
    SlotID() {
      this.getSlotDetails(this.SlotID);
    },
  },
  computed: {
    showDialog: {
      get() {
        return this.value;
      },
      set(value) {
        this.$emit("input", value);
      },
    },
  },
  methods: {
    getSlotDetails(id) {
      this.$api.slot
        .getSlotDetail(id)
        .then((res) => {
          this.customerAddressObj = res.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },},
  mounted() {
    if (this.SlotID) {
      this.getSlotDetails(this.SlotID);
    }
  },
};
</script>

<style></style>
