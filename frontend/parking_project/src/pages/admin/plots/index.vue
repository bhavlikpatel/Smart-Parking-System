<template>
  <div>
    <BaseLayout title="Parking Plot">
      <template #actions>
        <v-btn small depressed class="primary ma-2" @click="addPlot()">
          <v-icon small class="mr-1">mdi-plus</v-icon>
          <span class="mr-2">add plot</span>
        </v-btn>
      </template>
      <template #content>
        <div class="px-6">
          <v-row no-gutters class="pb-2">
            <v-col cols="3" class="mr-3 d-flex">
              <v-text-field
                label="search plots"
                hide-details="auto"
                prepend-inner-icon="mdi-magnify"
                v-model="search"
                outlined
                dense
                clearable
                @keydown.enter="searchPlot()"
                @click:clear="searchPlot(true)"
              ></v-text-field>
            </v-col>
            <v-col cols="3">
              <ColumnsToShow
                :allHeaders="headers"
                :selectedHeaders="headersSelected"
                localStorageKey="plots_columns"
                itemText="headerName"
                itemValue="field"
                @headers-changed="headersChanged"
              />
            </v-col>
          </v-row>
          <v-row no-gutters>
            <v-col cols="12" class="pt-4">
              <AgGridVue
                @grid-ready="gridReady"
                :context="context"
                :grid-options="gridOptions"
                :column-defs="headersForTable"
                :default-col-def="defaultColDef"
                :row-data="plotList"
                class="ag-theme-material app-table"
              >
              </AgGridVue>
            </v-col>
            <v-col cols="12" class="pt-3 d-flex justify-end">
              <Pagination
                :page-no="pageNo"
                :num-of-pages="totalPages"
                :page-size="itemsPerPage"
                @nextPage="nextPage"
                @prevPage="prevPage"
                @itemsPerPageChange="itemsPerPageChange"
              />
            </v-col>
          </v-row>
        </div>
      </template>
    </BaseLayout>
    <SlotDetails v-model="hasPlotDetails" :SlotID="selectPlotId" />
  </div>
</template>

<script>
/* eslint-disable vue/no-unused-components */
import BaseLayout from "@/components/common/Layouts/BaseLayout.vue";
import { bus } from "@/main";
import { AgGridVue } from "ag-grid-vue";
import Pagination from "@/components/common/Pagination.vue";
import ColumnsToShow from "@/components/common/aggrid/ColumnsToShow.vue";
import PlotButton from "@/components/common/aggrid/buttons/PlotButton.vue";
import SlotDetails from "@/components/slot/SlotDetails.vue";

export default {
  name: "SlotIndex",
  layout: "MainLayout",
  components: {
    BaseLayout,
    AgGridVue,
    Pagination,
    ColumnsToShow,
    PlotButton,
    SlotDetails,
  },
  data() {
    return {
      search: null,
      plotList: [],
      //   Aggrid data
      headersSelected: [],
      hasPlotDetails: false,
      selectPlotId: null,
      totalItems: 0,
      itemsPerPage: 10,
      pageNo: 1,
      defaultColDef: {
        lockPosition: true,
        resizable: true,
      },
      gridOptions: {
        onGridSizeChanged: () => {
          this.gridOptions.api.sizeColumnsToFit();
        },
        headerHeight: 40,
        rowHeight: 40,
      },
      headers: [
        {
          headerName: "Plot ID",
          field: "plot_id",
          pinned: "left",
          width: 270,
          minWidth: 250,
        },
        {
          headerName: "Plot Name",
          field: "plot_name",
        },
        {
          headerName: "City",
          field: "city",
        },
        {
          headerName: "Plot Address",
          field: "plot_address",
        },
      ],
    };
  },
  computed: {
    context() {
      return { parentComponent: this };
    },
    headersForTable() {
      return [
        ...this.headersSelected,
        ...[
          {
            headerName: "actions",
            width: 270,
            minWidth: 270,
            field: "actions",
            pinned: "right",
            hide: false,
            cellRendererFramework: "PlotButton",
          },
        ],
      ];
    },
    totalPages() {
      return Math.ceil(this.totalItems / this.itemsPerPage);
    },
    offset() {
      return this.itemsPerPage * (this.pageNo - 1);
    },
  },
  methods: {
    viewPlot(id) {
      this.$router.push({
        path: `/app/admin/plots/detail/${id}`,
      });
    },
    deletePlot(id) {
      if (confirm("Are you sure you want to delete this Plot?")) {
        this.$api.plot
          .deletePlot(id)
          .then((response) => {
            bus.$emit("showToastMessage", {
              message: response.data.message,
              color: "success",
            });
            this.getPlotList();
          })
          .catch(() => {
            bus.$emit("showToastMessage", {
              message: "can't fetch data",
              color: "error",
            });
          });
      }
    },
    editPlot(id) {
      this.$router.push({
        path: `/app/admin/plots/edit/${id}`,
      });
    },
    getSlotDetails(id) {
      this.$api.slot
        .getSlotDetail(id)
        .then((response) => {
          this.addressDetails = response.data;
        })
        .catch(() => {
          bus.$emit("showToastMessage", {
            message: "can't fetch data",
            color: "error",
          });
        });
    },
    addPlot() {
      this.$router.push({
        path: "/app/admin/plots/create",
      });
    },
    gridReady(params) {
      this.gridApi = params.api;
      this.columnApi = params.columnApi;
      this.gridOptions.api.sizeColumnsToFit();
    },
    headersChanged(value) {
      this.headersSelected = value;
      localStorage.setItem("plots_columns", JSON.stringify(value));
      setTimeout(() => {
        this.gridOptions.api.sizeColumnsToFit();
      }, 100);
    },
    autoSizeAll() {
      let allColumnIds = [];
      this.gridOptions.columnApi.getColumns().forEach(function (column) {
        allColumnIds.push(column.colId);
      });
      this.gridOptions.columnApi.autoSizeColumns(allColumnIds);
    },
    getPlotList(params = {}) {
      params = {
        ...params,
        limit: this.itemsPerPage,
        offset: this.offset,
      };
      bus.$emit("showLoader", true);
      this.$api.plot
        .getPlotList(params)
        .then((result) => {
          bus.$emit("showLoader", false);
          this.plotList = result.data.results;
          this.totalItems = result.data.count;
        })
        .catch((err) => {
          console.error(err);
          bus.$emit("showLoader", false);
        });
    },
    nextPage() {
      this.pageNo++;
      this.getPlotList();
    },
    prevPage() {
      this.pageNo--;
      this.getPlotList();
    },
    itemsPerPageChange(value) {
      this.pageNo = 1;
      this.itemsPerPage = value;
      this.getPlotList();
    },
    searchPlot(searchClear = false) {
      if (searchClear) {
        this.search = null;
      }
      this.pageNo = 1;
      const driver_params = {
        search: this.search,
      };
      this.getPlotList(driver_params);
    },
  },
  mounted() {
    this.getPlotList();
  },
};
</script>

<style>
.ag-theme-material .ag-ltr .ag-cell {
  display: flex;
  justify: center;
}
.ag-theme-material .ag-ltr .ag-cell {
  text-align: left;
}
</style>
