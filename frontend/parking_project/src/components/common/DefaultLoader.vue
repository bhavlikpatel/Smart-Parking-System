<template>
  <v-overlay :value="isLoader" z-index="1000">
    <v-progress-circular indeterminate size="64"></v-progress-circular>
  </v-overlay>
</template>

<script>
export default {
  props: {
    isLoader : Boolean
  },
  data() {
    return {};
  },
};
</script>