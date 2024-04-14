import { errorHandler, responseHandler } from "@/utils/functions.js";

export default (axios) => ({
  register(payload) {
    return new Promise((resolve, reject) => {
      axios
        .post("register/", payload)
        .then((res) => {
          resolve(responseHandler(res));
        })
        .catch((err) => {
          reject(errorHandler(err));
        });
    });
  },
  login(payload) {
    return new Promise((resolve, reject) => {
      axios
        .post("login/", payload)
        .then((res) => {
          resolve(responseHandler(res));
        })
        .catch((err) => {
          reject(errorHandler(err));
        });
    });
  },
});
