import AdminDashboard from "@/pages/client/dashboard/index.vue";
import Slots from "./slots";

export default [
  {
    path: "",
    redirect: "/app/client/dashboard",
  },
  {
    path: "dashboard",
    component: AdminDashboard,
  },
  ...Slots,
  
];
