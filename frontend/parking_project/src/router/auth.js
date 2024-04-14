import Default from "@/layouts/Default.vue";
import RegisterIndex from "@/pages/register/index.vue";
import LoginIndex from "@/pages/login/index.vue";
import AdminRoutes from "@/router/admin.js";
import ClientRoutes from "@/router/client.js";
import MainLayout from "@/layouts/MainLayout.vue";

export default [
  {
    path: "/",
    redirect: "/app",
  },
  {
    path: "/app",
    component: Default,
    children: [
      {
        path: "register",
        name: "register",
        component: RegisterIndex,
      },
      {
        path: "login",
        name: "login",
        component: LoginIndex,
      },
      {
        path: "client",
        name: "client",
        component: MainLayout,
        children: ClientRoutes,
      },
      {
        path: "admin",
        name: "admin",
        component: MainLayout,
        children: AdminRoutes,
      },
    ],
  },
  {
    path: "**",
    redirect: "/app",
  },
];
