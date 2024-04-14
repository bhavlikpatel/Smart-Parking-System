<template>
  <NuxtChild />
</template>

<script>
export default {
  mounted() {
    if (this.$route.path == "/app/client" || this.$route.path == "/app/client/") {
      this.$router.push({ path: "/app/client/dashboard" });
    }
  },
};
</script>

<style>
</style>