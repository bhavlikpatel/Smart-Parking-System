<template>
  <NuxtChild />
</template>

<script>
export default {
  name:"AdminIndex",
  mounted() {
    if (this.$route.path == "/app/admin" || this.$route.path == "/app/admin/") {
      this.$router.push({ path: "/app/admin/dashboard" });
    }
  },
};
</script>

<style>
</style>