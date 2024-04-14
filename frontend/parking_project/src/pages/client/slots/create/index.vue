<template>
<SlotForm formType="Add" />
</template>
<script>
import SlotForm  from '@/components/slot/SlotForm.vue'
export default {
  name: "slotsCreate",
  components : {
    SlotForm
  }
  
}
</script>