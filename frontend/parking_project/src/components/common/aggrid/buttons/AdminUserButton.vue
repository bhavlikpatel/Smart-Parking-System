<template>
  <div>
    <v-tooltip  v-if="admin_access" top>
      <template v-slot:activator="{ on, attrs }">
        <v-icon
          class="ma-0 mr-3 primary---text text-red"
          v-bind="attrs"
          v-on="on"
          @click="deleteUser()"
          >mdi-delete</v-icon
        >
      </template>
      <span class="text-capitalize">Delete Slot</span>
    </v-tooltip>
  </div>
</template>

<script>
export default {
  data() {
    return {
      admin_access: false,
    };
  },
  computed: {},
  methods: {
    viewSlot() {
      this.params.context.parentComponent.viewSlot(this.params.data.id);
    },
    deleteUser() {
      this.params.context.parentComponent.deleteAdminUser(this.params.data.id);
    },
  },
  mounted() {
    const user_detail = JSON.parse(localStorage.getItem("user_detail"));
    if (user_detail["user_type"] == "admin") {
      this.admin_access = true;
    }
  },
};
</script>
