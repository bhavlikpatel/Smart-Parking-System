import axios from "axios";
// import { selectedBranch } from "@/utils/functions.js";

function authHeader() {
  let user = localStorage.getItem("user");
  if (user) {
    return `token ${user}`;
  } else {
    return "";
  }
}

const axiosInstance = axios.create({
  baseURL: process.env.VUE_APP_BASE_URL,
});

axiosInstance.interceptors.request.use((config) => {
  let head = authHeader();
  // let branch = selectedBranch();
  if (head) {
    config.headers.Authorization = head;
  }
  config.params = { ...config.params };
  return config;
});

export default axiosInstance;
