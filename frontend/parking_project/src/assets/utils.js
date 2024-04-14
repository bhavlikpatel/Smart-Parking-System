
export function toCapitalize(string) {
  let words = string.split(" ");
  return words
    .map((word) => {
      word = word.split("");
      let char = "";
      if (word.length !== 0) {
        char = word[0].toUpperCase();
      }
      word[0] = char;
      return word.join("");
    })
    .join(" ");
}

export function returnToday() {
  let today = new Date();
  return getDateTime(today);
}

export function getDateTime(_d) {
  let _ = new Date(_d),
    date = _.getDate() < 10 ? "0" + _.getDate() : _.getDate(),
    month = _.getMonth() + 1,
    year = _.getFullYear();

  month = month < 10 ? "0" + month : month;

  return [year, month, date].join("-");
}

export function getExcelDate(serial, type) {
  let utc_days = Math.floor(serial - 25569);
  let utc_value = utc_days * 86400;
  let date_info = new Date(utc_value * 1000);

  let fractional_day = serial - Math.floor(serial) + 0.0000001;

  let total_seconds = Math.floor(86400 * fractional_day);

  let seconds = total_seconds % 60;

  total_seconds -= seconds;

  let hours = Math.floor(total_seconds / (60 * 60));
  let minutes = Math.floor(total_seconds / 60) % 60;

  if (hours < 10) {
    hours = "0" + hours;
  }
  if (minutes < 10) {
    minutes = "0" + minutes;
  }

  if (type == "date") {
    return [
      date_info.getFullYear(),
      date_info.getMonth() + 1,
      date_info.getDate(),
    ].join("-");
  } else {
    return [hours, minutes].join(":");
  }
}

export function toTitleCase(text) {
  text = text.replace("_", " ").replace("-", " ");
  return toCapitalize(text);
}

export function compareTwoStrings(a, b) {
  if (a.length == 0) return b.length;
  if (b.length == 0) return a.length;

  a = a.toLowerCase();
  b = b.toLowerCase();

  const matrix = [];

  // increment along the first column of each row
  let i;
  for (i = 0; i <= b.length; i++) {
    matrix[i] = [i];
  }

  // increment each column in the first row
  let j;
  for (j = 0; j <= a.length; j++) {
    matrix[0][j] = j;
  }

  // Fill in the rest of the matrix
  for (i = 1; i <= b.length; i++) {
    for (j = 1; j <= a.length; j++) {
      if (b.charAt(i - 1) == a.charAt(j - 1)) {
        matrix[i][j] = matrix[i - 1][j - 1];
      } else {
        matrix[i][j] = Math.min(
          matrix[i - 1][j - 1] + 1, // substitution
          Math.min(
            matrix[i][j - 1] + 1, // insertion
            matrix[i - 1][j] + 1
          )
        );
      }
    }
  }
  const distance = matrix[b.length][a.length];
  return (a.length + b.length - distance) / (a.length + b.length);
}

export function s2ab(s) {
  var buf = new ArrayBuffer(s.length);
  var view = new Uint8Array(buf);
  for (var i = 0; i < s.length; i++) view[i] = s.charCodeAt(i) & 0xff;
  return buf;
}

export function download(blob, uploadTo) {
  let url = window.URL.createObjectURL(blob);

  let a = document.createElement("a");
  a.href = url;
  a.download = uploadTo + " Sample excel file.xlsx";
  a.click();
  window.URL.revokeObjectURL(url);
}

export function getRemainingDays(date) {
  let date1 = new Date(date);
  let today = new Date();
  let diffInTime = date1.getTime() - today.getTime();
  let diffInDays = Math.ceil(diffInTime / (1000 * 3600 * 24));
  return diffInDays;
}
