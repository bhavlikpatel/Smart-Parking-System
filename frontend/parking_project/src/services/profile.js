import { user } from "@/utils/constants";
import { errorHandler, responseHandler } from "@/utils/functions";

export default (axios) => ({
  getProfileDetail(id) {
    return new Promise((resolve, reject) => {
      axios
        .get(`${user.userBase}${id}/`)
        .then((res) => {
          resolve(responseHandler(res));
        })
        .catch((err) => {
          reject(errorHandler(err));
        });
    });
  },
});
