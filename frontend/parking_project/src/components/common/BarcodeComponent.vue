<template>
  <v-dialog width="70%" max-width="900px" v-model="barcodeDialog">
    <v-card>
      <v-card-title>
        <span
          class="
            text-lg-subtitle-1 text-xl-h6 text-uppercase
            font-weight-black
            primary--text
          "
          >Parking Ticket</span
        >
        <v-spacer></v-spacer>
        <v-btn depressed fab class="mt-n3" small @click="barcodeDialog = false">
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-card-title>
      <v-card-text>
        <v-row id="barcodePdf">
          <v-col class="col-7">
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
                      Date :
                    </h6>
                  </th>
                  <td class="txt-left">
                    <h6 class="trip-sheet-title set-color-text">
                      {{ slotObject.slot_date }}
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
                      {{ slotObject.fixed_slot }}
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
                      {{ slotObject.contact_number }}
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
                      {{ slotObject.vehicle_plat_no }}
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
                      {{ slotObject.vehicle_type }}
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
                      {{ slotObject.from_time }} to {{ slotObject.to_time }}
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
                      {{ slotObject.payment_method }}
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
                      {{ slotObject.amount }}
                    </h6>
                  </td>
                </tr>
              </table>
            </div>
          </v-col>
          <v-col class="d-flex justify-center align-center">
            <div>
              <v-btn
                @click="downloadPDF"
                depressed
                color="primary"
                class="mb-5"
              >
                Download Ticket</v-btn
              >
              <br />
              <v-btn @click="printPreviewDisplay" depressed color="primary">
                Print Ticket
              </v-btn>
            </div>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>

    <PrintViewComponent
      v-model="showPrintPreviewDialog"
      :slotObj="slotObject"
      ref="preview"
      :barcodeString="barcodeString"
    />
  </v-dialog>
</template>

<script>
import html2pdf from "@/../node_modules/html2pdf.js";
import PrintViewComponent from "@/components/common/BarcodePrintPreviewComponent.vue";

export default {
  name: "BarcodeComponent",
  components: {
    PrintViewComponent,
  },
  props: {
    value: {
      type: Boolean,
      requred: true,
    },
    slotObject: {
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
  data() {
    return {
      showPrintPreviewDialog: false,
      reference_number: "ORD-3555464",
    };
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
    printPreviewDisplay() {
      this.showPrintPreviewDialog = true;
      this.$refs.preview.printPreview();
    },
    downloadBarcode() {
      let canvas = document.getElementById("barcode");
      let image = canvas.toDataURL("image/png");
      var a = document.createElement("a");
      a.href = image;
      a.setAttribute("download", this.reference_number);
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
    },
    downloadPDF() {
      let element = null;
      let filename = "";
      element = document.getElementById("barcodePdf");
      filename = "slotbarcode(" + this.slotObject.id + ").pdf";

      var opt = {
        margin: 0.25,
        filename: filename,
        image: { type: "jpeg", quality: 0.98 },
        html2canvas: { scale: 1 },
        jsPDF: { unit: "in", format: "letter", orientation: "landscape" },
      };
      html2pdf(element, opt);
    },
  },
};
</script>

<style>
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
  color: white;
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
  color: white;
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
  color: black;
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
