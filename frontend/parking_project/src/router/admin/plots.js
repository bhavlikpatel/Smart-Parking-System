import PlotsIndex from "@/pages/admin/plots/index.vue";
import PlotsCreate from "@/pages/admin/plots/create/index.vue";
import PlotsEdit from "@/pages/admin/plots/edit/_id/index.vue";
import PlotDetailIndex from "@/pages/admin/plots/detail/index.vue";

const Plots = [ 
  {
    path: "plots",
    component: PlotsIndex,
  },
  {
    path: "plots/create",
    component: PlotsCreate,
  },
  {
    path: "plots/edit/:id",
    component: PlotsEdit
  },
  {
    path: "plots/detail/:id",
    component: PlotDetailIndex,
  },
];

export default Plots;
