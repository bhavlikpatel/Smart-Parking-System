<template>
  <div>
    <div class="pa-6" v-if="!openAddSlotDialog">
      <h1>DashBoard</h1>
      <v-container class="mt-4">
        <v-row no_gutter justify="center">
          <v-text-field
            label="Search Plot Name, Ploy City, Plot ID"
            hide-details="auto"
            prepend-inner-icon="mdi-magnify"
            v-model="search"
            class="pa-2"
            outlined
            solo
            rounded
            dense
            clearable
            @keydown.enter="searchPlot()"
            @click:clear="searchPlot(true)"
          ></v-text-field>
        </v-row>
        <v-row no_gutter justify="center">
          <v-col cols="5">
            <v-chip class="ma-2 px-3 primary"></v-chip>
            <span>Empty Slot </span>
            <v-chip class="ma-2 px-3 yellow"></v-chip>
            <span>Patially Booked</span>
            <v-chip class="ma-2 px-3 orange"></v-chip>
            <span>Fully Booked</span>
          </v-col></v-row
        >
        <div v-for="(plot, index) in slotList" :key="index">
          <v-card
            elevation="2"
            outlined
            class="px-4 d-flex pa-1 primary text-white"
          >
            <v-card-title>ID: {{ plot.plot_id }} </v-card-title>
            <v-card-title>Plot Name: {{ plot.plot_name }} </v-card-title>
            <v-card-title>City: {{ plot.city }} </v-card-title>
            <v-card-title>Address: {{ plot.plot_address }} </v-card-title>
            <v-tooltip bottom>
              <template v-slot:activator="{ on, attrs }">
                <v-btn class="mt-5" v-bind="attrs" v-on="on">
                  <a
                    :href="`https://www.google.com/maps/search/${plot.plot_address}/`"
                    target="_blank"
                    ><v-icon class="text-red"> mdi-map </v-icon>
                  </a>
                </v-btn>
              </template>
              <span>View Map</span>
            </v-tooltip>
          </v-card>
          <v-card elevation="3" outlined class="pt-5 mb-4 pb-4 pa-4">
            <v-row no_gutter>
              <span v-for="(slot, index) in plot.plot_slots" :key="index">
                <v-col cols="12">
                  <v-hover>
                    <template v-slot:default="{ hover }">
                      <div
                        :class="`elevation-${hover ? 12 : 0}`"
                        class="mx-auto transition-swing"
                      >
                        <v-card
                          elevation="1"
                          height="100"
                          width="100"
                          :class="setSlotColor(slot.slot_status)"
                          @click="viewSlotDetail(slot, plot.id)"
                          style="border-width: inherit"
                        >
                          <v-row
                            class="fill-height"
                            :class="
                              slot.is_booked == true
                                ? 'text-black'
                                : 'text-white'
                            "
                            align="center"
                            justify="center"
                            style="font-size: 30px"
                          >
                            <span v-if="!slot.is_booked">
                              {{ slot.id }}
                            </span>
                            <span v-else>
                              <v-icon style="font-size: 60px">mdi-car</v-icon>
                            </span>
                          </v-row>
                        </v-card>
                      </div>
                    </template>
                  </v-hover>
                </v-col>
              </span>
            </v-row>
          </v-card>
        </div>
      </v-container>
      <div v-if="openSlotDetailDialog">
        <FixedSlotDetail
          v-model="openSlotDetailDialog"
          @addSlot="addSlot"
          :slot_id="slot_id"
          :is_full="is_full"
        />
      </div>
    </div>
    <div v-if="openAddSlotDialog">
      <SlotForm formType="Add" :fixed_slot="slot_id" :plot_id="plot_id" />
    </div>
  </div>
</template>

<script>
import { bus } from "@/main";
import FixedSlotDetail from "@/components/dashboard/FixedSlotDetail.vue";
import SlotForm from "@/components/slot/SlotForm.vue";

export default {
  name: "DashboardIndex",
  layout: "MainLayout",
  components: {
    FixedSlotDetail,
    SlotForm,
  },
  data() {
    return {
      search: null,
      slotList: [],
      openSlotDetailDialog: false,
      openAddSlotDialog: false,
      slot_id: null,
      plot_id: null,
      is_full: false,
    };
  },
  methods: {
    addSlot(value) {
      if (value) {
        this.openAddSlotDialog = true;
      }
    },
    setSlotColor(slot_status) {
      if (slot_status == "FULL_BOOKED_SLOT") {
        return "orange";
      } else if (slot_status == "PARTIAL_BOOKED_SLOT") {
        return "yellow";
      } else {
        return "blue";
      }
    },
    viewSlotDetail(slot, plot_id) {
      this.openSlotDetailDialog = true;
      this.slot_id = slot.id;
      this.plot_id = plot_id;
      if (slot.slot_status == "FULL_BOOKED_SLOT") {
        this.is_full = true;
      } else {
        this.is_full = false;
      }
    },
    getPlotList(params = {}) {
      this.$api.slot
        .getPlotList(params)
        .then((result) => {
          bus.$emit("showLoader", false);
          this.slotList = result.data;
        })
        .catch((err) => {
          console.error(err);
          bus.$emit("showLoader", false);
        });
    },
    searchPlot(searchClear = false) {
      if (searchClear) {
        this.search = null;
      }
      const plot_params = {
        search: this.search,
      };
      this.getPlotList(plot_params);
    },
  },
  mounted() {
    this.getPlotList();
  },
};
</script>

<style>
</style>