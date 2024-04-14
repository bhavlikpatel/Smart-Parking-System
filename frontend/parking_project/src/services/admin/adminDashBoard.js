import { dashboard } from "@/utils/constants";
import { errorHandler, responseHandler } from "@/utils/functions";

export default (axios) => ({
  getScoreBoard(params) {
    return new Promise((resolve, reject) => {
      axios
        .get(`${dashboard.adminDashboardBase}scoreboard/`,
        {
          params: params
        })
        .then((res) => {
          resolve(responseHandler(res));
        })
        .catch((err) => {
          reject(errorHandler(err));
        });
    });
  },
  getSlotUtilization(params) {
    return new Promise((resolve, reject) => {
      axios
        .get(`${dashboard.adminDashboardBase}slots_booking_chart/`,{
          params: params
        })
        .then((res) => {
          resolve(responseHandler(res));
        })
        .catch((err) => {
          reject(errorHandler(err));
        });
    });
  },
  });
