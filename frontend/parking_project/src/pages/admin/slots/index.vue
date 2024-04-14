<template>
  <div>
    <BaseLayout title="Parking Slots">
      <template #actions>
        <v-btn small depressed class="primary ma-2" @click="addSlot()">
          <v-icon small class="mr-1">mdi-plus</v-icon>
          <span class="mr-2">add slot</span>
        </v-btn>
      </template>
      <template #content>
        <div class="px-6">
          <v-row no-gutters class="pb-2">
            <v-col cols="3" class="mr-3 d-flex">
              <v-text-field
                label="search slots"
                hide-details="auto"
                prepend-inner-icon="mdi-magnify"
                v-model="search"
                outlined
                dense
                clearable
                @keydown.enter="searchSlot()"
                @click:clear="searchSlot(true)"
              ></v-text-field>
            </v-col>
            <v-col cols="3">
              <ColumnsToShow
                :allHeaders="headers"
                :selectedHeaders="headersSelected"
                localStorageKey="fixed_slots_columns"
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
                :row-data="slotList"
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
    <SlotDetails v-model="hasSlotDetails" :SlotID="selectSlotId" />
  </div>
</template>

<script>
/* eslint-disable vue/no-unused-components */
import BaseLayout from "@/components/common/Layouts/BaseLayout.vue";
import { bus } from "@/main";
import { AgGridVue } from "ag-grid-vue";
import Pagination from "@/components/common/Pagination.vue";
import ColumnsToShow from "@/components/common/aggrid/ColumnsToShow.vue";
import SlotButton from "@/components/common/aggrid/buttons/SlotButton.vue";
import SlotDetails from "@/components/slot/SlotDetails.vue";

export default {
  name: "SlotIndex",
  layout: "MainLayout",
  components: {
    BaseLayout,
    AgGridVue,
    Pagination,
    ColumnsToShow,
    SlotButton,
    SlotDetails,
  },
  data() {
    return {
      search: null,
      slotList: [],
      //   Aggrid data
      headersSelected: [],
      hasSlotDetails: false,
      selectSlotId: null,
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
          headerName: "Slot ID",
          field: "id",
          pinned: "left",
          width: 270,
          minWidth: 250,
        },
        {
          headerName: "Plot ID",
          field: "plot_id",
        },
        {
          headerName: "Plot Name",
          field: "plot_name",
        },
        {
          headerName: "Slot Status",
          field: "slot_status",
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
            cellRendererFramework: "SlotButton",
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
    viewSlot(id) {
      this.$router.push({
        path: `/app/admin/slots/detail/${id}`,
      });
    },
    deleteSlot(id) {
      if (confirm("Are you sure you want to delete this Plot?")) {
        this.$api.adminSlot
          .deleteSlot(id)
          .then(() => {
            bus.$emit("showToastMessage", {
              message: "Slot Delete Successfully",
              color: "success",
            });
            this.getAdminFixedSlotList();
          })
          .catch(() => {
            bus.$emit("showToastMessage", {
              message: "can't fetch data",
              color: "error",
            });
          });
      }
    },
    getSlotDetails(id) {
      this.$api.adminSlot
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
    addSlot() {
      this.$router.push({
        path: "/app/admin/slots/create",
      });
    },
    gridReady(params) {
      this.gridApi = params.api;
      this.columnApi = params.columnApi;
      this.gridOptions.api.sizeColumnsToFit();
    },
    headersChanged(value) {
      this.headersSelected = value;
      localStorage.setItem("fixed_slots_columns", JSON.stringify(value));
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
    getAdminFixedSlotList(params = {}) {
      params = {
        ...params,
        limit: this.itemsPerPage,
        offset: this.offset,
      };
      bus.$emit("showLoader", true);
      this.$api.adminSlot
        .getAdminFixedSlotList(params)
        .then((result) => {
          bus.$emit("showLoader", false);
          this.slotList = result.data.results;
          this.totalItems = result.data.count;
        })
        .catch((err) => {
          console.error(err);
          bus.$emit("showLoader", false);
        });
    },
    nextPage() {
      this.pageNo++;
      this.getAdminFixedSlotList();
    },
    prevPage() {
      this.pageNo--;
      this.getAdminFixedSlotList();
    },
    itemsPerPageChange(value) {
      this.pageNo = 1;
      this.itemsPerPage = value;
      this.getAdminFixedSlotList();
    },
    searchSlot(searchClear = false) {
      if (searchClear) {
        this.search = null;
      }
      this.pageNo = 1;
      const driver_params = {
        search: this.search,
      };
      this.getAdminFixedSlotList(driver_params);
    },
  },
  mounted() {
    this.getAdminFixedSlotList();
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
