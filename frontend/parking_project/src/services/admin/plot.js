import { plot } from "@/utils/constants";
import { errorHandler, responseHandler } from "@/utils/functions";

export default (axios) => ({
  getPlotList(params = {}) {
    return new Promise((resolve, reject) => {
      axios
        .get(plot.plotBase, {
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
  addPlot(data) {
    return new Promise((resolve, reject) => {
      axios
        .post(`${plot.plotBase}`, data)
        .then((res) => {
          resolve(responseHandler(res));
        })
        .catch((err) => {
          reject(errorHandler(err));
        });
    });
  },
  updatePlot(payload) {
    return new Promise((resolve, reject) => {
      axios
        .put(`${plot.plotBase}${payload.id}/`, payload)
        .then((res) => {
          resolve(responseHandler(res));
        })
        .catch((err) => {
          reject(errorHandler(err));
        });
    });
  },
  getPlotObject(id) {
    return new Promise((resolve, reject) => {
      axios
        .get(`${plot.plotBase}${id}/`)
        .then((res) => {
          resolve(responseHandler(res));
        })
        .catch((err) => {
          reject(errorHandler(err));
        });
    });
  },
  deletePlot(id) {
      return new Promise((resolve, reject) => {
        axios
          .delete(`${plot.plotBase}${id}/delete_plot/`)
          .then((res) => {
            resolve(responseHandler(res));
          })
          .catch((err) => {
            reject(errorHandler(err));
          });
      });
  },
});
