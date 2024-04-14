export function responseHandler(res) {
  let obj = {};
  if (res.data && typeof res.data == typeof {}) {
    obj.data = res.data;
    if (res.data.data) {
      obj.data = res.data.data;
    }
    if (res.data.count) {
      obj.count = res.data.count;
    }
  } else {
    obj = res;
  }
  return obj;
}

export function errorHandler(err) {
  console.error(err);
  let obj = {};
  if (err.response.data) {
    obj.data = err.response.data;
    if (obj.data.error) {
      obj.data = err.response.data.error;
    }
  }
  obj.status = err.response.status;
  return obj;
}

export function orderStatusDarkColor(status) {
  switch (status) {
    case "open_transaction":
      return "open_transaction";
    case "unassigned":
      return "unassigned";
    case "assigned":
      return "assigned";
    case "pickedup":
      return "pickedup";
    case "picked up":
      return "pickedup";
    case "not_pickedup":
      return "not_pickedup";
    case "partially_delivered":
      return "partially_delivered";
    case "partially delivered":
      return "partially_delivered";
    case "enroute":
      return "enroute";
    case "out for delivery":
      return "enroute";
    case "on_hold":
      return "on_hold";
    case "returned":
      return "returned";
    case "cancelled":
      return "cancelled";
    case "delivered":
      return "delivered";
    case "not_delivered":
      return "not_delivered";
    case "not delivered":
      return "not_delivered";
  }
}

export function orderStatusLightColor(status) {
  switch (status) {
    case "open_transaction":
      return "light_open_transaction";
    case "unassigned":
      return "light_unassigned";
    case "assigned":
      return "light_assigned";
    case "pickedup":
      return "light_pickedup";
    case "not_pickedup":
      return "light_not_pickedup";
    case "partially_delivered":
      return "light_partially_delivered";
    case "on_hold":
      return "light_on_hold";
    case "out for delivery":
      return "light_enroute";
    case "enroute":
      return "light_enroute";
    case "returned":
      return "light_returned";
    case "cancelled":
      return "light_cancelled";
    case "delivered":
      return "light_delivered";
    case "not_delivered":
      return "light_failed";
  }
}

export function tripStatusDarkColor(status) {
  switch (status) {
    case "loading":
      return "trip_loading";
    case "scheduled":
      return "unassigned";
    case "active":
      return "trip_active";
    case "paused":
      return "pickedup";
    case "cancelled":
      return "cancelled";
    case "completed":
      return "delivered";
  }
}

export function tripStatusLightColor(status) {
  switch (status) {
    case "loading":
      return "light_trip_loading";
    case "scheduled":
      return "light_unassigned";
    case "active":
      return "light_trip_active";
    case "paused":
      return "light_pickedup";
    case "cancelled":
      return "light_cancelled";
    case "completed":
      return "light_delivered";
  }
}

export function orderTextChange(orderStatus) {
  switch (orderStatus) {
    case "open_transaction":
      return "Open Transaction";
    case "unassigned":
      return "Unassigned";
    case "assigned":
      return "Assigned";
    case "pickedup":
      return "Pickedup";
    case "partially_delivered":
      return "Partially Delivered";
    case "out for delivery":
      return "Out For delivery";
    case "enroute":
      return "Out For delivery";
    case "on_hold":
      return "On Hold";
    case "returned":
      return "Returned";
    case "cancelled":
      return "Cancelled";
    case "delivered":
      return "Delivered";
    case "not delivered":
      return "Not delivered";
    case "not_delivered":
      return "Not delivered";
    case "not_pickedup":
      return "Not Pickedup";
  }
}

export function generateUrl(file) {
  return URL.createObjectURL(file);
}
export function getSize(bytes) {
  var sizes = ["Bytes", "KB", "MB", "GB", "TB"];
  if (bytes == 0) return "0 Byte";
  var i = parseInt(Math.floor(Math.log(bytes) / Math.log(1024)));
  return Math.round(bytes / Math.pow(1024, i), 2) + " " + sizes[i];
}

export function customerSubSagment(subSagment) {
  switch (subSagment) {
    case "HOUSEHOLDS":
      return "HOUSEHOLDS";
    case "CONSIGNMENT":
      return "CONSIGNMENT";
    case "B2C OFFICES":
      return "B2C OFFICES";
    case "OFFICES":
      return "OFFICES";
    case "RESTAURANTS":
      return "RESTAURANTS";
    case "HOTELS":
      return "HOTELS";
    case "TRADE PARTNER":
      return "TRADE PARTNER";
    case "PARTNER CATEGORY 1":
      return "PARTNER CATEGORY 1";
    case "PARTNER CATEGORY 2":
      return "PARTNER CATEGORY 2";
    case "PARTNER CATEGORY 3":
      return "PARTNER CATEGORY 3";
  }
}

export function userLogout() {
  if (window) {
    localStorage.clear();
    this.$router.push("/app/login");
  }
}

export function pastDate() {
  let today = new Date();
  today.setDate(today.getDate() - 1);
  return today.toISOString().slice(0, 10);
}
export function pastOneMonthDifference() {
  let today = new Date();
  let lastMonthOfDate = new Date(today.getFullYear(), today.getMonth() + 1, 0);
  today.setDate(today.getDate() - lastMonthOfDate.getDate());
  return today.toISOString().slice(0, 10);
}

export function setLocalStorage(key) {
  if (typeof key == "object") {
    return localStorage.setItem("value", JSON.stringify(key));
  } else {
    return localStorage.setItem("value", key);
  }
}

export function getLocalStorage(key) {
  if (typeof key == "string") {
    return localStorage.getItem("value", JSON.parse(key));
  } else {
    return localStorage.getItem("value", key);
  }
}

// Used in Google map
export function generateListOfHtmlTag(key, value) {
  return `<li class="pb-1 ma-0">
              <span class="text-primary text-caption font-weight-bold text-capitalize">${key.replace(
                /_/g,
                " "
              )} :</span>
              <span class="text-primary text-caption"> ${value}</span>
          </li>`;
}

export function selectedBranch() {
  let selectedBranch = JSON.parse(localStorage.getItem("selectedBranch"));
  if (selectedBranch) {
    return { branch: selectedBranch.id };
  }
}