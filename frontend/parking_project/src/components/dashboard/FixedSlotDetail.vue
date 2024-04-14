<template>
  <div>
    <v-dialog max-width="800px" v-model="openSlotDetailDialog">
      <v-card>
        <v-row class="pa-6">
          <v-col cols="8">Booked Slot Detail(Time Window)</v-col>
          <v-col>
            <v-btn
              v-show="!is_full"
              class="primary"
              @click="closeSlotDialog(true)"
            >
              <v-icon>+</v-icon>
              <span class="pl-2">Book Slot</span>
            </v-btn>
          </v-col>
          <v-col>
            <v-btn class="primary" @click="closeSlotDialog(false)">
              <v-icon>mdi-close</v-icon>
            </v-btn>
          </v-col>
        </v-row>
        <v-simple-table class="px-4" fixed-header height="300px" width="auto">
          <thead>
            <tr>
              <th class="text-left">SR No.</th>
              <th class="text-left">Slot No</th>
              <th class="text-left">From Time</th>
              <th class="text-left">To Time</th>
              <th class="text-left">Amount</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(slot, i) in slotObject" :key="i">
              <td>{{ i + 1 }}</td>
              <td>{{ slot.fixed_slot }}</td>
              <td>{{ slot.from_time }}</td>
              <td>{{ slot.to_time }}</td>
              <td>{{ slot.amount }}</td>
            </tr>
          </tbody>
        </v-simple-table>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { bus } from "@/main";

export default {
  name: "FixedSlotDetail",
  props: {
    slot_id: {
      type: [Number, String],
      required: true,
    },
    is_full: {
      type: [Boolean],
      required: true,
    },
    value: Boolean,
  },
  data() {
    return {
      slotObject: [],
      openAddSlotDialog: false,
    };
  },
  computed: {
    openSlotDetailDialog: {
      get() {
        return this.value;
      },
      set(value) {
        this.$emit("input", value);
      },
    },
  },
  methods: {
    closeSlotDialog(add_slot) {
      if (add_slot) {
        this.openAddSlotDialog = true;
        this.$emit("addSlot", this.openAddSlotDialog);
      } else {
        this.openSlotDetailDialog = false;
        this.$emit("addSlot", false);
      }
    },
    getSlotDetail() {
      this.$api.slot
        .getSlotDetail(this.slot_id)
        .then((result) => {
          bus.$emit("showLoader", false);
          this.slotObject = result.data;
        })
        .catch((err) => {
          console.error(err);
          bus.$emit("showLoader", false);
        });
    },
  },
  mounted() {
    this.getSlotDetail();
  },
};
</script>

<style scoped>
</style>