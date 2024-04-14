<template>
  <v-menu
    v-model="menu"
    :close-on-content-click="false"
    :nudge-right="40"
    transition="scale-transition"
    offset-y
    @click="menu != menu"
    @change="$emit('change')"
    min-width="auto"
  >
    <template v-slot:activator="{ on, attrs }">
      <v-text-field
        v-model="time"
        :label="label"
        append-icon="mdi-clock"
        readonly
        v-bind="{ ...attrs, ...$attrs }"
        v-on="{ ...on, $listeners }"
        v-on:click:append="menu = true"
      ></v-text-field>
    </template>
    <v-time-picker
      v-model="time"
      format="24hr"
      scrollable
      v-bind="$attrs"
      v-on="$listeners"
      @click:minute="menu = false"
    ></v-time-picker>
  </v-menu>
</template>

<script>
export default {
  data() {
    return {
      menu: false,
    };
  },
  props: {
    label: {
      type: String,
    },
    value: {
      required: true,
    },
  },
  computed: {
    time: {
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

<style>
</style>