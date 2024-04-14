<template>
  <v-card :elevation="boxShadow" :class="overClass" style="position: relative">
    <v-card-title
      class="
        line-box-shadow
        text-lg-subtitle-1 text-xl-h6 text-uppercase
        font-weight-black
        primary--text
        pb-4
        position-sticky
      "
    >
      <v-row class="d-flex align-center">
        <v-col cols="5" class="d-flex align-center">
          <v-btn
            v-if="['string', 'object'].indexOf(typeof backRoute) > -1"
            icon
            color="primary"
            class="mr-3"
            @click="callBackRoute"
          >
            <v-icon>mdi-arrow-left-bold-circle </v-icon>
          </v-btn>
          <span class="text-h5 font-weight-bold">{{ title }}</span>
        </v-col>
        <v-col cols="7" class="text-right">
          <slot name="formActions" />
        </v-col>
      </v-row>
    </v-card-title>
    <v-card-text
      class="d-flex flex-column pa-0"
      :class="overClass"
      ref="vehicleSectionForm"
    >
      <v-alert v-if="nonFieldError.length" dense type="error">
        <v-list
          class="pa-0"
          dense
          style="background: inherit !important"
          v-for="(error, i) in nonFieldError"
          :key="i"
        >
          <v-list-item dense style="min-height: 20px !important">
            <span>{{ i }} .</span><span>{{ error }}</span>
          </v-list-item>
        </v-list>
      </v-alert>
      <slot name="formContent" />
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "BaseFormLayout",
  props: {
    backRoute: {
      type: [String, Object],
    },
    title: {
      required: true,
      type: String,
    },
    nonFieldError: {
      required: true,
      type: Array,
      default: () => [],
    },
    overClass: {
      default: "",
      type: String,
    },
    boxShadow: {
      type: String,
      default: "0",
    },
  },
  methods: {
    callBackRoute() {
      this.$router.back()
    },
  },
};
</script>

<style scoped lang="scss">
.position-sticky {
  position: sticky !important;
  top: 64px;
  background-color: white;
  z-index: 2;
}
.line-box-shadow {
  -webkit-box-shadow: 0px 0px 5px 0px rgba(0, 0, 0, 0.19);
  -moz-box-shadow: 0px 0px 5px 0px rgba(0, 0, 0, 0.19);
  box-shadow: 0px 0px 5px 0px rgba(0, 0, 0, 0.19);
}
</style>
