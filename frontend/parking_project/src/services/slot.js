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
  getFixedSlotList(params = {}) {
    return new Promise((resolve, reject) => {
      axios
        .get(slot.fixedSlotBase, {
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
  getSlotList(params = {}) {
    return new Promise((resolve, reject) => {
      axios
        .get(slot.slotBase, {
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
  getTimeWindows(params) {
    return new Promise((resolve, reject) => {
      axios
        .get(`${slot.slotBase}${params["slot_id"]}/get_booked_slot_detail/`, {
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
  getPaymentDetail(params) {
    return new Promise((resolve, reject) => {
      axios
        .get(`${slot.slotBase}get_payment_from_time_windows/`, {
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
  addSlot(data) {
    return new Promise((resolve, reject) => {
      axios
        .post(`${slot.slotBase}`, data)
        .then((res) => {
          resolve(responseHandler(res));
        })
        .catch((err) => {
          reject(errorHandler(err));
        });
    });
  },
});
