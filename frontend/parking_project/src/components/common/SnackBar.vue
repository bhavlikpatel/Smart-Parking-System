<template>
  <v-snackbar
    v-bind="$attrs"
    v-on="$listeners"
    :color="color"
    :timeout="timeout"
    v-model="snackbar"
    class="text-capitalize"
  >
    {{ message }}
    <template v-slot:action="{ attrs }">
      <v-btn color="white" text v-bind="attrs" @click="snackbar = false">
        Close
      </v-btn>
    </template>
  </v-snackbar>
</template>

<script>
export default {
  name: "commonSnackbar",
  props: {
    value: Boolean,
    color: {
      type: String,
    },
    timeout: {
      type: Number,
      default: 1500,
    },
    message: {
      type: String,
      required: true,
    },
    hasActions: {
      type: Boolean,
      default: false,
    },
  },
  computed: {
    snackbar: {
      get() {
        return this.value;
      },
      set(val) {
        this.$emit("input", val);
      },
    },
  },
};
</script>