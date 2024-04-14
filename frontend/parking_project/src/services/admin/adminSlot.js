import { slot } from "@/utils/constants";
import { errorHandler, responseHandler } from "@/utils/functions";

export default (axios) => ({
  getPlotList(params = {}) {
    return new Promise((resolve, reject) => {
      axios
        .get(slot.plotBase, {
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
  getSlotDetail(id) {
    return new Promise((resolve, reject) => {
      axios
        .get(`${slot.slotBase}${id}/get_booked_slot_detail/`)
        .then((res) => {
          resolve(responseHandler(res));
        })
        .catch((err) => {
          reject(errorHandler(err));
        });
    });
  },
  getSlotObj(id) {
    return new Promise((resolve, reject) => {
      axios
        .get(`${slot.slotBase}${id}/`)
        .then((res) => {
          resolve(responseHandler(res));
        })
        .catch((err) => {
          reject(errorHandler(err));
        });
    });
  },
  adminAddSlots(data) {
    return new Promise((resolve, reject) => {
      axios
        .post(`${slot.adminSlotBase}create_fixed_slots/`, data)
        .then((res) => {
          resolve(responseHandler(res));
        })
        .catch((err) => {
          reject(errorHandler(err));
        });
    });
  },
  getAdminFixedSlotList(params = {}) {
    return new Promise((resolve, reject) => {
      axios
        .get(`${slot.adminSlotBase}fixed_slots/`, {
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
  deleteSlot(id) {
    return new Promise((resolve, reject) => {
      axios
        .delete(`${slot.adminSlotBase}fixed_slots/${id}/`)
        .then((res) => {
          resolve(responseHandler(res));
        })
        .catch((err) => {
          reject(errorHandler(err));
        });
    });
},
});
