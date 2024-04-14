// client
import AdminUserIndex from "@/pages/admin/users/index.vue";
import AdminUserCreate from "@/pages/admin/users/create/index.vue";
// import SlotDetailIndex from "@/pages/client/slots/detail/index.vue";
const AdminUser = [
  {
    path: "users",
    component: AdminUserIndex,
  },
  {
    path: "users/create",
    component: AdminUserCreate,
  },
];

export default AdminUser;
