<template>
  <v-dialog
    fullscreen
    hide-overlay
    width="70%"
    elevation-0
    primary
    max-width="900px"
    v-model="barcodeDialog"
    style="background-color: white !important"
  >
    <v-card style="padding: 5% !important">
      <v-card-text>
        <v-row id="barcodePdf">
          <v-col class="col-12">
            <div class="ba">
              <div style="text-align: center !important">
                <vue-barcode
                  id="barcode"
                  :value="barcodeString"
                  :options="options"
                />
              </div>
              <table>
                <tr style="display: flex">
                  <th class="txt-left">
                    <h6
                      class="trip-sheet-title set-color-title"
                      style="width: 160px !important"
                    >
                      Date:
                    </h6>
                  </th>
                  <td class="txt-left">
                    <h6 class="trip-sheet-title set-color-text">
                      {{ slotObj.slot_date }}
                    </h6>
                  </td>
                </tr>
                <tr style="display: flex">
                  <th class="txt-left">
                    <h6
                      class="trip-sheet-title set-color-title"
                      style="width: 160px !important"
                    >
                      Slot:
                    </h6>
                  </th>
                  <td class="txt-left">
                    <h6 class="trip-sheet-title set-color-text">
                      {{ slotObj.fixed_slot }}
                    </h6>
                  </td>
                </tr>
                <tr style="display: flex">
                  <th class="txt-left">
                    <h6
                      class="trip-sheet-title set-color-title"
                      style="width: 160px !important"
                    >
                      Contact Number:
                    </h6>
                  </th>
                  <td class="txt-left">
                    <h6 class="trip-sheet-title set-color-text">
                      {{ slotObj.contact_number }}
                    </h6>
                  </td>
                </tr>
                <tr style="display: flex">
                  <th class="txt-left">
                    <h6
                      class="trip-sheet-title set-color-title"
                      style="width: 160px !important"
                    >
                      Vehicle Plat No:
                    </h6>
                  </th>
                  <td class="txt-left">
                    <h6 class="trip-sheet-title set-color-text">
                      {{ slotObj.vehicle_plat_no }}
                    </h6>
                  </td>
                </tr>
                <tr style="display: flex">
                  <th class="txt-left">
                    <h6
                      class="trip-sheet-title set-color-title"
                      style="width: 160px !important"
                    >
                      Vehicle Type:
                    </h6>
                  </th>
                  <td class="txt-left">
                    <h6 class="trip-sheet-title set-color-text">
                      {{ slotObj.vehicle_type }}
                    </h6>
                  </td>
                </tr>
                <tr style="display: flex">
                  <th class="txt-left">
                    <h6
                      class="trip-sheet-title set-color-title"
                      style="width: 160px !important"
                    >
                      Time Windows:
                    </h6>
                  </th>
                  <td class="txt-left">
                    <h6 class="trip-sheet-title set-color-text">
                      {{ slotObj.from_time }} to {{ slotObj.to_time }}
                    </h6>
                  </td>
                </tr>
                <tr style="display: flex">
                  <th class="txt-left">
                    <h6
                      class="trip-sheet-title set-color-title"
                      style="width: 160px !important"
                    >
                      Payment type:
                    </h6>
                  </th>
                  <td class="txt-left">
                    <h6 class="trip-sheet-title set-color-text">
                      {{ slotObj.payment_method }}
                    </h6>
                  </td>
                </tr>
                <tr style="display: flex">
                  <th class="txt-left">
                    <h6
                      class="trip-sheet-title set-color-title"
                      style="width: 160px !important"
                    >
                      Amount
                    </h6>
                  </th>
                  <td class="txt-left">
                    <h6 class="trip-sheet-title set-color-text">
                      {{ slotObj.amount }}
                    </h6>
                  </td>
                </tr>
              </table>
            </div>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: "BarcodeGenerator",
  props: {
    value: {
      type: Boolean,
      requred: true,
    },
    slotObj: {
      type: Object,
      requred: true,
    },
    barcodeString: {
      type: [String, Number],
      required: true,
    },
    options: {
      type: Object,
      default: () => ({
        format: "CODE128",
        displayValue: true,
        height: 50,
      }),
    },
  },
  computed: {
    barcodeDialog: {
      get() {
        return this.value;
      },
      set(value) {
        this.$emit("input", value);
      },
    },
  },
  methods: {
    printPreview() {
      setTimeout(() => {
        window.print();
        this.barcodeDialog = false;
      }, 1000);
    },
  },
};
</script>

<style scoped>
thead {
  display: table-header-group;
}
tfoot {
  display: table-row-group;
}
tr {
  page-break-inside: avoid;
}
.txt-left {
  text-align: left !important;
}

.trip-sheet-title {
  padding: 0;
  margin: 0;
  color: #767779;
  font-size: 13px;
}
.trip-sheet-title {
  padding: 6px;
  margin: 0;
  color: black;
  font-size: 13px;
}
.trip-sheet-title-subtitle {
  padding: 2px 0px;
  margin: 0;
  color: primary;
  font-family: "Roboto";
  font-weight: 500 !important;
  font-size: 9px;
}
.trip-sheet-title-subtitle-text {
  padding: 0;
  margin: 0;
  color: #767779;
  font-family: "Roboto";
}

.trip-sheet-table-title {
  color: primary;
  margin: 20px 0px;
  font-size: 16px !important;
}

.trip-sheet-table {
  width: 100%;
  background-color: primary;
  padding: 3px 4px;
}

.trip-sheet-table-head h5 {
  padding: 6px 7px;
  font-size: 11px;
  color: black;
}

.trip-sheet-table-head {
  background-color: primary;
}
.trip-sheet-table-body h5 {
  font-size: 9px !important;
  font-family: "Roboto";
  font-weight: 500 !important;
  padding: 6px;
  margin: 0;
  color: #767779;
}
.set-color-title {
  color: primary;
}
.set-color-text {
  color: grey;
  font-weight: 400 !important;
  font-size: 12px;
}
.ba {
  border: 2px solid #8080802b;
}
</style>
