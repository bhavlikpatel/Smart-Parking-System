// client
import SlotsIndex from "@/pages/client/slots/index.vue";
import SlotsCreate from "@/pages/admin/slots/create/index.vue";
import SlotDetailIndex from "@/pages/client/slots/detail/index.vue";
// Admin
import AdminSlotsIndex from "@/pages/admin/slots/index.vue";
const Slots = [ 
  // Client
  {
    path: "slots",
    component: SlotsIndex,
  },
  {
    path: "slots/create",
    component: SlotsCreate,
  },
  {
    path: "slots/detail/:id",
    component: SlotDetailIndex,
  },
  // Admin
  {
    path: "fixed_slots",
    component: AdminSlotsIndex,
  },
  {
    path: "slots/create",
    component: SlotsCreate,
  },
];

export default Slots;
