import AdminDashboard from "@/pages/admin/dashboard/index.vue";
import Slots from "./admin/slots";
import Plots from "./admin/plots";
import AdminUser from "./admin/users";

export default [
  {
    path: "",
    redirect: "/app/admin/dashboard",
  },
  {
    path: "dashboard",
    component: AdminDashboard,
  },
  ...Slots,
  ...Plots,
  ...AdminUser,
  
];
