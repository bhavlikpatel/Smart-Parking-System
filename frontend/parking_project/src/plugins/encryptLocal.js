import { EncryptStorage } from "encrypt-storage";

const key = "Somethingdumbhashing";

export default ({ $axios }, inject) => {
  inject("encrypt", EncryptStorage(key));
};
