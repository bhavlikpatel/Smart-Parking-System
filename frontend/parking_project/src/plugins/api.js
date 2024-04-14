import axiosInstance from "./axios";
import auth from "../services/auth";
import slot from "../services/slot";
import profile from "../services/profile";

// Admin Services
import adminDashBoard from "../services/admin/adminDashBoard";
import adminSlot from "../services/admin/adminSlot";
import adminUser from "../services/admin/adminUser";
import plot from "../services/admin/plot";

export default {
  auth: auth(axiosInstance),
  profile: profile(axiosInstance),
  slot: slot(axiosInstance),
  

  // Admin
  adminSlot: adminSlot(axiosInstance),
  adminDashBoard: adminDashBoard(axiosInstance),
  plot: plot(axiosInstance),
  adminUser: adminUser(axiosInstance),
  
};
