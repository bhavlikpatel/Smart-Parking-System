<template>
  <BaseDetailsLayout
    title="slot details"
    :backRoute="backRoute"
    overClass="px-0"
    boxShadow="0"
  >
    <template #formContent>
      <div>
        <v-card class="pa-4 mx-5" elevation="0" tile>
          <v-row class="d-flex justify-center">
            <v-col cols="12">
              <v-simple-table class="px-4" style="border: 1px solid grey">
                <tbody>
                  <tr>
                    <th class="text-left">Plot Name</th>
                    <td>{{ plotDetails.plot_name }}</td>
                  </tr>
                  <tr>
                    <th class="text-left">Plot Id</th>
                    <td>{{ plotDetails.plot_id }}</td>
                  </tr>
                  <tr>
                    <th class="text-left">City</th>
                    <td>{{ plotDetails.city }}</td>
                  </tr>
                  <tr>
                    <th class="text-left">Address</th>
                    <td>{{ plotDetails.plot_address }}</td>
                  </tr>
                </tbody>
              </v-simple-table>
            </v-col>
          </v-row>
        </v-card>
      </div>      
    </template>
  </BaseDetailsLayout>
</template>

<script>
import BaseDetailsLayout from "@/components/common/Layouts/BaseDetailsLayout.vue";
import { bus } from "@/main";

export default {
  layout: "MainLayout",
  name: "SlotDetailIndex",
  components: {
    BaseDetailsLayout,
  },
  data() {
    return {
      plotDetails: {},
      height: null,
      scrollInvoked: 0,

      backRoute: { path: "/app/admin/plots" },
    };
  },
  methods: {
    onScroll() {
      this.scrollInvoked++;
    },
    getplotDetails(id) {
      this.$api.plot
        .getPlotObject(id)
        .then((result) => {
          this.plotDetails = result.data;
        })
        .catch((err) => {
          console.log(err);
          bus.$emit("showToastMessage", {
            message: "Couln't fetch data",
            color: "error",
          });
        });
    },
  },
  mounted() {
    if ("id" in this.$route.params) {
      this.getplotDetails(this.$route.params.id);
    }
  },
};
</script>
