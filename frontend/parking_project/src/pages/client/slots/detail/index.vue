<template>
  <BaseDetailsLayout
    title="slot details"
    :backRoute="backRoute"
    overClass="px-0"
    boxShadow="0"
  >
    <template #formContent>
      <div>
        <v-card class="pa-4 mx-5" elevation="0" tile>
          <v-row class="d-flex justify-center">
            <v-col cols="12">
              <v-simple-table class="px-4" style="border: 1px solid grey">
                <tbody>
                  <tr>
                    <th class="text-left">Slot Reference Number</th>
                    <td>{{ slotDetails.reference_number }}</td>
                  </tr>
                  <tr>
                    <th class="text-left">Slot Id</th>
                    <td>{{ slotDetails.fixed_slot }}</td>
                  </tr>
                  <tr>
                    <th class="text-left">Slot Booked Date</th>
                    <td>{{ slotDetails.slot_date }}</td>
                  </tr>
                  <tr>
                    <th class="text-left">Vehicle Plat No</th>
                    <td>{{ slotDetails.vehicle_plat_no }}</td>
                  </tr>
                  <tr>
                    <th class="text-left">Vehicle Type</th>
                    <td>{{ slotDetails.vehicle_type }}</td>
                  </tr>
                  <tr>
                    <th class="text-left">Contact Number</th>
                    <td>{{ slotDetails.contact_number }}</td>
                  </tr>
                  <tr>
                    <th class="text-left">Time window</th>
                    <td>{{ slotDetails.from_time }} to {{ slotDetails.to_time }}</td>
                  </tr>
                  <tr>
                    <th class="text-left">Payment Type</th>
                    <td>{{ slotDetails.payment_method }}</td>
                  </tr>

                  <tr>
                    <th class="text-left">Amount</th>
                    <td>{{ slotDetails.amount }}</td>
                  </tr>
                </tbody>
              </v-simple-table>
              <div class="d-flex justify-center">
                <v-tooltip top>
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn
                      class="mt-2 edit primary text-white"
                      small
                      elevation="5"
                      v-bind="attrs"
                      v-on="on"
                      depressed
                      x-large
                      @click="showBarcodeDialog = true"
                    >
                      <v-icon x-large>mdi-barcode</v-icon>
                    </v-btn>
                  </template>
                  <span>Generate Parking Ticket</span>
                </v-tooltip>
              </div>
            </v-col>
          </v-row>
        </v-card>
      </div>
      <div v-if="showBarcodeDialog">
        <BarcodeComponent
          v-model="showBarcodeDialog"
          :slotObject="slotDetails"
          :barcodeString="slotDetails.reference_number"
        />
      </div>
    </template>
  </BaseDetailsLayout>
</template>

<script>
import BaseDetailsLayout from "@/components/common/Layouts/BaseDetailsLayout.vue";
import BarcodeComponent from "@/components/common/BarcodeComponent.vue";
import { bus } from "@/main";

export default {
  layout: "MainLayout",
  name: "SlotDetailIndex",
  components: {
    BaseDetailsLayout,
    BarcodeComponent,
  },
  data() {
    return {
      slotDetails: {},
      showBarcodeDialog: false,
      height: null,
      scrollInvoked: 0,

      backRoute: { path: "/app/admin/slots" },
    };
  },
  methods: {
    onScroll() {
      this.scrollInvoked++;
    },
    editDriver(id) {
      this.$router.push({
        path: `/app/admin/slots/edit/${id}`,
      });
    },
    getslotDetails(id) {
      this.$api.slot
        .getSlotObj(id)
        .then((result) => {
          this.slotDetails = result.data;
        })
        .catch((err) => {
          console.log(err);
          bus.$emit("showToastMessage", {
            message: "Couln't fetch data",
            color: "error",
          });
        });
    },
  },
  mounted() {
    if ("id" in this.$route.params) {
      this.getslotDetails(this.$route.params.id);
    }
  },
};
</script>
