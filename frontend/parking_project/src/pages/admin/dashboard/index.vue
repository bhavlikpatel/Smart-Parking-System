<template>
  <div>
    <div class="pa-6" v-if="!openAddSlotDialog">
      <h1>Admin DashBoard</h1>
      <v-row class="border-top-light_black pt-4 d-flex mt-8">
        <v-col cols="3">
          <v-menu
            v-model="toDate"
            :close-on-content-click="false"
            :nudge-right="40"
            transition="scale-transition"
            offset-y
            min-width="auto"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                v-model="getFromDate"
                label="From"
                class="mr-4"
                prepend-inner-icon="mdi-calendar"
                readonly
                outlined
                dense
                hide-details="auto"
                v-bind="attrs"
                v-on="on"
              ></v-text-field>
            </template>
            <v-date-picker
              @change="dateValidator"
              :max="nowDate"
              v-model="getFromDate"
              @input="toDate = false"
            ></v-date-picker>
          </v-menu>
        </v-col>
        <v-col cols="3">
          <v-menu
            v-model="fromDate"
            :close-on-content-click="false"
            :nudge-right="40"
            transition="scale-transition"
            offset-y
            min-width="auto"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                v-model="getToDate"
                label="To"
                prepend-inner-icon="mdi-calendar"
                readonly
                dense
                outlined
                hide-details="auto"
                v-bind="attrs"
                v-on="on"
              ></v-text-field>
            </template>
            <v-date-picker
              @change="dateValidator"
              v-model="getToDate"
              :max="nowDate"
              @input="fromDate = false"
            ></v-date-picker>
          </v-menu>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" class="pt-4">
          <div
            class="
              pa-2
              primary
              rounded-t-lg
              border-x-light_black
              border-y-light_black
            "
          >
            <span
              class="px-3 text-white text-h6 text-uppercase font-weight-bold"
            >
              Slot Utilization
            </span>
          </div>
          <div
            class="
              rounded-b-lg
              pa-4
              border-x-light_black
              border-bottom-light_black
            "
          >
            <div v-if="slotUtilization">
              <LineChart
                v-if="chart"
                :datasets="slotUtilization"
                :options="barOptions"
              />
            </div>
            <div
              class="
                loader-container
                d-flex
                align-center
                justify-center
                full-width
              "
              v-if="!chart"
            >
              <v-progress-circular
                :size="70"
                :width="7"
                color="primary"
                indeterminate
              ></v-progress-circular>
            </div>
          </div>
        </v-col>
      </v-row>
      <v-row no_gutter justify="center">
        <v-col cols="2">
          <v-card
            class="py-6 primary text-white text-center"
            height="120"
            width="400"
            elevation="4"
          >
            <span>Total Slots</span>
            <h1>{{ scoreBoard.total_fixed_slots }}</h1>
          </v-card>
        </v-col>
        <v-col cols="2">
          <v-card
            class="py-6 primary text-white text-center"
            height="120"
            width="400"
            elevation="4"
          >
            <span>Total Plots</span>
            <h1>{{ scoreBoard.total_plot }}</h1>
          </v-card>
        </v-col>
        <v-col cols="2">
          <v-card
            class="py-6 primary text-white text-center"
            height="120"
            width="400"
            elevation="4"
          >
            <span>Total Payments</span>
            <h1>
              <span class="text-orange"> Rs.</span>
              {{ scoreBoard.total_payment }}
            </h1>
          </v-card>
        </v-col>
        <v-col cols="2">
          <v-card
            class="py-6 primary text-white text-center"
            height="120"
            width="400"
            elevation="4"
          >
            <span>Total Utilized Slots</span>
            <h1>{{ scoreBoard.user_slot_count }}</h1>
          </v-card>
        </v-col>
        <v-col cols="2">
          <v-card
            class="py-6 primary text-white text-center"
            height="120"
            width="400"
            elevation="4"
          >
            <span>AVG Slot Utilization</span>
            <h1>{{ scoreBoard.avg_slot_utilization }}%</h1>
          </v-card>
        </v-col>
      </v-row>
    </div>
  </div>
</template>

<script>
import { bus } from "@/main";
import LineChart from "@/components/common/aggrid/charts/LineChart.vue";

export default {
  name: "AdminDashboardIndex",
  layout: "MainLayout",
  components: { LineChart },
  data() {
    return {
      scoreBoard: [],
      openSlotDetailDialog: false,
      openAddSlotDialog: false,
      slot_id: null,
      chart: false,
      toDate: false,
      fromDate: false,
      nowDate: new Date().toISOString().slice(0, 10),
      getFromDate: new Date(new Date().setDate(new Date().getDate() - 7))
        .toISOString()
        .slice(0, 10),
      getToDate: new Date().toISOString().slice(0, 10),
      slotUtilization: {},
      barOptions: {
        scales: {
          yAxes: [
            {
              ticks: {
                stepSize: 50,
                beginAtZero: true,
              },
            },
          ],
        },
        responsive: true,
        maintainAspectRatio: false,
      },
    };
  },
  methods: {
    dateValidator() {
      if (
        this.getFromDate &&
        this.getToDate &&
        this.getFromDate > this.getToDate
      ) {
        let _ = this.getToDate;
        this.getToDate = this.getFromDate;
        this.getFromDate = _;

        this.getSlotUtilization();
        this.getFixedSlots();
      } else {
        this.getSlotUtilization();
        this.getFixedSlots();
      }
    },
    getFixedSlots() {
      let params = {};
      if (this.getFromDate && this.getToDate) {
        params.start_date = this.getFromDate;
        params.end_date = this.getToDate;
      }
      this.$api.adminDashBoard
        .getScoreBoard(params)
        .then((result) => {
          bus.$emit("showLoader", false);
          this.scoreBoard = result.data.scoreboard;
        })
        .catch((err) => {
          console.error(err);
          bus.$emit("showLoader", false);
        });
    },
    getSlotUtilization() {
      let params = {};
      if (this.getFromDate && this.getToDate) {
        params.start_date = this.getFromDate;
        params.end_date = this.getToDate;
      }
      this.chart = false;
      this.$api.adminDashBoard
        .getSlotUtilization(params)
        .then((result) => {
          this.chart = false;
          var slotUtilizationdata = result.data.utilized_slots;

          let chartStructure = {
            labels: [],
            datasets: [
              {
                label: "Slot Created per Day",
                backgroundColor: "#90CAF9",
                data: [],
              },
            ],
          };
          for (const key in slotUtilizationdata) {
            chartStructure.labels.push(
              Object.keys(slotUtilizationdata[key])[0]
            );
            chartStructure.datasets[0]["data"].push(
              Object.values(slotUtilizationdata[key])[0]
            );
          }

          this.slotUtilization = chartStructure;
          setTimeout(() => {
            this.chart = true;
          }, 200);
        })
        .catch((err) => {
          console.error(err);
          bus.$emit("showLoader", false);
        });
    },
  },
  mounted() {
    this.getFixedSlots();
    this.getSlotUtilization();
  },
};
</script>

<style>
</style>