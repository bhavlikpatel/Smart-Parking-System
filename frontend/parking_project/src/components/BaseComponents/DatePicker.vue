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
        v-model="date"
        :label="label"
        append-icon="mdi-calendar"
        readonly
        v-bind="{ ...attrs, ...$attrs }"
        v-on="{ ...on, $listeners }"
        v-on:click:append="menu=true"
      ></v-text-field>
    </template>
    <v-date-picker
      v-model="date"
      :type="type"
      v-bind="$attrs"
      v-on="$listeners"
      @input="menu = false"
    ></v-date-picker>
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
    type: {
      type: String,
    },

  },
  computed: {
    date: {
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