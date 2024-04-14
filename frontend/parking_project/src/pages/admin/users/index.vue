<template>
  <div>
    <BaseLayout title="Admin Users">
      <template #actions>
        <v-btn small depressed class="primary ma-2" @click="addUser()">
          <v-icon small class="mr-1">mdi-plus</v-icon>
          <span class="mr-2">Create User</span>
        </v-btn>
      </template>
      <template #content>
        <div class="px-6">
          <v-row no-gutters class="pb-2">
            <v-col cols="3" class="mr-3 d-flex">
              <v-text-field
                label="search Users"
                hide-details="auto"
                prepend-inner-icon="mdi-magnify"
                v-model="search"
                outlined
                dense
                clearable
                @keydown.enter="searchUser()"
                @click:clear="searchUser(true)"
              ></v-text-field>
            </v-col>
            <v-col cols="3">
              <ColumnsToShow
                :allHeaders="headers"
                :selectedHeaders="headersSelected"
                localStorageKey="admin_users_columns"
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
                :row-data="userList"
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
import AdminUserButton from "@/components/common/aggrid/buttons/AdminUserButton.vue";
import SlotDetails from "@/components/slot/SlotDetails.vue";

export default {
  name: "AdminUserIndex",
  layout: "MainLayout",
  components: {
    BaseLayout,
    AgGridVue,
    Pagination,
    ColumnsToShow,
    AdminUserButton,
    SlotDetails,
  },
  data() {
    return {
      search: null,
      userList: [],
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
          headerName: "Username",
          field: "username",
          pinned: "left",
          width: 270,
          minWidth: 250,
        },
        {
          headerName: "First Name",
          field: "first_name",
        },
        {
          headerName: "Last Name",
          field: "last_name",
        },
        {
          headerName: "Email",
          field: "email",
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
            cellRendererFramework: "AdminUserButton",
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
    deleteAdminUser(id) {
      if (confirm("Are you sure you want to delete this User?")) {
        this.$api.adminUser
          .deleteAdminUser(id)
          .then(() => {
            bus.$emit("showToastMessage", {
              message: "User Delete Successfully",
              color: "success",
            });
            this.getAdminUserList();
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
    addUser() {
      this.$router.push({
        path: "/app/admin/users/create",
      });
    },
    gridReady(params) {
      this.gridApi = params.api;
      this.columnApi = params.columnApi;
      this.gridOptions.api.sizeColumnsToFit();
    },
    headersChanged(value) {
      this.headersSelected = value;
      localStorage.setItem("admin_users_columns", JSON.stringify(value));
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
    getAdminUserList(params = {}) {
      params = {
        ...params,
        limit: this.itemsPerPage,
        offset: this.offset,
      };
      bus.$emit("showLoader", true);
      this.$api.adminUser
        .getAdminUserList(params)
        .then((result) => {
          bus.$emit("showLoader", false);
          this.userList = result.data.results;
          this.totalItems = result.data.count;
        })
        .catch((err) => {
          console.error(err);
          bus.$emit("showLoader", false);
        });
    },
    nextPage() {
      this.pageNo++;
      this.getAdminUserList();
    },
    prevPage() {
      this.pageNo--;
      this.getAdminUserList();
    },
    itemsPerPageChange(value) {
      this.pageNo = 1;
      this.itemsPerPage = value;
      this.getAdminUserList();
    },
    searchUser(searchClear = false) {
      if (searchClear) {
        this.search = null;
      }
      this.pageNo = 1;
      const user_params = {
        search: this.search,
      };
      this.getAdminUserList(user_params);
    },
  },
  mounted() {
    this.getAdminUserList();
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
