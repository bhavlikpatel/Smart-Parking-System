import { admin } from "@/utils/constants";
import { errorHandler, responseHandler } from "@/utils/functions";

export default (axios) => ({
  getAdminUserList(params = {}) {
    return new Promise((resolve, reject) => {
      axios
        .get(`${admin.adminBase}users/`, {
          params: params,
        })
        .then((res) => {
          resolve(responseHandler(res));
        })
        .catch((err) => {
          reject(errorHandler(err));
        });
    });
  },
  createAdminUser(data) {
    return new Promise((resolve, reject) => {
      axios
        .post(`${admin.adminBase}users/`, data)
        .then((res) => {
          resolve(responseHandler(res));
        })
        .catch((err) => {
          reject(errorHandler(err));
        });
    });
  },
  deleteAdminUser(id) {
    return new Promise((resolve, reject) => {
      axios
        .delete(`${admin.adminBase}users/${id}/`)
        .then((res) => {
          resolve(responseHandler(res));
        })
        .catch((err) => {
          reject(errorHandler(err));
        });
    });
  },
});
