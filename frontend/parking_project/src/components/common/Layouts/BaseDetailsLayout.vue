<template>
  <div class="d-flex h-100">
    <div
      :elevation="boxShadow"
      class="pa-0 w-100 d-flex flex-column"
      :class="overClass"
    >
      <div
        class="
          text-lg-subtitle-1 text-xl-h6 text-uppercase
          font-weight-black
          d-flex
          align-center
          primary--text
          pt-5
          pb-3
          px-4
        "
        v-if="['string', 'object'].indexOf(typeof backRoute) > -1"
      >
        <v-btn icon color="primary" class="mr-3" @click="callBackRoute">
          <v-icon color="primary"> mdi-arrow-left-bold-circle </v-icon>
        </v-btn>
        <span class="text-h5 font-weight-bold">{{ title }}</span>
      </div>
      <div class="px-0 pt-2 pb-0 h-100" :class="overClass">
        <slot name="formContent" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "BaseDetailsLayout",
  props: {
    backRoute: {
      type: [String, Object],
    },
    title: {
      required: true,
      type: String,
    },
    overClass: {
      default: "",
      type: String,
    },
    boxShadow: {
      type: String,
    },
  },
  methods: {
    callBackRoute() {
      this.$router.back()
    },
  },
};
</script>