<template>
  <div>
    <v-row class="d-flex">
      <v-col cols="12" sm="6" class="pl-9 pt-6 d-flex align-center">
        <v-btn
          elevation="0"
          icon
          small
          class="mr-4"
          v-if="backRoute"
          @click="callBackRoute"
        >
          <v-icon color="primary">mdi-arrow-left-bold-circle</v-icon>
        </v-btn>
        <span class="text-h5 text-uppercase font-weight-bold">
          {{ title }}
        </span>
      </v-col>
      <v-col cols="12" sm="6" class="text-right pr-9 pt-6">
        <slot name="actions" />
      </v-col>
      <v-col cols="12" class="text-right">
        <slot name="content" />
      </v-col>
      <v-col cols="12" class="pa-0">
        <slot name="dialog" />
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: "BaseLayout",
  props: {
    title: {
      type: String,
      default: "Title",
      required: true,
    },
    permissions: {
      type: Boolean,
      default: true,
    },
    backRoute: {
      type: [String, Object],
    },
  },
  methods: {
    callBackRoute() {
      this.$router.back();
    },
  },
};
</script>
