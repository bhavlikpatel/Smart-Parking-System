<template>
  <div>
    <v-tooltip top>
      <template v-slot:activator="{ on, attrs }">
        <v-icon
          class="ma-0 mr-3 primary---text text-primary"
          v-bind="attrs"
          v-on="on"
          @click="viewPlot()"
          >mdi-eye</v-icon
        >
      </template>
      <span class="text-capitalize">show details</span>
    </v-tooltip>
    <v-tooltip top>
      <template v-slot:activator="{ on, attrs }">
        <v-icon
          class="ma-0 mr-3 primary---text text-primary"
          v-bind="attrs"
          v-on="on"
          @click="editPlot()"
          >mdi-pencil</v-icon
        >
      </template>
      <span class="text-capitalize">Delete Plot</span>
    </v-tooltip>
    <v-tooltip top>
      <template v-slot:activator="{ on, attrs }">
        <v-icon
          class="ma-0 mr-3 primary---text text-red"
          v-bind="attrs"
          v-on="on"
          @click="deletePlot()"
          >mdi-delete</v-icon
        >
      </template>
      <span class="text-capitalize">Delete Plot</span>
    </v-tooltip>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
  computed: {},
  methods: {
    viewPlot() {
      this.params.context.parentComponent.viewPlot(this.params.data.id);
    },
    editPlot() {
      this.params.context.parentComponent.editPlot(this.params.data.id);
    },
    deletePlot() {
      this.params.context.parentComponent.deletePlot(this.params.data.id);
    },
  },
};
</script>
